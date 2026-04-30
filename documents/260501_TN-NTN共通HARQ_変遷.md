---
title: "TN/NTN 共通 HARQ — RAN1#124 → #124bis → #125 議論変遷"
status: draft
confidence: medium
created: 2026-05-01
updated: 2026-05-01
axes:
  technology-layer: [phy-mimo, phy-pdcch, phy-pusch, phy-pdsch, cross-layer, mac]
  generation: [rel-17, rel-18, rel-19, rel-20-6g]
  value: [latency, reliability, coverage, throughput, energy-efficiency]
  market: [ntn-satellite, b2b-industrial, ambient-iot, public-safety]
  adoption-factors: [standard-convergence, backward-compat, ecosystem-readiness]
  ip: [novelty, inventive-step, spec-mapping]
sources:
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx
    title: "RAN1#124 Chair Notes EoM_03（10.5.4.3 HARQ + 10.7 6GR NTN）"
    accessed: 2026-04-30
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx
    title: "RAN1#124bis Chair Notes EoM5（10.5.4.3 HARQ + 10.7 6GR NTN）"
    accessed: 2026-04-30
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Agenda/agenda.csv
    title: "RAN1#124 agenda.csv（AI 番号確定）"
    accessed: 2026-04-30
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Agenda/agenda.csv
    title: "RAN1#124bis agenda.csv（AI 番号確定）"
    accessed: 2026-04-30
  - url: https://ofinno.com/the-standards-readout-2/6g-takes-shape-in-gothenburg-and-goa-first-solutions-emerge-as-3gpp-moves-past-problem-identification/
    title: "Ofinno — 6G Takes Shape in Gothenburg and Goa（#124 NTN 原則の二次要約）"
    accessed: 2026-04-30
  - url: https://www.ericsson.com/en/blog/2024/10/ntn-payload-architecture
    title: "Ericsson — 5G Non-Terrestrial Networks in 3GPP Rel-19（regenerative payload と HARQ）"
    accessed: 2026-04-30
  - url: https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/3gpp-satellite-communication
    title: "Ericsson Technology Review — Promising new 3GPP technology for satellite communication（Rel-17/18 HARQ disable・32 process）"
    accessed: 2026-04-30
  - url: https://arxiv.org/html/2412.16611v1
    title: "A Tutorial on Non-Terrestrial Networks: Towards Global and Ubiquitous 6G Connectivity (arXiv:2412.16611)"
    accessed: 2026-04-30
  - url: https://www.3gpp.org/technologies/ntn-overview
    title: "3GPP — Non-Terrestrial Networks (NTN) Overview"
    accessed: 2026-04-30
references:
  - "[[Chair-Notes-RAN1-124-6GR-HARQ-NTN]]"
  - "[[Chair-Notes-RAN1-124bis-6GR-HARQ-NTN]]"
up: "[[260430_RAN1-124-125-13トピック議論変遷]]"
related:
  - "[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]"
  - "[[260428_RAN1-124bis-MIMO-operation-10.5.2]]"
  - "[[260501_6GR-Waveform-PAPR削減_変遷]]"
  - "[[260501_CSI圧縮_inter-vendor-pairing_変遷]]"
trace:
  ai_id: ["ai_6gr_harq", "ai_6gr_ntn", "ai_nr_ntn_r19_phase3"]
  meetings_in_scope: ["RAN1#124", "RAN1#124bis", "RAN1#125"]
  ai_map_resolved:
    "RAN1#124":
      ai_6gr_harq: "10.5.4.3"
      ai_6gr_ntn: "10.7"
      ai_nr_ntn_r19_phase3: "8.7"
    "RAN1#124bis":
      ai_6gr_harq: "10.5.4.3"
      ai_6gr_ntn: "10.7"
      ai_nr_ntn_r19_phase3: "8.6"
    "RAN1#125":
      ai_6gr_harq: "[要確認: agenda.csv 未公開]"
      ai_6gr_ntn: "[要確認]"
  completeness:
    chair_notes_obtained: ["RAN1#124", "RAN1#124bis"]
    chair_notes_missing: ["RAN1#125"]
    tdocs_obtained: 0
---

# TN/NTN 共通 HARQ — RAN1#124 → #124bis → #125 議論変遷

> **位置づけ**: 起点ノート [[260430_RAN1-124-125-13トピック議論変遷]] §8（HARQ）+ §10（NTN）の **縦深堀**。
> 6GR で物理層 HARQ を地上ネットワーク（TN）と非地上ネットワーク（NTN）でどこまで共通化するか／分離するかの議論を、Chair Notes 一次情報を元に追跡。
> **confidence: medium** — #124 / #124bis の Chair Notes（EoM_03, EoM5）を一次情報として取得済。#125 は未開催のため見どころのみ。

---

## 0. 要約（Executive Summary）

### 0.1 これまでに固まったこと

1. **TN 性能優先原則** — RAN1#124 で *"When targeting a common design TN performance is prioritized"* が **正式に Conclusion として記録**（一次情報出典: [[Chair-Notes-RAN1-124-6GR-HARQ-NTN#§10.7 NTN（6GR NTN specific requirements and design）|#124 §10.7 Conclusion para 6469-6477]]）。Ofinno blog の二次要約はこの Conclusion を圧縮したもの。
2. **HARQ は NTN 固有問題リストに明示的に含まれる** — #124 で *"HARQ issues: e.g. enable/disable HARQ feedback (which may include how to efficiently operate with HARQ feedback enabled/disabled), number of HARQ processes, etc."* が AI 10.7 のスコープ入り。
3. **HARQ stalling 解決策 4 候補** — #124bis で具体化:
   - Sol.1 HARQ feedback disabling、Sol.2 multi-slot PDSCH/PUSCH、Sol.3 same-process reuse before ACK、Sol.4 sufficient process count
   - **TN 化（harmonization）は FFS のまま** — 本ノートの SEP 仮説の起点
4. **6GR DL HARQ 基本骨格** — #124 で確定: Asynchronous + Adaptive、TB level 以上、L1 と higher-layer (MAC CE) の両 mechanism 検討
5. **#124bis での 6GR HARQ 拡張** — サブ TB granularity、TB 横断 bundling、HARQ-ACK codebook、payload 1〜1706 bits、4 種の timing/resource 決定方式、UL HARQ failure → fast ARQ trigger

### 0.2 主要対立軸

| 対立軸 | TN 派 | NTN 派 |
|:---|:---|:---|
| HARQ process 数 | 16〜32（5G NR ベース） | LEO 数十、GEO 数百が必要 |
| A/N timing | < 数 ms（PDCCH 直後） | LEO 数十 ms、GEO 数百 ms |
| disable mode | 不要（reliability 優先） | GEO 必須、LEO 状況依存 |
| 共通設計の優先度 | 端末ベンダー（Apple, Samsung, Qualcomm） | 衛星オペレータ（Thales, Iridium, SES, AST Space Mobile） |

### 0.3 #125 での見どころ（推定）

- HARQ stalling Sol.1〜4 と TN harmonization の FFS が片付くか
- 6GR HARQ-ACK codebook の structure と payload size の上限値確定
- HARQ-ACK timing/resource Method 1〜4 の down-selection
- NTN 用 k_offset の cell/beam specific 化、UE specific 化の FFS 解消

---

## 1. 議論の前提：HARQ 設計の TN/NTN 構造的差異

### 1.1 RTT スケールの桁違い

| シナリオ | RTT | 影響 |
|:---|:---|:---|
| TN（地上 macro cell） | < 1 ms | 5G の 16 process で十分、A/N は次スロット |
| LEO 600 km（NTN） | ~13 ms（往復） | 5G 16 process では HARQ stalling、Rel-17 で 32 へ拡張 |
| LEO 1200 km | ~16〜20 ms | 同上 |
| **MEO 7000 km**（#124bis 追加） | ~70〜80 ms | LEO/GEO 中間、process 数も中間 |
| GEO 36,000 km | ~480〜600 ms | process 数では実用不可、HARQ disable + RLC ARQ 必須 |

> 出典: [Ericsson Technology Review](https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/3gpp-satellite-communication), [arXiv:2412.16611](https://arxiv.org/html/2412.16611v1) §III-B.

### 1.2 HARQ stalling — NTN 固有の根本問題

> NTN では RTT が大きく、process ID 一意性のもと送信側は ACK 待ちの間 process を解放できない。
> 結果: 「全 process が ACK 待ち」状態で新規 TB が送れない（= HARQ stalling）。
> 5G NR では 16 process が default、Rel-17 で 32 process / process 単位 disable mode を追加して凌いだ。

### 1.3 Rel-17 → Rel-18 → Rel-19 NTN HARQ の系譜（前世代対比）

| Release | 範囲 | HARQ 関連の主要変更 |
|:---|:---|:---|
| **Rel-17** | NR-NTN（transparent payload） | HARQ process **16→32**、process 単位 enable/disable mode 導入 |
| **Rel-18** | IoT-NTN（NB-IoT/eMTC over NTN） | NR-NTN と同等の HARQ disable 機構を IoT-NTN にも導入 |
| **Rel-19** | NR-NTN Phase 3 + IoT-NTN Phase 3 | **regenerative payload**（衛星上 gNB） → RTT 大幅短縮、HARQ も恩恵。**Store-and-Forward**（IoT-NTN）対応 |
| **Rel-20** | NTN Phase 4 + IoT-NTN Phase 4 | NR-NTN GNSS resilience（#124bis: AI 9.5.1）。HARQ は maintenance 主体 |
| **Rel-20 (6GR SI)** | 6G Radio AI 10.7 NTN + AI 10.5.4.3 HARQ | **本ノートの主題**: 共通 HARQ フレームの設計時に TN performance 優先原則が制約 |

> 出典: [Ericsson Rel-19 NTN payload architecture](https://www.ericsson.com/en/blog/2024/10/ntn-payload-architecture), [arXiv:2412.16611](https://arxiv.org/html/2412.16611v1).

### 1.4 regenerative payload が HARQ に与える影響

衛星上に gNB を置く（regenerative）と、gNB ↔ UE 間の RTT は **service link RTT のみ**（feeder link 往復が不要）に短縮:
- LEO 600 km regenerative: ~10 ms（vs transparent ~13 ms）
- GEO regenerative: ~270 ms（vs transparent ~480 ms）

ただし衛星上 gNB の電力・SWaP 制約と、衛星間ハンドオーバ（ISL/ground feeder）時の HARQ state 引継ぎが新たな課題。Rel-19 NR-NTN Phase 3 で **regenerative payload 対応** が WI スコープ入り（参考: [Ericsson](https://www.ericsson.com/en/blog/2024/10/ntn-payload-architecture)）。

---

## 2. RAN1#124（Gothenburg, 2026-02-09〜13）

### 2.1 概況

- **6GR HARQ AI**: 10.5.4.3 — FL: **Kevin (OPPO)** — 30 件超の Tdoc
- **6GR NTN AI**: 10.7（10.7.1 GNSS-based, 10.7.2 GNSS-less placeholder）— FL: **Alberto (Qualcomm)** — 35 件以上の Tdoc
- **Rel-19 NR-NTN maintenance**: AI 8.7（CR endorse 中心、新規設計なし）

### 2.2 6GR HARQ（10.5.4.3）の合意事項（一次情報、Chair Notes EoM_03）

> 詳細: [[Chair-Notes-RAN1-124-6GR-HARQ-NTN#§10.5.4.3 HARQ related Aspects|参考ノート §10.5.4.3]]

| 合意 | 内容 |
|:---|:---|
| **設計の評価軸** | latency / reliability / coverage / power saving / NW・UE complexity / diverse services / throughput / overhead 9 軸を提示。**DL と UL の HARQ 設計は同じである必要はない**を明記 |
| **2 つのフィードバックメカニズム** | Mechanism 1（L1 signalling）と Mechanism 2（higher-layer / MAC CE）の **両方を検討**。NR は L1 一択だったが、6GR は MAC CE 経路も俎上に |
| **Asynchronous + Adaptive HARQ** | DL と UL 両方で採用。NR の synchronous HARQ（DL）からの逸脱を許容 |
| **TB level granularity 以上** | "**at least** TB level"。CBG-like のサブ TB は将来検討 |
| **Payload size 範囲を検討** | 上限値・下限値は未定 |

### 2.3 6GR NTN（10.7）の合意事項

> 詳細: [[Chair-Notes-RAN1-124-6GR-HARQ-NTN#§10.7 NTN（6GR NTN specific requirements and design）|参考ノート §10.7]]

| 合意 | 内容 |
|:---|:---|
| **TN 性能優先原則（Conclusion）** | "When targeting a common design TN performance is prioritized" — 共通設計フレームの優先順位を明文化 |
| **NTN 固有検討事項リスト** | **HARQ issues** を明記（enable/disable HARQ feedback、number of HARQ processes、efficient operation を含む）+ UL time-frequency synch、large RTT timing、coverage、multi-satellite、multi-beam、beam footprint mismatch |
| **link budget template** | TN を baseline に、行・値追加で対応 |
| **orbit/band 評価対象** | S-band（LEO 300/600/GEO）、Ka（LEO 300/600/1200/GEO）、Ku（LEO 1200/GEO） |
| **GNSS 用語定義** | GNSS-based / GNSS-degraded / GNSS-less の 3 種 |
| **3 GNSS モードを全てサポート** | 6GR NTN は 3 モード全てを対象 |
| **UL synch 原則** | NR NTN を baseline、satellite assistance info、UE 位置 + assist info で pre-compensation |
| **大遅延 scheduling offset** | Option 1（NR の k_offset 流用）と Option 2（K1/K2 統合）の 2 案 |

### 2.4 #124 で残された主要 FFS

- HARQ-ACK timing/resource 決定方式（具体案なし）
- HARQ-ACK payload upper limit
- 大遅延 scheduling offset の最終形（Option 1 vs Option 2）
- 多衛星運用の物理層詳細

---

## 3. RAN1#124bis（Saint Julians, Malta, 2026-04-13〜17）

### 3.1 概況

- 同 FL 体制（HARQ: Kevin OPPO / NTN: Alberto Qualcomm）
- 業界最大級 2,100 名出席（[[260430_RAN1-124-125-13トピック議論変遷|参照]]）

### 3.2 6GR HARQ（10.5.4.3）の追加合意

> 詳細: [[Chair-Notes-RAN1-124bis-6GR-HARQ-NTN#§10.5.4.3 HARQ related Aspects|参考ノート §10.5.4.3]]

| 合意 | 内容 |
|:---|:---|
| **サブ TB granularity 検討** | TB level に加え、smaller-than-TB（CBG-like）を **whether and how** で検討開始 |
| **TB 横断 bundling 検討** | 複数 TB を 1 ACK に bundle |
| **HARQ-ACK codebook の包括検討** | codebook 生成、granularity、overhead、misalignment、DTX/NACK 曖昧、scheduler 協調、複雑度の 7 観点 |
| **Payload size 上下限確定** | min=1 bit, max=1706 bits（5G NR Polar 上限を流用、Mechanism 1 用） |
| **HARQ-ACK timing 4 method** | Method 1 Dynamic DCI / Method 2 UE-initiated / Method 3 半静的 next slot / Method 4 RRC only |
| **HARQ → fast ARQ trigger** | UL HARQ process failure を explicit/implicit に通知して RAN2 fast ARQ を起動。**RAN2#133bis との連携必要** |

### 3.3 6GR NTN（10.7）の追加合意 — **TN/NTN 共通 HARQ の中核**

> 詳細: [[Chair-Notes-RAN1-124bis-6GR-HARQ-NTN#§10.7 NTN（6GR NTN specific requirements and design）|参考ノート §10.7]]

#### ★ HARQ stalling 解決策（Agreement, para 4594-4601）

> For the issue of HARQ stalling due to large RTT in NTN, study the following solutions:
> - **Solution 1**: HARQ feedback disabling
> - **Solution 2**: PDSCH / PUSCH transmissions that span multiple slots
> - **Solution 3**: aNB reusing the same HARQ process before receiving HARQ-ACK feedback for the previous transmission
> - **Solution 4**: Sufficient number of HARQ processes
> - Note: Combination of solutions above can be considered.
> - **FFS: Whether the above techniques can be harmonized with TN**

| 解決策 | アイデア | TN との関係 | 前世代の系譜 |
|:---|:---|:---|:---|
| Sol.1 HARQ feedback disabling | NTN で per-process disable + RLC ARQ 委任 | TN では reliability 低下、不要 | Rel-17 NR-NTN で導入済機構の継承 |
| Sol.2 multi-slot PDSCH/PUSCH | 1 process の occupancy 期間延長で実効 process 数増 | TN でも mTRP / 高 SCS で意味あり、共通化候補 | 新規（5G NR にはない概念） |
| Sol.3 process reuse before ACK | process ID 一意性原則の緩和 | TN では interference / decoder 衝突、共通化困難 | 新規・最も踏み込んだ案 |
| Sol.4 sufficient process count | process 数を 32→ 64 / 128 等へ | TN は不要、NTN 固有値 | Rel-17 の 32 拡張の延長 |

> **解釈**: Sol.1〜4 のうち **Sol.2** が「**TN/NTN 両方で意味があり共通化余地大**」、**Sol.3** が「最も新規性高いがソフト実装影響大」。FFS にぶら下がる harmonization 議論の中心はこの 2 つ。

#### その他の 6GR NTN 合意（#124bis）

| 合意 | 内容 |
|:---|:---|
| Beam footprint 不足 | SSB periodicity 値、hierarchical beam structure を study |
| **MEO-7000 を S-band orbit に追加** | LEO/GEO 中間の RTT スケール |
| Duplex types | FD-FDD と HD-FDD（UE side） |
| Multi-satellite operation | mobility と inter-satellite interference を正式 study |
| Antenna model | S-band LEO-300/600 SAN モデル + UE モデル（FFS 詳細）が working assumption |
| **k_offset 採用（Option 1 確定）** | NR k_offset を baseline reuse、broadcast k_offset 採用、cell/beam specific は FFS、UE-specific は FFS |
| TA report 検討 | 必要性を study |
| Satellite assistance info | NR NTN の SIB19 を starting point |

### 3.4 #124bis で残された主要 FFS

- **★ HARQ stalling Sol.1〜4 の TN harmonization の可否**（本ノート最大の SEP 余地）
- HARQ-ACK codebook 構造の細部（misalignment 解決）
- HARQ-ACK timing 4 method の down-selection
- HARQ-ACK payload max の最終値
- k_offset の cell/beam specific 化、UE-specific 化
- 多衛星運用の inter-satellite interference 詳細

---

## 4. RAN1#125（日付未確定、推定 2026-05〜06）

### 4.1 状況

- FTP `TSGR1_125/` フォルダ実在確認済（Agenda / Docs / Inbox / Invitation / LS / Report の 6 構成）
- agenda.csv 未公開（2026-04-30 時点）
- Chair Notes 未生成（会期前または会期中）
- 日付・場所は **要確認**（[3GPP portal](https://portal.3gpp.org/Meetings.aspx) で確認）

### 4.2 #125 で見るべきポイント（推定）

- **TN/NTN 共通 HARQ の harmonization FFS 解消**: Sol.2（multi-slot）の TN 共通化可否、Sol.3（process reuse）の NTN 限定確定可否
- **6GR HARQ-ACK timing 4 method の down-selection**: NR は Dynamic DCI が default、6GR で UE-initiated を残すか
- **6GR HARQ-ACK codebook の structure**: misalignment 耐性（DCI miss 時の bits order ズレ）の signalling 規則
- **NTN 多衛星 inter-satellite interference 物理層メカニズム**
- **TA report 採用可否**

---

## 5. 設計マトリクス：HARQ パラメータの TN / LEO-NTN / GEO-NTN / A-IoT 比較

> 行=パラメータ、列=シナリオ。値は #124bis 時点の Agreement / 既存 Rel-17/18 仕様 / 推定。

| パラメータ | TN（5G NR + 6GR baseline） | LEO-NTN（Rel-19 + 6GR） | GEO-NTN（Rel-19 + 6GR） | A-IoT（Rel-19 / Rel-20） |
|:---|:---|:---|:---|:---|
| **RTT 想定** | < 1 ms | ~10〜20 ms | ~270〜600 ms | 通信距離による（数 m〜数百 m）、固有 |
| **HARQ process 数** | 16（5G）→ 6GR 検討中（拡張余地） | 32（Rel-17）→ Sol.4 で 64+ 検討 | 32 では不足、disable 必須 | **HARQ なし**（passive device、ACK return 不可） |
| **HARQ-ACK timing 決定** | Dynamic DCI（K1）が主 → 6GR で 4 method 検討 | k_offset（Rel-17）+ NR K1 → 6GR で k_offset 流用採用 | k_offset 大値 + 多くは disable | N/A |
| **HARQ disable mode** | 不要（reliability 優先） | per-process disable（Rel-17 機構を 6GR でも study） | per-process disable 必須 | N/A（passive） |
| **A/N feedback path** | PUCCH（L1） | PUCCH（L1）、6GR で MAC CE も検討 | 同左 + disable 多用 | R2D ACK は capability 依存 |
| **再送方式** | adaptive + asynch（NR は synch DL）、6GR で両方サポート | adaptive + asynch | adaptive + asynch + RLC ARQ で補完 | physical layer 再送なし（network 側で重複検出） |
| **HARQ termination point** | gNB | regenerative payload では衛星上 gNB（Rel-19）、transparent では地上 gNB | 同上、ただし GEO regenerative は SWaP 厳しい | N/A |
| **HARQ codebook** | dynamic / semi-static codebook（NR）→ 6GR で再設計（misalignment 解決） | NR と共通方向（FFS） | 同左（disable 多用なので codebook 影響小） | N/A |
| **TN との共通化見込み** | — | Sol.2（multi-slot）共通化期待、Sol.4 値拡張は分離 | 共通設計困難、NTN-only に流れる可能性 | A-IoT は HARQ 概念外、別フレーム |

---

## 6. SEP 仮説（進歩性の余地）

### 6.1 共通化と分離の境界に着目

> **TN performance 優先原則** が制約として効くため、NTN 固有最適化は「共通設計では NTN 要件を満たせない」場合に限定される。
> この境界（共通化できる／できない）の **判定規則** が未定であり、ここに進歩性余地が大きい。

| # | 仮説的着想 | 競合領域 | 進歩性の根拠 |
|:---|:---|:---|:---|
| **1** | **HARQ process 数の動的拡張（dynamic process count signalling）** | NR の固定 16/32 process | TN では default 16、NTN cell entry 時に DCI/RRC で動的に process 数を 64/128 に拡張する規則。**TN/NTN 切替時のシグナリング設計**が新規 |
| **2** | **TN/NTN 切替時の HARQ state 引継ぎ** | regenerative LEO のセル間 HO | LEO 衛星間（regenerative gNB 切替）/ NTN→TN 移行時に、未完了 HARQ process の state（process ID, RV, NDI）を引継ぐ規則。Xn/Uu の hybrid signalling が新規 |
| **3** | **multi-slot PDSCH/PUSCH の "occupancy" 概念**（Sol.2 の TN 共通化版） | 5G NR の slot-based scheduling | 1 process が **複数 slot を占有**する scheduling フレーム。NTN では HARQ stalling 緩和、TN では low-latency / coverage で意義。**TN/NTN 共通な occupancy 表現の DCI フィールド**が新規 |
| **4** | **same-process pre-ACK retransmission rule**（Sol.3 の安全な定式化） | NR の strict process 一意性 | aNB 側で「ACK 待ち中に同じ process ID で次の PDSCH を送る」ことを許容する条件規則（distinguishability、UE buffer 管理、HARQ combining 規則）。NTN-only でも進歩性高い |
| **5** | **HARQ-ACK timing UE-initiated 機構** | NR の DCI K1 indication | Method 2（UE-initiated）の signalling 規則。XR / バーストトラフィックで UE が ACK を「投げ返す」タイミングを能動決定。NTN でも地上局（衛星）リソース効率化に寄与 |
| **6** | **HARQ → ARQ fast trigger の RAN1/RAN2 跨層規則** | 5G の MAC HARQ vs RLC ARQ 分離 | UL HARQ failure を即座に RAN2 fast ARQ へ送る explicit/implicit 通知。RAN2#133bis 連携の物理層 indication 設計（PUCCH bit、UCI フィールド、または DCI flag）が新規 |
| **7** | **MEO-7000 specific HARQ profile** | LEO・GEO 二極化想定 | LEO/GEO 中間（RTT ~70 ms）専用の HARQ 動作プロファイル（process 数、timing、disable 条件）。`SIB19` 拡張の satellite assistance info に MEO 軌道対応情報を加える設計 |

### 6.2 留意点（不変原則 5: 確信度）

- 上記仮説は **Chair Notes Agreement 文を直接根拠** にしているが、**個別 Tdoc（特に FL summary 内部）を未読**。具体的に何社が何を提案しているかは要追加調査
- 特許クレームの起草・法的助言は本ノートの範囲外（Skill Contract Will Not 6）

---

## 7. TN/NTN 共通 IA との接続（SSB / PRACH 連動論点）

### 7.1 IA 共通化と HARQ 共通化は連動する

| AI | #124 / #124bis での 6GR 状況 | TN/NTN 共通化の論点 |
|:---|:---|:---|
| **10.5.1.1 Synchronization & beam meas.** | 6GR で SSB 構造を新設計（NR から不継承） | NTN では beam が衛星アンテナと結合、TN との共通 numerology 設計が必要 |
| **10.5.1.2 PRACH and RACH procedure** | 6GR で PRACH 再設計、4-step / 2-step 同等議論 | NTN は preamble 長と TA pre-compensation で TN とズレ、k_offset 議論が PRACH にも波及 |
| **10.5.1.3 Bandwidth operation** | BWP 再設計 | NTN はキャリア切替（feeder link switch）と BWP 切替で interaction |
| **10.5.4.3 HARQ** | **本ノートの主題** | k_offset と HARQ-ACK timing が連動（RTT 補償の二重設計回避） |
| **10.7 NTN** | NTN 固有事項を集約、AI 横断で他へ波及 | Conclusion "TN performance prioritized" がスコープを絞る |

> **解釈**: 6GR NTN の k_offset（broadcast、cell/beam specific FFS）が PRACH / DL data scheduling / HARQ-ACK timing 全てに影響。**SSB / PRACH 共通化と HARQ 共通化は同じ k_offset 設計に乗る**ため、別個に解けない。SEP 仮説 #2（TN/NTN 切替時の state 引継ぎ）は IA 側にも対称な論点を持つ。

### 7.2 関連別ノート候補（未作成）

- `[[260501_TN-NTN共通IA-PRACH_変遷]]` — IA / PRACH の TN/NTN 共通化を別途追跡（**未作成、本ノートと対になる**）
- `[[260501_NTN-regenerative-payload_調査]]` — Rel-19 NR-NTN Phase 3 の regenerative payload を独立調査（**未作成**）

---

## 8. 未取得資料（fetch 候補）

### 8.1 個別 Tdoc（高優先）

`framework/3gpp-ftp-cookbook.md` §2.2 で取得すべき優先資料:

```bash
# RAN1#124 6GR HARQ FL summary（Kevin / OPPO）
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/drafts/10.5.4(DL_ctrl_HARQ)/...
# 具体名は会合 inbox listing で要確認

# RAN1#124 6GR NTN FL summary（Alberto / Qualcomm）
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601469.zip  # FL summary #1
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601470.zip  # FL summary #2
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601471.zip  # FL summary #3

# RAN1#124bis 6GR HARQ FL summary
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603251.zip  # FL #1
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603252.zip  # FL #2
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603253.zip  # FL #3
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603326.zip  # FL #4

# RAN1#124bis 6GR NTN FL summary
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603090.zip  # FL #1
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603091.zip  # FL #2（link budget endorsed）
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603093.zip  # FL #3

# 主要企業の HARQ 寄書（#124bis）
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603024.zip  # Qualcomm HARQ
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602197.zip  # Samsung HARQ
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2601937.zip  # Huawei HARQ
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602895.zip  # Ericsson HARQ
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602442.zip  # OPPO HARQ

# 主要企業の NTN 寄書（#124bis）
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603029.zip  # Qualcomm NTN
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602473.zip  # Ericsson NTN
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2601908.zip  # Thales+ESA+SES+Iridium+Eutelsat NTN
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602881.zip  # PNT 連名（Airbus, ESA, AST, Iridium, ...）
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602202.zip  # Samsung NTN
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602673.zip  # Apple NTN
```

### 8.2 RAN1#125 資料（会合後）

```
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Agenda/agenda.csv
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Tdoc_list/
https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/
```

### 8.3 二次情報

- Apex Standards #125 pre-meeting（未公開）
- Ofinno blog 続編（未公開、#124bis レビュー）

---

## 9. catalog 拡張提案

### 9.1 `framework/catalog/agenda-items.yaml` の更新

| キー | 修正前 | 修正後 |
|:---|:---|:---|
| `ai_6gr_harq` | aliases 8 件、AI 番号未登録 | **AI 番号 10.5.4.3 を確定**、FL = Kevin (OPPO) を追記 |
| `ai_6gr_ntn`（**新規**） | — | 新規キー追加。AI 番号 10.7、FL = Alberto (Qualcomm) |
| `ai_nr_ntn_r19_phase3` | aliases 9 件、AI 番号未登録 | **#124 で 8.7 / #124bis で 8.6** を `meetings.yaml` 側で管理 |

提案:
```yaml
ai_6gr_harq:
  title: "6GR HARQ related Aspects (10.5.4.3)"
  parent_si: "6GR_BasicAirInterface"
  parent_ai: "ai_6gr_dl_ctrl_sched_harq"  # 10.5.4 親
  current_phase: "study"
  aliases:
    - "6GR HARQ"
    - "6G HARQ"
    - "control/HARQ provisions"
    - "TN/NTN HARQ"
    - "HARQ process number"
    - "HARQ stalling"
    - "HARQ disable"
    - "HARQ-ACK codebook 6G"
    - "10.5.4.3"
  description: |
    6GR の HARQ 関連事項。FL: Kevin (OPPO)。
    #124 で 9 軸の評価軸 + Mechanism 1/2 + asynch/adaptive + TB level 確定。
    #124bis でサブ TB / TB 横断 bundling / codebook 包括 / payload 1〜1706 bits / timing 4 method / fast ARQ 連携。

ai_6gr_ntn:
  title: "6GR NTN (10.7)"
  parent_si: "6GR_BasicAirInterface"
  current_phase: "study"
  aliases:
    - "6GR NTN"
    - "6G NTN"
    - "TN/NTN 共通"
    - "TN/NTN common"
    - "NTN 6G"
    - "regenerative payload 6G"
    - "10.7"
    - "10.7.1"
    - "10.7.2"
  description: |
    6GR NTN 物理層検討。FL: Alberto (Qualcomm)。
    #124 で TN performance prioritized 原則 + GNSS 用語 + orbit/band 評価 + NTN 固有検討事項リスト。
    #124bis で HARQ stalling 4 解決策 + MEO-7000 + duplex + multi-satellite + k_offset 採用。
```

### 9.2 `framework/catalog/meetings.yaml` の更新

```yaml
"RAN1#124":
  ai_map:
    ai_6gr_harq: "10.5.4.3"    # 確定
    ai_6gr_ntn: "10.7"         # 確定
    ai_nr_ntn_r19_phase3: "8.7"  # 確定
"RAN1#124bis":
  ai_map:
    ai_6gr_harq: "10.5.4.3"    # 確定
    ai_6gr_ntn: "10.7"         # 確定
    ai_nr_ntn_r19_phase3: "8.6"  # 確定（#124 の 8.7 から繰上り）
```

### 9.3 work-items.yaml への追加候補

```yaml
NR_NTN_Ph3:
  type: WI
  release: rel-19
  rapporteur: "[要確認]"
  scope:
    - "ai_nr_ntn_r19_phase3"
  references:
    - "https://www.ericsson.com/en/blog/2024/10/ntn-payload-architecture"
  notes: |
    Rel-19 NR-NTN Phase 3。regenerative payload + IoT-NTN S&F。
    HARQ への影響: regenerative 配置で RTT 短縮、Store-and-Forward で ARQ/HARQ 整理。
```

---

## 10. Next Steps

- [ ] **#125 Chair Notes 取得** — 会合後速やかに `references/Chair-Notes-RAN1-125-6GR-HARQ-NTN.md` を作成
- [ ] **個別 Tdoc 取得** — Qualcomm / Ericsson / Samsung / Huawei / OPPO の HARQ + NTN 寄書を §8.1 のリストから取得し、企業別の主張差異を §6 SEP 仮説に反映
- [ ] **catalog 更新** — §9 の提案を [`framework/catalog/agenda-items.yaml`](../framework/catalog/agenda-items.yaml) と [`framework/catalog/meetings.yaml`](../framework/catalog/meetings.yaml) に反映
- [ ] **Rel-17 NR-NTN HARQ 詳細**（process 数 16→32 拡張、disable mechanism）の規格条文を `references/TS38.213-NTN-HARQ.md` 等に MD 化
- [ ] **regenerative payload の HARQ 終端位置** を Rel-19 仕様（TS 38.300 Phase 3 Annex 等）から逐語確認
- [ ] **arXiv 2412.16611（NTN tutorial）** を `/digest-paper` で深掘り、3GPP 実装制約とのギャップを抽出
- [ ] **`/connect-dots`** で本ノートと [[260501_6GR-Waveform-PAPR削減_変遷]] / [[260501_CSI圧縮_inter-vendor-pairing_変遷]] の連動論点を抽出（特に multi-rank UL DFT-s-OFDM × NTN HARQ）
- [ ] **TN/NTN 共通 IA / PRACH の変遷ノート** を別途作成（[[260501_TN-NTN共通IA-PRACH_変遷]] placeholder）

---

> **本ノートの限界**: Chair Notes EoM（一次情報）に依拠したが、**個別 Tdoc 内部の議論変遷**（提案者の動機、ベンダー間の利害衝突、実装難易度の主張）は未確認。§6 の SEP 仮説は Agreement 文と業界一般知見からの **論理的推測** であり、個別 Tdoc の根拠に裏付けされた段階で confidence を high に上げる。
