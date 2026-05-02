# /create-issue — Create a GitHub Issue / GitHub Issue の作成

Register a research task as a GitHub Issue.

## Usage

```
/create-issue <title>
/create-issue <title> --label <label>
```

## Steps

1. Organize the title and body
2. Choose an appropriate label (auto-detect if not given as an argument)
3. Create the issue via `gh issue create`
4. Display the URL of the created issue

## Label scheme

Use the following labels (create with `gh label create` if missing):

| ラベル | 用途 | 色 |
|:---|:---|:---|
| `research` | トピック調査タスク | `#0075ca` |
| `analysis` | ギャップ分析・考察タスク | `#7057ff` |
| `meeting` | 会合関連タスク | `#008672` |
| `paper` | 論文読解タスク | `#e4e669` |
| `framework` | フレームワーク改善 | `#d73a4a` |
| `idea` | アイデア・仮説 | `#f9d0c4` |

## Issue template

```markdown
## 目的

[このタスクで何を明らかにしたいか]

## 背景

[なぜこのタスクが必要か、どのトピック/会合/論文に関連するか]

## やること

- [ ] [具体的なアクション1]
- [ ] [具体的なアクション2]

## 関連ファイル

- `documents/<yymmdd>_<slug>.md`
- `references/<原文番号 or タイトル>.md`

## 該当する軸

[technology_layer / generation / value / market / adoption / ip]
```

## Auto-detection rules

Infer from the title or body:
- 「調査」「survey」 → `research`
- 「分析」「gap」「比較」 → `analysis`
- 「会合」「RAN1」「FFS」 → `meeting`
- 「論文」「paper」「arXiv」 → `paper`
- 「アイデア」「仮説」「組合せ」 → `idea`