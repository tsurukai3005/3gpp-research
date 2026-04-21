# /status — 研究ノート全体の状態確認

全ノートの status / confidence を一覧表示し、陳腐化や未レビューを可視化する。

## 手順

1. `documents/`, `documents/`, `documents/`, `documents/`, `documents/` 配下の
   全 `.md` ファイル（README.md 除く）を走査する
2. 各ファイルの frontmatter から `status`, `confidence`, `updated` を抽出する
3. 以下の形式で一覧を出力する

## 出力フォーマット

```markdown
## 研究ノート ステータス一覧（YYYY-MM-DD 時点）

### 要注意
| ファイル | status | confidence | 最終更新 | 備考 |
|:---|:---|:---|:---|:---|
| ... | draft | low | 2026-01-15 | 3ヶ月以上未更新 |

### documents/
| ファイル | status | confidence | 最終更新 |
|:---|:---|:---|:---|
| mimo/cell-free-mmimo.md | reviewed | medium | 2026-04-10 |
| ... | ... | ... | ... |

### documents/
...

### 統計
- 全ノート数: N
- draft: N / reviewed: N / stable: N / obsolete: N
- confidence low: N / medium: N / high: N
- 3ヶ月以上未更新: N
```

## 「要注意」の判定基準

- `status: draft` かつ `updated` が 30 日以上前
- `status: reviewed` かつ `updated` が 90 日以上前
- `confidence: low` のまま 60 日以上経過
- frontmatter に `status` や `axes` が欠落している
