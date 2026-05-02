# tools/pptx

`.pptx` を Python から構築・読込・改変するための基盤。`python-pptx` を直接叩くため pandoc 等の外部バイナリ依存はない。

入力 MD のフォーマットは規定しない。任意のドキュメントから **エージェント側で文脈を読み取り、構造化スペック (JSON)** を組み立て、本ライブラリに渡す運用を想定する。

## 依存

| ツール | 用途 | 必須/任意 |
|:---|:---|:---|
| Python 3.10+ | 実行 | 必須 |
| python-pptx 1.x | 構築・改変・読取の中核 | 必須 |

```bash
pip install python-pptx
```

PyYAML は不要（`styles-meta/*.yaml` は内蔵パーサで読む）。

## ディレクトリ構成

```
tools/pptx/
├── pptx_builder.py        ← ライブラリ (構築・改変・読取の API)
├── build_slides.py        ← CLI (build / inspect / apply / list-styles)
├── styles/                ← 任意のテンプレ pptx (通常は空)
└── styles-meta/           ← スタイル定義 (YAML)
```

出力既定: `slides/pptx/<title>.pptx`（リポジトリ直下の pptx 専用ディレクトリ）。pptx は git 追跡対象。TeX 系の出力は `slides/tex/` に分離されているため、ここは PPTX 専用と理解してよい。

## スタイル

スタイルは [`styles-meta/default.yaml`](./styles-meta/default.yaml) に集約する。色・レイアウト・フォントを一元管理し、スライド作成時にコード側で見出しバー・フッタ・参考文献欄・callout を描画する（テンプレ pptx を編集する必要はない）。

スタイル定義（抜粋）:

| 要素 | 値 |
|:---|:---|
| 比率 | 16:9 (13.333 × 7.5 inch) |
| Main 色 | `#CC0033` (R204 G0 B51) — 見出しバー塗り、本文強調 (`**…**`) |
| Assort 色 | `#5B6B7E` — callout 既定塗り、フッタ文字 |
| Accent 色 | `#E8ECF1` — callout (accent) の薄塗り、表偶数行 |
| 文字色 | `#1F1F1F` |
| 背景 | `#FFFFFF` |
| フォント | Yu Gothic UI (JP) / Calibri (Latin) |

3 色 + 文字色 + 背景以外は使わない。詳細は [`framework/slide-styles-pptx.md`](../../framework/slide-styles-pptx.md)。

## 構造化スペック (build 時)

`build` サブコマンドは以下の JSON を入力に取る。

```json
{
  "style": "default",
  "metadata": {
    "title": "発表タイトル",
    "subtitle": "サブタイトル",
    "author": "発表者",
    "date": "2026-05-15"
  },
  "slides": [
    {"type": "title"},
    {"type": "section", "title": "1. 背景"},
    {
      "type": "content",
      "title": "完全文ヘッドライン",
      "reference": "TS 38.211 §4.3.2",
      "body": [
        "通常の箇条書き行",
        "**強調**は Main 色（赤）で太字になる",
        {"kind": "callout", "tone": "main",   "text": "結論: 一行で言い切る"},
        {"kind": "callout", "tone": "assort", "text": "比較: 既存手法は ..."},
        {"kind": "callout", "tone": "accent", "text": "前提: ..."}
      ],
      "notes": "演者ノート"
    },
    {
      "type": "table",
      "title": "比較表",
      "reference": "TS 38.211 Table 4.3.2-1",
      "headers": ["列A", "列B"],
      "rows": [["値1", "値2"], ["値3", "値4"]]
    }
  ]
}
```

スライド型と意味:

| `type`    | 用途 | 必須 | 任意 |
|:---|:---|:---|:---|
| `title`   | 表紙（赤の細帯＋大タイトル） | （`metadata` から自動展開可） | `title` `subtitle` `author` `date` `notes` |
| `section` | セクション扉（中央に太いバー） | `title` | `notes` `reference` |
| `content` | 本文（箇条書き＋callout） | `title` | `body[]` `notes` `reference` |
| `table`   | 表（ヘッダ赤塗り、偶数行 Accent） | `title` `headers[]` `rows[][]` | `notes` `reference` |

各スライドのクローム:

- 上部: 高さ 0.7" の見出しバー（Main 色塗り、白タイトル）。右端 3" は参考文献欄（`reference`）
- 左下: 資料タイトル（`metadata.title`、Assort 色、10pt）
- 右下: ページ番号 `n / N`（Assort 色、10pt）。表紙は付かない

`body` 要素:

- 文字列 → 箇条書き行（先頭に `▪ `、`**…**` で Main 色強調）
- `{"kind": "bullet", "text": "..."}` → 上と同じ
- `{"kind": "callout", "tone": "main"|"assort"|"accent", "text": "..."}` → 塗りつぶしテキストボックス（高さ 0.7"）

連続する箇条書きは 1 つのテキストフレームにまとめられ、callout は順序通りに stacked される。

## 既存 pptx の構造を読み取る (inspect)

```bash
python tools/pptx/build_slides.py inspect slides/pptx/foo.pptx --out foo.json
```

出力 JSON は次の形:

```json
{
  "path": ".../slides/pptx/foo.pptx",
  "slide_size": {"width_inch": 13.333, "height_inch": 7.5, ...},
  "layouts": ["Title Slide", "Title and Content", ...],
  "slides": [
    {
      "index": 1,
      "layout": "Blank",
      "title": null,
      "body": ["...", "..."],
      "tables": [{"rows": [["..", ".."], ["..", ".."]]}],
      "shapes": [{"name": "...", "shape_type": "...", "text": [...]}],
      "notes": "..."
    }
  ]
}
```

`shape.name` が `__page_number__` のテキストボックスがフッタ右下のページ番号。

## 既存 pptx を改変する (apply)

操作 JSON を渡すと、既存 pptx に上書き（または別ファイル出力）で適用する。

```json
{
  "operations": [
    {"op": "append", "slide": {"type": "content", "title": "新規末尾", "body": ["..."]}},
    {"op": "insert", "index": 3, "slide": {"type": "section", "title": "2. 提案"}},
    {"op": "replace", "index": 5, "slide": {"type": "content", "title": "差替え", "body": ["..."]}},
    {"op": "delete", "index": 7},
    {"op": "move", "from_index": 4, "to_index": 2},
    {"op": "update_text", "index": 6, "find": "古い表現", "replace": "新しい表現"}
  ]
}
```

`index` はすべて **1-origin**。`update_text` は本文・表セル・ノートを横断して run 単位で置換し、置換数を返す。

```bash
python tools/pptx/build_slides.py apply slides/pptx/foo.pptx ops.json
```

`--out` を省略すると元 pptx を上書きする。新規追加スライド（`append` / `insert` / `replace`）は `--style` で指定したスタイル（既定: `default`）でクロームを再生成する。

## CLI 一覧

```bash
# 新規ビルド
python tools/pptx/build_slides.py build <spec.json> [--style default] [--out <pptx>]

# 既存 pptx → JSON
python tools/pptx/build_slides.py inspect <pptx> [--out <json>]

# 既存 pptx に操作適用
python tools/pptx/build_slides.py apply <pptx> <ops.json> [--style default] [--out <pptx>]

# スタイル一覧
python tools/pptx/build_slides.py list-styles
```

`<spec.json>` `<ops.json>` は `-` を渡すと標準入力から読む。

## エージェント運用フロー

新規作成:

1. ソース文書（MD・テキスト・既存ノート）を読む
2. 文脈を解釈して slides 配列を構成（強調は `**…**`、結論は `callout: main`、比較は `callout: assort`）
3. `build_slides.py build <spec.json>` を呼ぶ

修正:

1. `build_slides.py inspect <pptx>` で現状を JSON 化
2. 差分意図に応じて `operations` を組む
3. `build_slides.py apply <pptx> <ops.json>` を呼ぶ

source MD のフォーマットは固定しない。slides 配列を作る責務はエージェント側にある。

## テンプレ pptx を使う場合（任意）

`styles/<name>.pptx` を配置すると、PresentationBuilder の起点に使われる（マスタ・テーマフォント・ロゴ等）。配置がなければ python-pptx 既定マスタにフォールバックする。クロームはコード側で描画するため、テンプレを使わなくても見た目は完成する。

## 既知の限界

- 旧スライドを `delete` した後、リレーション（パーツ）の完全削除は最善努力。多くのビューワでは表示に影響しないが、最終提出前に PowerPoint で「未使用スライド」を確認するのが安全
- 図の自動生成は対象外。図は PowerPoint 側で挿入し、`update_text` 等で前後のテキストだけ更新する運用を想定
- `body` の callout は固定高さ 0.7"。長文を入れるとはみ出す可能性があるので、callout は **一行で言い切る** ことを徹底する（長文は箇条書き側で書く）
