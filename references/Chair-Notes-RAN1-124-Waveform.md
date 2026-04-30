---
title: "Chair Notes RAN1#124 — AI 10.2.1 Waveform 抜粋（EoM_03）"
type: chair-notes
source_url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx
accessed: 2026-04-30
authors:
  - "Wanshi Chen (RAN1 Chair)"
  - "Klaus (Nokia) — FL for 124-R20-6GR-Waveform"
year: 2026
venue: "RAN1#124, Gothenburg, Sweden, 2026-02-09 to 02-13"
identifiers:
  spec: "TR 38.901-related; 6GR FS_6G_Radio SI"
related:
  - "[[260501_6GR-Waveform-PAPR削減_変遷]]"
  - "[[260430_RAN1-124-125-13トピック議論変遷]]"
---

# Chair Notes RAN1#124 — AI 10.2.1 Waveform（抜粋）

> 出典: [Chair notes RAN1#124 - eom_03.docx](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)、アクセス日 2026-04-30
> 変換: `pandoc 'Chair notes RAN1#124 - eom_03.docx' -t gfm --wrap=none`
> 抽出範囲: §"Waveform for 6GR air interface" のみ。Channel coding, MIMO, etc. は別途。
> 元ファイルサイズ: 1.06 MB / 18,456 行。本ファイルは Waveform セクションのみ（246 行）。

> **読み方**: `<span class="mark">…</span>` は元 docx の蛍光マーキング（FL/議長による強調）。`Agreement:` / `Conclusion:` / `Observation:` が合意動詞。Tdoc 番号は `[[R1-XXXXXXX]]` で wikilink される設計（個別 reference は未取得）。

---

# Waveform for 6GR air interface

### Waveform

*Note 1: Including proposals for improving spectrum efficiency, power efficiency, coexistence and coverage, etc.*

[124-R20-6GR-Waveform] Email discussion on Rel-20 6GR-Waveform – Klaus (Nokia)

- To be used for sharing updates on online/offline schedule, details on what is to be discussed in online/offline sessions, tdoc number of the moderator summary for online session, etc

R1-2601512 Session Notes of AI 10.2.1 Ad-Hoc Chair (NTT DOCOMO, INC.)

Session notes are endorsed and incorporated the session notes below.

## R1-2600786 Feature Lead summary #1 on 6G waveform — Nokia

**Agreement:** Extend the RAN1#123 endorsed table to characterize each (waveform) proposal as a potential RAN1 observation as follows to cover also impacts to transmitter and receiver processing operation:

| Field | Description |
|----|----|
| Name of the proposal |  |
| Motivation of the proposal | E.g. TN, NTN, ISAC, etc… |
| Applicable link direction | DL/UL/both |
| Enhancement to CP-OFDM? | No/Yes |
| Enhancement to DFT-s-OFDM? | No/Yes |
| Additional OFDM-compatible waveform? | No/Yes |
| Target channel(s)/signal(s) | PDCCH/PDSCH/PUCCH/PUSCH/xxx |
| Target modulation |  |
| Motivation / use case | Improved spectral efficiency, … |
| Key Metric / KPI | Spectral efficiency, … |
| Key spec impact foreseen |  |
| MRSS compatibility | Please explain |
| Multiplexing/coexistence with other waveforms | Please explain |
| Multi-user multiplexing | Please explain |
| MIMO compatibility | Please explain |
| Implementation/operation impacts on transmitter processing | Please explain |
| Implementation/operation impacts on receiver processing | Please explain |

## R1-2600787 Feature Lead summary #2 on 6G waveform — Nokia

**Conclusion:** DFT-s-OFDM waveform including related enhancements for 6GR **Downlink** will be no further discussed as part of AI 10.2.1.

- Note: for DL signal (e.g., SS, WUS, sensing), it may or may not be separately discussed in corresponding AI.

**Conclusion:** Studies on UL coverage improvements through low UL PAPR enhancement for DFT-s-OFDM are to be handled with **high priority** in AI 10.2.1.

**Conclusion:** Studies on DFT-s-OFDM for **multi-rank UL MIMO** are to be handled with **high priority** in AI 10.2.1.

**Agreement:** For the evaluations of spectrum extension and spectrum truncation for UL low-PAPR solutions, the number of subcarriers A before extension / truncation is

- Option 1: 12 \* 2^x \* 3^y \* 5^z subcarriers
- Option 2: 2^x \* 3^y \* 5^z subcarriers
- FFS: whether the maximum value for A is needed

Note: Companies are encouraged to investigate above options and bring inputs to RAN1#124bis.
Note: the occupied bandwidth B is given in terms of number of RBs.

**Agreement:** NR Rel-15 DFT-s-OFDM should be used as the **baseline reference** when evaluating the gains of UL low-PAPR proposals.

## R1-2600788 Feature Lead summary #3 on 6G waveform — Nokia

**Agreement:** Following metrics are used for SLS evaluations for multi-layer UL DFT-s-OFDM and CP-OFDM studies.

- User perceived throughput (UPT), including:
  - High percentile (90%)
  - mean
  - median
  - cell edge (5 & 10-percentile)
- Optional for full buffer traffic only: cell average throughput
- Companies are encouraged to report the CDF of instantaneous UL TX power across all UEs
- Companies are encouraged to report the statistics on the UL TX rank.
- Companies are encouraged to report the statistics on the applied MCS.

**Agreement:** Following metrics are used for LLS evaluation for multi-layer UL DFT-s-OFDM and CP-OFDM studies.

- BLER curves (for a subset of NR MCS (covering whole range with spanning), HARQ re-transmissions disabled) for same transmission rank, for same resource allocation and same transmission power for DFT-s-OFDM and CP-OFDM
  - Companies may derive Link-level throughput vs SNR based on BLER curves
- Netgain

**Agreement:** For 2-layer/2Tx UL DFT-s-OFDM and CP-OFDM studies, following two cases are considered.

- UE capable of only non-coherent precoder
  - For UL CP-OFDM and DFT-s-OFDM rank-2 transmission, only non-coherent precoder option is allowed.
- UE capable of fully-coherent precoder
  - For UL CP-OFDM rank-2 transmission, all NR precoder options are allowed.
  - For UL DFT-s-OFDM rank-2 transmission, **only non-coherent precoder option is allowed**.

**Agreement:** For the multi-layer UL DFT-s-OFDM and CP-OFDM studies, the NR reference should be evaluated assuming the **Release 16 full power mode 1** to be enabled.

## R1-2600789 Feature Lead summary #4 on 6G waveform — Nokia

**Agreement:** The following UL low-PAPR proposals for DFT-s-OFDM are for further consideration:

- **Non-AI-ML-based**
  - FDSS (R1-2601092 Ofinno, R1-2600751 Samsung, R1-2600801 InterDigital, R1-2600823 Apple, R1-2600914 Sharp, R1-2601156 Ericsson)
  - FDSS – spectrum extension (R1-2600027 Nokia, R1-2601092 Ofinno, R1-2600823 Apple, R1-2600751 Samsung, R1-2600914 Sharp, R1-2601156 Ericsson, R1-2600261 ZTE)
  - FDSS – spectrum truncation for π/2 BPSK (R1-2601268 Qualcomm, R1-2601212 PCL, R1-2601092 Ofinno, R1-2601156 Ericsson)
  - Tone Reservation (R1-2600261 ZTE, R1-2600716 Lekha, R1-2601268 Qualcomm)
    - For π/2 BPSK or other modulation orders
  - GMSK-Approximation based FDSS (R1-2600823 Apple)
  - 3-tap filter based FDSS (R1-2508684 — Rel-19 NES carry-over)
  - CFR-SE (R1-2600499 vivo)
  - Offset-QAM or π/2-PAM with FDSS-spectrum truncation (R1-2600909 MediaTek, R1-2600138 Huawei, R1-2601268 Qualcomm, R1-2600751 Samsung)
  - Offset-QAM or π/2-PAM with FDSS-spectrum extension (R1-2600909 MediaTek, R1-2600138 Huawei, R1-2600751 Samsung, R1-2600823 Apple)
  - Interpolation-based modulation (R1-2600261 ZTE)
  - AFDM based on DFT-s-OFDM (R1-2600999 ETRI/Surrey, R1-2601019 SJTU/NERC-DTV)
- **AI-ML-based**
  - AI/ML-based waveform (R1-2600499 vivo, R1-2600751 Samsung)

Note: tdoc numbers described in each proposal provide information on the proposal for further consideration, and it does not mean these tdocs support the proposal.

**Conclusion:** Further clarifications on evaluations of UL low-PAPR proposals for DFT-s-OFDM:

- In the evaluation assumptions, companies should disclose the necessary knowledge (e.g., filter coefficients, extension scheme, …) of the waveform at the receiver to process if any.

## Submitted Tdoc list (AI 10.2.1, RAN1#124)

| Tdoc | Title | Source |
|:---|:---|:---|
| R1-2600027 | On remaining aspects of waveform for 6GR | Nokia |
| R1-2600138 | Waveform for 6GR air interface | Huawei, HiSilicon |
| R1-2600188 | On waveform enhancements/additions for 6G Radio | OPPO |
| R1-2600239 | Discussion on waveform for 6GR | LG Electronics |
| R1-2600255 | Discussion on waveform for 6GR air interface | THALES |
| R1-2600261 | Views on the waveform for 6G | ZTE Corporation, Sanechips |
| R1-2600295 | Discussions on waveform for 6GR | CATT |
| R1-2600366 | Waveform design for 6G air interface | Tejas Network Limited |
| R1-2600384 | Discussion on the waveform design for 6G radio | CMCC |
| R1-2600424 | Further discussion on 6GR waveform | Xiaomi |
| R1-2600499 | Discussion on Waveform for 6GR air interface | vivo |
| R1-2600572 | Discussion on Waveform for 6GR Air Interface | IMU, Turkcell |
| R1-2600584 | Discussion on 6G Waveform | NEC |
| R1-2600612 | Waveform for 6GR Air Interface | **Cohere Technologies** |
| R1-2600627 | Waveform for 6GR Air Interface | Google |
| R1-2600716 | Discussions on 6G Waveforms | Lekha Wireless Solutions |
| R1-2600751 | Discussion on waveform for 6GR | **Samsung** |
| R1-2600801 | Waveform for 6GR air interface | InterDigital, Inc. |
| R1-2600823 | On Waveforms for 6GR air interface | Apple |
| R1-2600909 | Waveform for 6GR air interface | MediaTek Inc. |
| R1-2600914 | Study on waveform for 6GR | Sharp |
| R1-2600999 | Discussion on 6GR waveform | ETRI, University of Surrey |
| R1-2601019 | Discussion on New Waveform for 6GR Air Interface | Shanghai Jiao Tong University, NERC-DTV |
| R1-2601047 | Discussion on 6GR waveform design | Hanbat National University |
| R1-2601080 | Discussion on Waveform for 6GR | Lenovo |
| R1-2601092 | Discussion on waveform for 6GR air interface | Ofinno |
| R1-2601110 | New waveform for 6GR air interface | NICT |
| R1-2601113 | Discussion on waveform for 6GR air interface | Panasonic |
| R1-2601127 | Waveforms for 6GR | Sony |
| R1-2601156 | On waveform for 6GR | Ericsson |
| R1-2601176 | Discussion on Waveform | NTT DOCOMO, INC |
| R1-2601212 | Discussion on waveform for 6GR air interface | Pengcheng Laboratory |
| R1-2601268 | Waveforms for 6GR | **Qualcomm Incorporated** |
| R1-2601294 | Discussion on waveform for 6G air interface | Quectel |
| R1-2601354 | Discussion on waveform for 6GR air interface | KDDI Corporation |
| R1-2601366 | Enhancements for pi/2-BPSK DFT-s-OFDM: Overlapped Allocations | Wisig Networks, IITH |
| R1-2601517 | Discussion on Waveform (Revision of R1-2601176) | NTT DOCOMO, INC |

> Note: Jio Platforms は AI 10.2.1（Waveform）には寄書を出していない。Jio は AI 10.3.1（Channel Coding, R1-2601203/R1-2601423）と AI 10.4（Energy Efficiency, R1-2601315）で活動。
