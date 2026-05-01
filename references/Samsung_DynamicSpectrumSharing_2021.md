---
title: "Dynamic Spectrum Sharing — Samsung Technical White Paper"
type: whitepaper
source_url: https://images.samsung.com/is/content/samsung/assets/global/business/networks/insights/white-papers/0122_dynamic-spectrum-sharing/Dynamic-Spectrum-Sharing-Technical-White-Paper-Public.pdf
accessed: 2026-05-01
authors: ["Samsung Electronics"]
year: 2021
venue: "Samsung Networks Technical White Paper"
identifiers:
  arxiv: ""
  doi: ""
  tdoc: ""
  spec: ""
related:
  - "[[260501_DSS-Dynamic-Spectrum-Sharing-3GPP採用経緯]]"
---

# Dynamic Spectrum Sharing — Samsung Technical White Paper (January 2021)

> 出典: <https://images.samsung.com/is/content/samsung/assets/global/business/networks/insights/white-papers/0122_dynamic-spectrum-sharing/Dynamic-Spectrum-Sharing-Technical-White-Paper-Public.pdf>
> アクセス日: 2026-05-01
> 変換コマンド: `pdftotext -layout Samsung_DSS_2021.pdf Samsung_DSS_2021.txt`
> 引用範囲: 本リポジトリの `documents/` 配下からの研究目的引用に限定。再配布禁止。

以下は `pdftotext -layout` による本文抽出を、図キャプションとページヘッダ・フッタ（数字のみのページ番号）を保持したまま貼ったもの。表は崩れるため必要に応じ原文 PDF を参照。

## Contents（原文目次）

- Introduction (p.3)
- DSS Overview (p.5) — Coverage Benefit through Spectrum Sharing / Flexible Band Utilization for NR Traffic
- 3GPP Standards for DSS (p.9) — LTE-NR Co-Existence Support in 3GPP Release 15 / Enhancement in 3GPP Release 16 and Release 17 / Mid-band TDD DSS
- DSS Design and Effect (p.15) — NR Broadcast and Signaling Message Transmission / NR DL Control and Data Transmission / NR DL Reference Signal On-Demand Transmission / LTE Always-on Signal Transmission
- Considerations for DSS (p.23) — Capacity Aspect / Deployment and Operation
- Summary (p.26)

## 主要トピック（抽出）

### Rel-15 で導入された LTE-NR 共存サポート機能（p.9〜）

1. **NR 100 kHz channel raster for FDD bands** — 既存の LTE FDD バンドは NR 用に再定義され、LTE と同じ 100 kHz チャネルラスターを共有することで「同一 RF チャネル・同一中心周波数」配置が可能（Figure 7）。
2. **Optional NR UL 7.5 kHz shift for FDD bands** — LTE UL は SC-FDMA 専用のため UL ラスターが DL に対して 7.5 kHz シフトされている。NR UL では OFDMA も使うため、オプションで 7.5 kHz シフトを選び LTE UL グリッドと直交整列させる（Figure 8）。
3. **NR PDSCH with rate matching of LTE CRS** — CRS port 数・CRS 位置・LTE 帯域幅を RRC で NR UE に通知し、PDSCH を LTE CRS のリソースエレメント（RE）を避けるように rate-match する。Figure 9。
4. **NR PDSCH alternative additional DMRS symbol location** — 通常 12 シンボル目に置かれる追加 DMRS を、LTE CRS の最終シンボルと重ならないよう **13 シンボル目** に移動するオプション（Figure 10）。
5. **NR flexible CORESET/PDCCH resource configuration** — 必須は first 3 OFDM symbols 内 CORESET。LTE PDCCH との分割が必要な場合 NR PDCCH を 2nd/3rd symbol に置く。オプションで 3 シンボルを超えた CORESET 配置（PDSCH mapping type B 用）。

### Rel-16 / Rel-17 強化機能

- **Multiple CRS rate matching patterns** — Rel-15 では NR と LTE の帯域幅が一致する場合のみ CRS rate match 可能。Rel-16 で **NR キャリア内に最大 3 つの LTE CRS rate matching pattern** を設定可能とし、LTE 側 CA に対応（Figure 11）。
- **Enhancement of PDSCH mapping type B** — Rel-15 では type B が 2/4/7 シンボル長のみだった。Rel-16 で 10 シンボル PDSCH 等を追加し、PDCCH を first 3 symbols より後ろに置いた場合も残スロットを使い切れる（Figure 12）。
- **Cross-carrier scheduling（Rel-17）** — 共有キャリアで NR PDCCH 容量が逼迫するため、SCell の PDCCH で P(S)Cell の PDSCH/PUSCH をスケジュールする方式を Rel-17 で追加（Figure 13）。
- **Mid-band TDD DSS** — n41 等 3 GHz 超の TDD バンドは 100 kHz ラスターを持たず 15/30 kHz ラスターのみのため、LTE-NR 中心周波数整列が単純ではなく、共存可能な周波数が限定される。3GPP は同一 TDD 周波数範囲に 15/30 kHz ラスターの新バンドを別途定義した。

### 主要設計原則と DSS Design and Effect

- **NR Broadcast and Signaling Message Transmission**: 初期アクセス段階の UE は CRS rate match を仮定できないため、SSB は **MBSFN subframe** に置く必要がある（CRS が LTE 制御領域のみに限定されるため）。SSB は 20 RB × 4 OFDM symbol を占有し、通常サブフレームでは LTE CRS と衝突する。SA NR では SIB1, OSI, Paging, RAR も MBSFN サブフレームに載せる。
- **EN-DC NSA で SSB のみ 20 ms 周期 + RAR 同 MBSFN 共用 → 5% オーバーヘッド** が最小ケース。SA はさらに増える（Figure 16）。
- **NR DL Control**: 4CRS port 構成では NR PDCCH が 1 symbol のみ使える。CCE 8 までしか取れず、最大 aggregation level 8 を必要とする UE が 1 つしか収容できない例（Figure 18）。
- **NR DL Reference Signal On-Demand**: TRS は 20/40 ms 周期で連続 2 スロット送信。NR UE が接続している間のみ送信して LTE 側の影響を最小化（on-demand）。
- **LTE Always-on Signal**: CRS は基地局が起動している限り常時送信され、NR から見ると恒久的なオーバーヘッドになる。
- **隣接セル干渉**: 隣接セルの CRS 位置は通常ずらしてあるため、自セル NR データが隣セル CRS と衝突しうる。re-farm された純 NR 環境では発生しない問題。

### NR DL overhead by LTE CRS and PDCCH（Table 2）

| Configuration | Average overhead in a RB |
|:---|:---|
| 2 CRS, 1 LTE PDCCH | 14% |
| 2 CRS, 2 LTE PDCCH | 21% |
| 4 CRS | 23% |

（1フレーム中に 1 MBSFN サブフレームを送信するという仮定）

### Considerations for DSS（p.23〜）

- **Capacity**: トラフィックが LTE/NR で均等に分かれている場合、スペクトラムを静的に二分しキャリア毎に分けたほうが DSS よりも合計容量が大きい。DSS のオーバーヘッド分が常に減算される。多バンドを全部 DSS にするより、一部を NR re-farm したほうが NR 需要増局面では総容量が大きくなる。
- **Peak rate degradation**: 静的分割だと NR と LTE を DC でキャリア集約してピーク到達できるが、DSS だとピーク劣化が発生（Figure 21）。
- **Deployment cost**: 既存 radio unit の置換、新 baseband 追加、LTE-NR 間のリアルタイム調整 IF、コミット済 LTE ソフトの DSS 対応版開発が必要。
- **Service trade-off**: DSS 環境下では URLLC の低遅延（30/60 kHz SCS）が使えず（LTE 15 kHz SCS との共存制約）、低遅延機能と DSS の同時採用は困難。
- **Vendor lock-in**: LTE-NR の密結合は専有 IF または統合スケジューラに依存し、マルチベンダー DSS は実質困難。

### Summary（要旨）

DSS は中・mmWave バンドのカバレッジ不足を補うため、LTE 占有の低周波バンドで早期に 5G を提供する手段として有効。一方で、(1) 容量とピークレート低下、(2) HW/SW 移行コスト、(3) LTE/NR の動的協調による低遅延機能の喪失、(4) ベンダーロックインを伴う。「seamless transition」とは矛盾しうる側面があるため、適用は慎重に判断すべき。

## References（原文）

- [1] 3GPP TR 38.912. "Study on New Radio (NR) access technology"
- [2] 3GPP TS 38.101. "User Equipment (UE) radio transmission and reception; Part 1: Range 1 Standalone"
- [3] 3GPP TS 38.212. "Multiplexing and channel coding"
- [4] 3GPP TS 38.331. "Radio Resource Control (RRC) protocol specification"
- [5] 3GPP TS 38.211. "Physical channels and modulation"

---

> 注: 本ファイルは `pdftotext -layout` による抽出の要点抜粋を Markdown で再構成したもの。図表の正確な数値は原文 PDF を参照すること。
