---
up: "[[README|axes]]"
related:
  - "[[02-generation]]"
  - "[[../lenses/standardization-dynamics]]"
---

# 軸1: 技術レイヤー

**問い: この技術は物理層のどこに位置し、他のレイヤーとどう結合しているか？**

> 親: [[README|axes（軸 MoC）]] | 兄弟軸: [[02-generation|軸2]] / [[03-value|軸3]] / [[04-market|軸4]] / [[05-adoption-factors|軸5]] / [[06-ip|軸6]]


## 分類

- **物理層（PHY）**: 波形・変調 / チャネルコーディング / MIMO / 基準信号（RS）
- **高位層**: スケジューリング（MAC） / 制御（RRC） / プロトコル
- **クロスレイヤ**: PHY と高位層を横断する設計（例: セマンティック通信）

## 問いかけ

- このトピックは物理層のどの機能（波形/符号化/MIMO/基準信号）に属するか？
- 高位層（スケジューリング、RRC）とどう結合しているか？
- シグナリング（DCI / MAC CE / RRC）の負担はあるか？
- 制御情報のビット数制約が性能にどう影響するか？
- ハードウェア実装（チップ面積・消費電力）への影響は？

## frontmatter での記録

```yaml
axes:
  technology_layer: [phy-mimo, phy-coding, higher-layer, cross-layer]
```
