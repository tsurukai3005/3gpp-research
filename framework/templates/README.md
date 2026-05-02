# templates — 問いかけテンプレート（Map of Content）

スキル（[[../../.claude/skills|.claude/skills/]]）が参照する定型的な問いかけと出力フォーマット。
1スキル ≒ 1テンプレートで対応する。

## テンプレート一覧

| テンプレート | ファイル | 呼び出し元スキル | 主な内容 |
|:---|:---|:---|:---|
| トピック新規調査 | [[survey-topic]] | `/survey-topic` | 7項目の調査構造と frontmatter スキーマ |
| 論文読解 | [[paper-digest]] | `/digest-paper` | 主張・前提・3GPP 実装制約ギャップテーブル |
| ギャップ分析 | [[gap-analysis]] | `/analyze-gap` | Gap A/B/C の3バケット分類 |
| 世代比較 | [[generation-comparison]] | `/success-pattern` | 5列マトリクス（3G〜6G）と普及要因の問い |
| トピック間接続 | [[connect-dots]] | `/connect-dots` | 共通軸・相乗効果・矛盾の分析手順 |
| 需要逆引き | [[demand-reverse]] | `/demand-reverse` | ペルソナのペインから候補抽出 |
| TeX/Beamer スライド | [slide-tex/](slide-tex/) | `/render-tex-slides` | skeleton + slide-parts + presets。PPTX 系（`tools/pptx/`）と命名空間が分離されている |

## 関連

- 親: [[../README|framework/README]]
- 全スキル共通の出力規則: [[../skill-contract|skill-contract]]
- リンク・命名規則: [[../linking-policy|linking-policy]]、[[../references-policy|references-policy]]
- 評価軸: [[../axes/README|axes]] / [[../personas/README|personas]]

## テンプレートの追加・更新

- 追加: 新スキルを設けるときに本ディレクトリへ `<skill-name>.md` を置き、本ファイルの一覧に行を追加する
- 更新: 出力スキーマ（frontmatter のフィールドなど）を変更したら、対応するスキル `SKILL.md` 側の参照も同時に確認する
