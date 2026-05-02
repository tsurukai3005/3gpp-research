# slide-tex テンプレ変更履歴

このファイルは `framework/templates/slide-tex/` 配下のテンプレ・プリセット・スケルトンに対する
**意味のある変更**だけを記録する。コミット履歴のミラーではない（細かい修正は git に任せる）。

## 2026-05-02

- 初版を作成。
- skeleton: `main.tex.template`, `latexmkrc`, `.gitignore` を配置（lualatex + Metropolis 前提、`.latex-cache/` で中間隔離）。
- slide-parts: `title`, `agenda`, `plain`, `two-column`, `image-with-caption`, `table`, `equation-focus`, `qa` の 8 種を追加。
- presets: `tex.ja-aspect43-9pt`（既定）, `tex.ja-aspect169-11pt`, `tex.ja-haranoaji-only` の 3 種を追加。
- assets/metropolistheme: ベンダ手順の README のみ配置。実体ファイルは未投入（TeX Live 同梱の Metropolis を一次経路とする方針）。
