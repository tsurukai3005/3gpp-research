# /pr-template — PR 説明文の生成

ブランチの変更内容を分析し、PR の説明文を生成する。

## 使い方

```
/pr-template              ← 現在のブランチの変更をまとめる
/pr-template <PR番号>     ← 既存 PR の説明文を生成する
```

## 手順

1. 対象を特定する:
   - 引数なし → `git diff main...HEAD` で現在のブランチの全変更を取得
   - PR 番号あり → `gh pr diff <番号>` で差分を取得
2. 変更ファイルをカテゴリ別に分類する
3. 以下のテンプレートで説明文を生成する
4. 結果をチャットに出力する

## 出力テンプレート

```markdown
## 概要

[1-3 文で変更の目的を説明]

## 変更内容

### フレームワーク変更（framework/）
- ...

### スキル・コマンド（.claude/）
- ...

### 自分の調査ノート（documents/）
- ...

### 参考文献の MD 化（references/）
- ...

### ドキュメント・設定（CLAUDE.md / README.md / .obsidian / 設定）
- ...

## 該当する軸

[この PR で主に扱った軸を列挙]

## レビュー観点

- [ ] 出典の URL は記録されているか
- [ ] 一次情報は references/ に MD 化されているか
- [ ] 論文の理想仮定と 3GPP 実装制約の差が意識されているか
- [ ] 前世代との対比が含まれているか
- [ ] frontmatter の axes が適切に記録されているか
- [ ] frontmatter の up / related / references にリンクが入っているか（孤立ノートが生まれていないか）
- [ ] ファイル名は yymmdd_<slug>.md（documents/）または原文の番号/タイトル（references/）に従っているか
```
