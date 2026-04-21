# /create-issue — GitHub Issue の作成

研究タスクを GitHub Issue として登録する。

## 使い方

```
/create-issue <タイトル>
/create-issue <タイトル> --label <ラベル>
```

## 手順

1. タイトルと内容を整理する
2. 適切なラベルを選択する（引数で指定がなければ自動判定）
3. `gh issue create` で Issue を作成する
4. 作成した Issue の URL を表示する

## ラベル体系

以下のラベルを使用する（未作成の場合は `gh label create` で作成する）:

| ラベル | 用途 | 色 |
|:---|:---|:---|
| `research` | トピック調査タスク | `#0075ca` |
| `analysis` | ギャップ分析・考察タスク | `#7057ff` |
| `meeting` | 会合関連タスク | `#008672` |
| `paper` | 論文読解タスク | `#e4e669` |
| `framework` | フレームワーク改善 | `#d73a4a` |
| `idea` | アイデア・仮説 | `#f9d0c4` |

## Issue テンプレート

```markdown
## 目的

[このタスクで何を明らかにしたいか]

## 背景

[なぜこのタスクが必要か、どのトピック/会合/論文に関連するか]

## やること

- [ ] [具体的なアクション1]
- [ ] [具体的なアクション2]

## 関連ファイル

- `documents/...`
- `documents/...`

## 該当する軸

[technology_layer / generation / value / market / adoption / ip]
```

## 自動判定のルール

タイトルや内容から以下を推定する:
- 「調査」「survey」→ `research`
- 「分析」「gap」「比較」→ `analysis`
- 「会合」「RAN1」「FFS」→ `meeting`
- 「論文」「paper」「arXiv」→ `paper`
- 「アイデア」「仮説」「組合せ」→ `idea`
