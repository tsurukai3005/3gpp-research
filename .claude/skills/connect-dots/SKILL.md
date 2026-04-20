---
name: connect-dots
description: トピック間の相乗効果・矛盾・組合せ価値を発見し、考察メモを生成する
user-invocable: true
---

# connect-dots

## 使い方

```
/connect-dots <topic-a> <topic-b>
/connect-dots <topic-a> <topic-b> --persona <persona-file>
```

## 手順

1. `00_framework/templates/connect-dots.md` を読み、分析手順を確認する
2. `10_topics/` から指定された両トピックのノートを読む
3. **共通軸の比較**: 両トピックの frontmatter の axes を比較し、共通する値を特定する
4. **相乗効果の仮説**: 両トピックを組み合わせることで生まれる価値を仮説として生成する
   - 「A + B により [KPI] が改善される」形式で記述
5. **矛盾・トレードオフの検出**: 両トピックの前提や要件が矛盾する点を特定する
   - 「A は [X] を前提とするが、B は [Y] を要求する」形式で記述
6. **ペルソナ視点の評価**（`--persona` 指定時）:
   - 指定されたペルソナファイル（`00_framework/personas/`）を読む
   - その組合せがペルソナにとって価値があるか、コスト的に成立するかを評価
7. **Next Steps** を記載する
8. 結果を `40_ideas/YYYY-MM-DD__topicA-x-topicB.md` に保存する（`status: draft`）

## 考察の質を高めるための問い

- この組合せは単なる「足し算」か、それとも「掛け算」（相乗効果）か？
- この組合せを実現するために必要な前提条件は何か？
- この組合せに対して標準化の場で反対されそうな理由は何か？
  （必要に応じて `00_framework/lenses/standardization-dynamics.md` を参照）
