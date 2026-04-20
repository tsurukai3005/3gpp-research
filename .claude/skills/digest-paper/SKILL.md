---
name: digest-paper
description: 論文を読み、3GPP実装制約との差分を強調した構造化メモを 50_sources/papers/ に保存する
user-invocable: true
---

# digest-paper

## 使い方

`/digest-paper <論文の URL or タイトル>` で起動。

## 手順

1. 論文の内容を取得する（URL、PDF、またはユーザーからの情報提供）
2. `00_framework/templates/paper-digest.md` を読み、抽出項目を確認する
3. 以下を抽出する:
   - メタ情報（著者/年/会議/DOI）
   - 主張（Contribution）を 3-5 点で要約
   - **前提仮定**を明示的にリスト化
   - **3GPP 実装時のギャップ**（最重要：前提仮定 vs NR 仕様の制約の差をテーブルで記述）
4. 該当する `10_topics/<slug>.md` の `related` セクションにリンクを追記する
5. **Next Steps**（この論文を踏まえて次に調べるべきこと）を記載する
6. `50_sources/papers/YYYY-MM-DD__author__slug.md` に保存する（`status: draft`）

## 最重要ルール

**「前提仮定 vs 3GPP 実装制約のギャップ」セクションに最も注力する。**
ここが特許の進歩性の源泉（原則2）。
