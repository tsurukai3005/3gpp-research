---
up: "[[README|axes]]"
related:
  - "[[../personas/README]]"
  - "[[03-value]]"
  - "[[05-adoption-factors]]"
---

# 軸4: 市場軸

**問い: この技術は誰が使い、そのユースケース市場は成熟しているか？**

> 親: [[README|axes（軸 MoC）]] | 兄弟軸: [[01-technology-layer|軸1]] / [[02-generation|軸2]] / [[03-value|軸3]] / [[05-adoption-factors|軸5]] / [[06-ip|軸6]]
> 連携: [[../personas/README|personas]] と密接に組み合わせて使う


## セグメント分類

| セグメント | 典型的ユースケース | 市場成熟度 |
|:---|:---|:---|
| Consumer (eMBB/XR) | 動画配信、没入型 XR、クラウドゲーミング | 高（eMBB）/ 低（XR） |
| B2B (Industry 4.0) | スマートファクトリー、自動運転、遠隔医療 | 低（5G で苦戦中） |
| FWA | 家庭用ブロードバンド代替 | 中（5G で唯一の成功例） |
| NTN | 衛星通信、HAPS、海洋・山間部カバレッジ | 低→中（急成長中） |
| Ambient IoT | バッテリーレスセンサー、物流タグ | 黎明期 |

## 問いかけ

- 想定ユースケースは consumer か B2B か FWA か NTN か？
- そのユースケース市場は成熟しているか、これから立ち上がるか？
- 既存の代替手段（Wi-Fi、LPWAN、有線）と比較してどう優位か？
- この技術がないとそのユースケースは実現不可能か、それとも性能が劣るだけか？

## ペルソナとの連携

より詳細な需要分析には [[../personas/README|personas]] のペルソナファイルを参照する。
市場軸はセグメント分類を担い、ペルソナは「誰にとって」を深掘りする。

## frontmatter での記録

```yaml
axes:
  market: [consumer-xr, b2b-industrial, fwa, ntn, ambient-iot]
```
