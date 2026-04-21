# テンプレート: トピック間接続（考察）

スキル `/connect-dots` から参照される。

## 入力

- トピック A: `documents/` のノート
- トピック B: `documents/` のノート
- （オプション）ペルソナ: `framework/personas/` のファイル

## 分析の手順

### 1. 共通軸の比較

両トピックの frontmatter の axes を比較し、共通する値を特定する。

```
トピック A の axes: {value: [energy-efficiency], market: [ntn]}
トピック B の axes: {value: [energy-efficiency, coverage], market: [fwa, ntn]}
→ 共通: value=energy-efficiency, market=ntn
```

### 2. 相乗効果の仮説

共通軸を起点に、両トピックを組み合わせることで生まれる価値を仮説として生成する。

```markdown
## 相乗効果の仮説
- [仮説1]: A + B により [KPI] が [理由] で改善される可能性
- [仮説2]: ...
```

### 3. 矛盾・トレードオフの検出

両トピックの前提や要件が矛盾する点を特定する。

```markdown
## 矛盾・トレードオフ
- [矛盾1]: A は [X] を前提とするが、B は [Y] を要求する
- [矛盾2]: ...
```

### 4. ペルソナ視点の評価（オプション）

指定されたペルソナファイルを読み、以下を問う:
- この組合せはそのペルソナにとって価値があるか？
- コスト的に成立するか？
- そのペルソナの優先事項に合致するか？

### 5. Next Steps

- この組合せを深掘りするために次に調べるべきこと
- 関連する論文、Tdoc、ホワイトペーパー

## 出力先

`documents/YYYY-MM-DD_接続考察-topicA-x-topicB.md`
