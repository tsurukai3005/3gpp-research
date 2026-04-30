---
title: "Chair Notes RAN1#124bis — AI 10.2.1 Waveform 抜粋（EoM5）"
type: chair-notes
source_url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx
accessed: 2026-04-30
authors:
  - "Wanshi Chen (RAN1 Chair)"
  - "Klaus (Nokia) — FL for 124b-R20-6GR-Waveform"
year: 2026
venue: "RAN1#124bis, Saint Julians, Malta, 2026-04-13 to 04-17"
identifiers:
  spec: "6GR FS_6G_Radio SI"
related:
  - "[[260501_6GR-Waveform-PAPR削減_変遷]]"
  - "[[260430_RAN1-124-125-13トピック議論変遷]]"
  - "[[260428_RAN1-124bis-MIMO-operation-10.5.2]]"
---

# Chair Notes RAN1#124bis — AI 10.2.1 Waveform（抜粋）

> 出典: [Chair notes RAN1#124bis_eom5.docx](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)、アクセス日 2026-04-30
> 変換: `pandoc 'Chair notes RAN1#124bis_eom5.docx' -t gfm --wrap=none`
> 抽出範囲: §"Waveform for 6GR air interface" のみ（MRSS § の末尾と Channel coding § の冒頭の境界）。
> 元ファイルサイズ: 1.28 MB / 12,041 行。本ファイルは Waveform セクション 336 行のみ。

> **読み方**: `<span class="mark">…</span>` は元 docx の蛍光マーキング。NOTED テーブル（§ 後段）は #124bis で **deprioritized** された提案リスト — 重要な「対立軸の決着」点。

---

# Waveform for 6GR air interface

[124b-R20-6GR-Waveform] Email discussion on Rel-20 6GR-Waveform – Klaus (Nokia)

R1-2603279 Session Notes of AI 10.2.1 Ad-Hoc Chair (NTT DOCOMO, INC.)

Session notes are endorsed and incorporated the session notes below.

### Waveform

*Note 1: Including proposals for improving spectrum efficiency, power efficiency, coexistence and coverage, etc.*

*Note 2: Companies' views about how to coordinate the study of waveform between RAN1 and RAN4, e.g., work plan, and sequence of investigation of some aspects, etc.*

## R1-2603310 / R1-2603311 / R1-2603312 — Feature Lead summary #1〜#3 — Moderator (Nokia)

**Agreement:** Prioritize the following cases in the RAN1 study on UL coverage improvements through low UL PAPR enhancement for DFT-s-OFDM, based on Table in 5.3.1 of R1-2603312:

- **FDSS** \[for π/2 BPSK, QPSK, 16QAM\]
  - Opt1: Transparent filter
    - Filter defined through transmitter requirement such as spectrum flatness by RAN4
  - Opt2: non-transparent filter
    - Filter coefficients specified in RAN1
  - Note: This includes all the listed FDSS filtering variants

- **FDSS for \[π/2 BPSK, QPSK, 16QAM\] with spectral extension**
  - For FDSS part,
    - Opt1: Transparent filter (filter defined through transmitter requirement such as spectrum flatness by RAN4)
    - Opt2: non-transparent filter (filter coefficients specified in RAN1)
  - Note: This includes all the listed variants of the spectrum extension

- **FDSS for π/2 BPSK with spectral truncation**
  - For FDSS part,
    - Opt1: Transparent filter
    - Opt2: non-transparent filter (filter coefficients specified in RAN1)
  - Note: This includes all the listed variants of the spectrum truncation
  - Note: At least one variant of spectral extension, offset-QPSK with smaller DFT size can result in the same signal as the FDSS for π/2 BPSK-ST

- Note: companies are encouraged to report whether transparent CFR is used or not

## R1-2603313 — Feature Lead summary #4 — Moderator (Nokia)

**Conclusion:** The study on the following listed proposals is **noted**. Further discussion on these is not planned under the waveform agenda item in RAN1 unless tasked by RAN at or after RAN#112.

| Proposal | Company providing evaluation (Tdoc#) | Should consider for 6GR? |
|:---|:---|:---|
| TR (downlink) | ZTE (R1-2602275) | ZTE: YES |
| DFT-s-OFDM with enhanced time domain resource multiplexing | ZTE (R1-2602275) | ZTE: YES |
| GFB-OFDM | ZTE (R1-2602275) | ZTE: YES |
| SLM | ZTE (R1-2508856), CATT (R1-2602492) | ZTE: YES, CATT: YES |
| **Zak-OTFS-over-OFDM** | **Cohere (R1-2602263)** | Cohere: YES |
| **Zak-OTFS** | **Cohere (R1-2602263)** | Cohere: YES |
| Interlace OFDM | (no proponent listed) | — |
| Spectral Precoding | NICT (R1-2602831) | NICT: YES |
| OSDM | Sheffield (R1-2602259) | Shef: YES |
| CP-OFDM with time-domain precoding | PCL (R1-2602302) | PCL: YES |
| DFT-s-OFDM with flexible frequency domain mapping (e.g., FD data-DMRS multiplexing) | QC (R1-2603008), CATT (R1-2602492) | QC: Yes, CATT: Yes |
| Multi-Tx Enhancement for DFT-s-OFDM | QC (R1-2603008), IITH/Wisig (R1-2602880) | QC: Yes, IITH/Wisig: Yes |
| Two-segment DFT-S-OFDM | CATT (R1-2602492) | CATT: Yes |

### Observations — Max-rank = 2 for UL DFT-s-OFDM

- Companies report negligible SNR loss from DFT-s-OFDM with larger number of aNB Rx antenna elements, such as at least 16 or 32. Link level loss with 4 layers has not been studied. A lower number of aNB antenna elements may result with SNR loss at the receiver
- All companies acknowledge that when the UE is Tx power limited, there is a Tx power gain from DFT-s-OFDM, **highest reported gain of around 2.5 dB**.
- The system level impact depends on scenario and scheduling strategy due to vastly differing probabilities for UE to be power limited and use rank=2, as well as the used traffic model and the assumed number of aNB Rx antenna elements.

  - **Two companies reported cases with average system level throughput LOSS** \[R1-2601827 Nokia, R1-2602177 Samsung\], of which one company indicated cell edge throughput loss \[R1-2602177 Samsung\]. One company reported no average and cell-edge system level throughput gain \[R1-2602254 InterDigital\], while **6 companies reported cases with average system level throughput GAINS** and/or cell edge throughput gains \[R1-2602004 vivo, R1-2603056 DOCOMO, R1-2602468 Ericsson, R1-2603008 Qualcomm, R1-2603286 Apple, R1-2601921 Huawei\].

  - **Codebook for multi-layer UL DFT-s-OFDM**
    - The lower PAPR property of DFT-s-OFDM is **diminished with coherent precoders** due to mixing of two (or more) layers for each power amplifier.
    - RAN1#124 agreed to focus the DFT-s-OFDM studies to non-coherent CB only (with the exception of lower number of layers than Tx antennas) for 2Tx UE for waveform evaluation purposes.
    - **Four companies report moderate system level gains** for DFT-s-OFDM non-coherent codebook only relative to CP-OFDM non-coherent codebook \[R1-2603056 DOCOMO, R1-2602468 Ericsson, R1-2603008 Qualcomm, R1-2603286 Apple\], while **two companies report system level loss** \[R1-2601827 Nokia, R1-2602177 Samsung\].
    - One company reports system level gains also for DFT-s-OFDM with **coherent codebook** relative to CP-OFDM with coherent codebook \[R1-2602468 Ericsson\].
    - **Six companies** report system level gains for DFT-s-OFDM with non-coherent multi-layer codebook AND coherent single-layer codebook relative to CP-OFDM with coherent single/multi-layer codebook \[R1-2602426 OPPO, R1-2602468 Ericsson, R1-2602004 vivo, R1-2603008 Qualcomm, R1-2603286 Apple, R1-2601921 Huawei\], while **one company** reports no gain \[R1-2602254 InterDigital\].

  - **Dynamic waveform switching (DWS)**
    - One company observes comparable performance for DWS among DFT-s-OFDM (1L+2L) and CP-OFDM (1L+2L) vs DWS among DFT-s-OFDM (1L only) and CP-OFDM (1L+2L) for full buffer; gain for non-full buffer \[R1-2603286 Apple\].
    - One company observes loss for DFT-s-OFDM (1L+2L) compared to DFT-s-OFDM (1L only) + CP-OFDM (1L+2L) with waveform switching \[R1-2601827 Nokia\].
    - One company observes comparable performance \[R1-2602254 InterDigital\].
    - One company observes loss for DFT-s-OFDM (1L) and DFT-s-OFDM/CP-OFDM (2L) compared to DFT-s-OFDM (1L only) + CP-OFDM (1L+2L) \[R1-2602177 Samsung\].

Note: this observation is not intended to be captured as it is in TR.

## R1-2603314 / R1-2603315 — Feature Lead summary #5/#6 — Moderator (Nokia)

(本文中の合意事項は EoM5 ではこれ以上明示的に記録されていない — 残課題は #125 へ持ち越し)

## Submitted Tdoc list (AI 10.2.1, RAN1#124bis)

| Tdoc | Title | Source |
|:---|:---|:---|
| R1-2601827 | On remaining aspects of waveform for 6GR | Nokia |
| R1-2601895 | Discussions on 6G Waveforms | Lekha Wireless Solutions |
| R1-2601921 | Waveform for 6GR air interface | Huawei, HiSilicon |
| R1-2601947 | Discussion on 6G Waveform | NEC |
| R1-2602004 | Discussion on Waveform for 6GR air interface | vivo |
| R1-2602050 | Discussion on the waveform design for 6G radio | CMCC |
| R1-2602125 | Waveform for 6GR air interface | Tejas Networks Limited |
| R1-2602127 | Discussion on waveform for 6GR | LG Electronics |
| R1-2602134 | Discussion on waveform for 6GR | Spreadtrum, UNISOC |
| R1-2602177 | Discussion on waveform for 6GR | **Samsung** |
| R1-2602254 | Waveform for 6GR air interface | InterDigital, Inc. |
| R1-2602259 | New Waveform for 6GR - OSDM | University of Sheffield |
| R1-2602263 | Waveform for 6GNR1 | **Cohere Technologies** |
| R1-2602275 | Views on the waveform for 6G | ZTE Corporation, Sanechips |
| R1-2602302 | Discussion on waveform for 6GR air interface | Pengcheng Laboratory |
| R1-2602366 | PAPR reduction for 6GR Waveforms | Sony |
| R1-2602426 | On waveform enhancements/additions for 6G Radio | OPPO |
| R1-2602455 | Waveform for 6GR air interface | MediaTek Inc. |
| R1-2602468 | On waveform for 6GR | Ericsson |
| R1-2602492 | Discussions on waveform for 6GR | CATT |
| R1-2602565 | Further discussion on 6GR waveform | Xiaomi |
| R1-2602624 | Discussion on waveform for 6GR air interface | Panasonic |
| R1-2602627 | Waveform for 6GR Air Interface | Google |
| R1-2602666 | On Waveforms for 6GR air interface | Apple |
| R1-2603286 | On Waveforms for 6GR air interface (revision) | Apple |
| R1-2602781 | Discussion on 6GR waveform | ETRI, University of Surrey |
| R1-2602831 | New waveform for 6GR air interface | NICT |
| R1-2602880 | On Uplink Multi-layer enhancements | IITH, Wisig Networks |
| R1-2602900 | Discussion on Waveform for 6GR | Lenovo |
| R1-2602925 | Waveform for 6GR air interface | Charter Communications, Inc |
| R1-2602932 | Discussion on waveform for 6GR air interface | Ofinno |
| R1-2602951 | Study on waveform for 6GR | Sharp |
| R1-2603008 | Waveforms for 6GR | **Qualcomm Incorporated** |
| R1-2603056 | Discussion on Waveform | NTT DOCOMO, INC. |
| R1-2603094 | Discussion on waveform for 6GR | KAIST |
| R1-2603117 | IMU Views on Waveform for 6GR | IMU, Turkcell |
| R1-2603123 | Discussion on waveform for 6G communication system | Quectel |
| R1-2603149 | Discussion on Waveform for 6GR Air Interface | Indian Institute of Tech (M) |
| R1-2603150 | Discussion on waveform for 6GR air interface | KDDI Corporation |
| R1-2603231 | CP length reduction for 6G Waveform | ST Engineering iDirect |

## RAN1↔RAN4 連携（参考: 5.4.4 章の関連 LS、別 AI から本 AI へ参照）

- **R1-2508069 → R1-2601767** — Reply LS on PA models in 6GR waveform evaluations (RAN4 → RAN1; co-source: Huawei, vivo)
  - "RAN1's agreements on evaluation assumptions should also be taken into account for RAN4's evaluations"
  - RAN1 が RAN4 の波形評価仮定を考慮することを確認
  - 本 AI 10.2.1 で扱う（dedicated action 不要）
