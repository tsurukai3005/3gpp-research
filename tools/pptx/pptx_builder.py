"""pptx_builder.py — python-pptx を直接叩いて pptx を構築・読込・改変するライブラリ

外部依存:
    必須: python-pptx (1.x)

公開シンボル:
    PresentationBuilder        生成・改変オブジェクト
    Style                      レイアウト・色・フォント定義
    load_style(name)           styles-meta/<name>.yaml を読み込む
    inspect_pptx(path)         既存 pptx を辞書化
    build_from_spec(spec, ...) 仕様 (dict) から Presentation を構築
    apply_ops(path, ops, ...)  既存 pptx に変更操作 (list[dict]) を適用

スライド型 (`type` フィールド) と意味:
    title    タイトルスライド (title / subtitle / author / date)
    section  セクション扉   (title)
    content  本文 (title / body[bullet|callout])
    table    表 (title / headers[list[str]] / rows[list[list[str]]])

各スライドは以下の任意フィールドを持つ:
    notes      発表者ノート (str)
    reference  参考文献 (str) — 見出しバー右端に小さく配置

content の body 要素は次のいずれか:
    "string"                                       単純な箇条書き行
    {"kind": "bullet", "text": "..."}              明示的な箇条書き
    {"kind": "callout", "text": "...",
     "tone": "main"|"assort"|"accent"}             塗りつぶしテキストボックス

bullet の text 内では `**強調**` が Main 色の太字になる。

操作型 (`op` フィールド) と意味 (apply_ops):
    append          末尾に追加         (slide)
    insert          指定 index に挿入  (index, slide)        ※index 1-origin
    replace         置換               (index, slide)
    delete          削除               (index)
    move            並べ替え           (from_index, to_index)
    update_text     スライド内文字列置換 (index, find, replace)
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt


# ---------------------------------------------------------------------------
# Style: YAML 読み込み
# ---------------------------------------------------------------------------


STYLES_META_DIR = Path(__file__).resolve().parent / "styles-meta"


@dataclass(frozen=True)
class Style:
    name: str
    description: str
    slide_width_emu: int
    slide_height_emu: int
    fonts: dict[str, Any]
    colors: dict[str, str]
    layout: dict[str, float]

    def font(self, key: str, default: Any = None) -> Any:
        return self.fonts.get(key, default)

    def color(self, key: str) -> RGBColor:
        return _hex_to_rgb_color(self.colors[key])

    def inch(self, key: str) -> int:
        """layout の inch 値を EMU で返す。"""
        return Inches(float(self.layout[key]))


_DEFAULT_STYLE_FALLBACK: dict[str, Any] = {
    "name": "default",
    "description": "16:9 with red heading bar (Meiryo).",
    "slide_size": {"width_inch": 13.333, "height_inch": 7.5},
    "fonts": {
        "primary": "Meiryo",
        "primary_jp": "Meiryo",
        "mono": "Consolas",
        "size_title_pt": 22,
        "size_body_pt": 18,
        "size_callout_pt": 18,
        "size_footer_pt": 10,
        "size_reference_pt": 10,
        "size_cover_title_pt": 40,
        "size_cover_subtitle_pt": 20,
        "size_cover_meta_pt": 14,
        "size_toc_title_pt": 32,
        "size_toc_entry_pt": 20,
        "line_spacing_body": 1.25,
        "line_spacing_callout": 1.15,
    },
    "colors": {
        "main": "#CC0033",
        "assort": "#5B6B7E",
        "accent": "#E8ECF1",
        "text": "#1F1F1F",
        "bg": "#FFFFFF",
    },
    "layout": {
        "header_height_inch": 0.7,
        "footer_height_inch": 0.35,
        "margin_x_inch": 0.5,
        "body_top_gap_inch": 0.2,
        "body_bottom_gap_inch": 0.1,
        "reference_width_inch": 3.0,
        "callout_height_inch": 0.55,
        "callout_gap_inch": 0.14,
        "bullet_to_callout_gap_inch": 0.18,
        "table_row_height_inch": 0.45,
        "table_cell_pad_inch": 0.06,
    },
}


def load_style(name: str = "default") -> Style:
    """styles-meta/<name>.yaml を読み込んで Style を返す。

    PyYAML 非依存の小さな YAML パーサで、本プロジェクトのスキーマ
    （2 階層マッピング・スカラー・`|` ブロック）のみをサポートする。
    パース不能な場合は組み込みデフォルトにフォールバックする。
    """
    path = STYLES_META_DIR / f"{name}.yaml"
    raw: dict[str, Any]
    if path.exists():
        try:
            raw = _parse_yaml_config(path.read_text(encoding="utf-8"))
        except Exception:
            raw = dict(_DEFAULT_STYLE_FALLBACK)
    else:
        raw = dict(_DEFAULT_STYLE_FALLBACK)

    size = raw.get("slide_size") or _DEFAULT_STYLE_FALLBACK["slide_size"]
    fonts = {**_DEFAULT_STYLE_FALLBACK["fonts"], **(raw.get("fonts") or {})}
    colors = {**_DEFAULT_STYLE_FALLBACK["colors"], **(raw.get("colors") or {})}
    layout = {**_DEFAULT_STYLE_FALLBACK["layout"], **(raw.get("layout") or {})}

    return Style(
        name=str(raw.get("name") or name),
        description=str(raw.get("description") or ""),
        slide_width_emu=Inches(float(size["width_inch"])),
        slide_height_emu=Inches(float(size["height_inch"])),
        fonts=fonts,
        colors=colors,
        layout=layout,
    )


def _parse_yaml_config(text: str) -> dict[str, Any]:
    """限定スキーマの YAML パーサ。

    対応:
      - 0/2 スペースインデント
      - top-level スカラー / 1階層ネスト
      - `key: |` ブロックスカラー（インデント保持）
      - クォート文字列（"' 両対応）
      - int / float / 文字列の自動判別
      - コメント `#`（ただしクォート内では無視）
    """
    result: dict[str, Any] = {}
    section: str | None = None
    block_target: tuple[str | None, str] | None = None
    block_lines: list[str] = []
    block_base_indent: int | None = None

    def commit_block() -> None:
        nonlocal block_target, block_lines, block_base_indent
        if block_target is None:
            return
        sec, key = block_target
        value = "\n".join(block_lines).rstrip("\n")
        if sec is None:
            result[key] = value
        else:
            result.setdefault(sec, {})[key] = value
        block_target = None
        block_lines = []
        block_base_indent = None

    for raw in text.splitlines():
        if block_target is not None:
            if raw.strip() == "":
                block_lines.append("")
                continue
            indent = len(raw) - len(raw.lstrip(" "))
            if indent > 0:
                if block_base_indent is None:
                    block_base_indent = indent
                trimmed = raw[block_base_indent:] if indent >= block_base_indent else raw.lstrip(" ")
                block_lines.append(trimmed)
                continue
            commit_block()

        line = _strip_trailing_comment(raw).rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.lstrip(" ")
        if ":" not in content:
            continue
        key, _, val = content.partition(":")
        key, val = key.strip(), val.strip()

        if indent == 0:
            section = None
            if val == "|":
                block_target = (None, key)
                block_lines = []
                block_base_indent = None
            elif val == "":
                result[key] = {}
                section = key
            else:
                result[key] = _coerce_scalar(val)
        elif indent == 2 and section is not None:
            if val == "|":
                block_target = (section, key)
                block_lines = []
                block_base_indent = None
            else:
                result[section][key] = _coerce_scalar(val)
    commit_block()
    return result


def _strip_trailing_comment(line: str) -> str:
    in_quote: str | None = None
    for i, ch in enumerate(line):
        if in_quote:
            if ch == in_quote:
                in_quote = None
        else:
            if ch in '"\'':
                in_quote = ch
            elif ch == "#":
                return line[:i]
    return line


def _coerce_scalar(s: str) -> Any:
    if not s:
        return ""
    if (s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'"):
        return s[1:-1]
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        return s


def _hex_to_rgb_color(hex_str: str) -> RGBColor:
    h = hex_str.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


# ---------------------------------------------------------------------------
# レイアウト解決（python-pptx 既定マスタ上で使う）
# ---------------------------------------------------------------------------


LAYOUT_CANDIDATES: dict[str, list[str]] = {
    "title":   ["Blank", "白紙", "Title Slide", "タイトル スライド", "タイトル"],
    "toc":     ["Blank", "白紙", "Title Slide", "タイトル スライド", "タイトル"],
    "section": ["Blank", "白紙", "Section Header", "セクション見出し"],
    "content": ["Blank", "白紙", "Title and Content", "タイトルとコンテンツ"],
    "table":   ["Blank", "白紙", "Title and Content", "タイトルとコンテンツ"],
}

LAYOUT_FALLBACK_INDEX: dict[str, int] = {
    "title":   6,  # python-pptx 既定では Blank が index 6
    "toc":     6,
    "section": 6,
    "content": 6,
    "table":   6,
}


def _resolve_layout(prs: Any, slide_type: str) -> Any:
    names = LAYOUT_CANDIDATES.get(slide_type, [])
    layouts = list(prs.slide_layouts)
    name_map = {layout.name: layout for layout in layouts}
    for name in names:
        if name in name_map:
            return name_map[name]
    idx = LAYOUT_FALLBACK_INDEX.get(slide_type, 6)
    if idx < len(layouts):
        return layouts[idx]
    return layouts[-1]


def _strip_all_placeholders(slide: Any) -> None:
    """レイアウト由来のプレースホルダを全削除し、白紙状態にする。"""
    for shape in list(slide.shapes):
        try:
            sp = shape._element
            sp.getparent().remove(sp)
        except Exception:
            pass


# ---------------------------------------------------------------------------
# テキスト・フォント補助
# ---------------------------------------------------------------------------


def _apply_font(
    run: Any,
    *,
    size_pt: int,
    color: RGBColor,
    bold: bool = False,
    name: str | None = None,
    name_jp: str | None = None,
) -> None:
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.color.rgb = color
    if name:
        run.font.name = name
    if name_jp:
        # 日本語フォントを East Asia として明示
        rPr = run._r.get_or_add_rPr()
        for tag in ("ea", "cs"):
            existing = rPr.find(qn(f"a:{tag}"))
            if existing is not None:
                rPr.remove(existing)
        ea = rPr.makeelement(qn("a:ea"), {"typeface": name_jp})
        rPr.append(ea)


def _clear_paragraph_runs(p: Any) -> None:
    for run in list(p.runs):
        run._r.getparent().remove(run._r)


def _parse_inline_emphasis(text: str) -> list[tuple[str, bool]]:
    """`**strong**` を抽出して (segment, is_emph) のリストにする。"""
    out: list[tuple[str, bool]] = []
    i = 0
    while i < len(text):
        idx = text.find("**", i)
        if idx == -1:
            tail = text[i:]
            if tail:
                out.append((tail, False))
            break
        if idx > i:
            out.append((text[i:idx], False))
        end = text.find("**", idx + 2)
        if end == -1:
            tail = text[idx:]
            if tail:
                out.append((tail, False))
            break
        seg = text[idx + 2:end]
        if seg:
            out.append((seg, True))
        i = end + 2
    return out


# ---------------------------------------------------------------------------
# クローム描画 (heading bar / reference / footer / cover)
# ---------------------------------------------------------------------------


def _draw_filled_rect(
    slide: Any,
    *,
    x: int,
    y: int,
    w: int,
    h: int,
    fill_color: RGBColor,
) -> Any:
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape


def _draw_textbox(
    slide: Any,
    *,
    x: int,
    y: int,
    w: int,
    h: int,
) -> Any:
    return slide.shapes.add_textbox(x, y, w, h)


def _set_text_frame(
    tf: Any,
    *,
    margin_in: float = 0.05,
    anchor: Any = MSO_ANCHOR.MIDDLE,
    word_wrap: bool = True,
) -> None:
    tf.margin_left = Inches(margin_in)
    tf.margin_right = Inches(margin_in)
    tf.margin_top = Inches(max(margin_in - 0.02, 0.0))
    tf.margin_bottom = Inches(max(margin_in - 0.02, 0.0))
    tf.vertical_anchor = anchor
    tf.word_wrap = word_wrap


def _draw_header_bar(
    slide: Any,
    *,
    style: Style,
    title: str,
    reference: str | None,
    slide_width: int,
) -> None:
    h = style.inch("header_height_inch")
    bar = _draw_filled_rect(
        slide, x=0, y=0, w=slide_width, h=h, fill_color=style.color("main")
    )
    # 見出しバー内のタイトル
    margin_x = style.inch("margin_x_inch")
    ref_w = style.inch("reference_width_inch") if reference else 0
    ref_gap = Inches(0.15) if reference else 0
    title_x = margin_x
    title_w = slide_width - 2 * margin_x - ref_w - ref_gap
    tf = bar.text_frame
    _set_text_frame(tf, margin_in=0.0, anchor=MSO_ANCHOR.MIDDLE)
    # rectangle 内蔵 text_frame は left=0 から始まるので、左パディングは段落で取る
    tf.margin_left = title_x
    tf.margin_right = ref_w + ref_gap + margin_x
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    _clear_paragraph_runs(p)
    run = p.add_run()
    run.text = title
    _apply_font(
        run,
        size_pt=style.font("size_title_pt"),
        color=_hex_to_rgb_color("#FFFFFF"),
        bold=True,
        name=style.font("primary"),
        name_jp=style.font("primary_jp"),
    )

    # 参考文献欄（見出しバー内・右寄せ）
    if reference:
        ref_x = slide_width - margin_x - ref_w
        ref_box = _draw_textbox(
            slide, x=ref_x, y=0, w=ref_w, h=h
        )
        ref_box.fill.background()
        ref_box.line.fill.background()
        rtf = ref_box.text_frame
        _set_text_frame(rtf, margin_in=0.05, anchor=MSO_ANCHOR.MIDDLE)
        rp = rtf.paragraphs[0]
        rp.alignment = PP_ALIGN.RIGHT
        _clear_paragraph_runs(rp)
        rrun = rp.add_run()
        rrun.text = reference
        _apply_font(
            rrun,
            size_pt=style.font("size_reference_pt"),
            color=_hex_to_rgb_color("#FFFFFF"),
            bold=False,
            name=style.font("primary"),
            name_jp=style.font("primary_jp"),
        )


def _draw_footer(
    slide: Any,
    *,
    style: Style,
    doc_title: str,
    page_placeholder: str,
    slide_width: int,
    slide_height: int,
) -> Any:
    """左に資料タイトル、右にページ番号枠（後でテキスト差し替え）を置く。

    page_placeholder は最終的に "n / N" に書き換えるためのマーカー。
    返り値は page number を保持する shape。
    """
    fh = style.inch("footer_height_inch")
    margin_x = style.inch("margin_x_inch")
    foot_y = slide_height - fh
    half_w = (slide_width - 2 * margin_x) // 2

    # 左フッタ: 資料タイトル
    if doc_title:
        left = _draw_textbox(slide, x=margin_x, y=foot_y, w=half_w, h=fh)
        left.fill.background()
        left.line.fill.background()
        ltf = left.text_frame
        _set_text_frame(ltf, margin_in=0.05, anchor=MSO_ANCHOR.MIDDLE)
        lp = ltf.paragraphs[0]
        lp.alignment = PP_ALIGN.LEFT
        _clear_paragraph_runs(lp)
        lrun = lp.add_run()
        lrun.text = doc_title
        _apply_font(
            lrun,
            size_pt=style.font("size_footer_pt"),
            color=style.color("assort"),
            name=style.font("primary"),
            name_jp=style.font("primary_jp"),
        )

    # 右フッタ: ページ番号
    right = _draw_textbox(
        slide, x=margin_x + half_w, y=foot_y, w=half_w, h=fh
    )
    right.fill.background()
    right.line.fill.background()
    right.name = "__page_number__"
    rtf = right.text_frame
    _set_text_frame(rtf, margin_in=0.05, anchor=MSO_ANCHOR.MIDDLE)
    rp = rtf.paragraphs[0]
    rp.alignment = PP_ALIGN.RIGHT
    _clear_paragraph_runs(rp)
    rrun = rp.add_run()
    rrun.text = page_placeholder
    _apply_font(
        rrun,
        size_pt=style.font("size_footer_pt"),
        color=style.color("assort"),
        name=style.font("primary"),
        name_jp=style.font("primary_jp"),
    )
    return right


# ---------------------------------------------------------------------------
# Body 描画
# ---------------------------------------------------------------------------


_BULLET_PREFIX = "▪  "


def _normalize_body_items(body: Iterable[Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for item in body:
        if isinstance(item, str):
            out.append({"kind": "bullet", "text": item})
        elif isinstance(item, dict):
            kind = item.get("kind") or "bullet"
            entry: dict[str, Any] = {"kind": kind, "text": str(item.get("text", ""))}
            if kind == "callout":
                entry["tone"] = item.get("tone") or "assort"
            out.append(entry)
        else:
            out.append({"kind": "bullet", "text": str(item)})
    return out


def _render_body(
    slide: Any,
    *,
    style: Style,
    body_items: list[dict[str, Any]],
    slide_width: int,
    slide_height: int,
) -> None:
    if not body_items:
        return
    margin_x = style.inch("margin_x_inch")
    header_h = style.inch("header_height_inch")
    footer_h = style.inch("footer_height_inch")
    top_gap = style.inch("body_top_gap_inch")
    bottom_gap = style.inch("body_bottom_gap_inch")
    callout_h = style.inch("callout_height_inch")
    callout_gap = style.inch("callout_gap_inch")
    bullet_to_callout_gap = style.inch("bullet_to_callout_gap_inch")

    body_x = margin_x
    body_y_top = header_h + top_gap
    body_w = slide_width - 2 * margin_x
    body_y_bottom = slide_height - footer_h - bottom_gap
    avail_h = max(body_y_bottom - body_y_top, Inches(0.5))

    body_size_pt = float(style.font("size_body_pt", 18))
    line_spacing = float(style.font("line_spacing_body", 1.25))

    # 連続する bullets を一つのテキストフレームにまとめる
    groups: list[dict[str, Any]] = []
    bullet_run: list[str] = []
    for item in body_items:
        if item["kind"] == "bullet":
            bullet_run.append(item["text"])
        else:
            if bullet_run:
                groups.append({"kind": "bullets", "items": bullet_run})
                bullet_run = []
            groups.append({"kind": "callout", "text": item["text"], "tone": item.get("tone", "accent")})
    if bullet_run:
        groups.append({"kind": "bullets", "items": bullet_run})

    # 行数ベースで箇条書きブロックの高さを計算（残り領域は余白として残す）
    line_height_emu = Pt(body_size_pt * line_spacing)
    text_frame_pad = Inches(0.20)  # tf 上下マージン + 末尾ディセンダ余白

    def bullet_block_height(n_lines: int) -> int:
        return n_lines * line_height_emu + text_frame_pad

    sized: list[dict[str, Any]] = []
    for g in groups:
        if g["kind"] == "bullets":
            sized.append({**g, "h": bullet_block_height(len(g["items"]))})
        else:
            sized.append({**g, "h": callout_h})

    # 隣接間ギャップを集計
    total_h = sum(s["h"] for s in sized)
    for i in range(1, len(sized)):
        prev_kind = sized[i - 1]["kind"]
        cur_kind = sized[i]["kind"]
        if prev_kind == "bullets" and cur_kind == "callout":
            total_h += bullet_to_callout_gap
        elif prev_kind == "callout" and cur_kind == "bullets":
            total_h += bullet_to_callout_gap
        else:
            total_h += callout_gap

    # 高さが領域を超える場合は箇条書き側を比例縮小
    if total_h > avail_h:
        bullet_groups = [s for s in sized if s["kind"] == "bullets"]
        excess = total_h - avail_h
        if bullet_groups:
            shrink_per = excess // len(bullet_groups)
            min_h = Inches(0.4)
            for s in bullet_groups:
                s["h"] = max(s["h"] - shrink_per, min_h)

    cur_y = body_y_top
    for i, sg in enumerate(sized):
        if i > 0:
            prev_kind = sized[i - 1]["kind"]
            if prev_kind == "bullets" and sg["kind"] == "callout":
                cur_y += bullet_to_callout_gap
            elif prev_kind == "callout" and sg["kind"] == "bullets":
                cur_y += bullet_to_callout_gap
            else:
                cur_y += callout_gap
        if sg["kind"] == "bullets":
            _render_bullet_block(
                slide,
                style=style,
                items=sg["items"],
                x=body_x,
                y=cur_y,
                w=body_w,
                h=sg["h"],
                line_spacing=line_spacing,
            )
        else:
            _render_callout(
                slide,
                style=style,
                text=sg["text"],
                tone=sg.get("tone", "accent"),
                x=body_x,
                y=cur_y,
                w=body_w,
                h=sg["h"],
            )
        cur_y += sg["h"]


def _render_bullet_block(
    slide: Any,
    *,
    style: Style,
    items: list[str],
    x: int,
    y: int,
    w: int,
    h: int,
    line_spacing: float = 1.25,
) -> None:
    if not items:
        return
    tb = _draw_textbox(slide, x=x, y=y, w=w, h=h)
    tb.fill.background()
    tb.line.fill.background()
    tf = tb.text_frame
    _set_text_frame(tf, margin_in=0.08, anchor=MSO_ANCHOR.TOP)
    body_size = style.font("size_body_pt")
    text_color = style.color("text")
    main_color = style.color("main")
    primary = style.font("primary")
    primary_jp = style.font("primary_jp")

    for i, raw in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        _clear_paragraph_runs(p)
        p.level = 0
        p.alignment = PP_ALIGN.LEFT
        try:
            p.line_spacing = float(line_spacing)
        except Exception:
            pass
        # bullet 記号
        prefix = p.add_run()
        prefix.text = _BULLET_PREFIX
        _apply_font(
            prefix,
            size_pt=body_size,
            color=main_color,
            bold=True,
            name=primary,
            name_jp=primary_jp,
        )
        # 本文（**...** で強調）
        for seg, is_emph in _parse_inline_emphasis(raw):
            run = p.add_run()
            run.text = seg
            _apply_font(
                run,
                size_pt=body_size,
                color=main_color if is_emph else text_color,
                bold=is_emph,
                name=primary,
                name_jp=primary_jp,
            )


def _render_callout(
    slide: Any,
    *,
    style: Style,
    text: str,
    tone: str,  # 後方互換のため受け取るが描画は accent に統一
    x: int,
    y: int,
    w: int,
    h: int,
) -> None:
    del tone  # 色分けは廃止: 全 callout を Accent (#E8ECF1) に統一
    fill = style.color("accent")
    text_color = style.color("text")
    box = _draw_filled_rect(slide, x=x, y=y, w=w, h=h, fill_color=fill)
    tf = box.text_frame
    _set_text_frame(tf, margin_in=0.15, anchor=MSO_ANCHOR.MIDDLE)
    tf.margin_left = Inches(0.18)
    tf.margin_right = Inches(0.18)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    _clear_paragraph_runs(p)
    try:
        p.line_spacing = float(style.font("line_spacing_callout", 1.15))
    except Exception:
        pass
    for seg, is_emph in _parse_inline_emphasis(text):
        run = p.add_run()
        run.text = seg
        _apply_font(
            run,
            size_pt=style.font("size_callout_pt"),
            color=text_color,
            bold=is_emph,
            name=style.font("primary"),
            name_jp=style.font("primary_jp"),
        )


# ---------------------------------------------------------------------------
# 表紙描画
# ---------------------------------------------------------------------------


def _render_cover(
    slide: Any,
    *,
    style: Style,
    title: str,
    subtitle: str | None,
    author: str | None,  # 表示しない（後方互換のため引数のみ受ける）
    date: str | None,
    slide_width: int,
    slide_height: int,
) -> None:
    del author  # 仕様: 表紙に著者名は表示しない

    # 全面赤背景
    _draw_filled_rect(
        slide, x=0, y=0, w=slide_width, h=slide_height, fill_color=style.color("main")
    )

    margin_x = style.inch("margin_x_inch")
    primary = style.font("primary")
    primary_jp = style.font("primary_jp")
    white = _hex_to_rgb_color("#FFFFFF")

    # タイトル + subtitle + date を縦に積み、ブロック全体を縦中央に配置
    block_w = slide_width - 2 * margin_x
    block_h = Inches(3.6)
    block_y = (slide_height - block_h) // 2

    box = _draw_textbox(slide, x=margin_x, y=block_y, w=block_w, h=block_h)
    box.fill.background()
    box.line.fill.background()
    tf = box.text_frame
    _set_text_frame(tf, margin_in=0.0, anchor=MSO_ANCHOR.MIDDLE)

    # タイトル
    tp = tf.paragraphs[0]
    tp.alignment = PP_ALIGN.CENTER
    _clear_paragraph_runs(tp)
    trun = tp.add_run()
    trun.text = title
    _apply_font(
        trun,
        size_pt=style.font("size_cover_title_pt"),
        color=white,
        bold=True,
        name=primary,
        name_jp=primary_jp,
    )

    # サブタイトル
    if subtitle:
        sp = tf.add_paragraph()
        sp.alignment = PP_ALIGN.CENTER
        try:
            sp.space_before = Pt(18)
        except Exception:
            pass
        srun = sp.add_run()
        srun.text = subtitle
        _apply_font(
            srun,
            size_pt=style.font("size_cover_subtitle_pt"),
            color=white,
            name=primary,
            name_jp=primary_jp,
        )

    # 日付
    if date:
        dp = tf.add_paragraph()
        dp.alignment = PP_ALIGN.CENTER
        try:
            dp.space_before = Pt(28)
        except Exception:
            pass
        drun = dp.add_run()
        drun.text = date
        _apply_font(
            drun,
            size_pt=style.font("size_cover_meta_pt"),
            color=white,
            name=primary,
            name_jp=primary_jp,
        )


# ---------------------------------------------------------------------------
# 目次描画
# ---------------------------------------------------------------------------


def _render_toc(
    slide: Any,
    *,
    style: Style,
    title: str,
    entries: list[str],
    slide_width: int,
    slide_height: int,
) -> None:
    """全面赤背景・白文字の目次スライドを描画する。entries は MD 側で明示する。"""
    _draw_filled_rect(
        slide, x=0, y=0, w=slide_width, h=slide_height, fill_color=style.color("main")
    )

    margin_x = style.inch("margin_x_inch")
    primary = style.font("primary")
    primary_jp = style.font("primary_jp")
    white = _hex_to_rgb_color("#FFFFFF")

    # タイトル: 上部
    title_pt = style.font("size_toc_title_pt", 32)
    title_h = Inches(1.1)
    title_y = Inches(0.9)
    title_box = _draw_textbox(
        slide, x=margin_x, y=title_y, w=slide_width - 2 * margin_x, h=title_h
    )
    title_box.fill.background()
    title_box.line.fill.background()
    ttf = title_box.text_frame
    _set_text_frame(ttf, margin_in=0.0, anchor=MSO_ANCHOR.MIDDLE)
    tp = ttf.paragraphs[0]
    tp.alignment = PP_ALIGN.CENTER
    _clear_paragraph_runs(tp)
    trun = tp.add_run()
    trun.text = title or "目次"
    _apply_font(
        trun,
        size_pt=title_pt,
        color=white,
        bold=True,
        name=primary,
        name_jp=primary_jp,
    )

    if not entries:
        return

    # entries: タイトル下に箇条書き（中央寄せの縦帯）
    entry_pt = style.font("size_toc_entry_pt", 20)
    block_y = title_y + title_h + Inches(0.5)
    block_w = Inches(8.5)
    block_h = slide_height - block_y - Inches(0.6)
    block_x = (slide_width - block_w) // 2
    ebox = _draw_textbox(slide, x=block_x, y=block_y, w=block_w, h=block_h)
    ebox.fill.background()
    ebox.line.fill.background()
    etf = ebox.text_frame
    _set_text_frame(etf, margin_in=0.0, anchor=MSO_ANCHOR.TOP)

    n = len(entries)
    width = len(str(n))
    for i, entry in enumerate(entries):
        p = etf.paragraphs[0] if i == 0 else etf.add_paragraph()
        _clear_paragraph_runs(p)
        p.alignment = PP_ALIGN.LEFT
        try:
            p.line_spacing = 1.6
        except Exception:
            pass
        run = p.add_run()
        run.text = f"{str(i + 1).rjust(width)}.  {entry}"
        _apply_font(
            run,
            size_pt=entry_pt,
            color=white,
            name=primary,
            name_jp=primary_jp,
        )


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------


@dataclass
class _BuildContext:
    prs: Any
    style: Style
    metadata: dict[str, Any] = field(default_factory=dict)


class PresentationBuilder:
    """pptx 構築・改変の高レベル API。"""

    def __init__(
        self,
        template_path: str | Path | None = None,
        style: Style | None = None,
    ) -> None:
        self._template_path = Path(template_path).resolve() if template_path else None
        if self._template_path and self._template_path.exists():
            self._prs = Presentation(str(self._template_path))
            self._wipe_existing_slides()
        else:
            self._prs = Presentation()
        self._style = style or load_style("default")
        # スライドサイズをスタイルに合わせる
        self._prs.slide_width = self._style.slide_width_emu
        self._prs.slide_height = self._style.slide_height_emu
        self._doc_title: str = ""
        self._page_number_shapes: list[Any] = []

    @classmethod
    def open(
        cls, pptx_path: str | Path, style: Style | None = None
    ) -> "PresentationBuilder":
        """既存 pptx を改変対象として開く（テンプレ起点とは異なり、現状を保つ）。"""
        self = object.__new__(cls)
        self._template_path = None
        self._prs = Presentation(str(pptx_path))
        self._style = style or load_style("default")
        self._doc_title = ""
        self._page_number_shapes = []
        return self

    # ---- 内部ユーティリティ ----

    def set_doc_title(self, title: str) -> None:
        self._doc_title = title or ""

    @property
    def style(self) -> Style:
        return self._style

    def _wipe_existing_slides(self) -> None:
        sldIdLst = self._prs.slides._sldIdLst
        for sldId in list(sldIdLst):
            sldIdLst.remove(sldId)

    def _add_slide(self, slide_type: str) -> Any:
        layout = _resolve_layout(self._prs, slide_type)
        slide = self._prs.slides.add_slide(layout)
        _strip_all_placeholders(slide)
        return slide

    def _slide_size(self) -> tuple[int, int]:
        return self._prs.slide_width, self._prs.slide_height

    def _add_chrome(
        self, slide: Any, *, title: str, reference: str | None
    ) -> None:
        sw, sh = self._slide_size()
        _draw_header_bar(
            slide,
            style=self._style,
            title=title,
            reference=reference,
            slide_width=sw,
        )
        page_shape = _draw_footer(
            slide,
            style=self._style,
            doc_title=self._doc_title,
            page_placeholder="?",
            slide_width=sw,
            slide_height=sh,
        )
        self._page_number_shapes.append(page_shape)

    # ---- スライド追加 API ----

    def add_title_slide(
        self,
        title: str,
        subtitle: str | None = None,
        author: str | None = None,
        date: str | None = None,
        notes: str | None = None,
        reference: str | None = None,
    ) -> Any:
        slide = self._add_slide("title")
        sw, sh = self._slide_size()
        _render_cover(
            slide,
            style=self._style,
            title=title,
            subtitle=subtitle,
            author=author,
            date=date,
            slide_width=sw,
            slide_height=sh,
        )
        # 表紙はフッタ・ページ番号を持たない
        if notes:
            _set_notes(slide, notes)
        return slide

    def add_toc_slide(
        self,
        title: str = "目次",
        entries: list[str] | None = None,
        notes: str | None = None,
        reference: str | None = None,
    ) -> Any:
        slide = self._add_slide("toc")
        sw, sh = self._slide_size()
        _render_toc(
            slide,
            style=self._style,
            title=title or "目次",
            entries=list(entries or []),
            slide_width=sw,
            slide_height=sh,
        )
        # 目次もフッタ・ページ番号を持たない（表紙と一貫性）
        if notes:
            _set_notes(slide, notes)
        return slide

    def add_section_slide(
        self,
        title: str,
        notes: str | None = None,
        reference: str | None = None,
    ) -> Any:
        slide = self._add_slide("section")
        sw, sh = self._slide_size()
        # セクション扉は通常より太い見出しバーを使う
        margin_x = self._style.inch("margin_x_inch")
        header_h = self._style.inch("header_height_inch")
        bar_h = header_h + Inches(0.4)
        bar_y = (sh - bar_h) // 2 - Inches(0.4)
        bar = _draw_filled_rect(
            slide, x=0, y=bar_y, w=sw, h=bar_h, fill_color=self._style.color("main")
        )
        tf = bar.text_frame
        _set_text_frame(tf, margin_in=0.0, anchor=MSO_ANCHOR.MIDDLE)
        tf.margin_left = margin_x
        tf.margin_right = margin_x
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        _clear_paragraph_runs(p)
        run = p.add_run()
        run.text = title
        _apply_font(
            run,
            size_pt=self._style.font("size_cover_title_pt"),
            color=_hex_to_rgb_color("#FFFFFF"),
            bold=True,
            name=self._style.font("primary"),
            name_jp=self._style.font("primary_jp"),
        )
        page_shape = _draw_footer(
            slide,
            style=self._style,
            doc_title=self._doc_title,
            page_placeholder="?",
            slide_width=sw,
            slide_height=sh,
        )
        self._page_number_shapes.append(page_shape)
        if notes:
            _set_notes(slide, notes)
        return slide

    def add_content_slide(
        self,
        title: str,
        body: list[Any] | None = None,
        notes: str | None = None,
        reference: str | None = None,
    ) -> Any:
        slide = self._add_slide("content")
        self._add_chrome(slide, title=title, reference=reference)
        sw, sh = self._slide_size()
        if body:
            items = _normalize_body_items(body)
            _render_body(
                slide,
                style=self._style,
                body_items=items,
                slide_width=sw,
                slide_height=sh,
            )
        if notes:
            _set_notes(slide, notes)
        return slide

    def add_table_slide(
        self,
        title: str,
        headers: list[str],
        rows: list[list[str]],
        notes: str | None = None,
        reference: str | None = None,
    ) -> Any:
        slide = self._add_slide("table")
        self._add_chrome(slide, title=title, reference=reference)
        sw, sh = self._slide_size()
        margin_x = self._style.inch("margin_x_inch")
        header_h = self._style.inch("header_height_inch")
        footer_h = self._style.inch("footer_height_inch")
        top_gap = self._style.inch("body_top_gap_inch")
        bottom_gap = self._style.inch("body_bottom_gap_inch")
        left = margin_x
        top = header_h + top_gap
        width = sw - 2 * margin_x
        avail_h = sh - header_h - footer_h - top_gap - bottom_gap

        n_rows = 1 + len(rows)
        n_cols = max(1, len(headers))

        # 行高を内容ベースで決める。avail_h を超えそうなら均等縮小。
        row_h = self._style.inch("table_row_height_inch")
        desired_h = n_rows * row_h
        if desired_h > avail_h:
            row_h = avail_h // n_rows
            height = avail_h
        else:
            height = desired_h
        cell_pad = self._style.inch("table_cell_pad_inch")

        tbl_shape = slide.shapes.add_table(n_rows, n_cols, left, top, width, height)
        tbl = tbl_shape.table
        for r in range(n_rows):
            tbl.rows[r].height = row_h

        body_pt = self._style.font("size_body_pt")
        primary = self._style.font("primary")
        primary_jp = self._style.font("primary_jp")
        white = _hex_to_rgb_color("#FFFFFF")
        text_color = self._style.color("text")
        main_color = self._style.color("main")
        accent_color = self._style.color("accent")

        def _setup_cell(cell: Any, fill: RGBColor) -> Any:
            cell.fill.solid()
            cell.fill.fore_color.rgb = fill
            tf = cell.text_frame
            tf.clear()
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf.margin_left = cell_pad
            tf.margin_right = cell_pad
            tf.margin_top = cell_pad
            tf.margin_bottom = cell_pad
            tf.word_wrap = True
            return tf

        # ヘッダ行
        for c, htxt in enumerate(headers):
            cell = tbl.cell(0, c)
            tf = _setup_cell(cell, main_color)
            p = tf.paragraphs[0]
            _clear_paragraph_runs(p)
            run = p.add_run()
            run.text = str(htxt)
            _apply_font(
                run,
                size_pt=body_pt,
                color=white,
                bold=True,
                name=primary,
                name_jp=primary_jp,
            )

        # 本文行
        for r, row in enumerate(rows, start=1):
            zebra = accent_color if r % 2 == 0 else white
            for c in range(n_cols):
                cell = tbl.cell(r, c)
                tf = _setup_cell(cell, zebra)
                txt = str(row[c]) if c < len(row) else ""
                p = tf.paragraphs[0]
                _clear_paragraph_runs(p)
                run = p.add_run()
                run.text = txt
                _apply_font(
                    run,
                    size_pt=body_pt,
                    color=text_color,
                    name=primary,
                    name_jp=primary_jp,
                )
        if notes:
            _set_notes(slide, notes)
        return slide

    # ---- 改変 API ----

    def slide_count(self) -> int:
        return len(self._prs.slides)

    def append_from_spec(self, slide_spec: dict) -> None:
        _add_slide_from_spec(self, slide_spec)

    def insert_from_spec(self, index_1: int, slide_spec: dict) -> None:
        if index_1 < 1 or index_1 > self.slide_count() + 1:
            raise ValueError(
                f"insert index out of range: {index_1} (1..{self.slide_count() + 1})"
            )
        _add_slide_from_spec(self, slide_spec)
        self.move_slide(self.slide_count(), index_1)

    def replace_slide(self, index_1: int, slide_spec: dict) -> None:
        if index_1 < 1 or index_1 > self.slide_count():
            raise ValueError(
                f"replace index out of range: {index_1} (1..{self.slide_count()})"
            )
        _add_slide_from_spec(self, slide_spec)
        self.move_slide(self.slide_count(), index_1)
        self.delete_slide(index_1 + 1)

    def delete_slide(self, index_1: int) -> None:
        if index_1 < 1 or index_1 > self.slide_count():
            raise ValueError(
                f"delete index out of range: {index_1} (1..{self.slide_count()})"
            )
        sldIdLst = self._prs.slides._sldIdLst
        sldId_children = list(sldIdLst)
        target = sldId_children[index_1 - 1]
        rId = target.get(
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
        )
        sldIdLst.remove(target)
        if rId is not None:
            try:
                self._prs.part.drop_rel(rId)
            except Exception:
                pass

    def move_slide(self, from_index_1: int, to_index_1: int) -> None:
        n = self.slide_count()
        if from_index_1 < 1 or from_index_1 > n or to_index_1 < 1 or to_index_1 > n:
            raise ValueError(
                f"move index out of range: from={from_index_1} to={to_index_1} (1..{n})"
            )
        if from_index_1 == to_index_1:
            return
        sldIdLst = self._prs.slides._sldIdLst
        sldId_children = list(sldIdLst)
        target = sldId_children[from_index_1 - 1]
        sldIdLst.remove(target)
        sldIdLst.insert(to_index_1 - 1, target)

    def update_text(self, index_1: int, find: str, replace: str) -> int:
        if index_1 < 1 or index_1 > self.slide_count():
            raise ValueError(
                f"update_text index out of range: {index_1} (1..{self.slide_count()})"
            )
        slide = list(self._prs.slides)[index_1 - 1]
        count = 0
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        if find in run.text:
                            run.text = run.text.replace(find, replace)
                            count += 1
            if shape.has_table:
                for row in shape.table.rows:
                    for cell in row.cells:
                        for para in cell.text_frame.paragraphs:
                            for run in para.runs:
                                if find in run.text:
                                    run.text = run.text.replace(find, replace)
                                    count += 1
        if slide.has_notes_slide:
            tf = slide.notes_slide.notes_text_frame
            for para in tf.paragraphs:
                for run in para.runs:
                    if find in run.text:
                        run.text = run.text.replace(find, replace)
                        count += 1
        return count

    # ---- ページ番号差し替え（保存直前に呼ぶ）----

    def _finalize_page_numbers(self) -> None:
        total = self.slide_count()
        for s_idx, slide in enumerate(self._prs.slides, start=1):
            for shape in slide.shapes:
                if getattr(shape, "name", "") != "__page_number__":
                    continue
                if not shape.has_text_frame:
                    continue
                tf = shape.text_frame
                if not tf.paragraphs:
                    continue
                p = tf.paragraphs[0]
                if not p.runs:
                    continue
                p.runs[0].text = f"{s_idx} / {total}"

    # ---- 保存 ----

    def save(self, path: str | Path) -> None:
        self._finalize_page_numbers()
        out = Path(path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        self._prs.save(str(out))


# ---------------------------------------------------------------------------
# spec / ops のディスパッチャ
# ---------------------------------------------------------------------------


def _set_notes(slide: Any, text: str) -> None:
    if not text:
        return
    notes_tf = slide.notes_slide.notes_text_frame
    notes_tf.clear()
    p = notes_tf.paragraphs[0]
    if p.runs:
        p.runs[0].text = text
    else:
        p.add_run().text = text


def _add_slide_from_spec(builder: PresentationBuilder, spec: dict) -> None:
    t = spec.get("type", "content")
    notes = spec.get("notes")
    reference = spec.get("reference")
    if t == "title":
        builder.add_title_slide(
            title=spec.get("title", ""),
            subtitle=spec.get("subtitle"),
            author=spec.get("author"),
            date=spec.get("date"),
            notes=notes,
            reference=reference,
        )
    elif t == "toc":
        builder.add_toc_slide(
            title=spec.get("title", "目次"),
            entries=spec.get("entries", []),
            notes=notes,
            reference=reference,
        )
    elif t == "section":
        builder.add_section_slide(
            title=spec.get("title", ""), notes=notes, reference=reference
        )
    elif t == "table":
        builder.add_table_slide(
            title=spec.get("title", ""),
            headers=spec.get("headers", []),
            rows=spec.get("rows", []),
            notes=notes,
            reference=reference,
        )
    elif t == "content":
        builder.add_content_slide(
            title=spec.get("title", ""),
            body=spec.get("body", []),
            notes=notes,
            reference=reference,
        )
    else:
        raise ValueError(f"unknown slide type: {t}")


def build_from_spec(
    spec: dict,
    template_path: str | Path | None = None,
    style: Style | None = None,
) -> PresentationBuilder:
    """spec dict から Presentation を構築し、Builder を返す（save は呼び出し側で）。"""
    style = style or load_style(spec.get("style", "default"))
    builder = PresentationBuilder(template_path=template_path, style=style)
    metadata = spec.get("metadata") or {}
    builder.set_doc_title(str(metadata.get("title", "")))
    slides = spec.get("slides") or []
    expanded: list[dict] = []
    for s in slides:
        if s.get("type") == "title" and "title" not in s and metadata:
            expanded.append(
                {
                    "type": "title",
                    "title": metadata.get("title", ""),
                    "subtitle": metadata.get("subtitle"),
                    "author": metadata.get("author"),
                    "date": metadata.get("date"),
                    "notes": s.get("notes"),
                    "reference": s.get("reference"),
                }
            )
        else:
            expanded.append(s)
    for s in expanded:
        builder.append_from_spec(s)
    return builder


def apply_ops(
    pptx_path: str | Path,
    ops: list[dict],
    out_path: str | Path | None = None,
    style: Style | None = None,
) -> PresentationBuilder:
    """既存 pptx を開き、操作列を適用した Builder を返す。"""
    builder = PresentationBuilder.open(pptx_path, style=style)
    for i, op in enumerate(ops):
        kind = op.get("op")
        try:
            if kind == "append":
                builder.append_from_spec(op["slide"])
            elif kind == "insert":
                builder.insert_from_spec(int(op["index"]), op["slide"])
            elif kind == "replace":
                builder.replace_slide(int(op["index"]), op["slide"])
            elif kind == "delete":
                builder.delete_slide(int(op["index"]))
            elif kind == "move":
                builder.move_slide(int(op["from_index"]), int(op["to_index"]))
            elif kind == "update_text":
                n = builder.update_text(int(op["index"]), op["find"], op["replace"])
                op.setdefault("_result", {})["replaced"] = n
            else:
                raise ValueError(f"unknown op: {kind}")
        except Exception as e:
            raise RuntimeError(f"op[{i}] {kind} failed: {e}") from e
    if out_path:
        builder.save(out_path)
    return builder


# ---------------------------------------------------------------------------
# inspect: 既存 pptx → 辞書
# ---------------------------------------------------------------------------


def _extract_text(text_frame: Any) -> list[str]:
    out: list[str] = []
    for para in text_frame.paragraphs:
        line = "".join(run.text for run in para.runs)
        out.append(line)
    return out


def inspect_pptx(pptx_path: str | Path) -> dict:
    prs = Presentation(str(pptx_path))
    slide_w = prs.slide_width
    slide_h = prs.slide_height
    info: dict[str, Any] = {
        "path": str(Path(pptx_path).resolve()),
        "slide_size": {
            "width_emu": slide_w,
            "height_emu": slide_h,
            "width_inch": round(slide_w / 914400, 3),
            "height_inch": round(slide_h / 914400, 3),
        },
        "layouts": [layout.name for layout in prs.slide_layouts],
        "slides": [],
    }
    for i, slide in enumerate(prs.slides, start=1):
        s: dict[str, Any] = {
            "index": i,
            "layout": slide.slide_layout.name,
            "title": None,
            "body": [],
            "tables": [],
            "shapes": [],
            "notes": "",
        }
        try:
            if slide.shapes.title is not None and slide.shapes.title.has_text_frame:
                s["title"] = slide.shapes.title.text_frame.text
        except Exception:
            pass
        for shape in slide.shapes:
            entry: dict[str, Any] = {"name": shape.name, "shape_type": str(shape.shape_type)}
            if shape.has_text_frame:
                lines = _extract_text(shape.text_frame)
                entry["text"] = lines
                if shape != slide.shapes.title:
                    s["body"].extend(line for line in lines if line.strip())
            if shape.has_table:
                tbl = shape.table
                rows = []
                for row in tbl.rows:
                    rows.append([cell.text_frame.text for cell in row.cells])
                table_entry = {"rows": rows}
                s["tables"].append(table_entry)
                entry["table"] = table_entry
            s["shapes"].append(entry)
        if slide.has_notes_slide:
            s["notes"] = slide.notes_slide.notes_text_frame.text
        info["slides"].append(s)
    return info


__all__ = [
    "PresentationBuilder",
    "Style",
    "load_style",
    "build_from_spec",
    "apply_ops",
    "inspect_pptx",
]
