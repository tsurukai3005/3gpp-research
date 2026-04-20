---
name: survey-topic
description: 指定したトピックを6軸で体系的に調査し、10_topics/ 配下の Markdown として記録する
user-invocable: true
---

# survey-topic

## 使い方

`/survey-topic <トピック名>` で起動。

## 手順

1. `00_framework/principles.md` を読み、不変原則を確認する
2. `00_framework/axes/` 配下の全軸ファイルを読み、各軸の問いかけを把握する
3. `00_framework/templates/survey-topic.md` を読み、調査項目を確認する
4. `00_framework/sources.md` の情報源から優先順に情報を収集する:
   - まず 3GPP ポータル / arXiv を確認
   - 次に NGMN / ITU-R の要件文書
   - 次にベンダー（Qualcomm/Ericsson/Nokia/Samsung）の技術ブログ
5. テンプレートの7項目（定義と背景 / 技術要点 / 実装制約 / 前世代との差分 / 主要プレイヤー / 未解決課題 / 市場・知財余地）で整理する
6. 6軸のうち該当する軸を frontmatter `axes:` に記録する
7. **過去世代（3G/4G/5G）との対比**を必ず1セクション設ける
8. **Next Steps**（次に調べるべきこと）を必ず記載する
9. 結果を `10_topics/<category>/<slug>.md` に保存する（`status: draft`）
10. 関連する他のトピックへのリンクを `related:` に追加する

## 禁止事項

- 一次情報の URL なしに事実を記載しない
- 不確実な情報は `[要確認]` と明示する
- 論文の理想仮定を無批判に受け入れない（原則2を常に意識）
