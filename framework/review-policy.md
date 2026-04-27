# レビューポリシー

## ステータスと確信度

全てのノートは frontmatter に以下を持つ:

```yaml
status: draft | reviewed | stable | obsolete
confidence: low | medium | high
```

- **status**: ファイルの成熟度（レビュープロセス上の位置）
- **confidence**: 内容への確信度（draft でも confidence: high はありうる）

## ステータス遷移

```
draft → reviewed → stable → obsolete
```

- スキルが生成するファイルは `status: draft` で始める
- ユーザーが確認したら `reviewed` に変更する
- 他ノートからの参照や考察の入力にする際は `reviewed` 以上を推奨
- 情報が古くなったら `obsolete` に変更する

## 現在のルール

- `draft` ファイルを引用する場合は `[draft]` と明記する
- それ以上の制約は現時点では設けない

## リンク健全性チェック（[linking-policy.md](./linking-policy.md)）

レビュー時に以下を確認する:

- ノートに最低1本の wikilink（本文中 or `up` / `related`）があるか
- 参照している `[[ファイル名]]` が実在するか（赤字 placeholder は `next:` に明記されているか）
- 引用している論文・Tdoc が `references/` に MD 化されているか、もしくは references 化対象外と判断できるか

## confidence の目安

| 値 | 意味 | 典型的な状況 |
|:---|:---|:---|
| high | 一次情報に直接基づく | TS/Tdoc の直接引用、査読済み論文の主張 |
| medium | 複数情報源から推論 | ベンダーブログの要約、複数論文の総合 |
| low | 仮説・推測を含む | 標準化動向の予測、市場の見通し |

## 将来の拡張余地

以下は現時点では実装しない。必要になったら本ファイルに追加する:

- 会合サイクルに連動したレビュートリガー
- obsolete の自動提案（更新日から N 日経過）
- レビューコメントの構造化フォーマット
- 複数人レビューのワークフロー
