# /status — 研究ノート全体の状態確認

全ノートの status / confidence を一覧表示し、陳腐化や未レビュー、リンク健全性を可視化する。

## 手順

1. `documents/` および `references/` 配下の全 `.md` ファイル（README.md 除く）をフラットに走査する
2. 各ファイルの frontmatter から `status`, `confidence`, `updated`, `up`, `related` を抽出する
3. 各ファイルの本文を読んで `[[...]]` wikilink の数を数え、リンク切れ（実在しない wikilink）と孤立ノート（被リンクも発リンクも 0 のノート）を検出する
4. 以下の形式で一覧を出力する

## 出力フォーマット

```markdown
## 研究ノート ステータス一覧（YYYY-MM-DD 時点）

### 要注意
| ファイル | status | confidence | 最終更新 | リンク数 | 備考 |
|:---|:---|:---|:---|:---|:---|
| 260101_xxx.md | draft | low | 2026-01-15 | 0 | 孤立ノート / 3ヶ月以上未更新 |

### documents/（自分の調査ノート）
| ファイル | status | confidence | 最終更新 | up | リンク数 |
|:---|:---|:---|:---|:---|:---|
| 260421_xxx.md | reviewed | medium | 2026-04-21 | [[260420_yyy]] | 4 |

### references/（一次情報）
| ファイル | type | accessed | 被リンク数 |
|:---|:---|:---|:---|
| arXiv-2508.08225.md | paper | 2026-04-21 | 2 |

### 統計
- 全ノート数: documents N / references M
- draft: N / reviewed: N / stable: N / obsolete: N
- confidence low: N / medium: N / high: N
- 3ヶ月以上未更新: N
- 孤立ノート: N
- リンク切れ: N
```

## 「要注意」の判定基準

- `status: draft` かつ `updated` が 30 日以上前
- `status: reviewed` かつ `updated` が 90 日以上前
- `confidence: low` のまま 60 日以上経過
- frontmatter に `status` や `axes` が欠落している
- **孤立ノート**（`up` も `related` も空、かつ本文中の wikilink が 0、かつ被リンクが 0）
- **リンク切れ**（本文または frontmatter の `[[...]]` が実ファイルを指していない）
- references から1つも引用されていないノートで `sources` が外部 URL のみの場合（要 references 化検討）
