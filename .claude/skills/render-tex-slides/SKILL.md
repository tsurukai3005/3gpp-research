---
name: render-tex-slides
description: 研究ノート（documents/<note>.md）から Beamer/Metropolis のスライドを生成し、latexmk で PDF までビルドする
user-invocable: true
---

# render-tex-slides

## モチベーション

`/build-presentation` Phase 4 の出力（`## Slide N: <headline>` 形式の Markdown）を、
**手動編集と共存可能な形で TeX/Beamer + PDF に変換する**。

PPTX 系（[`tools/pptx/build_slides.py`](../../../tools/pptx/build_slides.py)）が
構造化スペック JSON → pptx の決定論的変換を担うのに対し、本スキルは
**LaTeX の柔軟さを保ちつつ、再生成しても手書きスライドが上書きされない**ことを優先する。

両系統は出力先・テンプレ・プリセット名前空間が完全に分離されている:

| 系統 | テンプレ | 出力 | スキル / ツール |
|:---|:---|:---|:---|
| TeX | `framework/templates/slide-tex/` | `slides/tex/<yymmdd>_<slug>/` | `/render-tex-slides`（本スキル） |
| PPTX | `tools/pptx/styles/` `tools/pptx/styles-meta/` | `slides/pptx/<title>.pptx` | `tools/pptx/build_slides.py` |

## 使い方

```
/render-tex-slides <documents/path.md>
/render-tex-slides <documents/path.md> --preset <name>
/render-tex-slides <documents/path.md> --slide <id|N>
/render-tex-slides <documents/path.md> --no-build
/render-tex-slides <documents/path.md> --dry-run
/render-tex-slides <documents/path.md> --rebuild-manifest
```

| フラグ | 既定 | 用途 |
|:---|:---|:---|
| `--preset <name>` | `tex.ja-aspect43-9pt` | プリセット選択。値は `framework/templates/slide-tex/presets/*.yaml` の `name` |
| `--slide <id\|N>` | — | 特定スライドだけ再生成。`id` は `parts/<id>.tex` のステム、`N` は manifest の 1-origin インデックス |
| `--no-build` | False | 自動 `latexmk` を抑制。生成のみ |
| `--dry-run` | False | 何を書き換えるかチャットに表示し、ファイルは触らない |
| `--rebuild-manifest` | False | 既存 `manifest.yaml` を破棄して再生成。`source: manual` のスライドは保護対象として再列挙される |

## 入力と前提

- **必須入力**: `documents/<note>.md`。`/build-presentation` Phase 4 の出力もしくは同等構造（後述 §「ソースノートの読取仕様」）
- **環境前提**: `lualatex --version` と `latexmk --version` が PATH 上で実行可能。詳細は [`framework/tools.md`](../../../framework/tools.md) §「3. lualatex / latexmk」
- **テンプレ**: [`framework/templates/slide-tex/`](../../../framework/templates/slide-tex/) が存在（リポジトリに同梱）
- **実行不可の条件**:
  - ソースに `## Slide N: <headline>` セクションが 1 件もない → エラー終了し、`/build-presentation --phase 4` を案内
  - `lualatex` が見つからない → `framework/tools.md` の導入手順を案内し停止

## 実行フロー

### 1. 環境前提チェック

1. `lualatex --version` と `latexmk --version` を Bash で実行。stderr/stdout に出力があれば成功とみなす
2. 失敗した場合、`framework/tools.md` の該当手順を 1 ブロック引用してチャットに出し、ここで停止

### 2. 出力先の決定

ソースノートのパスから出力先を決める:

- ソース: `documents/<yymmdd>_<slug>.md`
- 出力先: `slides/tex/<yymmdd>_<slug>/`
  - `<yymmdd>` はソースの frontmatter `created`（YYYY-MM-DD）の年下2桁+月+日
  - `<slug>` はソースのファイル名から `<yymmdd>_` を取り除いた残り（拡張子なし）
- 既存ディレクトリがあれば再利用。なければ作成

### 3. skeleton の展開（初回または --rebuild-manifest 時のみ）

[`framework/templates/slide-tex/skeleton/`](../../../framework/templates/slide-tex/skeleton/) を出力先に複製:

- `main.tex.template` → `<出力先>/main.tex`（プレースホルダ未置換のまま。後続ステップで Edit）
- `latexmkrc` → `<出力先>/latexmkrc`（そのまま）
- `.gitignore` → `<出力先>/.gitignore`（そのまま）
- `<出力先>/parts/`、`<出力先>/figures/` ディレクトリを作成

### 4. ソースノートの読取とパース

ソース `documents/<note>.md` を最初から最後まで読み、以下を順に解釈する:

1. **frontmatter**: `title`, `audience`, `takeaway`, `duration_min`, `source_notes`, `venue`, `format` を取得
2. **`## Slide N: <headline>` 単位で本文を分割**。N と headline を抽出
3. 各スライド内の任意のメタ部:
   - `### 視覚コンテンツ` → 画像参照（`![alt](path)`）と図キャプション
   - `### 原稿`（推定時間表記を含んでよい） → 話者原稿。`<出力先>/原稿.md` に集約
   - `### 補足` → トランジション・Q&A 想定・注記。話者原稿に併合
   - `### スライド種別` → `type:` 明示（あれば優先）
4. **本文**: テキスト・箇条書き・Markdown 表を抽出
5. **画像**: `![alt](path)` を `\includegraphics[width=<width>\linewidth]{<basename>}` に変換。パスは `<出力先>/figures/` の相対参照に正規化。ファイルが未配置でも警告のみ（ビルドエラーにしない）

### 5. スライド種別の判定

`### スライド種別` で明示されていればそれを採用。なければ次の優先順で自動判定:

| 判定条件 | 採用テンプレ |
|:---|:---|
| Slide 1 | `title` |
| headline に「目次」「Agenda」を含む | `agenda` |
| 本文に Markdown 表（`\| ... \| ... \|` のヘッダ＋アライン行）が含まれる | `table` |
| 画像参照のみで本文 ≤ 50 文字 | `image-with-caption` |
| `\begin{equation}` 風の数式が支配的（数式行 ≥ 本文の 50%） | `equation-focus` |
| `### 左 \| ### 右` または `\|\|\|` 区切りが明示 | `two-column` |
| 最終スライドで headline が「Q&A」「Thank you」 | `qa` |
| その他 | `plain` |

### 6. manifest.yaml の生成 / 反映

`<出力先>/manifest.yaml` の有無で分岐:

- **存在しない、または `--rebuild-manifest`** → ソースの全スライドを `source: generated` で並べた manifest を生成
- **既存** → 読み込み、ソース側で `## Slide N` の数や順序が変化していたら次の規則で更新する:
  - manifest にあるが source から消えた id → 削除候補。チャットでユーザに確認してから削る（`--dry-run` ならチャットに警告するだけ）
  - source にあるが manifest にない → 末尾に `source: generated` で追加
  - 順序の差し替えはユーザの操作と見做して manifest を優先する

manifest の `source` 値:

| 値 | 振る舞い |
|:---|:---|
| `generated` | ソースノートの内容で毎回 `parts/<id>.tex` を上書き |
| `manual` | スキルは絶対に上書きしない。`from_section` も無視 |
| `frozen` | 既存 `parts/<id>.tex` を保持。ソースが更新されても再生成しない。`frozen_at:` フィールドにフリーズ日付を記録 |

manifest の最小スキーマ:

```yaml
preset: tex.ja-aspect43-9pt
metadata:
  title: "発表タイトル"
  subtitle: ""
  author: "発表者氏名"
  institute: "所属"
  date: "2026-05-15"
slides:
  - id: 01_title
    source: generated
    type: title
    from_section: null
  - id: 02_agenda
    source: generated
    type: agenda
    from_section: "## Slide 2: 目次"
  - id: 03_<headline-slug>
    source: generated
    type: plain
    from_section: "## Slide 3: ..."
```

`id` は `<NN>_<headline_slug>` の形（NN は 2 桁ゼロ埋め、headline_slug は ASCII 化したヘッドライン or 連番）。`source: manual` のスライドは `from_section: null` でよい。

### 7. parts/<id>.tex の生成

manifest の各エントリについて `source: generated` のものだけ:

1. `framework/templates/slide-tex/slide-parts/<type>.tex.template` を読む
2. 該当する `from_section` の本文をパースしてプレースホルダ `<<NAME>>` を埋める
3. `<出力先>/parts/<id>.tex` に書き出す

`source: manual` / `source: frozen` のスライドは **絶対に書き換えない**（既存ファイルを開かず Read もしない。誤上書きの根本予防）。

#### 表変換（`type: table`）

ソースの Markdown 表を以下のルールで booktabs に変換する:

| Markdown | LaTeX |
|:---|:---|
| `:---` | `l`（左寄せ） |
| `---:` | `r`（右寄せ） |
| `:---:` | `c`（中央寄せ） |
| `**text**` | `\textbf{text}` |
| `*text*` | `\emph{text}` |
| `` `code` `` | `\texttt{code}` |
| `\|` のエスケープ | `|` |

例:

```markdown
| 手法 | 性能 | 備考 |
|:---|---:|:---:|
| MMSE | 1.40 | 従来 |
| DU-MMSE | **1.61** | 提案 |
```

→ template 展開後:

```latex
\begin{frame}{<headline>}
\centering
\begin{tabular}{lrc}
\toprule
手法 & 性能 & 備考 \\
\midrule
MMSE & 1.40 & 従来 \\
DU-MMSE & \textbf{1.61} & 提案 \\
\bottomrule
\end{tabular}
\end{frame}
```

### 8. main.tex の組み立て

skeleton の `main.tex` を以下で更新する:

- preset YAML の `skeleton.*` を読み、`<<ASPECT_RATIO>>` `<<BASE_FONT_SIZE>>` `<<JA_FONT_PRESET>>` `<<LATIN_SANS_FONT>>` `<<LATIN_MONO_FONT>>` を置換
- `manifest.yaml.metadata` から `<<TITLE>>` `<<SUBTITLE>>` `<<AUTHOR>>` `<<INSTITUTE>>` `<<DATE>>` を置換
- `<<SLIDE_INPUTS>>` を manifest の `slides[]` 順に並べた `\input{parts/<id>}` に展開（行ごと改行）

### 9. 自動ビルド

`--no-build` が指定されていない場合、出力ディレクトリ内で次を実行:

```bash
cd <出力先>
latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error
```

- 成功時: 生成された PDF の絶対パスをチャットに 1 行で報告（`<出力先>/main.pdf`）
- 失敗時: ビルドログ（`.latex-cache/main.log`）から最初の `! ` 行 1 件と、その前後 3 行を抽出して提示。ログ全文は提示しない
- いずれの場合も `.latex-cache/` 配下のファイルは git 追跡外（`.gitignore` 同梱）

### 10. 結果報告

チャットに以下を 1 ブロックで提示:

```
出力先: slides/tex/<yymmdd>_<slug>/
manifest: <変更なし | 新規生成 | N 件追加 / M 件更新>
parts: <X 件 generated / Y 件 manual 保護 / Z 件 frozen 保護>
ビルド: <成功: <絶対パス> | 失敗: <抽出ログ> | 抑制(--no-build)>
画像未配置警告: [<相対パス>, ...] （無ければ省略）
```

## 出力

- **形式**: ファイル群（チャットには結果報告のみ）
- **保存先**: `slides/tex/<yymmdd>_<slug>/` 直下
  - `main.tex`, `latexmkrc`, `.gitignore`, `manifest.yaml`, `parts/*.tex`, `figures/`（空でよい）, `原稿.md`（任意）
  - `main.pdf` は **git 追跡外**（`.gitignore` で除外）
- **frontmatter**: 出力ファイルそのものは `.tex` / `.yaml` であり Obsidian frontmatter は不要。ソースノートの frontmatter は変更しない

## このスキル固有の注意点

1. **manifest.yaml は single source of truth**。`source: manual` / `frozen` を絶対に上書きしない。再生成・並べ替え・差し込みは manifest を経由する
2. **プレースホルダは `<<NAME>>` 形式に固定**。本文中のブレース `{}` と衝突しないため Mustache は採用しない
3. **手書きスライドの保護**: `parts/<id>.tex` を Read してから書き換えるのは `source: generated` のときだけ。`manual` / `frozen` の場合は Read もせず触らない（誤上書きの根本予防）
4. **画像未配置を理由に止めない**: `\graphicspath{{figures/}}` の解決失敗は警告のみ。発表者がローカルで図を配置してから再ビルドする運用
5. **PPTX 系と混在しない**: 出力先・テンプレ・プリセット・スキル名のいずれも PPTX 側と分離されている。PPTX が必要な場合は `/build-presentation` の Phase 4 後段で `tools/pptx/build_slides.py` を呼ぶ
6. **思考工程をスキップしない**: ソースノートに `## Slide N` 形式の構造ができていない場合は、本スキルではなく `/build-presentation --phase 4` を先に走らせる
7. **`/review` の対象**: 本スキル・本テンプレ群はリポジトリの `/review` 対象に含める。`slides/tex/**` の生成物は対象外

## 関連スキル

- 前段: [`/build-presentation`](../build-presentation/SKILL.md) — Phase 4 でソースノート（`## Slide N` 構造）を生成
- 並列: `tools/pptx/build_slides.py` — PPTX で同等の出力が要るときの代替経路
- 参照: [`framework/templates/slide-tex/README.md`](../../../framework/templates/slide-tex/README.md) — テンプレ・プレースホルダ規約
- 参照: [`framework/tools.md`](../../../framework/tools.md) — `lualatex` / `latexmk` / フォントの導入
