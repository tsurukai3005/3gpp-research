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
5. 以下の優先順で情報を収集する:
   - **3GPP ポータル**: 該当する WI/SI の有無、Tdoc リスト、Chairman's Notes
   - **arXiv / IEEE**: 主要論文（引用数上位、直近2年）
   - **NGMN / ITU-R**: 要件文書での位置づけ
   - **ベンダーブログ**: Qualcomm / Ericsson / Nokia / Samsung の技術解説
6. テンプレートの7項目で整理する:
   - 定義と背景（Why） / 技術要点（What） / 実装制約（How）
   - 前世代との差分 / 主要プレイヤー / 未解決課題 / 市場・知財余地
7. 6軸のうち該当する軸を frontmatter `axes:` に記録する
8. **前世代（3G/4G/5G）との対比**セクションが空にならないことを確認する
9. **Next Steps** を記載する（検索クエリ、文書番号、URL を含む具体的なアクション）
10. `documents/YYYY-MM-DD_<slug>.md` に保存する（`status: draft`）
11. 関連する既存トピックがあれば `related:` に追加する

**情報が不十分な場合**: 見つからなかった項目は `[要確認]` と明記し、Next Steps に調査方法を記載する。空欄のまま放置しない。

## 出力

- **形式**: ファイル保存 + チャットにサマリー表示
- **保存先**: `documents/YYYY-MM-DD_<slug>.md`
  - category: `mimo/`, `coding/`, `ai/`, `iot/` 等（既存カテゴリに合わせる。該当なければ新設）
- **frontmatter**: `framework/skill-contract.md` の共通スキーマに準拠
- **status**: `draft`

## このスキル固有の注意点

- **カテゴリの判断**: 既存の `documents/` 配下のディレクトリ構造を確認し、最も近いカテゴリに配置する。複数カテゴリにまたがる場合は主要な側に置き、`related:` で他方をリンクする
- **粒度の判断**: 1トピック = 1つの独立した技術概念。「MIMO」は広すぎ、「Cell-Free Massive MIMO のパイロット汚染対策」は狭すぎ。「Cell-Free Massive MIMO」程度が適切
- **3GPP 情報が存在しない場合**: 学術段階のトピックでも調査可能。「3GPP での議論状況: なし（学術段階）」と明記する

## 関連スキル

- → `/analyze-gap` — 調査結果から具体的なギャップを抽出
- → `/digest-paper` — 調査中に見つけた重要論文の詳細分析
- → `/connect-dots` — 他トピックとの相乗効果を探索