# 外部ツールの運用ガイド

調査・分析の前段で使う外部ツールの呼び出し手順。
スキル（`.claude/skills/*`）から参照される実装ガイド。

---

## 1. pandoc — Word/HTML をテキスト化する

### 1.1 何のために使うか

3GPP の Chair Notes、提案書（Tdoc）、論文の多くは **`.docx` / `.pdf`** で配布される。
バイナリのまま AI に渡すと:

- 読み込み時間がかかる
- 表構造が崩れて誤読する
- ツール側で開けない/部分的にしか読めないことがある

> **ルール**: `.docx` / `.pptx` / `.odt` / `.rtf` を読む前に、必ず pandoc で Markdown 化してから Read / Grep する。
> PDF は pandoc では崩れやすいため、テキスト抽出が主目的なら `pdftotext`（poppler-utils）を優先する。

### 1.2 インストール先（Windows）

- 実行ファイル: `C:\Program Files\Pandoc\pandoc.exe`
- ユーザー PATH に登録済み（2026-04-27 設定）→ 新しいシェルから `pandoc` で直接呼べる
- バージョン確認: `pandoc --version`

### 1.3 コマンド一覧（コピペ用）

| 目的 | コマンド |
|:---|:---|
| 標準変換（最小） | `pandoc input.docx -o output.md` |
| **3GPP 文書向け推奨** | `pandoc input.docx -t gfm --wrap=none --extract-media=./media -o output.md` |
| 本文の改行は維持したい | `pandoc input.docx -t gfm --extract-media=./media -o output.md` |
| 画像を埋め込まず捨てる | `pandoc input.docx -t gfm --wrap=none -o output.md` |
| 標準出力に流す（ファイル化しない） | `pandoc input.docx -t gfm --wrap=none` |
| ディレクトリ内 docx を一括変換 | `for f in *.docx; do pandoc "$f" -t gfm --wrap=none -o "${f%.docx}.md"; done` |

### 1.4 オプションの意味

- `-t gfm` … GitHub Flavored Markdown 出力（表が崩れにくい）
- `--wrap=none` … 自動改行を無効化（grep / AI 読込の精度向上）
- `--extract-media=./media` … 画像を `./media/` に展開、Markdown 内は相対パス参照
- `-o file.md` … 出力先指定。省略時は標準出力

### 1.5 Claude が docx を扱う標準フロー

1. ファイル名から元拡張子を控える（例: `R1-2503456.docx`）
2. 同ディレクトリに `.md` を生成する:

   ```bash
   pandoc R1-2503456.docx -t gfm --wrap=none --extract-media=./media -o R1-2503456.md
   ```

3. 以降の Read / Grep は `.md` に対して行う
4. 生成した `.md` は分析の中間生成物。コミット要否はタスクの性質で判断する:
   - **コミット推奨**: Chair Notes の和訳元、長期参照する Tdoc 本文
   - **gitignore 推奨**: 一回読み捨ての一次情報

### 1.6 トラブルシュート

| 症状 | 対処 |
|:---|:---|
| `pandoc: command not found` | 新しいシェル/ターミナルを開く（PATH 反映）。それでも出ない場合は `'/c/Program Files/Pandoc/pandoc.exe'` をフルパスで叩く |
| 表が `&nbsp;` だらけ | 元 docx が複雑なネスト表。`-t commonmark_x` を試す |
| 数式が崩れる | `--mathjax` を追加（HTML 経由で読む前提） |
| 日本語が文字化け | 入出力とも UTF-8 が前提。化ける場合は出力ファイルをエディタで UTF-8 として再保存 |

---

## 2. pdftotext — PDF から本文だけ抽出する

論文・3GPP TR/TS の本文だけ素早く欲しい場合は、pandoc の PDF 入力より `pdftotext` の方が速くて安定する。

> **ルール**: PDF を読むときは、まず `pdftotext -layout input.pdf -` で本文を確認する。
> docx 版が同梱されているなら、表の保持を優先して docx → pandoc を選ぶ。

### 2.1 インストール先（Windows）

確認済み（2026-04-27）。**追加インストール不要**:

| シェル | 実体 | バージョン |
|:---|:---|:---|
| Git Bash | `/mingw64/bin/pdftotext`（= `C:\Program Files\Git\mingw64\bin\pdftotext.exe`） | Xpdf 4.00 |
| PowerShell / cmd | `%USERPROFILE%\texlive\2025\bin\windows\pdftotext.exe`（TeXLive 2025 同梱） | Xpdf 派生 |

どちらも単に `pdftotext` で呼べる（PATH 通過済み）。

### 2.2 コマンド一覧（コピペ用）

| 目的 | コマンド |
|:---|:---|
| **論文向け（推奨）** | `pdftotext -layout input.pdf output.txt` |
| 標準出力に流す | `pdftotext -layout input.pdf -` |
| ページ範囲を指定 | `pdftotext -layout -f 1 -l 5 input.pdf -` |
| 表が中心の文書 | `pdftotext -table input.pdf output.txt` |
| 段組崩しを避ける（連続テキストが欲しい） | `pdftotext -raw input.pdf output.txt` |
| ページ区切りを入れない | `pdftotext -layout -nopgbrk input.pdf -` |

### 2.3 オプションの意味

- `-layout` … 元の物理レイアウトを保持（標準。論文・仕様書はまずこれ）
- `-table` … 表に最適化（多列の表が多い文書向け）
- `-raw` … コンテンツストリーム順。段組や注釈で本文が分断されるのを避けたいとき
- `-f N -l M` … N〜M ページのみ抽出（巨大 TS の Section 取り出し）
- `-nopgbrk` … `\f`（フォームフィード）でのページ区切りを抑制
- `-enc UTF-8` … 出力エンコーディング指定（既定で UTF-8 だが化ける場合に明示）

### 2.4 制約と限界

- 同梱版は **Xpdf 4.00（2017）** で古い。日本語/CJK や複雑な合字で崩れることがある
- 3GPP 仕様の **表は `-layout` でも崩れる**。表が要るなら docx 版（あれば）を pandoc 経由で読む方が確実
- 暗号化 PDF は `-upw <password>` / `-opw <password>` を渡す
- スキャン PDF（画像のみ）は抽出不能 → OCR が別途必要（本ガイドの範囲外）

### 2.5 もっと精度が必要なとき（任意アップグレード）

CJK / 複雑レイアウトで頻繁に崩れる場合は、Poppler 版 pdftotext に乗り換える:

```bash
winget install --id oschwartz10612.Poppler
```

導入後、PowerShell から PATH を追加（ユーザー環境変数）:

```powershell
$p = "$env:LOCALAPPDATA\Microsoft\WinGet\Links"  # winget 既定の shim パス
$u = [Environment]::GetEnvironmentVariable('Path', 'User')
if (($u -split ';') -notcontains $p) { [Environment]::SetEnvironmentVariable('Path', "$u;$p", 'User') }
```

> **判断基準**: Xpdf 版で 2 回以上連続して崩れたら Poppler 検討。それまでは標準の Xpdf 同梱版で十分。

---

## 3. lualatex / latexmk — TeX/Beamer スライドをビルドする

### 3.1 何のために使うか

[`/render-tex-slides`](../.claude/skills/render-tex-slides/SKILL.md) が
`framework/templates/slide-tex/` のテンプレを展開した後、`slides/tex/<yymmdd>_<slug>/` を
ビルドして PDF を生成するために使う。

> **ルール**: `/render-tex-slides` を呼ぶ前に `lualatex --version` と `latexmk --version` の
> 双方が成功することを確認する。失敗する場合は本節の手順で導入し、それまではスキルを実行しない。

### 3.2 インストール先（Windows）

確認済み（2026-04-27）— **TeX Live 2025 を `%USERPROFILE%\texlive\2025\` に導入済み**:

| 実体 | 用途 |
|:---|:---|
| `%USERPROFILE%\texlive\2025\bin\windows\lualatex.exe` | LuaLaTeX 本体 |
| `%USERPROFILE%\texlive\2025\bin\windows\latexmk.exe` | ビルドオーケストレーション |
| `%USERPROFILE%\texlive\2025\texmf-dist\tex\latex\beamer\` | Beamer クラス |
| `%USERPROFILE%\texlive\2025\texmf-dist\tex\latex\beamertheme-metropolis\` | Metropolis テーマ（既定） |

PATH 通過済み。Bash / PowerShell どちらからも `lualatex` / `latexmk` で呼べる。

### 3.3 コマンド一覧（コピペ用）

| 目的 | コマンド |
|:---|:---|
| **/render-tex-slides の標準ビルド**（中間ファイルは `.latex-cache/` に隔離） | `latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error` |
| ビルド成果物のクリーンアップ | `latexmk -C` |
| 中間ファイルだけ削除（PDF は残す） | `latexmk -c` |
| 単発の lualatex 実行（デバッグ用） | `lualatex -interaction=nonstopmode main.tex` |
| 失敗ログから最初のエラー行を抽出 | `grep -m1 -n "^!" .latex-cache/main.log` |
| エラー前後 3 行をまとめて見る | `grep -nC3 "^!" .latex-cache/main.log` |

### 3.4 フォント要件

既定プリセット `tex.ja-aspect43-9pt` は **筑紫B丸ゴシック**（OpenType、有償）を想定する。
未導入環境では以下のいずれかを選ぶ:

- プリセットを `tex.ja-haranoaji-only` に切り替える（TeX Live full のみで動く）
- 筑紫B丸ゴシックを OS にインストールしてから `luatexja-preset` の `tsukuxuB-mgothic` を読む

### 3.5 トラブルシュート

| 症状 | 対処 |
|:---|:---|
| `! LaTeX Error: File 'beamerthememetropolis.sty' not found` | TeX Live のフルインストールでない可能性。`tlmgr install beamertheme-metropolis pgfplots` |
| `! Package luatexja-preset Error: Font preset 'tsukuxuB-mgothic' not available` | 筑紫B丸ゴシック未導入。プリセットを `tex.ja-haranoaji-only` に切替 |
| `! Undefined control sequence \xx{}` のような単発エラー | parts/<id>.tex のプレースホルダ未置換が原因のことが多い。manifest の該当 id の `source` を確認 |
| ビルドが遅い（30 秒超） | 図ファイルのサイズが大きい、もしくは `-shell-escape` 系パッケージを多用している。プリセット側でパッケージを削るか、`figures/` の PDF を縮小 |
| 同じ文書を何度ビルドしても警告が消えない | `latexmk -C` で `.latex-cache/` を一度クリアしてから再ビルド |
