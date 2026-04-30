---
title: "6GR Waveform — DFT-s-OFDM PAPR 削減候補の議論変遷（RAN1#124 → #124bis → #125）"
status: draft
confidence: high
created: 2026-05-01
updated: 2026-05-01
axes:
  technology-layer: [phy-waveform, phy-ul-mimo]
  generation: [rel-20-6g]
  value: [coverage, energy-efficiency, throughput]
  market: [consumer-xr, b2b-industrial, ntn-satellite]
  adoption-factors: [standard-convergence, backward-compat, ecosystem-readiness]
  ip: [novelty, inventive-step, spec-mapping]
sources:
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx
    title: "Chair notes RAN1#124 - eom_03.docx（FL: Klaus / Nokia）"
    accessed: 2026-04-30
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx
    title: "Chair notes RAN1#124bis_eom5.docx（FL: Klaus / Nokia）"
    accessed: 2026-04-30
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/drafts/10.2(Waveform)/RAN1-124%2010.2.1%20FL%20summary%20v68_KDDI_QC.docx
    title: "RAN1-124 10.2.1 FL summary v68 (KDDI/QC checkout) — 60 社の提案集約版"
    accessed: 2026-04-30
  - url: https://arxiv.org/abs/2509.19064
    title: "Optimum Spectrum Extension for PAPR Reduction of DFT-s-OFDM (Pitaval, Berggren, Popovic — Huawei)"
    accessed: 2026-04-30
  - url: https://arxiv.org/html/2508.08225v1
    title: "Industrial Viewpoints on RAN Technologies for 6G (arXiv:2508.08225)"
    accessed: 2026-04-30
  - url: https://arxiv.org/html/2404.16137v1
    title: "Learned Pulse Shaping Design for PAPR Reduction in DFT-s-OFDM (Carpi, Garg, Erkip — NYU/Samsung)"
    accessed: 2026-04-30
references:
  - "[[Chair-Notes-RAN1-124-Waveform]]"
  - "[[Chair-Notes-RAN1-124bis-Waveform]]"
up: "[[260430_RAN1-124-125-13トピック議論変遷]]"
related:
  - "[[260428_RAN1-124bis-MIMO-operation-10.5.2]]"
  - "[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]"
trace:
  ai_id: "ai_6gr_waveform"
  meetings_in_scope: ["RAN1#124", "RAN1#124bis", "RAN1#125"]
  completeness:
    chair_notes_obtained: ["RAN1#124", "RAN1#124bis"]
    chair_notes_missing: ["RAN1#125"]   # 未開催（FTP folder のみ存在）
    tdocs_obtained: 1   # FL summary v68（個別社 Tdoc は未取得）
    fl_summary_obtained: ["RAN1#124 10.2.1 v68_KDDI_QC"]
    fl_summary_missing: ["RAN1#124bis 10.2.1 (R1-2603310〜R1-2603315 Nokia)"]
---

# 6GR Waveform — DFT-s-OFDM PAPR 削減候補の議論変遷

> **位置づけ**: 起点ノート [[260430_RAN1-124-125-13トピック議論変遷]] §1（Waveform）の **縦深堀**。Chair Notes EoM (#124/#124bis) と #124 FL summary v68 を一次情報として、DFT-s-OFDM PAPR 削減候補を巡る企業対立を技術根拠まで追う。
> **scope**: AI 10.2.1（Waveform、umbrella 10.2）のみ。CP-OFDM PAPR 削減と DL DFT-s-OFDM は別途扱い（後者は #124 で deprioritize 済）。
> **confidence: high**（一次情報ベース）— 個別 Tdoc は未取得のため、企業内部の評価根拠の細部は要確認。

---

## 0. 結論サマリー

### 0.1 #124 → #124bis でわかったこと

| 観点 | 到達点 |
|:---|:---|
| **DL DFT-s-OFDM** | **deprioritize（廃案）** — Nokia/Samsung/Sharp/Ericsson 主導で「合意」。明示的な対立軸は存在せず |
| **UL low-PAPR DFT-s-OFDM** | high-priority study に格上げ。#124 で 11 候補リスト化、#124bis で **3 候補に絞り込み**（FDSS / FDSS-SE / FDSS-ST for π/2 BPSK） |
| **AI/ML PAPR** | #124 リストに含まれたが、#124bis で down-selection の主軸からは外れる。Samsung/vivo 提案は維持されるが down-selected の 3 候補には入らず |
| **Multi-rank UL DFT-s-OFDM** | high-priority study。**rank-2 のみ非コヒーレント precoder** が #124 baseline。#124bis で評価結果が割れる（6 vs 2 vs 1） |
| **新規波形（Zak-OTFS など）** | #124bis で「**noted**（廃案）」。Cohere の Zak-OTFS は Nokia/Qualcomm の deprioritize 提案により Tdoc-only 運用で打ち切り |

### 0.2 主要対立軸（明示的に確認できたもの）

| 対立 | 派閥 A | 派閥 B | 決着 |
|:---|:---|:---|:---|
| **Filter spec 化** | 非透過（RAN1 specifies coefficients） — Samsung, Apple | 透過（RAN4 spectrum flatness のみ） — Nokia 寄り | **両論併記（Opt1+Opt2）** で #124bis 終結 |
| **AI/ML PAPR** | 推進 — Samsung, vivo, ETRI/Surrey | 慎重・否定 — Nokia, Qualcomm | down-select から外れたが「研究は継続」 |
| **Zak-OTFS / 新規波形** | Cohere（独立支援） | Nokia, Qualcomm（明示的 deprioritize） | **#124bis で noted（廃案）** |
| **Multi-rank UL DFT-s-OFDM** | 推進 — Huawei, vivo, DOCOMO, Apple, Qualcomm, Ericsson, OPPO | 反対 — InterDigital, Nokia, Samsung（条件付き） | 評価継続、結論は #125 以降 |

### 0.3 #125 の見どころ

- 3 候補（FDSS / FDSS-SE / FDSS-ST for π/2 BPSK）の Opt1 vs Opt2（透過 vs 非透過）の **どれか一方への絞り込み**
- Multi-rank UL DFT-s-OFDM の **採択可否 + max rank**（2 で固定 or 4 まで再開）
- TR への Net Gain 値の取り込みフォーマット
- Jio Platforms は AI 10.2.1 では寄書未提出（10.3.1 Channel Coding と 10.4 Energy Efficiency が活動領域）— **ユーザー入力にあった「Jio の ZAC OTFS」は Cohere の Zak-OTFS の誤認**を本ノートで訂正

---

## 1. 用語整理（読み手のための事前整理）

| 略号 | 意味 | 何が嬉しいか |
|:---|:---|:---|
| **DFT-s-OFDM** | Discrete Fourier Transform-spread OFDM。OFDM の前段に DFT precoding を入れて単一搬送波（SC）的性質を回復した波形 | UL の **PAPR が CP-OFDM より低く**、UE の PA バックオフ削減＝カバレッジ拡張に直結 |
| **PAPR** | Peak-to-Average Power Ratio。波形の瞬時ピークと平均の比 | PA を線形領域で動かすには PAPR 分の電力ヘッドルームが必要。**PAPR 1 dB 改善 ≒ Tx 電力 1 dB 増 ≒ 同 dB のカバレッジ改善** |
| **FDSS** | Frequency Domain Spectrum Shaping。DFT 出力に周波数ドメインで window/filter を掛けて PAPR を整形 | π/2 BPSK 等と組合せ、特に Apple の GMSK 近似で **PAPR < 1 dB（Samsung 観測）** |
| **FDSS-SE** | FDSS + Spectrum Extension。DFT 出力を **拡張（重複）して送信**、受信側でエッジを削る | 拡張比 α = (B-A)/B。InterDigital 観測: α=1/4 で正の Net Gain、α≧3/8 で負 |
| **FDSS-ST** | FDSS + Spectrum Truncation for π/2 BPSK。**送信側で DFT サイズを縮め**、受信側でゼロ埋めして復元 | Qualcomm 推し。π/2 BPSK 専用 |
| **Tone Reservation** | データに使わないトーンを残してピーク打ち消し信号を載せる | 古典手法。Qualcomm が「**サイドバンド隣接トーン**」で限定 |
| **Net Gain** | 評価指標（合意済）。`PAPR/Tx 電力 gain – SNR degradation @10% BLER` | 単純な PAPR dB ではなく、**復号 BLER まで含めた実効カバレッジ gain** |
| **Coherent / Non-coherent precoder** | UE の Tx ポート間位相整合度。coherent は完全位相同期 | DFT-s-OFDM の低 PAPR 性は **コヒーレント precoder で消失** — 単一 PA に複数レイヤが混合されるため |
| **CFR / CFR-SE** | Crest Factor Reduction（一般用語） / +Spectrum Extension。vivo の主用語 | FDSS の上位概念として vivo が議論を統合しようとしている |
| **DWS** | Dynamic Waveform Switching。スロット単位で DFT-s-OFDM/CP-OFDM 切替 | Rel-18 で導入。multi-layer 時の評価軸 |

---

## 2. RAN1#124（Gothenburg, 2026-02-09 〜 02-13）

> FL: Klaus (Nokia) / Ad-Hoc Chair: NTT DOCOMO  
> Tdoc 件数（AI 10.2.1）: 37 件 + revisions  
> FL summary versions: v00（Moderator）→ **v68（KDDI_QC checkout）** が最終

### 2.1 概況と論争の起点

#122 (2025-08) で 6GR の **「DL=CP-OFDM、UL=DFT-s-OFDM」継承**が大枠合意済み（[6Ghow First Agreements](https://www.6ghow.com/first_6G_agreements/)）。しかし「DFT-s-OFDM を DL にも使うか」「UL の PAPR をどう下げるか」「multi-rank UL DFT-s-OFDM を許すか」の 3 大論点は #122 / #123 では持ち越されていた。

#124 はこれら 3 点に **方向性の合意**を与えた最初の会合。

### 2.2 主要争点の顛末

#### 2.2.1 DL DFT-s-OFDM — **deprioritize で決着**

[Chair Notes 124 — R1-2600787 FL #2](Chair-Notes-RAN1-124-Waveform.md) が確定:

> **Conclusion:** DFT-s-OFDM waveform including related enhancements for 6GR **Downlink** will be no further discussed as part of AI 10.2.1.

主要根拠（FL summary v68 から再構成）:

| 企業 | Tdoc | 主張 |
|:---|:---|:---|
| **Nokia** | R1-2600027 §3 | (a) DL CP-OFDM + 透過 PAPR 削減で同等 PAPR、(b) DL EIRP は CP-OFDM で既に上限張付き、(c) UE/BS 両側で DFT 復号負荷増、(d) MU-MIMO・MRSS 制約多発 |
| **Samsung** | R1-2600751 §6 | F1〜F5（非連続 FDRA / CA / 高 PA レーティング / ビーム / multi-layer MIMO）+ D1〜D3（多重損 / Rx 複雑度 / SE 損） |
| **Sharp** | R1-2600914 §1 | 直接「RAN1 should NOT study DL DFT-s-OFDM」 |
| **Ericsson** | R1-2601156 §1 | NES/NTN/ISAC/7GHz 全てで利点なし、システム複雑度回避 |
| OPPO | R1-2600188 §7 | TN は不支持。NTN 用は別途検討 |

支持側（少数派）:
- **Ofinno** (R1-2601092): 「7GHz 大規模アンテナのエネ効率向上に有効」「同期/WUS 等共通信号には PAPR が小さい方が有利」
- **PCL** (R1-2601212): 「DL の補助波形として」
- **Quectel** (R1-2601294): MU-DL-DFT-s-OFDM PDSCH での Joint DFT
- **Hanbat NU** (R1-2601047): 学術視点で DL FDSS+SLM
- **Huawei** (R1-2600138): DL 全廃ではなく「**追加同期信号 / DL-WUS 用**」のみ Net Gain 評価対象として残す

→ **Nokia 主導の deprioritize 派が圧倒**。例外的に Huawei の「DL 用途は同期信号/WUS にスコープ限定」が #125 以降の AI 10.5（IA）/ 10.6（WUS）に飛び火する可能性のみ残る。

#### 2.2.2 UL low-PAPR — **11 候補リスト化合意**

[Chair Notes 124 — R1-2600789 FL #4](Chair-Notes-RAN1-124-Waveform.md) で **further consideration** リストが固定:

```
Non-AI-ML-based:
  - FDSS                           [Samsung, Ofinno, InterDigital, Apple, Sharp, Ericsson]
  - FDSS – spectrum extension      [Nokia, Samsung, Apple, Ofinno, Sharp, Ericsson, ZTE]
  - FDSS – spectrum truncation for π/2 BPSK
                                   [Qualcomm, PCL, Ofinno, Ericsson]
  - Tone Reservation               [ZTE, Lekha, Qualcomm]
  - GMSK-Approximation based FDSS  [Apple]
  - 3-tap filter based FDSS        [Rel-19 NES carry-over R1-2508684]
  - CFR-SE                         [vivo]
  - Offset-QAM / π/2-PAM with FDSS-ST  [MediaTek, Huawei, Qualcomm, Samsung]
  - Offset-QAM / π/2-PAM with FDSS-SE  [MediaTek, Huawei, Samsung, Apple]
  - Interpolation-based modulation [ZTE]
  - AFDM based on DFT-s-OFDM       [ETRI/Surrey, SJTU/NERC-DTV]
AI-ML-based:
  - AI/ML-based waveform           [vivo, Samsung]
```

**重要な構造**:
1. **非 AI/ML 11 種を網羅、AI/ML は別カテゴリで 1 種**。これは「AI/ML を従来手法と並列評価」という慎重派（Nokia/Qualcomm）の妥協ライン
2. **Samsung は AI/ML カテゴリ + 5 つの非 AI/ML 候補（FDSS, FDSS-SE, FDSS-ST, Offset-QAM ST, Offset-QAM SE）の両足張り** — 主導権確保戦略
3. **Cohere の Zak-OTFS はこのリストに**含まれない — 別カテゴリ「new waveform」へ流される伏線（#124bis で deprioritize）

#### 2.2.3 評価メトリクス（合意済）

[Chair Notes 124 — R1-2600788 FL #3](Chair-Notes-RAN1-124-Waveform.md):

- SLS (System-Level Sim): UPT (90%/mean/median/cell edge 5&10%-tile) + 全 UE の瞬時 UL Tx 電力 CDF + UL Tx rank 統計 + MCS 統計
- LLS (Link-Level Sim): BLER curves（HARQ 無効、同 rank/同 RA/同 Tx 電力で DFT-s-OFDM vs CP-OFDM）+ **Net Gain**
- ベースライン: **NR Rel-15 DFT-s-OFDM** + Rel-16 full power mode 1
- A（subcarrier 数）の制約: 12 \* 2^x \* 3^y \* 5^z（Opt1）or 2^x \* 3^y \* 5^z（Opt2）— **DFT 効率**

> Nokia (R1-2600027) と Qualcomm (R1-2601268) が「A の値は efficient DFT サイズになるべき」と独立に提案、両社が珍しく一致。

#### 2.2.4 Multi-rank UL DFT-s-OFDM — high-priority study に格上げ

| 観点 | 内容 |
|:---|:---|
| **合意（#124）** | rank-2/2Tx に絞る + **DFT-s-OFDM 側は非コヒーレント precoder のみ許容** |
| **理由（FL summary v68 §"Rank>1 for UL DFT-s-OFDM"）** | コヒーレント precoder は複数レイヤを 1 PA に混合 → 低 PAPR 性が消失（[Chair Notes 124bis Observation](Chair-Notes-RAN1-124bis-Waveform.md) で再確認） |
| **企業対立** | 推進 12 社 vs 反対 1 社（**InterDigital R1-2600801: 「Multi-rank UL DFT-s-OFDM is not supported for 6GR」**） + Nokia の懐疑（rank-1 ベースライン提案） |

### 2.3 RAN1#124 で確定した Tdoc-cited 合意

| Agreement | 制約条件 |
|:---|:---|
| 11 候補リスト（§2.2.2） | down-select は #124bis 以降 |
| Net Gain 定義 + SLS/LLS メトリクス | 全候補共通の評価枠 |
| A = 12 \* 2^x \* 3^y \* 5^z または 2^x \* 3^y \* 5^z | DFT 効率制約 |
| rank-2 / 非コヒーレント precoder（DFT-s-OFDM） | `Release 16 full power mode 1 enabled` |
| NR Rel-15 DFT-s-OFDM = baseline | 追加要件: 受信側で必要なフィルタ係数等の knowledge を開示 |

---

## 3. RAN1#124bis（Saint Julians, Malta, 2026-04-13 〜 04-17）

> FL: Klaus (Nokia) 継続  
> Tdoc 件数（AI 10.2.1）: 40 件超（Charter Communications 等の新規エントリ含む）  
> FL summary R1-2603310〜R1-2603315 — **本ノート時点で個別 docx 未取得**（注: ユーザー入力の v56 は #124 のもので #124bis ではない）

### 3.1 概況

「リスト化」から「down-selection」へ。Chair Notes EoM5 から **3 つの大きな決着** が読める:

1. **down-select 完了**: 11 候補 → 3 候補（FDSS / FDSS-SE / FDSS-ST for π/2 BPSK）
2. **新規波形群の deprioritize**: Cohere の Zak-OTFS / Zak-OTFS-over-OFDM、ZTE の TR(DL)/eDFT-s-OFDM/GFB-OFDM/SLM、Sheffield の OSDM、PCL の CP-OFDM with TD precoding、QC の DFT-s-OFDM with flexible FD mapping、QC/IITH の Multi-Tx Enhancement、CATT の Two-segment DFT-S-OFDM ──**全 13 提案を「noted」**
3. **multi-rank の評価結果が割れる** — 「Max-rank=2」と「乖離する Net Gain」を Observations として記録、TR には未反映で持ち越し

### 3.2 down-select されたもの・されなかったもの

#### 3.2.1 Survived（3 候補）

[Chair Notes 124bis — R1-2603310〜12 FL #1〜#3](Chair-Notes-RAN1-124bis-Waveform.md) に基づく:

| 候補 | スコープ | 各候補に Opt1（透過 / RAN4 spectrum flatness）と Opt2（非透過 / RAN1 specifies filter coefficients）の二案併記 |
|:---|:---|:---|
| **FDSS** | π/2 BPSK, QPSK, 16QAM | 全 FDSS filtering 派生を包含（GMSK-approx, 3-tap, half-sine 等） |
| **FDSS – Spectral Extension** | π/2 BPSK, QPSK, 16QAM | 全 SE 派生を包含 |
| **FDSS – Spectral Truncation** | **π/2 BPSK のみ** | Note: 拡張の 1 派生 + offset-QPSK with smaller DFT が同等信号 |

> **Note: 「companies are encouraged to report whether transparent CFR is used or not」** — vivo の CFR 概念を「報告事項」として残し、FDSS と並列で評価可能にした

#### 3.2.2 Noted（13 提案、#124bis で deprioritize）

| 提案 | 提案社 | 廃案理由（推定/明示） |
|:---|:---|:---|
| TR (downlink) | ZTE | DL 全体が #124 で deprioritized |
| DFT-s-OFDM with enhanced TD resource multiplexing | ZTE | high-speed scenario 限定、汎用性不足 |
| GFB-OFDM | ZTE | spectrum utilization 改善余地が小さい |
| SLM | ZTE, CATT | 副情報のオーバーヘッド大 |
| **Zak-OTFS-over-OFDM** | **Cohere** | Nokia 提案: CP-OFDM が現実条件で同等以上、想定された伝搬条件は典型でない、システム変更が大、複雑度増 |
| **Zak-OTFS** | **Cohere** | 同上 |
| Interlace OFDM | （提案社空欄） | サポート皆無 |
| Spectral Precoding | NICT | 単独提案 |
| OSDM | Sheffield | 単独提案 |
| CP-OFDM with TD precoding | PCL | 単独提案 |
| **DFT-s-OFDM with flexible FD mapping** | **QC, CATT** | FDSS 派生で類似機能をカバーできる |
| **Multi-Tx Enhancement for DFT-s-OFDM** | **QC, IITH/Wisig** | rank-2 議論と重複、本 AI でなく MIMO AI 10.5 へ |
| Two-segment DFT-S-OFDM | CATT | 単独提案 |

> **重要観察**: Qualcomm の **「DFT-s-OFDM with flexible FD mapping」と「Multi-Tx Enhancement」両方が deprioritize された**点。Qualcomm は #124bis で「自社主張の半分」を譲った形。残った主軸は **「FDSS-ST for π/2 BPSK + Tone Reservation」**。

#### 3.2.3 Multi-rank UL DFT-s-OFDM の評価結果（[Chair Notes 124bis Observations](Chair-Notes-RAN1-124bis-Waveform.md)）

「6 vs 2 vs 1」の構図が明示:

| 観点 | Gain 派 | Loss 派 |
|:---|:---|:---|
| **非コヒーレント CB のみ vs CP-OFDM 非コヒーレント CB** | DOCOMO, Ericsson, Qualcomm, Apple（4 社、moderate gain） | Nokia, Samsung（2 社、SLS loss） |
| **非コヒーレント multi-layer + コヒーレント single-layer vs CP-OFDM コヒーレント** | OPPO, Ericsson, vivo, Qualcomm, Apple, Huawei（6 社、SLS gain） | InterDigital（1 社、no gain） |
| **コヒーレント CB DFT-s-OFDM vs コヒーレント CB CP-OFDM** | Ericsson のみ（1 社、SLS gain） | — |
| **Tx 電力 gain（UE が Tx 電力制限時）** | 全社認める、最大 **2.5 dB** | — |

> **構造的ポイント**:
> - **Nokia と Samsung が loss を報告**したことが #125 以降の議論で重く効く（FL は Nokia 自身）
> - **Apple、Qualcomm、Ericsson、Huawei が gain を主張** — 中国系（Huawei）と米系（Apple, QC）が珍しく一致
> - InterDigital は #124 「multi-rank UL DFT-s-OFDM is not supported」を維持

### 3.3 RAN1↔RAN4 連携（#124bis 新規）

`R1-2508069 → R1-2601767`（co-source: Huawei, vivo）— **PA models in 6GR waveform evaluations** の Reply LS。

> "RAN1's agreements on evaluation assumptions should also be taken into account for RAN4's evaluations" + RAN4 の評価仮定を RAN1 が考慮する

→ **PA モデル統一が #125 以降の評価結果に直結**。RAN1 の Net Gain 数値が RAN4 の testability/EVM/IBE/ACLR と整合する必要。

---

## 4. 企業マトリクス — 行=候補手法、列=企業、セル=賛否＋根拠

> 凡例: **◎=主提案者 / ○=支持表明 / △=条件付き / ×=明示反対 / ─=スコープ外 / ?=未確認**

### 4.1 PAPR 削減手法 × 主要企業

| 候補手法 | Nokia (FL) | Samsung | vivo | Qualcomm | Ericsson | Huawei | Apple | InterDigital | Cohere | MediaTek | ZTE | OPPO |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **FDSS（baseline）** | ○ | ◎ | ○ | ○ | ○ | ○ | ○ | ◎ | ─ | ○ | ○ | ○ |
| **FDSS – SE** | ◎ | ◎ | ○ (CFR-SE) | ○ | ○ | ○ | ◎ | **◎ (α=1/4 推奨)** | ─ | ◎ | ─ | ○ |
| **FDSS – ST for π/2 BPSK** | ○ | ○ | △ | **◎** | ○ | ─ | ─ | ─ | ─ | ─ | ─ | ─ |
| **Tone Reservation** | △ | ─ | ─ | **◎ (sideband)** | ─ | ─ | ─ | ─ | ─ | ─ | ◎ | ─ |
| **GMSK-Approx FDSS** | ─ | ─ | ─ | ─ | ─ | ─ | **◎** | ─ | ─ | ─ | ─ | ─ |
| **CFR / CFR-SE** | ─ | ─ | **◎** | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─ |
| **AI/ML-based PAPR** | × | **◎ (4.3 dB 観測)** | **◎** | × | ?（未確認） | ?（未確認） | ?（未確認） | ─ | ─ | ─ | ─ | ─ |
| **Offset-QAM / π/2-PAM + FDSS** | ─ | ◎ | ─ | ◎ | ─ | ◎ | ◎ | ─ | ─ | **◎** | ─ | ─ |
| **AFDM based on DFT-s-OFDM** | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─（ETRI/Surrey, SJTU 提案） |
| **Zak-OTFS** | × (deprioritize 提案者) | × | ─ | × | ─ | ─ | ─ | ─ | **◎** | ─ | ─ | ─ |
| **Multi-Tx Enhancement (DFT-s-OFDM)** | ─ | ─ | ─ | ◎（#124bis で deprioritized） | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─ |
| **DFT-s-OFDM with flexible FD mapping** | ─ | ─ | ─ | ◎（#124bis で deprioritized） | ─ | ─ | ─ | ─ | ─ | ─ | ─ | ─ |

### 4.2 Multi-rank UL DFT-s-OFDM × 主要企業

| 企業 | rank-2 採否 | precoder | 観測結果（#124bis SLS） | 出典 |
|:---|:---:|:---:|:---|:---:|
| **Nokia** | △（rank-1 ベースライン推奨） | non-coherent only | SLS loss を報告 | R1-2601827 |
| **Samsung** | ○（rank-2 のみ） | non-coherent only | SLS loss（cell edge も） | R1-2602177 |
| **vivo** | ○ | non-coherent | SLS gain | R1-2602004 |
| **Qualcomm** | ◎（多層） | non-coherent multi + coherent single | SLS gain（複数構成） | R1-2603008 |
| **Ericsson** | ◎ | non-coherent / coherent 両方で gain 報告 | gain（最も広範） | R1-2602468 |
| **Huawei** | ◎（rank-2 必須） | non-coherent | SLS gain | R1-2601921 |
| **Apple** | ◎ | non-coherent multi + coherent single | gain + DWS で full buffer 同等、non-full で gain | R1-2603286 |
| **DOCOMO** | ◎ | non-coherent | gain | R1-2603056 |
| **OPPO** | ○ | non-coherent multi + coherent single | gain | R1-2602426 |
| **InterDigital** | × **「rank>1 not supported」** | — | no gain | R1-2600801, R1-2602254 |
| **MediaTek** | ○ | unified DFT-s-OFDM/CP-OFDM 統一手法 | — | R1-2600909 |
| **KDDI** | ○（rank-4 評価も推奨） | non-coherent baseline | — | R1-2601354 |
| **Lekha** | ○（rank=2 が実用上限） | non-coherent | — | R1-2600716 |

### 4.3 中立企業の立ち位置（深堀）

| 企業 | 立場 | 根拠 |
|:---|:---|:---|
| **Nokia** | FL（中立を装うが寄書 R1-2600027/R1-2601827 で deprioritize 立場） | DL DFT-s-OFDM 廃止、rank-1 推奨、Zak-OTFS 廃止 — **保守派の旗手** |
| **Ericsson** | 多角的支持（FDSS/FDSS-SE/FDSS-ST、multi-layer 全部 OK） | 「広く支持して特定提案に肩入れしない」標準的中立性 + 唯一 coherent CB でも gain 報告 |
| **Huawei** | 強力推進（multi-rank、Pruning QAM、Offset-QAM）+ DL DFT-s-OFDM の限定的擁護（同期信号） | 寄書 R1-2600138 / R1-2601921 で**最広スコープ提案** |

---

## 5. 評価メトリクスの合意状況

### 5.1 PAPR 削減量と coverage gain（dB）の関係

合意動詞: **Net Gain [dB] = PAPR (or Tx-power) gain – SNR degradation @10% BLER**

> 出典: [Chair Notes RAN1#124 — R1-2600788](Chair-Notes-RAN1-124-Waveform.md) §LLS metrics + ZTE R1-2600261 Proposal 2

| メトリック | 適用 | 注 |
|:---|:---|:---|
| **PAPR (CCDF 10⁻³)** | LLS 一次指標 | dB |
| **Tx-power gain** | UE 電力制限時のヘッドルーム回復量 | 最大報告値 = **2.5 dB**（#124bis Observation） |
| **SNR degradation @10% BLER** | フィルタ歪/ETN による復号劣化 | 候補ごとに公平比較 |
| **Net Gain** | 統合指標 | **これが正なら採用検討、負なら却下** |
| **UPT (90/mean/median/5%/10%)** | SLS 一次指標 | 全 UE 統計 |
| **CDF of instantaneous UL Tx power** | SLS 副指標 | **電力制限 UE の頻度** |
| **Tx rank 統計、MCS 統計** | SLS 副指標 | scenario 依存性の説明 |

### 5.2 複雑度評価（合意レベル：弱い、Hanbat NU R1-2601047 Proposal 4 等で提起）

| 評価軸 | 議論状況 |
|:---|:---|
| FFT 演算数 | 暗黙的に Net Gain に含まれるが明示メトリック未合意 |
| レイテンシ | Klaus FL summary では明示メトリックなし |
| UE 電力（PA 効率向上 vs ベースバンド負荷増） | Net Gain が「Tx 電力 gain」を含むので部分カバー |
| **AI/ML 専用**: Model Complexity (params, FLOPs/symbol)、推論複雑度 vs オフライン学習複雑度 | Hanbat NU Proposal 4 が提起、未合意 |

→ **これが #125 以降の論点**: Net Gain 単独では AI/ML 系の評価に不十分、複雑度メトリクス追加合意が必要。

### 5.3 NR Rel-15 DFT-s-OFDM ベースラインへの追加要件

合意済（[Chair Notes 124 R1-2600789](Chair-Notes-RAN1-124-Waveform.md) Conclusion）:

> 評価仮定で「受信側に必要な knowledge（フィルタ係数、拡張スキーム等）を開示」

これは **非透過フィルタ（Opt2）の暗黙の前提条件** — Samsung/Apple の「filter spec 化」要求が技術的に意味を持つための土台。

---

## 6. Multi-rank UL MIMO for DFT-s-OFDM との連動

### 6.1 PAPR 削減手法と rank scalability の組合せ

| PAPR 削減手法 | rank-1 | rank-2 (non-coherent) | rank-2 (coherent) | rank-2+ |
|:---|:---:|:---:|:---:|:---:|
| **FDSS（filter only）** | ◎ | ○（PAPR 性が一部維持） | △（PAPR 性消失） | △（同上） |
| **FDSS-SE** | ◎ | ○ | △ | △ |
| **FDSS-ST for π/2 BPSK** | ◎ | △（π/2 BPSK は rank-2 で稀） | × | × |
| **Tone Reservation** | ◎ | ○（reserved tones を共有可） | △ | △ |
| **GMSK-Approx FDSS** | ◎ | △（near-CE 性が消失） | × | × |
| **AI/ML PAPR** | ◎ | ?（未検証） | ? | ? |

> **核心の発見**: Chair Notes 124bis Observation の「**The lower PAPR property of DFT-s-OFDM is diminished with coherent precoders due to mixing of two (or more) layers for each power amplifier**」が rank scalability の制約。
> → **rank-2 で non-coherent precoder のみ** にしないと PAPR 削減効果が消失するため、PAPR 削減と rank-up は **トレードオフ関係**。

### 6.2 各候補の rank scalability（FL summary v68 §"Rank>1 for UL DFT-s-OFDM" + #124bis Observations より）

- **rank-2 まで（非コヒーレント）**: FDSS / FDSS-SE / FDSS-ST 全て成立 — #124bis で確認
- **rank-2 でコヒーレント**: Ericsson のみ独自 SLS gain 報告。一般化困難（5/6 社が反対 or 無評価）
- **rank-4**: KDDI が「thorough evaluation」を要求 (R1-2601354 Proposal 2)。**現時点で未評価**
- **AI/ML × multi-rank**: 全社未検証

→ **SEP 進歩性候補**: 「**多層 UL DFT-s-OFDM での PAPR 削減**」は標準的に未解決領域。Samsung が AI/ML で 4.3 dB の PAPR gain を rank-1 で達成しているが、これを rank-2 以上に拡張する具体技術は #124〜#124bis で **誰も提案していない**。

---

## 7. 学術理論との距離 — arXiv:2509.19064 ほか

### 7.1 arXiv:2509.19064 — Optimum Spectrum Extension for PAPR Reduction of DFT-s-OFDM

**著者: Renaud-Alexandre Pitaval, Fredrik Berggren, Branislav M. Popovic — 全員 Huawei**

| 観点 | 論文の主張 | 標準提案との照合 |
|:---|:---|:---|
| **対象** | FDSS-SE with parametrized FDSS windows + 任意の subcarrier 円シフト | #124bis で down-select された「FDSS-SE for π/2 BPSK / QPSK / 16QAM」と完全一致 |
| **主結果** | (a) PAPR 最小化に最適な SE サイズが存在 + (b) rate 最大化に別の最適 SE サイズが存在 | InterDigital R1-2600801 の「α=1/4 で正の Net Gain」と整合（α≧3/8 で負） |
| **不変性** | PAPR 最適 SE size は window 減衰に依存、帯域に **ほぼ非依存** | InterDigital が B=8/64/128/256 全てで一貫した結果 — 論文の不変性主張と整合 |
| **理論下限** | Capacity-PAPR トレードオフを定量化 | 標準でまだ Capacity 側を Net Gain に組み込んでいない — **#125 以降のメトリクス拡張余地** |

→ Huawei の 3 名の論文が標準化提案（R1-2600138 / R1-2601921）の理論的バックボーン。Huawei が「Pruning QAM + multi-rank + Offset-QAM」と広範に張る理由が論文に裏打ちされている。

### 7.2 arXiv:2404.16137 — Learned Pulse Shaping Design for PAPR Reduction in DFT-s-OFDM

**著者: Fabrizio Carpi (NYU), Sundeep Garg, Elza Erkip — 一部 Samsung Research America インターン期間中**

| 観点 | 論文の主張 |
|:---|:---|
| **手法** | NN ベースの pulse shaping filter 学習 |
| **PAPR gain** | 従来 FDSS フィルタを上回る |
| **Samsung との関係** | Carpi が SRA でインターン → Samsung R1-2600751 の AI/ML PAPR 提案 (Observation 9: two-sided 4.3 dB, UE-side 2.3 dB) の**学術的源流**と推測 |

→ Samsung の AI/ML 推進は **学術的バックボーンを伴った戦略的提案**。Qualcomm の慎重路線（複雑度懸念）と対立する根拠もここにある — Samsung は「学習済み filter で複雑度を相殺できる」と主張可能。

### 7.3 arXiv:2508.08225 — Industrial Viewpoints on RAN Technologies for 6G

業界横断の「6G で何を入れるか」のホワイトペーパー的存在。

- **Waveform に関する記述**: 「CP-OFDM/DFT-s-OFDM が 5G 継承で大枠合意、革新性は限定的」と #124 までの方向性を反映
- **新規波形の評価**: 「OTFS 等は simulation 不足で保留」 — Cohere の Zak-OTFS が #124bis で deprioritize された理由付けと整合

---

## 8. SEP 仮説 — PAPR-rank-coverage の三角関係での進歩性候補

> **disclaimer**: 以下は **調査・考察の範囲**。特許クレームの起草・法的助言ではない（[`framework/principles.md`](../framework/principles.md), [`framework/skill-contract.md`](../framework/skill-contract.md) Global Will Not 6）。

### 8.1 進歩性が出やすい技術領域（仮説）

| 領域 | 既存ギャップ | 進歩性の着想方向 |
|:---|:---|:---|
| **AI/ML PAPR × multi-rank** | rank-1 では Samsung 4.3 dB 達成だが rank-2+ は未検証 | **ポート間相関を考慮した joint NN pulse shaper**。各ポートで独立学習ではなく、レイヤ間 PAPR ピーク同期を回避する loss function |
| **Filter coefficient signaling** | 非透過 FDSS (Opt2) の filter 係数を DCI/RRC でどう送るか未確定 | **filter codebook + sub-codebook indication** で DCI 数ビット化。Type-II codebook の発想を流用 |
| **Net Gain と RAN4 PA model の整合化** | RAN1 の Net Gain と RAN4 の EVM/IBE/ACLR で評価結果が乖離する可能性 | **PA model を含む joint optimization**。RAN1 評価で RAN4 制約を内包したフィルタ最適化 |
| **rank-adaptive FDSS** | rank-1 と rank-2 で同じ filter 使用 → rank-2 で PAPR 性能劣化 | **rank に応じた filter 切替**（rank-1 = aggressive PAPR、rank-2 = mild PAPR）。DWS と組合せ |
| **FDSS-SE の SE size adaptation** | 固定の α（拡張比）使用 | **SNR/CQI 依存の動的 α 選択**。arXiv:2509.19064 の「PAPR-optimal vs rate-optimal SE size」を実装可能化 |
| **CFR-SE の MU 共有** | vivo 提案: 拡張部分を UE 間共有 → ネットワーク SE 改善 | **共有拡張領域での干渉抑制 signaling** + 共有スケジューラ規則 |
| **Tone Reservation × π/2 BPSK** | Lekha が「**hybrid π/2 BPSK + TR**」で最低 PAPR 達成と主張（Proposal 8） | **DCI で TR 位置を可変化**しつつ π/2 BPSK 制約と両立する pilot 配置 |

### 8.2 PAPR-rank-coverage トライアド

```
       PAPR 削減
          ▲
          │
   FDSS  │   ┌─ 標準合意（rank-1）
   FDSS-SE│  │
   FDSS-ST│  │   未開拓領域（SEP 余地大）
          │  │   ▼
          ●──┤   AI/ML × rank-2+
          │  │   filter codebook signaling
          │  │   PA-aware joint design
          │  │
          ▼  └→
        rank ≥ 2          ←→         coverage gain
        （非コヒーレント）          （Net Gain 2.5 dB max）
```

### 8.3 #125 以降の watch list（特許出願タイミングから逆算）

| 技術 | watch 理由 |
|:---|:---|
| **filter codebook の構造（Opt2 filter coefficients spec 化）** | #125 で具体規定が出れば、それに先んじて出願 |
| **AI/ML PAPR の評価メトリクス追加合意** | Net Gain だけでは不十分、複雑度メトリクスの規定で AI/ML 提案の生死が決まる |
| **rank scalability** | rank-4 を KDDI が要求、合意されれば AI/ML の応用機会拡大 |
| **TR sideband adjacency**（Qualcomm 推し） | tone reservation の物理位置が DCI 化される可能性 |

---

## 9. 未取得資料（fetch 候補）

[`framework/3gpp-ftp-cookbook.md`](../framework/3gpp-ftp-cookbook.md) §2.3 に従って取得すべき資料:

```bash
# 既取得 ✓
# - https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx
# - https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx
# - https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/drafts/10.2(Waveform)/RAN1-124%2010.2.1%20FL%20summary%20v68_KDDI_QC.docx

# 未取得（優先度順）

# 1. RAN1#124bis FL summary（10.2.1 Waveform） — Inbox/drafts/10.2.1(Waveform)/ は EoM5 時点で空のため、
#    R1-2603310〜R1-2603315 の Tdoc を Docs/ から個別取得する必要
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603310.zip" -o R1-2603310.zip
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603311.zip" -o R1-2603311.zip
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603312.zip" -o R1-2603312.zip
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603313.zip" -o R1-2603313.zip
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603314.zip" -o R1-2603314.zip
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603315.zip" -o R1-2603315.zip

# 2. 各社 Tdoc（#124bis、対立軸の根拠を逐語確認用）
#    Samsung（loss 報告）、Nokia（loss 報告）、InterDigital（multi-rank not supported）の根拠
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602177.zip" -o R1-2602177.zip  # Samsung
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2601827.zip" -o R1-2601827.zip  # Nokia
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602254.zip" -o R1-2602254.zip  # InterDigital
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603008.zip" -o R1-2603008.zip  # Qualcomm
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602468.zip" -o R1-2602468.zip  # Ericsson
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602004.zip" -o R1-2602004.zip  # vivo

# 3. RAN1#125 関連（会合後）
# https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/  # 会合後出現
# https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Agenda/agenda.csv   # AI 番号 10.2.1 維持確認

# 4. 学術論文（references/ 化候補）
curl -s "https://arxiv.org/pdf/2509.19064" -o arXiv-2509.19064.pdf  # Huawei optimum SE
curl -s "https://arxiv.org/pdf/2404.16137" -o arXiv-2404.16137.pdf  # NYU/Samsung learned pulse shaping
```

> **取得後の作業**:
> - pandoc で md 化 → `references/R1-XXXX.md` 命名で保存（[`framework/references-policy.md`](../framework/references-policy.md)）
> - 本ノート §4 企業マトリクスの「?」を埋める
> - §8.1 の SEP 仮説を Tdoc 内の具体根拠と照合し、進歩性度合いを再評価

---

## 10. catalog 拡張提案

### 10.1 `framework/catalog/agenda-items.yaml` への aliases 追加（既存 `ai_6gr_waveform` の拡充）

```yaml
ai_6gr_waveform:
  # 既存に追加すべき alias 候補
  aliases:
    # ↓ 既存維持
    - "6GR waveform"
    - "6G 波形"
    - "PAPR reduction"
    - "FDSS"
    - "DFT-s-OFDM PAPR"
    - "spectrum extension"
    - "tone reservation"
    - "CP-OFDM 6G"
    - "10.2.1"
    # ↓ 本ノート作成時に判明した追加候補
    - "FDSS-SE"
    - "FDSS-ST"
    - "GMSK approximation FDSS"
    - "AI/ML PAPR"
    - "AI ML waveform"
    - "multi-rank UL DFT-s-OFDM"
    - "multi-layer DFT-s-OFDM"
    - "low PAPR waveform"
    - "Net Gain 6GR"
    - "Zak-OTFS"   # deprioritized だが追跡用
    - "CFR-SE"
    - "Pruning QAM"
    - "AFDM"
```

### 10.2 `framework/catalog/meetings.yaml` の更新

- **RAN1#124**: `ai_map` に `ai_6gr_waveform: "10.2.1"` を **確定**（本ノートで Chair Notes から確認済）
- **RAN1#124bis**: 同様に `ai_map.ai_6gr_waveform: "10.2.1"` を確定（既存に追加）

### 10.3 新規 work-item キー候補

`framework/catalog/work-items.yaml`（未存在）を作る場合:

```yaml
6GR_BasicAirInterface:
  type: SI
  release: rel-20-6g
  start: "2025-08"
  target_completion: "2027-05"
  ran1_owner: "Wanshi Chen (RAN1 Chair)"
  ai_children:
    - ai_6gr_waveform   # 10.2.1
    - ai_6gr_channel_coding  # 10.3.1
    - ai_6gr_mimo_operation  # 10.5.2 umbrella
    - ai_6gr_initial_access  # 10.5.1
    - ai_6gr_scheduling      # 10.5.4.1
    - ai_6gr_harq            # 10.5 系
```

---

## 11. Next Steps

- [ ] **#124bis FL summary 6 件取得** (R1-2603310〜R1-2603315) → references 化
  - 特に R1-2603312（PAPR 削減 down-select の根拠）と R1-2603313（noted リストの理由）
- [ ] **企業 Tdoc 取得（最低 6 社）**: Samsung R1-2602177、Nokia R1-2601827、InterDigital R1-2602254、Qualcomm R1-2603008、Ericsson R1-2602468、vivo R1-2602004 → references 化 → §4 企業マトリクスの「?」埋め
- [ ] **arXiv:2509.19064（Huawei）と arXiv:2404.16137（Samsung 系）の digest** を `/digest-paper` で実施 → §7 と §8 SEP 仮説の根拠強化
- [ ] **`framework/catalog/agenda-items.yaml` に §10.1 の alias 追加** + meetings.yaml の ai_map 確定（PR 化）
- [ ] **#125 開催後**:
  - Chair Notes EoM 取得
  - 3 候補（FDSS / FDSS-SE / FDSS-ST）の **Opt1 vs Opt2** 決着確認
  - rank-4 議論の進展確認（KDDI 提案）
  - AI/ML PAPR の標準化スコープ決着（評価メトリクス合意可否）
- [ ] **横展開**:
  - `/connect-dots` で「PAPR 削減 ↔ Multi-rank ↔ AI/ML」の三角関係を分析
  - `/analyze-gap` で「Net Gain 単独 vs 複雑度メトリクス追加」のギャップを 3 バケット分類
  - `/digest-paper` で arXiv:2509.19064 を読み 3GPP 制約との差分を記録

---

## 12. 本ノートの限界

| 限界 | 影響 |
|:---|:---|
| 個別 Tdoc 未取得（FL summary v68 と Chair Notes のみ） | 企業内部の評価条件（PA model 詳細、channel model 選択）は未確認 |
| #124bis FL summary（R1-2603310〜R1-2603315）未取得 | down-select の正確な根拠表（5.3.1 of R1-2603312）が未参照 |
| RAN4 連携の詳細（R1-2601767 LS 全文）未参照 | PA model 統一の具体仕様は未確認 |
| #125 未開催 | down-selection の最終決着、rank-4 の可否は本ノート時点で未確定 |
| Jio Platforms の Channel Coding (10.3.1) 寄書未読 | 起点ノートの情報訂正は本ノートで行ったが、Jio の 6GR スタンスは別調査が必要 |

> 本ノートは **会合横断の構造マップ** として、個別 Tdoc digest が `references/` に揃うほど精度が上がる設計。**俯瞰ノート → 本変遷ノート → 個別 Tdoc digest** の 3 段階で深まる前提で運用。
