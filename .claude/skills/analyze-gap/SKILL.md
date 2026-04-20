---
name: analyze-gap
description: 指定トピックについて学術/3GPP/実装制約のギャップを3バケットで可視化する
user-invocable: true
---

# analyze-gap

## 使い方

`/analyze-gap <トピック名>` で起動。

## 手順

1. 対象トピックの `10_topics/` ノートを読み込む
2. `00_framework/templates/gap-analysis.md` を読み、3バケットの定義を確認する
3. 最新の関連論文（arXiv）と 3GPP の該当 WI/SI の状況を確認する
4. ギャップを3バケットで分類する:
   - **Gap A**: 学術で解決済みだが 3GPP に未取込
   - **Gap B**: 3GPP FFS に残っており学術でも議論中（特許の最短距離）
   - **Gap C**: 実装制約ギャップ（進歩性の最大の源泉）
5. 各ギャップに知財軸（`00_framework/axes/06-ip.md`）の評価を付ける
6. **Next Steps** を記載する
7. 結果をチャットに出力する
8. 永続化する場合は `10_topics/<slug>/gap-YYYYMM.md` に保存する

## 重要な視点

- Gap C（実装制約ギャップ）に最も注力する
- `00_framework/axes/06-ip.md` の「論文の理想仮定 vs 3GPP の実装制約」テーブルを参照
- 「この論文のアイデアを OFDM フレーム構造に落とし込んだらどうなるか？」を常に問う
