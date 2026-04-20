---
name: success-pattern
description: 過去世代（3G/4G/5G）の成功・失敗事例から普及要因を学び、6Gの検討課題に照射する
user-invocable: true
---

# success-pattern

## 使い方

`/success-pattern <トピック名>` で起動。

## 手順

1. `20_history/` 配下の世代別ノートを読む（あれば）
2. `00_framework/templates/generation-comparison.md` を読み、マトリクス構造を確認する
3. `00_framework/axes/05-adoption-factors.md` を読み、普及要因の5項目を確認する
4. 現在のトピックを過去世代に投影し、マトリクスを作成する
5. 普及要因軸を中心に以下を問う:
   - 4G LTE が成功した構造的要因はこのトピックでも機能するか？
   - 5G が苦戦した要因は繰り返されるか？
   - 事業者 ROI が成立するシナリオは何か？
6. 結論を「6G で成功するための条件」の形で3点に絞って出力する
7. **Next Steps** を記載する

## 参考情報源

- `00_framework/sources.md` の「市場・普及データ」セクション
- GSMA Intelligence, 5G Americas, Ericsson Mobility Report
- `20_history/cross-generation-lessons.md`（あれば）
