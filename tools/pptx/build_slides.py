#!/usr/bin/env python3
"""build_slides.py — 構造化スペックから .pptx を生成・読込・改変する CLI

サブコマンド:
    build      <spec.json>              スペックから新規 pptx を構築
    inspect    <pptx>                   既存 pptx の構造を JSON 化
    apply      <pptx> <ops.json>        既存 pptx に変更操作を適用
    list-styles                         利用可能なスタイル一覧

スペック / 操作の詳細スキーマは tools/pptx/pptx_builder.py を参照。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
PPTX_TOOLS_DIR = Path(__file__).resolve().parent
STYLES_DIR = PPTX_TOOLS_DIR / "styles"
STYLES_META_DIR = PPTX_TOOLS_DIR / "styles-meta"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "slides" / "pptx"
DEFAULT_STYLE = "default"

sys.path.insert(0, str(PPTX_TOOLS_DIR))
from pptx_builder import (  # noqa: E402
    apply_ops,
    build_from_spec,
    inspect_pptx,
    load_style,
)


def _resolve_template(name: str | None) -> Path | None:
    """テンプレ名から `tools/pptx/styles/<name>.pptx` を解決。

    現状はテンプレ pptx を使わずコード側でクロームを描画するため通常 None。
    PowerPoint 編集テンプレを置きたい場合のみ存在をチェックする。
    """
    if not name:
        return None
    candidate = STYLES_DIR / f"{name}.pptx"
    return candidate if candidate.exists() else None


def _list_styles() -> list[dict[str, Any]]:
    """styles-meta/*.yaml をスキャンしてスタイル情報を返す。"""
    out: list[dict[str, Any]] = []
    if not STYLES_META_DIR.exists():
        return out
    for yaml_path in sorted(STYLES_META_DIR.glob("*.yaml")):
        name = yaml_path.stem
        try:
            style = load_style(name)
            out.append(
                {
                    "name": style.name,
                    "description": style.description,
                    "size_inch": (
                        round(style.slide_width_emu / 914400, 3),
                        round(style.slide_height_emu / 914400, 3),
                    ),
                    "colors": style.colors,
                }
            )
        except Exception as e:
            out.append({"name": name, "error": str(e)})
    return out


def _read_json(path: str) -> Any:
    if path == "-":
        return json.loads(sys.stdin.read())
    return json.loads(Path(path).read_text(encoding="utf-8"))


def cmd_build(args: argparse.Namespace) -> int:
    spec = _read_json(args.spec)
    if not isinstance(spec, dict):
        raise SystemExit("spec の最上位は object であること")
    style_name = args.style or spec.get("style") or DEFAULT_STYLE
    style = load_style(style_name)
    template_path = _resolve_template(args.template or spec.get("template"))

    if args.out:
        out_path = Path(args.out).resolve()
    else:
        title = (spec.get("metadata") or {}).get("title") or "presentation"
        slug = title.replace(" ", "_").replace("/", "_")
        out_path = (DEFAULT_OUTPUT_DIR / f"{slug}.pptx").resolve()

    builder = build_from_spec(spec, template_path=template_path, style=style)
    builder.save(out_path)

    print(f"生成完了: {out_path}")
    print(f"  スタイル: {style.name}")
    print(f"  スライド数: {builder.slide_count()}")
    if template_path:
        print(f"  テンプレ pptx: {template_path}")
    return 0


def cmd_inspect(args: argparse.Namespace) -> int:
    info = inspect_pptx(args.pptx)
    out_text = json.dumps(info, ensure_ascii=False, indent=2)
    if args.out and args.out != "-":
        Path(args.out).write_text(out_text, encoding="utf-8")
        print(f"書き出し: {args.out}")
    else:
        print(out_text)
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    payload = _read_json(args.ops)
    if isinstance(payload, dict) and "operations" in payload:
        ops = payload["operations"]
    elif isinstance(payload, list):
        ops = payload
    else:
        raise SystemExit("ops は配列、または {operations: [...]} を持つ object であること")

    style_name = args.style or DEFAULT_STYLE
    style = load_style(style_name)
    out_path = Path(args.out).resolve() if args.out else Path(args.pptx).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if out_path == Path(args.pptx).resolve():
        tmp_path = out_path.with_suffix(out_path.suffix + ".tmp")
        builder = apply_ops(args.pptx, ops, out_path=tmp_path, style=style)
        tmp_path.replace(out_path)
    else:
        builder = apply_ops(args.pptx, ops, out_path=out_path, style=style)

    print(f"適用完了: {out_path}")
    print(f"  操作数: {len(ops)}, スライド数: {builder.slide_count()}")
    return 0


def cmd_list_styles(_args: argparse.Namespace) -> int:
    items = _list_styles()
    if not items:
        print("(スタイル定義なし)")
        return 0
    for s in items:
        if "error" in s:
            print(f"- {s['name']:<14} [ERROR] {s['error']}")
            continue
        w, h = s["size_inch"]
        first_line = (s.get("description") or "").splitlines()[0] if s.get("description") else ""
        print(f"- {s['name']:<14} ({w} x {h} inch)  {first_line}")
        for ck, cv in s["colors"].items():
            print(f"    {ck:<6} {cv}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="build_slides",
        description="構造化スペックから pptx を生成・読込・改変する",
    )
    sub = p.add_subparsers(dest="cmd")

    pb = sub.add_parser("build", help="スペックから新規 pptx を構築")
    pb.add_argument("spec", help="スペック JSON のパス（- で標準入力）")
    pb.add_argument("--style", default=None, help="スタイル名（既定: spec の `style` か default）")
    pb.add_argument("--template", default=None, help="テンプレ pptx 名（任意）")
    pb.add_argument("--out", default=None, help="出力 pptx パス")
    pb.set_defaults(func=cmd_build)

    pi = sub.add_parser("inspect", help="既存 pptx の構造を JSON 化")
    pi.add_argument("pptx", help="既存 pptx パス")
    pi.add_argument("--out", default=None, help="書き出し JSON パス（既定: stdout）")
    pi.set_defaults(func=cmd_inspect)

    pa = sub.add_parser("apply", help="既存 pptx に操作列 (ops.json) を適用")
    pa.add_argument("pptx", help="既存 pptx パス")
    pa.add_argument("ops", help="操作列 JSON のパス（- で標準入力）")
    pa.add_argument("--style", default=None, help="新規追加スライドに適用するスタイル名")
    pa.add_argument("--out", default=None, help="出力 pptx パス（既定: 元を上書き）")
    pa.set_defaults(func=cmd_apply)

    pl = sub.add_parser("list-styles", help="利用可能なスタイル一覧")
    pl.set_defaults(func=cmd_list_styles)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.cmd is None:
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
