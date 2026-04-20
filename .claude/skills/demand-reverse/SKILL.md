---
name: demand-reverse
description: ペルソナの課題（ペインポイント）から解決候補となる技術トピックを逆引きする
user-invocable: true
---

# demand-reverse

## 使い方

```
/demand-reverse <persona-file> <pain-point>
```

例:
```
/demand-reverse personas/regions/southeast-asia.md カバレッジコスト
/demand-reverse personas/industries/mno-operator.md エネルギー消費
/demand-reverse personas/stakeholders/operator-cxo.md 5G投資回収
```

## 手順

1. `00_framework/templates/demand-reverse.md` を読み、分析手順を確認する
2. 指定されたペルソナファイル（`00_framework/personas/`）を読む
3. ペルソナのペインポイント、重視する価値軸、技術への関心を把握する
4. `10_topics/` の全トピックをスキャンし、各トピックの axes を確認する
5. ペインポイントとの適合度を以下の基準で評価する:
   - 直接的関連性（ペインポイントを直接解決するか）
   - 成熟度（3GPP での議論段階）
   - 実装実現性（ペルソナの制約で実現可能か）
   - 代替手段の有無
6. 適合度の高い順にランク付けして出力する
7. **調査提案**: 各候補について次に調べるべき情報源を具体的に提案する
8. **未カバー領域**: `10_topics/` にまだノートがないが関連しそうな技術を特定する
9. 保存する場合は `40_ideas/YYYY-MM-DD__demand-reverse__persona-slug.md` に保存

## 重要な視点

- 「技術的に最適」ではなく「このペルソナにとって現実的に導入可能」かどうかを重視する
- コスト制約、インフラ状況、政策環境を考慮する
- 5G で同様のアプローチが試みられて失敗した例がないかを確認する
