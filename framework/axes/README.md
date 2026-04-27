# axes — 分析軸（Map of Content）

すべてのトピックに対して必ず適用する6つの直交した分析軸。
1軸1ファイルで管理し、追加するときは新ファイルを置くだけ。

## 6軸一覧

| 軸 | ファイル | 問い |
|:---|:---|:---|
| 1. 技術レイヤー | [[01-technology-layer]] | この技術は物理層のどこに位置し、他のレイヤーとどう結合しているか |
| 2. 世代 | [[02-generation]] | どのリリースで標準化されるか、前世代との連続/断絶は |
| 3. 価値 | [[03-value]] | スループット以外にどの KPI を改善するか |
| 4. 市場 | [[04-market]] | どのセグメント・地域で最初に展開されるか |
| 5. 普及要因 | [[05-adoption-factors]] | 採用を左右するボトルネックは何か |
| 6. 知財 | [[06-ip]] | 知財ポジションの現状と機会はどこか |

## 関連

- 親: [[../README|framework/README]]
- 補完: [[../lenses/README|lenses（オプショナル視点）]]、[[../personas/README|personas（需要側モデル）]]
- 軸4市場 ↔ [[../personas/README|personas]] は密接に連携する（市場軸が分類、ペルソナが深掘り）
- 各スキルの実行フローはこの全6軸を参照する。詳細は [[../skill-contract|skill-contract]]

## frontmatter での記録

研究ノートは frontmatter `axes:` に該当する軸の値を記載する:

```yaml
axes:
  technology-layer: [phy-mimo, phy-coding, higher-layer, cross-layer]
  generation: [rel-15, rel-16, ..., rel-21]
  value: [energy-efficiency, coverage, ai-integration, throughput, latency, connectivity, reliability]
  market: [consumer-xr, b2b-industrial, fwa, ntn, ambient-iot]
  adoption-factors: [killer-app, standard-convergence, operator-roi, economies-of-scale, backward-compat]
  ip: [novelty, inventive-step, spec-mapping]
```

各値の語彙は対応する軸ファイルの「分類」セクションを参照。
