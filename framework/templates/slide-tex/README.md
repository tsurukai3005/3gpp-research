# framework/templates/slide-tex — TeX/Beamer スライドテンプレ

`/render-tex-slides` が参照する LaTeX/Beamer のテンプレート群。
PPTX 側の対応物は [`tools/pptx/`](../../../tools/pptx/) と
[`framework/slide-styles-pptx.md`](../../slide-styles-pptx.md) であり、
両系統は **テンプレ・出力先・スキル名・プリセット名前空間** がすべて分離されている。

| 区分 | TeX 系 | PPTX 系 |
|:---|:---|:---|
| テンプレ | `framework/templates/slide-tex/`（このディレクトリ） | `tools/pptx/styles/`、`tools/pptx/styles-meta/` |
| 出力ルート | `slides/tex/<yymmdd>_<slug>/` | `slides/pptx/<title>.pptx` |
| スキル | `/render-tex-slides` | `/build-presentation` 経由で `tools/pptx/build_slides.py` |
| プリセット | `tex.ja-aspect43-9pt` 等 | `default`（PPTX 側のスタイル名） |

## 1. ディレクトリ構成

```
framework/templates/slide-tex/
├── README.md                          このファイル
├── CHANGELOG.md                       テンプレ変更履歴
├── skeleton/
│   ├── main.tex.template              親ファイル雛形（プレースホルダ <<NAME>>）
│   ├── latexmkrc                      lualatex 固定、.latex-cache/ に中間隔離
│   └── .gitignore                     ビルド成果物を git 追跡外にする
├── slide-parts/                       1スライド=1テンプレートの定型パーツ
│   ├── title.tex.template             表紙
│   ├── agenda.tex.template            目次（enumerate 可変長）
│   ├── plain.tex.template             単一カラム本文
│   ├── two-column.tex.template        2カラム本文
│   ├── image-with-caption.tex.template 画像＋キャプション
│   ├── table.tex.template             表（booktabs）
│   ├── equation-focus.tex.template    数式中心
│   └── qa.tex.template                standout（質疑応答）
├── presets/
│   ├── ja-aspect43-9pt.yaml           日本語/4:3/9pt（既定。master 発表互換）
│   ├── ja-aspect169-11pt.yaml         日本語/16:9/11pt
│   └── ja-haranoaji-only.yaml         筑紫B丸ゴシック未導入環境向け
└── assets/metropolistheme/            Metropolis dtx をベンダする場合の予約場所
```

## 2. プレースホルダ規約

- すべてのテンプレートはプレースホルダ `<<NAME>>` 形式を使う（`{{ }}` 形式は採用しない。Mustache 等の処理系を前提にしないため、本文中のブレースと衝突しない）。
- スキル `/render-tex-slides` がプレースホルダを置換する。手書きで埋める場合は `manifest.yaml` で `source: manual` に切り替えれば本ファイル群は読まれない。
- 既知のプレースホルダ:

| プレースホルダ | 出現箇所 | 値の出どころ |
|:---|:---|:---|
| `<<ASPECT_RATIO>>` | skeleton | preset.skeleton.aspect_ratio |
| `<<BASE_FONT_SIZE>>` | skeleton | preset.skeleton.base_font_size |
| `<<JA_FONT_PRESET>>` | skeleton | preset.skeleton.ja_font_preset |
| `<<LATIN_SANS_FONT>>` | skeleton | preset.skeleton.latin_sans_font |
| `<<LATIN_MONO_FONT>>` | skeleton | preset.skeleton.latin_mono_font |
| `<<TITLE>>` `<<SUBTITLE>>` `<<AUTHOR>>` `<<INSTITUTE>>` `<<DATE>>` | skeleton, slide-parts/title | manifest.yaml.metadata |
| `<<SLIDE_INPUTS>>` | skeleton | manifest.yaml.slides[] の id を `\input{parts/<id>}` に展開 |
| `<<HEADLINE>>` | 全 slide-parts | ソースノートの `## Slide N: <headline>` |
| `<<BODY>>` | plain | 箇条書き / 段落の LaTeX 化 |
| `<<LEFT_BODY>>` `<<RIGHT_BODY>>` | two-column | カラム左右の本文 |
| `<<AGENDA_ITEMS>>` | agenda | `\item ...` を改行区切り |
| `<<COL_SPEC>>` `<<HEADER_ROW>>` `<<BODY_ROWS>>` | table | Markdown 表の変換結果 |
| `<<EQUATION>>` `<<EXPLAIN>>` | equation-focus | 式本体と一行解説 |
| `<<IMAGE_PATH>>` `<<IMAGE_WIDTH>>` `<<CAPTION>>` | image-with-caption | 画像参照と幅と説明 |

## 3. スタイル原則

- フレームの装飾は **Metropolis テーマ**（赤バー・section スライド）を一次経路とする。独自フッタや色の追加は最小限に留める。
- 表は **booktabs** （`\toprule \midrule \bottomrule`）固定。罫線（`\hline`）は使わない。
- 図は `figures/` 配下に置き、`\graphicspath{{figures/}}` を skeleton に固定する。
- 数式は `amsmath` 環境（`equation*` / `align*`）。inline 内 `$ ... $` は許容。
- ハイパーリンクは `hyperref` で `colorlinks=true`、URL のみ青系。

## 4. プリセット選択

| プリセット | 用途 |
|:---|:---|
| `tex.ja-aspect43-9pt` | 既定。master 発表互換。9pt は情報量重視 |
| `tex.ja-aspect169-11pt` | プロジェクタ・画面共有でワイドスクリーンが要件のとき |
| `tex.ja-haranoaji-only` | TeX Live full のみ。筑紫B丸ゴシックが入っていない PC で動かす |

`/render-tex-slides <input> --preset <name>` で切替。指定がなければ `tex.ja-aspect43-9pt`。

## 5. 表生成（Markdown → booktabs）

`/render-tex-slides` がソースノートの Markdown 表を `slide-parts/table.tex.template` に流し込む。
変換ルールは [`.claude/skills/render-tex-slides/SKILL.md`](../../../.claude/skills/render-tex-slides/SKILL.md) §「表変換」を参照。

## 6. 関連

- スキル: [`/render-tex-slides`](../../../.claude/skills/render-tex-slides/SKILL.md)
- 入力ノートを作るスキル: [`/build-presentation`](../../../.claude/skills/build-presentation/SKILL.md)
- 前提コマンド（`lualatex`, `latexmk`, フォント）: [`framework/tools.md`](../../tools.md)
- PPTX 系の対称ガイド: [`framework/slide-styles-pptx.md`](../../slide-styles-pptx.md)

## 7. 移植元

- [tsurukai/ML-Precoding-for-Cell-Free-MIMO/presentation/](https://github.com/tsurukai/ML-Precoding-for-Cell-Free-MIMO) — テンプレ構造とフォント設定の参考
