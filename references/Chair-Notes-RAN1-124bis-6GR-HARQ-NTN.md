---
title: "Chair Notes RAN1#124bis — AI 10.5.4.3 HARQ + AI 10.7 6GR NTN 抜粋（EoM5）"
type: chair-notes
source_url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx
accessed: 2026-04-30
authors:
  - "Wanshi Chen (RAN1 Chair)"
  - "Kevin (OPPO) — FL for 124b-R20-6GR-HARQ related (10.5.4.3)"
  - "Alberto (Qualcomm) — FL for 124b-R20-6GR-NTN specific (10.7)"
year: 2026
venue: "RAN1#124bis, Saint Julians, Malta, 2026-04-13 to 04-17"
identifiers:
  spec: "6GR FS_6G_Radio SI"
related:
  - "[[260501_TN-NTN共通HARQ_変遷]]"
  - "[[260430_RAN1-124-125-13トピック議論変遷]]"
  - "[[Chair-Notes-RAN1-124bis-Waveform]]"
  - "[[260428_RAN1-124bis-MIMO-operation-10.5.2]]"
---

# Chair Notes RAN1#124bis — AI 10.5.4.3 HARQ + AI 10.7 6GR NTN（抜粋）

> 出典: [Chair notes RAN1#124bis_eom5.docx](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)、アクセス日 2026-04-30
> 変換: `python-docx` で Heading + Agreement 段落を抽出（cookbook §2.4）。
> 抽出範囲: §10.5.4.3 HARQ related Aspects（para 4168-4253）+ §10.7 NTN（para 4581-4751）。
> 元ファイルサイズ: 1.28 MB / 5,056 段落。本ファイルは関連 2 章のみ。

---

## §10.5.4.3 HARQ related Aspects

> [124b-R20-6GR-HARQ related] Email discussion on Rel-20 6GR-HARQ related – **Kevin (OPPO)**
> FL summaries: R1-2603251 (#1), R1-2603252 (#2), R1-2603253 (#3), R1-2603326 (#4)
> Tdoc 数: 30 件超

### Agreement [para 4176] — TB より細かい granularity を検討

In 6GR, study whether and how to support **downlink HARQ-ACK feedback granularity smaller than TB-level**, considering at least the following factors:
- Feedback overhead
- Retransmission efficiency
- Implementation feasibility

> **解釈**: #124 で "at least TB level" を確定したが、#124bis ではサブ TB（CBG-like）も再検討対象に。

### Agreement [para 4182] — TB 横断バンドリング検討

In 6GR, study whether and how to support **HARQ-ACK bundling across multiple TBs**.

### Agreement [para 4189] — HARQ-ACK codebook 設計（包括）

Study **HARQ-ACK codebook(s)** and its operation for downlink HARQ operation in 6GR, considering at least the following aspects:
- HARQ-ACK codebook generation
- HARQ-ACK feedback granularity, e.g., TB-level, smaller than TB-level, bundling across multiple TBs, etc.
- Feedback overhead
- HARQ-ACK payload size and bits order misalignment between NW and UE due to DCI missing
- Ambiguity between DTX of DL assignment and PDSCH decoding failure when network decodes a NACK in a HARQ-ACK codebook
- Coordination between schedulers, e.g., between multiple carriers, between DL and UL, etc.
- Feedback complexity

### Agreement [para 4199] — Payload size の上下限

In 6GR, the **minimum downlink HARQ-ACK payload size is 1** and the **upper limit supported by 5G NR Polar coding can be reused (i.e., 1706 bits)** at least for Mechanism 1 of HARQ feedback if supported.
- Note 1: this upper limit does not imply the max HARQ-ACK payload size would be 1706.
- Note 2: the exact value of the maximum size may be determined at a later stage if needed.

### Agreement [para 4204] — HARQ-ACK timing/resource の決定方式 4 候補

In 6GR, study the details and pros and cons of the following methods to determine timing and resource for downlink HARQ-ACK feedback:
- **Method 1**: Dynamic indication in DCI
- **Method 2**: UE initiated HARQ-ACK feedback
- **Method 3**: Next available/feasible time slot of semi-static configured resources that satisfy UE processing time/capability
- **Method 4**: Only based on configuration via RRC

Note: combinations of above methods and other methods are not precluded.

> **解釈**: NR では DCI dynamic indication（K1 値）が主流だが、6GR では UE-initiated feedback も俎上に。これは XR / バーストトラフィック / 不規則伝送への対応で進歩性余地。

### Agreement [para 4215] — Fast ARQ 連動

For 6GR UL: Study an **explicit indication or implicit indication for a given HARQ process failure** to trigger faster ARQ procedure in UL.

Note: Companies are encouraged to check RAN2 agreements and LS if any on fast ARQ in **RAN2#133bis**.

> **解釈**: HARQ↔ARQ 跨層連携（HARQ 失敗 → 即 ARQ 起動）の標準化検討。NR では HARQ-ARQ 間の interaction は限定的だが、6GR では進歩。

---

## §10.7 NTN（6GR NTN specific requirements and design）

> [124b-R20-6GR-NTN specific] Email discussion – **Alberto (Qualcomm)**
> FL summaries: R1-2603090 (#1), R1-2603091 (#2), R1-2603093 (#3)
> Tdoc 数: 35 件以上（衛星オペレータ・宇宙機関を含む）

### **★ Agreement [para 4594-4601] — TN/NTN 共通 HARQ の最重要合意（HARQ stalling 解決策）**

For the issue of **HARQ stalling due to large RTT in NTN**, study the following solutions (which may or may not have specification impact), including their applicability:
- **Solution 1**: HARQ feedback disabling
- **Solution 2**: PDSCH / PUSCH transmissions that span multiple slots
- **Solution 3**: aNB reusing the same HARQ process before receiving HARQ-ACK feedback for the previous transmission
- **Solution 4**: Sufficient number of HARQ processes
- Note: Combination of solutions above can be considered.
- **FFS: Whether the above techniques can be harmonized with TN**

> **本ノートの中核**: この Agreement が「TN/NTN 共通 HARQ」の **議論の入口**。
> - **Solution 1**（HARQ 無効化）は Rel-17 NR-NTN / Rel-18 IoT-NTN で既にサポート済の手法を 6GR でも踏襲する案。
> - **Solution 2**（multi-slot PDSCH/PUSCH）は新規。1 process の occupancy 期間を拡張することで実効的に process 数を増やす効果。
> - **Solution 3**（process 再利用）は HARQ プロトコルの根幹（process ID 一意性）に手を入れる踏み込み案。NTN 固有運用が前提だが、TN への波及は要検討。
> - **Solution 4**（process 数増加）は Rel-17 で 16→32 にした延長線。Solution 1 と組合せ運用が想定される。
> - **FFS**: TN との harmonization が **FFS** に明記された点が、本ノートの SEP 仮説の起点。

### Agreement [para 4609-4631] — 6GR NTN リンクバジェットテンプレ確定

For 6GR NTN, the **link budget template attached to R1-2603091 is endorsed**.
Note: "Candidate 2" is not considered for NTN.

Conclusion: アンテナ仮想化モードの取扱を reflector / phased array / omni それぞれで規定（詳細は 4615-4631）。

### Agreement [para 4635-4638] — Beam footprint 不足問題の解決策

In 6GR NTN, for the issue of **satellite having more beam footprints than simultaneously active beams**, study the following solutions, including their achievable coverage ratio of satellite and applicability:
- Value of default SSB periodicity
- Hierarchical beam structure (e.g. using beams of various sizes)

### Agreement [para 4643-4646] — Duplex 種別

For 6GR NTN study, RAN1 considers at least the following duplex types:
- **FD-FDD**
- **HD-FDD on UE side**

### Agreement [para 4649-4658] — Multi-satellite operation

In 6GR NTN, under the label of "**physical layer aspects of multi-satellite operation**", at least the following aspects are studied:
- Physical layer aspects related to **mobility**（RAN2 連携必要）
- Physical layer aspects related to **inter-satellite interference management**（FFS: 詳細）
  - NOTE: For the two aspects above it is assumed that the UE is only connected to one satellite at a time.

### Working assumption [para 4663-4675] — アンテナモデル

For 6GR NTN, for **S-band LEO-600 and LEO-300**, the assumption for SAN antenna model is adopted (50% efficiency 考慮)。
For **UE antenna model for S-band (all orbits)**, consider a subset of combinations（FFS: どれを採用するか）。

### Agreement [para 4678-4680] — MEO-7000 を追加

For 6GR NTN evaluations, consider the following additional orbit for S-band, at least for link budget calculation purposes:
- **MEO-7000**

> **解釈**: #124 で確定した evaluation orbit リスト（LEO 300/600/1200, GEO）に MEO-7000 が追加。MEO は LEO と GEO の中間で RTT も中間（数十 ms 級）。HARQ process 数の検討で LEO 単独議論よりレンジが広がる。

### Agreement [para 4684-4690] — k_offset の扱い（#124 Option 1 を採用）

For 6GR NTN, for realizing large scheduling offsets, the following is supported in principle:
- **Reuse the k_offset concept from NR as a baseline with potential modifications.**
- NOTE: Under this option, additional scheduling offsets (e.g. similar to K1/K2 in NR) are assumed to be supported for scheduling flexibility, which apply in addition to k_offset.
- **At least broadcast (FFS whether cell or beam specific) k_offset is supported.**
- FFS whether UE-specific k_offset is supported.
- NOTE: This agreement may be revised if 6GR does not define concepts such as K1/K2, or if the baseline design of 6GR scheduling can already cover the RTT range of NTN.

> **解釈**: #124 の 2 オプション（Option 1: k_offset 流用 / Option 2: K1/K2 統合）から **Option 1** を採用。NTN 固有の k_offset を先に規定し、6GR 全体スケジューリングフレームの帰結を待つ条件付。

### Agreement [para 4697-4701] — TA report と satellite assistance info

For 6GR NTN, RAN1 to study whether **TA report is beneficial**.

For 6GR NTN, at least for GNSS-based operation, study which parameters are needed for **satellite assistance info for UL time-frequency pre-compensation**, considering NR NTN parameters in **SIB19 as starting point**.

> **解釈**: SIB19（NR-NTN の satellite ephemeris broadcast）が starting point。Rel-19 NR-NTN の延長線で 6GR NTN がスムースに繋がる設計。

### §10.7.2 GNSS-less/resilient operation [para 4751-4754]

> Placeholder only. **No contributions before RAN1#126.**
> R1-2601849 — On NTN specific requirements and design for GNSS-less/resilient operation in 6GR — Nokia（参考のみ）

---

## 参考: 提出 Tdoc（10.5.4.3 HARQ, RAN1#124bis）

主要企業（35 社程度）: Spreadtrum / Nokia / Huawei / MediaTek / vivo / CMCC / NEC / Samsung / China Telecom / InterDigital / KT / Panasonic / TCL / Sony / OPPO / CATT / LG / Xiaomi / Google / Apple / 1Finity / Sharp / ZTE / ETRI / Lenovo / **CAICT** / **Fainity Innovation** / Ericsson / Ofinno / Qualcomm / NTT DOCOMO / CEWiT

## 参考: 提出 Tdoc（10.7 6GR NTN, RAN1#124bis）

#124 と同水準の 35+ 社。新規参加: HONOR, **ROBERT BOSCH GmbH**, **Toyota ITC**, **AST Space Mobile**, **JSAT**（PNT 連名）, ST Engineering iDirect 等。

衛星オペレータ／宇宙機関の連名（R1-2602881）:
> Airbus, ESA, European Commission, Thales, Fraunhofer IIS, Fraunhofer HHI, DLR, TNO, Novamint, SES, AST Space Mobile, Iridium, Sateliot, **Toyota ITC**, ETRI, JSAT
> — Positioning, Navigation and Timing (PNT) with 6GR NTN

> **解釈**: PNT（測位＋ナビ＋タイミング）が宇宙機関連名で押し込まれている。HARQ 観点では直接関係しないが、衛星アシスト情報（時刻基準）が HARQ 動作前提と密接。

---

## RAN1#124 → #124bis の変化点（HARQ + NTN）

| 観点 | #124 で確定 | #124bis で進展 |
|:---|:---|:---|
| HARQ-ACK granularity | "at least TB level" | サブ TB / TB 横断 bundling 検討開始 |
| HARQ-ACK payload size | "範囲を検討" | min=1 bit, max=1706 bits（NR Polar 上限流用） |
| HARQ-ACK timing 決定 | （未決） | 4 methods（Dynamic DCI / UE-initiated / 半静的 next slot / RRC only） |
| HARQ-ARQ 連携 | （未決） | UL HARQ failure → fast ARQ trigger 検討開始 |
| TN/NTN 共通 HARQ 原則 | "TN performance prioritized" 確定 | NTN 固有 4 解決策 + TN harmonization の **FFS** 化 |
| NTN orbit set | LEO 300/600/1200, GEO | + **MEO-7000** 追加 |
| NTN scheduling offset | k_offset / K1+K2 統合 の 2 案 | k_offset 流用案を採用、broadcast 確定（FFS: cell/beam, UE-specific） |
| NTN duplex 種別 | （未決） | FD-FDD + HD-FDD（UE side）採用 |
| NTN 多衛星運用 | NTN 固有検討事項に明示 | mobility + inter-satellite interference を study スコープに正式化 |
| NTN GNSS-less | placeholder（#126 から） | placeholder 維持（#126 から） |
