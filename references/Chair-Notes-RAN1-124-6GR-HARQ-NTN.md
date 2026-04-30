---
title: "Chair Notes RAN1#124 — AI 10.5.4.3 HARQ + AI 10.7 6GR NTN 抜粋（EoM_03）"
type: chair-notes
source_url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx
accessed: 2026-04-30
authors:
  - "Wanshi Chen (RAN1 Chair)"
  - "Kevin (OPPO) — FL for 124-R20-6GR-HARQ related (10.5.4.3)"
  - "Alberto (Qualcomm) — FL for 124-R20-6GR-NTN specific (10.7)"
year: 2026
venue: "RAN1#124, Gothenburg, Sweden, 2026-02-09 to 02-13"
identifiers:
  spec: "6GR FS_6G_Radio SI"
related:
  - "[[260501_TN-NTN共通HARQ_変遷]]"
  - "[[260430_RAN1-124-125-13トピック議論変遷]]"
  - "[[Chair-Notes-RAN1-124-Waveform]]"
---

# Chair Notes RAN1#124 — AI 10.5.4.3 HARQ + AI 10.7 6GR NTN（抜粋）

> 出典: [Chair notes RAN1#124 - eom_03.docx](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)、アクセス日 2026-04-30
> 変換: `pandoc` ではなく `python-docx` で `Heading` + `Agreement` パラグラフを抽出（cookbook §2.4）。
> 抽出範囲: §10.5.4.3 HARQ related Aspects（para 6021-6094）+ §10.7 NTN（para 6383-6510）。
> 元ファイルサイズ: 1.06 MB / 6,551 段落。本ファイルは関連 2 章のみ。

> **読み方**: `Agreement` / `Conclusion` / `Working assumption` が合意動詞。Tdoc 番号は将来 `[[R1-XXXXXXX]]` で wikilink 化予定（個別 reference は未取得）。

---

## §10.5.4.3 HARQ related Aspects

> **AI 10.5.4.3** = 6GR Downlink control channel, scheduling and HARQ operation > **HARQ related Aspects**
> Note 1: Including proposals for timing line, content and report mechanism (e.g., PUCCH or other mechanism).
> [124-R20-6GR-HARQ related] Email discussion on Rel-20 6GR-HARQ related – **Kevin (OPPO)**
> Tdoc 数: ~30 件、FL summaries #1〜#3（R1-2601540 / R1-2601541 / R1-2601542 / R1-2601716）

### Agreement [para 6026-6037] — HARQ 設計の評価軸

In 6GR, DL and UL HARQ operation designs considers at least the following aspects:
- latency
- reliability
- coverage
- power saving (NW and UE)
- NW complexity
- UE complexity
- diverse services/applications/traffics
- system efficiency/system throughput/user throughput
- feedback efficiency/UL and DL overhead

**Note: the design of DL and UL HARQ does not necessarily be the same**

### Agreement [para 6039-6042] — 2 つのフィードバック・メカニズム並列検討

For DL HARQ in 6GR, study both following HARQ-ACK feedback mechanisms:
- **Mechanism 1**: HARQ-ACK information bits are transmitted via L1 signalling
- **Mechanism 2**: HARQ-ACK information bits are transmitted via higher layer signalling (e.g., MAC CE)

### Agreement [para 6044-6048] — Asynchronous + Adaptive HARQ 採用

For discussion purposes:
- **Asynchronous HARQ** refers to that retransmission(s) occurs in a non pre-determined occasion once the corresponding initial transmission is scheduled.
- **Adaptive HARQ** refers that the transmission parameters and resources for the retransmission can be adaptively adjusted.

For DL and UL in 6GR, support **asynchronous and adaptive HARQ operation**.

### Agreement [para 6050-6051] — Payload size 範囲を検討

Study possible HARQ-ACK payload size range.

### Agreement [para 6054-6055] — TB 単位 granularity

In 6GR, support **at least TB level granularity** for HARQ-ACK feedback.

---

## §10.7 NTN（6GR NTN specific requirements and design）

> **AI 10.7** = 6GR NTN（10.7.1 GNSS-based, 10.7.2 GNSS-less/resilient）
> Note 1: Including common part for GNSS based operation and GNSS-less/resilient operation, as well as NTN specific evaluation assumptions.
> [124-R20-6GR-NTN specific] Email discussion on Rel-20 6GR-NTN specific– **Alberto (Qualcomm)**
> Tdoc 数: 35 件 + FL summaries #1〜#3（R1-2601469 / R1-2601470 / R1-2601471）

### Agreement [para 6431-6432] — リンクバジェットは TN を流用

For NTN link budget template, RAN1 to take the **TN link budget template as baseline** with specific rows / values (including adding new rows) to be further discussed.

### Agreement [para 6435-6444] — 評価対象の orbit/band 組合せ

RAN1 will define evaluation parameters for at least the following combinations of satellite orbit and bands:
- **S-band**: LEO 300, LEO 600, GEO
- **Ka band**: [LEO 300], LEO 600, [LEO 1200], GEO
- **Ku band**: LEO 1200, GEO

NOTE 1: The evaluations for S band are expected to be similar to L-band.
NOTE 2: This is only for the purpose of evaluations.

### Agreement [para 6447-6454] — GNSS 依存度の用語定義

RAN1 to use the following terminology when discussing GNSS availability at least for physical layer operation:

| 用語 | 定義 |
|:---|:---|
| **GNSS-based** | 端末が GNSS 受信機を持ち、規定精度内の position fix を取得できるネットワーク動作モード |
| **GNSS-degraded** | 端末は GNSS 受信機を持ち、過去に position fix を取得したが、現在は規定精度を満たさない可能性 |
| **GNSS-free / GNSS-less** | 端末が GNSS 受信機を持たない、または持っていても物理層に使える position fix がないモード |

FFS: How often the UE may be required to obtain a position fix, which may be related to the required accuracy.
FFS: if position under this operation can be obtained by means other than GNSS that provides a comparable accuracy.

### Agreement [para 6460-6461] — 3 つの GNSS モード全てをターゲット

6GR NTN targets to support **GNSS-based operation, GNSS-degraded operation and GNSS-less/GNSS-free operation**.

### Agreement [para 6463-6467] — UL synch は NR NTN を踏襲

6GR NTN uplink time-frequency synchronization follows the same principle as **NR NTN as baseline**:
- The concept of "uplink synchronization reference point" is introduced in 6GR NTN.
- 6GR NTN provides satellite assistance information.
- At least for GNSS-based operation, it is supported that UE uses its own location information + satellite assistance information to perform time-frequency pre-compensation.

### **★ Conclusion [para 6469-6477] — TN/NTN 共通設計の優先順位原則（最重要）**

**As a general principle for 6GR NTN study:**

- Under NTN agenda item, we will identify issues / requirements specific to NTN.
- Potential solutions to these issues / requirements may be studied under the NTN agenda.
- The outcome of this study may be discussed under other agenda items if **common design** is possible.
- These solutions may end up resulting in an extension of the TN design.
- This may depend on the solution / issue / requirement.
- NTN specific solutions may be introduced when a common / extended design cannot meet the NTN requirements.
- **When targeting a common design TN performance is prioritized.**

> **解釈**: これが #124 で固まった「共通設計時の優先順位原則」。Ofinno blog で要約引用された "terrestrial-network performance is prioritized when designing common TN/NTN solutions" の出典は本 Conclusion。
> NTN 固有最適化が認められるのは「共通／拡張設計では NTN 要件を満たせない」場合に限定される。HARQ・IA・スケジューリングの全アジェンダにこの原則が波及する。

### Agreement [para 6484-6488] — 大遅延 RTT を吸収する scheduling offset

6GR supports large scheduling offsets to accommodate the RTT introduced by the satellite channel. Further discuss how to realize these scheduling offsets:
- **Option 1**: Reuse the **k_offset** concept from NR as a baseline with potential modifications.
  - NOTE: Under this option, additional scheduling offsets (e.g. similar to K1/K2 in NR) may be supported for scheduling flexibility, which apply in addition to k_offset.
- **Option 2**: The large scheduling delays to accommodate the RTT are incorporated into the scheduling offsets (e.g. similar to K1/K2 in NR), which may or may not be common for TN and NTN.

### Conclusion [para 6490-6491] — 評価入力の xls 形式

When reporting inputs for the link budget template and evaluation assumptions to RAN1#124b, companies are encouraged to provide them in an xls attached to their contribution following the format of the xls attached to R1-2601471.

### **★ Agreement [para 6493-6502] — NTN 固有検討事項リスト（HARQ を明示的に含む）**

Study NTN specific issues/requirements at least for the following aspects for 6GR NTN under this agenda:
- Uplink time-frequency synchronization
- **HARQ issues**: e.g. enable/disable HARQ feedback (which may include how to efficiently operate with HARQ feedback enabled/disabled), **number of HARQ processes**, etc.
- Timing relationships with large RTT
- Coverage target
- Physical layer aspects of multi-satellite operation (including multi-orbit)
- Aspects related to Multiple beams per satellite
- Aspects related to satellite having more beam footprints than simultaneously active beams
- Other aspects are not precluded.

> **解釈**: HARQ enable/disable と process 数拡張は **NTN 固有問題** として正式に AI 10.7 のスコープ入り。汎用 HARQ AI（10.5.4.3）と並走する形で、NTN 観点の HARQ 議論が始まった。

### §10.7.2 GNSS-less/resilient operation [para 6506-6507]

> Placeholder only. **No contributions before RAN1#126.**

---

## 参考: 提出 Tdoc（10.5.4.3 HARQ）

| Tdoc | Title | Source |
|:---|:---|:---|
| R1-2600043 | Views on HARQ related aspects in 6GR | Nokia |
| R1-2600123 | Discussion on 6GR HARQ related aspects | Spreadtrum, UNISOC |
| R1-2600155 | HARQ related aspects for 6GR | Huawei, HiSilicon |
| R1-2600205 | Discussion on HARQ for 6GR | OPPO |
| R1-2600310 | Discussion on HARQ related aspects for 6GR | CATT |
| R1-2600400 | Discussion on 6GR HARQ design | CMCC |
| R1-2600440 | Discussion on 6G HARQ related aspects | Xiaomi |
| R1-2600515 | Discussion on 6GR HARQ related aspects | vivo |
| R1-2600555 | Discussion on HARQ related aspects for 6GR | LG Electronics |
| R1-2600576 | Discussion on HARQ related aspects | TCL |
| R1-2600616 | HARQ related aspects | InterDigital, Inc. |
| R1-2600635 | HARQ Related Aspects | Google |
| R1-2600653 | Discussion on HARQ related operation | NEC |
| R1-2600703 | Discussion on HARQ related aspects | China Telecom |
| R1-2600714 | HARQ for 6GR | Lenovo |
| R1-2600767 | On 6GR HARQ Related Aspects | Samsung |
| R1-2600839 | On HARQ related aspects | Apple |
| R1-2600856 | Discussion on HARQ related aspects | Fujitsu |
| R1-2600926 | Discussion on HARQ related Aspects for 6GR air interface | Sharp |
| R1-2600977 | Discussion on HARQ related aspects for 6GR | ZTE Corporation, Sanechips |
| R1-2601013 | Discussion on HARQ related Aspects | ETRI |
| R1-2601048 | Scheduling and HARQ operation for 6GR | **Ericsson, T-Mobile USA** |
| R1-2601099 | HARQ related aspects | **Qualcomm** |
| R1-2601105 | HARQ related aspects | Ofinno |
| R1-2601116 | Discussion on HARQ related aspects for 6GR | Panasonic |
| R1-2601139 | Discussion on 6G HARQ Related Aspects | Sony |
| R1-2601193 | Discussion on HARQ-related aspects for 6GR | NTT DOCOMO |
| R1-2601359 | Discussion on HARQ related aspects in 6GR | MediaTek |
| R1-2601401 | Discussion on HARQ related Aspects | CEWiT |

提出企業数: 30 社（FL OPPO 含む）。Ericsson + T-Mobile USA は co-source、運用者視点が珍しく入っている。

## 参考: 提出 Tdoc（10.7 6GR NTN）

主要企業: Nokia / FUTUREWEI / Spreadtrum / Huawei / OPPO / **THALES** / ZTE / CATT / Tejas / CMCC / Xiaomi / TCL / vivo / InterDigital / NEC / China Telecom / Fraunhofer / Samsung / **Amazon Web Services** / Apple / MediaTek / Sharp / Lenovo / LG / Panasonic / ETRI / Ericsson / Airbus+ESA+Fraunhofer+Thales+Iridium+Novamint+Sateliot+TNO+SES+Eutelsat (PNT 連名 R1-2601078) / Ofinno / Sony / NTT DOCOMO / Qualcomm / Google Korea / CEWiT / CSCN

> 衛星オペレータ・宇宙機関（Thales, Airbus, ESA, Iridium, SES, Eutelsat, Sateliot, TNO, Novamint）と、超巨大プラットフォーマ（AWS）が参加している点が NTN の特徴。
