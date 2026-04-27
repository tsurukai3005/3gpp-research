---
name: survey-topic
description: 指定したトピックを6軸で体系的に調査し、documents/ 配下の Markdown として記録する
user-invocable: true
---

# survey-topic

## モチベーション

新しい技術トピックに初めて触れるとき、断片的な情報を集めるだけでは知財の種は見えない。
6軸の問いを体系的に当てることで、**どこに実装制約ギャップがあるか**（= 特許の進歩性の源泉）を
初期調査の段階から浮かび上がらせる。

## 使い方

```
/survey-topic <トピック名>
```

## 入力と前提

- **必須入力**: トピック名（例: `Cell-Free Massive MIMO`、`GRAND decoding`）
- **前提条件**: なし（このスキルが新規トピックの起点）
- **実行不可の条件**: トピック名が曖昧すぎて検索クエリに変換できない場合 → ユーザーに具体化を求める

## 実行フロー

1. `framework/principles.md` を読み、6原則を確認する
2. `framework/axes/` 配下の全6ファイルを読み、各軸の問いかけを把握する
3. `framework/templates/survey-topic.md` を読み、7つの調査項目を確認する
4. `framework/sources.md` を読み、情報源の優先順位を確認する
5. `framework/linking-policy.md` と `framework/references-policy.md` を読み、保存規則を確認する
6. **既存ノートのスキャン**: `documents/` を grep して関連する既存トピックを必ず先に探す（孤立ノートを生まないため）
7. 以下の優先順で情報を収集する:
   - **3GPP ポータル**: 該当する WI/SI の有無、Tdoc リスト、Chairman's Notes
   - **arXiv / IEEE**: 主要論文（引用数上位、直近2年）
   - **NGMN / ITU-R**: 要件文書での位置づけ
   - **ベンダーブログ**: Qualcomm / Ericsson / Nokia / Samsung の技術解説
8. **一次情報の Markdown 化**: 引用する論文・Tdoc・仕様書は `tools.md` に従って `references/` に MD 変換して保存する。命名は論文タイトル/寄書番号/arXiv ID をそのまま使う（`framework/references-policy.md`）
9. テンプレートの7項目で整理する:
   - 定義と背景（Why） / 技術要点（What） / 実装制約（How）
   - 前世代との差分 / 主要プレイヤー / 未解決課題 / 市場・知財余地
10. 6軸のうち該当する軸を frontmatter `axes:` に記録する
11. **前世代（3G/4G/5G）との対比**セクションが空にならないことを確認する
12. **Next Steps** を記載する（検索クエリ、文書番号、URL を含む具体的なアクション）
13. **ノートを `documents/<yymmdd>_<slug>.md` に保存する**（`status: draft`、`yymmdd` は今日の日付の年下2桁+月+日）
14. **リンクを必ず張る**:
    - 引用した references を frontmatter `references:` に wikilink で列挙
    - 関連既存ノートを `up`（最も近い親 1本）と `related`（兄弟）に列挙
    - 本文中でも初出の関連トピックは `[[260420_NRフレーム構造とリソースブロックの進化まとめ|フレーム構造]]` のように wikilink で言及する
    - 親ノート側にも逆方向の `[[新規ノート]]` を追記する（双方向リンク）

**情報が不十分な場合**: 見つからなかった項目は `[要確認]` と明記し、Next Steps に調査方法を記載する。空欄のまま放置しない。

## 出力

- **形式**: ファイル保存 + チャットにサマリー表示
- **保存先**: `documents/<yymmdd>_<slug>.md`（フラット、サブフォルダ禁止）
- **frontmatter**: `framework/skill-contract.md` の共通スキーマに準拠（`up` / `related` / `references` を埋める）
- **status**: `draft`

## このスキル固有の注意点

- **粒度の判断**: 1トピック = 1つの独立した技術概念。「MIMO」は広すぎ、「Cell-Free Massive MIMO のパイロット汚染対策」は狭すぎ。「Cell-Free Massive MIMO」程度が適切
- **3GPP 情報が存在しない場合**: 学術段階のトピックでも調査可能。「3GPP での議論状況: なし（学術段階）」と明記する
- **フォルダ分けはしない**: ノートはすべて `documents/` 直下に置く。カテゴリ分けは将来必要になってから判断する

## 関連スキル

- → `/analyze-gap` — 調査結果から具体的なギャップを抽出
- → `/digest-paper` — 調査中に見つけた重要論文の詳細分析
- → `/connect-dots` — 他トピックとの相乗効果を探索