---
title: "NR Dynamic spectrum sharing in Rel-17 — 3GPP Technologies page"
type: web-article
source_url: https://www.3gpp.org/technologies/nr-dynamic-spectrum-sharing-in-rel-17
accessed: 2026-05-01
authors: ["3GPP MCC"]
year: 2022
venue: "3gpp.org Technologies page (Rel-17 summary)"
identifiers:
  arxiv: ""
  doi: ""
  tdoc: "RP-211345 (WI), RP-220464 (WI summary)"
  spec: "TR 21.917 §15"
related:
  - "[[260501_DSS-Dynamic-Spectrum-Sharing-3GPP採用経緯]]"
---

# NR Dynamic spectrum sharing in Rel-17 — 3GPP Technologies page

> 出典: <https://www.3gpp.org/technologies/nr-dynamic-spectrum-sharing-in-rel-17>
> 投稿日: Aug 08, 2022（最終更新 Aug 23, 2022）
> アクセス日: 2026-05-01
> 取得方法: `curl -A "Mozilla/5.0" https://www.3gpp.org/technologies/nr-dynamic-spectrum-sharing-in-rel-17`（WebFetch は 403 のため）
> 引用範囲: 公開情報の原文。研究目的の引用に限定。

以下は 3GPP 公式 Technologies ページの本文を、HTML タグを除去して抽出したもの。

---

## 本文（抽出）

> Source: Summary of Rel-17 Work Items (TR 21.917, section 15), 'Summary of Rel17 WI on NR DSS' (RP-220464).

Dynamic spectrum sharing (DSS) provides a very useful migration path from LTE to NR by allowing LTE and NR to share the same carrier. DSS was included already in Rel-15 and further enhanced in Rel-16. As the number of NR devices in a network increases it is important that sufficient scheduling capacity for NR UEs on the shared carriers is ensured. This is addressed by the **NR_DSS Work Item (WI)**, which introduces the support for cross-carrier scheduling from SCell to PCell/PSCell.

### Work Item identifiers

| Field | Value |
|:---|:---|
| UID (umbrella) | 860043 |
| WI name | NR Dynamic spectrum sharing (DSS) — `NR_DSS` |
| Approval Tdoc | RP-211345 |
| UID (Core part) | 860143 |
| Core part name | Core part: NR DSS — `NR_DSS-Core` |
| Lead WG | RAN1 |
| Releases | Rel-17（拡張は Rel-18 / Rel-19 でも継続） |

### Rel-17 で追加された主要振る舞い（cross-carrier scheduling）

- When cross-carrier scheduling from an SCell to sPCell is configured:
  - PDCCH on that SCell can schedule sPCell's PDSCH and PUSCH.
  - PDCCH on the sPCell can schedule sPCell's PDSCH and PUSCH but cannot schedule PDSCH and PUSCH on any other cell.
- Only **one** SCell can be configured to be used for cross-carrier scheduling to sPCell.
- The maximum number of monitoring candidates and non-overlapping CCEs for PDCCH monitoring (to schedule the sPCell) are split between the sPCell and the SCell used for scheduling the sPCell. The split is indicated via an RRC configured scaling factor.
- Note: sPCell refers to 'Special Cell'. For Dual Connectivity operation the term Special Cell refers to the PCell of the MCG or the PSCell of the SCG, otherwise the term Special Cell refers to the PCell.

### Impacted existing specifications

| TS | Description of change |
|:---|:---|
| 38.211 | NR; Physical channels and modulation — L1 functionality to support the DSS enhancements |
| 38.212 | NR; Multiplexing and channel coding — L1 functionality to support the DSS enhancements |
| 38.213 | NR; Physical layer procedures for control — L1 functionality to support the DSS enhancements |
| 38.214 | NR; Physical layer procedures for data — L1 functionality to support the DSS enhancements |
| 38.331 | NR; Radio Resource Control (RRC); Protocol specification — RRC signalling to support the DSS enhancements |
| 38.300 | NR; NR and NG-RAN Overall description; Stage-2 — Stage 2 spec updates to support the DSS enhancements |
| 38.306 | NR; User Equipment (UE) radio access capabilities — UE capability updates to support the DSS enhancements |

### References

- List of related CRs: select "TSG Status = Approved" in <https://portal.3gpp.org/ChangeRequests.aspx?q=1&workitem=860043,860143>
- 3GPP Work Plan: <https://www.3gpp.org/ftp/Information/WORK_PLAN/>（Excel の acronym フィールドで 'DSS' を検索）

### 略語（原文記載）

| 略語 | 展開 |
|:---|:---|
| PCell / SCell | Primary Cell / Secondary Cell |
| PDCCH | Physical Downlink Control channel |
| PDSCH | Physical Downlink Shared channel |
| PSCell | Primary SCG Cell |
| PUSCH | Physical Uplink Shared channel |
| SCG | Secondary Cell Group |
| sPCell | Special Cell |

---

> 注: 本ページに添えられた IMPORTANT NOTE — "these pages are a snapshot of the work going on in 3GPP. The full picture of all work is contained in the Work Plan."
