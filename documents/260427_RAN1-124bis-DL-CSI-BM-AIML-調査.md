---
title: "RAN1#124bis (Malta, 2026-04-13〜04-17) — DL CSI / Beam Management / AI-ML 寄書と議論の整理"
status: draft
confidence: high
created: 2026-04-27
updated: 2026-04-28
axes:
  technology-layer: [phy-mimo, cross-layer]
  generation: [rel-19, rel-20]
  value: [throughput, ai-integration, latency, energy-efficiency]
  market: [consumer-xr, b2b-industrial, fwa]
  adoption-factors: [standard-convergence, backward-compat, economies-of-scale, operator-roi]
  ip: [novelty, inventive-step, spec-mapping]
sources:
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/
    title: "3GPP FTP — RAN1#124-bis meeting folder (TSGR1_124b)"
    accessed: 2026-04-27
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Agenda/agenda.csv
    title: "RAN1#124-bis Agenda (CSV、Chair: Patrick Merias)"
    accessed: 2026-04-27
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Agenda/R1-2601750.zip
    title: "R1-2601750 — Draft Agenda of RAN1#124bis meeting"
    accessed: 2026-04-27
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Tdoc_list/TDoc_List_Meeting_RAN1%23124-bis%20(260417).xlsx
    title: "TDoc List — RAN1#124-bis (final, 2026-04-17、1,724件)"
    accessed: 2026-04-27
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom4.docx
    title: "Chair notes RAN1#124bis_eom4.docx — End-of-Meeting (final)"
    accessed: 2026-04-27
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/
    title: "Chair_notes フォルダ（v00〜v15、eom〜eom4 全リビジョン）"
    accessed: 2026-04-27
  - url: https://www.3gpp.org/specifications-technologies/releases/release-20
    title: "3GPP Release 20 ページ"
    accessed: 2026-04-27
  - url: https://www.3gpp.org/technologies/ai-ml-nr
    title: "AI/ML for NR Air Interface — 概要（rapporteur: Juan Montojo, Qualcomm）"
    accessed: 2026-04-27
  - url: https://www.3gpp.org/technologies/ran-rel-19
    title: "RAN Rel-19 Status and a Look Beyond"
    accessed: 2026-04-27
  - url: https://arxiv.org/html/2507.18538v2
    title: "AI/ML Life Cycle Management for Interoperable AI Native RAN（NR_AIML_air_Ph2 解説）"
    accessed: 2026-04-27
  - url: https://research.samsung.com/blog/6G-AI-ML-for-Physical-layer-Part-II-CSI-Compression-with-JSCM
    title: "Samsung Research — 6G AI/ML for Physical-layer Part II: CSI compression with JSCM（2025-12-30）"
    accessed: 2026-04-28
  - url: https://research.samsung.com/blog/Enable-JSCC-based-CSI-Feedback-for-B5G-6G-Design-Standardization-and-Prototype
    title: "Samsung Research — Enable JSCC-based CSI Feedback for B5G/6G: Design, Standardization and Prototype（2025-10）"
    accessed: 2026-04-28
  - url: https://research.samsung.com/blog/Coherent-Joint-Transmission-CJT-High-Capacity-Enabler-for-6G
    title: "Samsung Research — Coherent Joint Transmission (CJT): High-Capacity Enabler for 6G（2026-02-12）"
    accessed: 2026-04-28
up: "[[260420_標準化特許申請のための調査戦略]]"
related:
  - "[[260422_Rel-15-NR-勉強会トピック調査ガイド]]"
  - "[[260420_NRフレーム構造とリソースブロックの進化まとめ]]"
  - "[[260428_RAN1-124bis-MIMO-operation-10.5.2]]"
  - "[[260430_RAN1-124-125-13トピック議論変遷]]"
  - "[[260501_CSI圧縮_inter-vendor-pairing_変遷]]"
---

# RAN1#124bis（Malta、2026-04-13〜04-17）— DL CSI / Beam Management / AI-ML

> 本ノートは「学術理想 vs 3GPP 実装制約」のギャップ可視化を目的とし、Malta 会合の Tdoc / Chair Notes（end-of-meeting v4 = `eom4`）から RAN1 が実際に何を合意したかを整理する。  
> **補足ノート**: 10.5.2（MIMO Operation: PDCCH / PDSCH / PUSCH 伝送方式）の詳細は [[260428_RAN1-124bis-MIMO-operation-10.5.2]] を参照。本ノートでは 10.5.2.4（Beam Management）のみ扱う。本会合は **2026-04-13〜04-17（5 日間）**、登録 1,724 件の Tdoc が提出された。
> Word 文書（`docx`/`xlsx`）への直接リンクは frontmatter `sources:` を参照。Chair Notes はリビジョン制で `v00`〜`v15`、会期最終日（4/17）以降に `_eom`〜`_eom4` がアップロードされる運用。

## 1. 会合の基礎情報と一次情報リンク

| 項目 | 内容 |
|:---|:---|
| 会合名 | RAN1#124-bis |
| 期間 | 2026-04-13（月）〜 2026-04-17（金） |
| 会場 | Malta（マルタ） |
| 親プロジェクト | RP-26 plenary（RAN#111、2026 年 3 月）配下 |
| Chair | Patrick Merias（ETSI MCC 配下、RAN1 議長） |
| 同時開催 WG | SA2#174 など全 12 WG が同地で開催（参加者 ~2,100 名） |
| Tdoc 総数（4/17 final） | 1,724 件（agenda 65 項目に分類） |
| 一次フォルダ | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/` |

> [要確認] 参加者数 ~2,100 は他社まとめ（ATIS）からの数字、RAN1 単独ではなく Malta 共催会合全体の値。

### 1.1 Word/Excel ファイルへのアクセス

3GPP の FTP は **公開** で誰でも DL 可。代表ファイル:

- **Tdoc 一覧（XLSX）**: 会期中に毎日更新される `TDoc_List_Meeting_RAN1#124-bis (YYMMDD).xlsx`（260413〜260417）。最終版は 260417。Schema は `TDoc / Title / Source / Type / Agenda item / TDoc Status / Release / Spec / Related WIs / ...`（36 列）。
- **Chair Notes（DOCX）**: `Chair notes RAN1#124bis_v00.docx` 〜 `_v15.docx`（会期中の更新）→ 会期後 `_eom`〜`_eom4`（最終確定）。
- **Agenda（CSV/ZIP）**: `agenda.csv` がプレーンテキスト、`R1-2601750.zip` が議長提出版の同等物。
- **FL Summary（DOCX）**: 各 agenda item 配下の `Inbox/drafts/9.1.1(...)/...` などに格納される議論まとめ（後述する Feature Lead が起草）。

> 認証は不要。`curl -A "Mozilla/5.0" <URL>` で取得可能（直接 IIS 配信）。Anthropic 系の WebFetch では User-Agent 拒否で 403 が出ることがある。

## 2. アジェンダ構造（DL CSI / BM / AI-ML 関連）

`agenda.csv` の番号体系。本ノートが扱うのは以下 9 項目。

| AI 番号 | タイトル | リリース | 主担当 (Feature Lead / Email moderator) |
|:---|:---|:---|:---|
| **8.1** | Maintenance on AI/ML for NR Air Interface | Rel-19 maint | Samsung（FL）／Ericsson（Ad-Hoc Chair）／Email moderator: **Juan Montojo (Qualcomm)** |
| **9.1.1** | CSI spatial/frequency compression without temporal aspects ("Case 0") | Rel-20 NR | **Qualcomm Incorporated**（FL summary #1〜#4 を一社で起草） |
| **9.1.2** | Inter-vendor training collaboration for two-sided AI/ML models | Rel-20 NR | **Apple**（FL summary #1〜#4） |
| **9.2** | NR MIMO Phase 6 | Rel-20 NR | **MediaTek (Darcy)** + **CATT**（co-FL；MTK が DL CSI、CATT が SRS 担当） |
| **10.5.1.1** | Synchronization acquisition and beam measurement | Rel-20 6GR (SI) | **Huawei + Xiaomi**（co-Moderator） |
| **10.5.2.4** | Beam management for downlink and uplink | Rel-20 6GR (SI) | **ZTE (Bo) + Apple (Hong)**（co-Moderator） |
| **10.5.3.1** | Aspects of downlink-based CSI acquisition | Rel-20 6GR (SI) | **Samsung (Feifei) + vivo (Hao)**（co-Moderator） |
| **10.5.3.2** | Aspects of uplink-based CSI acquisition | Rel-20 6GR (SI) | **CATT (Xin)** |
| **10.5.3.3** | Other aspects (joint DL/UL, finer time/frequency tracking RS) | Rel-20 6GR (SI) | **Lenovo (Bingchao)** |

### 2.1 全体感（Tdoc 提出件数 Top）

| AI | タイトル略 | 件数 |
|:---|:---|---:|
| 10.5.3.1 | 6G DL CSI | **66** |
| 10.5.0 | 6G MIMO 全般 | 55 |
| 10.5.2.2 | 6G DL DSCH 送信 | 55 |
| 10.5.1.1 | 6G Sync/beam 測定 | 52 |
| 10.5.2.4 | 6G BM | 44 |
| 10.5.3.2 | 6G UL CSI | 39 |
| 9.1.1 | Rel-20 AI/ML CSI Case 0 | 43 |
| 9.1.2 | Rel-20 Inter-vendor training | 41 |
| 9.2 | Rel-20 NR MIMO Phase 6 | 39 |
| 10.5.3.3 | 6G CSI other | 32 |
| 8.1 | Rel-19 AI/ML maint | 14 |

> **観察**: 6G DL CSI（10.5.3.1）が単一 agenda として最多 66 件。FL Summary も #1〜#10 まで起草され、Samsung+vivo は会期中に 10 ラウンドの議論を回した。これが今回 Malta 会合の最大の論点であったと読み取れる。

## 3. 寄書を出した企業（agenda 別 Top 観察）

> Source 列を区切らず「共同提出企業群そのまま」をカウント。`Moderator` ラベルは FL summary 用の特殊エントリ。

### 3.1 9.1.1 — Rel-20 AI/ML CSI Case 0（Tdoc 43 件）

- **Qualcomm が FL（Juan Montojo）。FL summary を 4 ラウンド単独起草**。
- 通常の discussion 寄書は 1 社 1 件原則：FUTUREWEI / Spreadtrum,UNISOC / Huawei,HiSilicon / Southeast Univ / MediaTek / vivo / CMCC / NEC / InterDigital / Tejas / Samsung / China Telecom / ZTE,Sanechips / KT Corp / TCL / LG Electronics / Ericsson / OPPO / CATT / Lenovo / Xiaomi / 1Finity / Sharp / Panasonic / Google / Apple / HONOR / ETRI / Ofinno / Nokia / NTT DOCOMO / TOYOTA Info Tech / Transsion / Pengcheng Lab / Quectel / Pengcheng+BUPT+X-NET。
- **特徴**: 学術機関（Pengcheng Lab、Southeast Univ、BUPT、X-NET、Tejas）の参加が目立つ。CSI compression は数学的設計余地が大きく、研究機関が寄りやすい領域。

### 3.2 9.1.2 — Inter-vendor training collaboration（Tdoc 41 件）

- **Apple が FL（FL summary を #1〜#4 単独起草）**。これは 5G-A〜6G を通じて「UE-側エンコーダと NW-側デコーダをどう pair させるか」を巡る最重要トピックで、Apple がリードを取ったのは戦略的。
- Apple discussion 寄書も含めると Apple ソースは **5 件**（FL 4 + 通常 1）で、agenda 9.1.2 で他社を圧倒。
- 共同提出に Fraunhofer HHI+IIS、ASUSTeK、Pengcheng Lab+BUPT+X-NET、Pengcheng Lab、Apple、ETRI など多彩。
- ベンダー間訓練連携の 3 方式は arxiv:2507.18538 の整理に対応:
  - **Direction A**: reference model 共有（Apple が推す）
  - **Direction B**: encoder parameter 交換
  - **Direction C**: dataset 整列

### 3.3 9.2 — NR MIMO Phase 6（Tdoc 39 件、Rel-20 5G-A 仕様）

- **WID は RP-252936（MediaTek rapporteur、RAN#111）**。スコープは 3 サブトピック: (a) Early SRS/CSI/CSI-RS triggering, (b) CSI-RS density reduction, (c) Improvement of SRS capacity and coverage。
- **co-FL: MediaTek (Darcy) — DL CSI 系 / CATT — SRS 系**。MediaTek が「DL CSI acquisition」Round 0〜Final を、CATT が「SRS capacity and coverage」Round 1〜3 を独立に進行。
- 主要寄書源: Huawei,HiSilicon / vivo / Samsung / OPPO / Ericsson / Qualcomm / Nokia / Apple / NTT DOCOMO / LG / ZTE,Sanechips / InterDigital / CMCC / China Telecom など全主要 RAN ベンダー。

### 3.4 10.5.1.1 — 6GR Sync/beam measurement（Tdoc 52 件）

- **co-FL: Huawei + Xiaomi**（中国陣の組合せ）。
- **6GR SSB / SSB burst / SSB burst set** という 3 階層用語が今回正式に「議論用」として定義された（Example 1〜4-2 まで例示）。これは 6G 初期アクセス設計の基礎。

### 3.5 10.5.2.4 — 6GR Beam management（Tdoc 44 件）

- **co-Moderator: ZTE (Bo) + Apple (Hong)** — 中国インフラ + 米端末という対立軸を融合させる組み合わせ。
- 主要 6 件の FL summary を発行。AT&T、KDDI といったオペレータ寄書もあり Tdoc が広い。
- BeammWave AB、Beijing Digital Nebula など新興プレイヤーも参加。

### 3.6 10.5.3.1 — 6GR DL CSI（Tdoc **66 件、本会合最大**）

- **co-Moderator: Samsung (Feifei) + vivo (Hao)**。FL summary は **#1〜#10** までと、本会合で最多のラウンド数（他は 4〜5）。
- 学術機関多数: BJTU、Pengcheng Lab、Shanghai Jiao Tong Univ、IIT Kanpur、BUPT+X-NET+PCL、IMU+Turkcell、CEWiT、CAICT、NICT、Wistron、ITRI など。
- Orange, Rakuten Symphony, KDDI など欧州・日本オペレータも参加。

### 3.7 10.5.3.2 — 6GR UL CSI（Tdoc 39 件）

- **FL: CATT (Xin)** 単独。SRS 設計の検討で、5G の ZC/CGS 系列をベースラインに採用（後述）。

### 3.8 10.5.3.3 — 6GR CSI other（Tdoc 32 件）

- **FL: Lenovo (Bingchao)**。joint DL/UL CSI と finer time/frequency tracking RS を扱う。

### 3.9 8.1 — Rel-19 AI/ML maintenance（Tdoc 14 件）

- 件数が少なく、Rel-19 の細かな TS 38.212 / TS 38.214 の修正 CR が中心。
- **FL: Samsung**, Ad-Hoc Chair: Ericsson, Email moderator: **Juan Montojo (Qualcomm)** — 3 社体制で Rel-19 の最終調整。

## 4. 議論内容と結論（Chair Notes _eom4 から要点抽出）

> 各セクションは「Agreement」「Conclusion」「FFS（For Further Study）」を明示。Conclusion は「合意できなかった」を含むことに注意。

### 4.1 8.1 — Rel-19 AI/ML maintenance（CR 確定）

| 種別 | 内容 |
|:---|:---|
| **Agreement** | TS 38.212 §6.3.1.1.2 への TP（Text Proposal）endorsed。CR `R1-2603378` 確定。理由: 性能監視のための P/SP CSI 報告が PUCCH 上で 1〜2 ビット payload になるケースを救済（**RS-PAI を 3 ビットへゼロパディング**） |
| **Agreement** | TS 38.214 §5.2.1.6 への TP endorsed。CR `R1-2603379`。理由: ビーム管理向け UE 側データ収集の **CPU 持続時間（CPU duration）** を正しく仕様化。UE-side training 用 periodic CSI report をサポート |
| **Conclusion** | **合意なし**: PDSCH の VRB マッピングで、推論用 CSI report（Set A）の NZP CSI-RS 周辺の RE で rate matching を行わない、という案 — 不採用 |

> **読み解き**: Rel-19 のフリーズ後（2025-06）に出てきた spec バグの粛々とした修正。残った "合意なし" は Rel-19 では救済されず、Rel-20 で改めて議論される可能性。

### 4.2 9.1.1 — Rel-20 AI/ML CSI Case 0（two-sided model）

> Case 0 = 「現スロットのみの空間-周波数領域 CSI 圧縮、時間方向の予測なし」。NR_AIML_air_Ph2 WI（RAN#108、2025-06 承認）の中核ユースケース。

| Agreement | 内容（要点） |
|:---|:---|
| **量子化コードブック** | NW がコードブックを交換しない場合の標準 SQ コードブック: **Q=2 で {1/8, 3/8, 5/8, 7/8}**、**Q=1 で {1/4, 3/4}** をサポート |
| **PMI スコープ** | precoding matrix feedback via two-sided model: **最大 128 ports / rank ≤ 4 / subbands ≤ 19** |
| **UCI 構造** | **two-part UCI** を採用。Part 1 = CQI/RI/CRI、Part 2 = PMI（全レイヤ）。レイヤを Group 1 / Group 2 に分割し、レイヤ強度順（強→弱）に bit を並べる |
| **NW 側データ収集** | target CSI 量子化方式は **Option 1a（real-imaginary）と 1b（amplitude-phase）の二択にダウンセレクト** |
| **性能監視** | paired CSI feedback と target CSI sample で監視。L3 シグナリング (Option 1) と L1 シグナリング (Option 2) のさらなる検討 |

> **インプリ制約の核心**: 学術論文では量子化を float のまま扱うが、3GPP は ±1/8 単位の SQ で離散化を強制する。Apple+Qualcomm の覇権争いはこの離散化と FFS の細部で決着が変わる。

### 4.3 9.1.2 — Inter-vendor training collaboration（Direction A）

> Direction A = 「リファレンスモデル交換」方式。Apple が FL を取った領域。

| Agreement | 内容 |
|:---|:---|
| **Payload pair** | Option 4-1 (Direction A) で、target CSI = port-subband 領域の precoding matrix のとき、レイヤ毎に **{32,2}, {64,2}, {96,2}, {128,2}, {192,2}, {32,1}** を支持（Layer 1〜3）。Layer 4 は {32,2}, {64,2}, {96,2}, {32,1}。NW は subset のみ交換可 |
| **Pairing ID** | pairing ID とデータセットは **1:1 対応**、データセット間にリンクなし |
| **性能ターゲット** | レイヤ毎・CSI feedback set 毎に交換 |

> RAN2 から `LS on pairing ID for two-sided models`（R1-2601756, RAN2/Ericsson）が入っており、5G Rel-20 の two-sided model における pairing ID は SA5（管理面）にも影響する。**この pairing ID は SEP 余地が大きい設計領域**。

### 4.4 9.2 — Rel-20 NR MIMO Phase 6（実装制約の現場）

#### Early SRS/CSI/CSI-RS triggering（IDLE/INACTIVE → CONNECTED 遷移時）

| Agreement | 内容 |
|:---|:---|
| アンテナスイッチング | Rel-15 の SRS-AS（1T1R/1T2R/1T4R/2T2R/2T4R/4T4R）を流用 |
| Aperiodic CSI-RS | **最大 32 ポート** |
| Aperiodic TRS | 最大 2 バースト |
| Conclusion | aperiodic SRS-AS / TRS の MAC-CE-in-MSG4 トリガリングは **必須化しない** |
| **次会合 RAN1#125 で down-select** | aperiodic CSI-RS の QCL: Option-1 = SSB と QCL Type-C / Option-2 = AP-TRS と QCL Type-A（条件付き） |

#### CSI-RS density reduction

| Agreement | 内容 |
|:---|:---|
| 周波数密度 | ρ ∈ {1/3, 1/4, 1/6, 1/8} を 48/64/128 ポート集約に対し RRC 設定 RB-level offset で指示 |
| FFS | 候補値、配置制約、resource/set どちらの粒度か |
| **次会合で down-select** | RB 制約 3 案: ZP CSI-RS と整合 (Opt-1) / 1〜2 連続 RB (Opt-2) / 均等分散 (Opt-3) |

#### Improvement of SRS capacity and coverage

| Agreement | cross-slot SRS で PUSCH (priority 0) と DMRS の transmission をフルに U-slot 配置の SRS 後に置く |
| Agreement | aperiodic SRS の per-resource slot offset を resource configuration に含める |
| Conclusion | intra-repetition hopping は UE 実装に委ねる（仕様化しない） |

### 4.5 10.5.1.1 — 6GR Sync/beam measurement（用語定義段階）

> **Note: まだ用語の合意の段階。具体的なシンボル数や周期の数値合意は次回以降。**

| Agreement | 6GR SSB / 6GR SSB burst / 6GR SSB burst set / 6GR SSB periodicity を「議論用語」として定義。Example 1（4 SSB / no rep）〜 Example 4-2（4 SSB×4 interleaved rep × 4 burst）を例示 |

### 4.6 10.5.2.4 — 6GR Beam management（評価方法と方針）

| Agreement | **SLS / LLS の評価仮定テーブル**を採用（チャネルモデル、UE 速度、antenna 配置 等の前提を統一） |
| Agreement | **UE-initiated beam management (UEIBM)** の 2 イベントを single-TRP starting point として研究: Event-1=現/サービングビームの予測品質が閾値以下、Event-2=候補ビームが閾値以上に良い |
| Agreement | 空間/時間/周波数領域のビーム測定/予測（AI/非AI 両方）について、**FLOPs / モデルパラメータ数 / Set-A or Set-B ベンチマーク**で比較 |
| Agreement | network-initiated beam reporting で **L1-RSRP** を最低限の量とする。L1-SINR は FFS |
| Agreement | **MIMO とモビリティで統一フレームワークを目指す**（RAN1 strives for unified framework）— これは新ポリシー |

> **重要**: 6G では UE-initiated と NW-initiated の両方が並走。Set-A/Set-B フレーム（学術: 全ビーム/部分ビーム）が引き続き使われる。**FLOPs と Parameter 数を仕様化する流れ**は SEP 余地として注目。

### 4.7 10.5.3.1 — 6GR DL CSI（66 Tdoc、最大論点）

| Agreement | **コードブック設計**: SU/MU-MIMO, single/multi-TRP（CJT 含む）, HST/Near-Field/Spatial Non-Stationary（**SNS**）を含めて 5G より良い性能を達成 |
| Agreement | NR の L1-based CSI 報告から出発、 L1 vs L2 報告の比較軸を **A1〜A7（efficiency, latency, reliability, UE 複雑度, NW 複雑度, congestion, payload 範囲）** + **B1〜B4（scheduling 制約緩和、multiplexing/collision 簡素化、timeline 緩和、可変 payload）** で評価 |
| Agreement | 空間領域 CSI 予測のベースライン #2 = **線形補間** |
| Agreement | **CSI-RS 最大ポート数**の検討候補: Alt-1=128 / Alt-2=256 / Alt-3=512（5G NR は 32 が上限なので大幅増） |
| Agreement | DL CSI は **NZP CSI-RS** をチャネル測定 RS、**CSI-IM** を干渉測定 RS のベースライン |
| Agreement | 時間領域: periodic + aperiodic を最低限サポート、SP-CSI-RS は FFS |
| Agreement | **CSI-RS パターン = CDM グループの集約**として定義。CDM 配置（Localized vs Comb）、CDM サイズ（既存 1/2/4/8 vs 新 16）、新 CDM タイプ（fd-CDM4, cdm8-FD4-TD2）など 6 検討軸 |
| Agreement | **JSCM ベース CSI 圧縮**（Joint Source-Channel Modulation）を AI ベース CSI 圧縮の上に追加検討 — Projection-matrix or encoder ベース、PAPR 制約、QAM/APSK 等への離散コンステレーション写像、誤り検出設計 |
| Agreement | **CSI-RS RE 共有**の 4 ユースケース: 異なる port 数間 / 異なる周波数密度間 / 異なる time domain 間 / 5G CSI-RS と 6G CSI-RS 間 |
| Agreement | 一般化評価で UMa/InH / 屋内屋外比 / antenna 仮想化 / UL channel/interference / UE Tx/Rx 実装 / 多様な layer/subband |
| Agreement | **Channel Property Information (CPI)** という新概念を導入: RS 設定支援 / scheduling 連携 / event-triggered CSI / CSI 予測支援に使う情報。各 use case で benchmark, KPI, report 量, 計算複雑度を検討 |
| Agreement | **時間域 CSI 予測の評価前提**（非 AI / AI 両方）: 中間 metric = サブバンドレベル per レイヤの SGCS・NMSE（NW 側 vs UE 側予測の比較は CSI 報告の影響を考慮）。システム metric = UPT（平均・5%tile）と CSI 報告オーバーヘッド。リンク metric = BLER/SE/スループット。複雑度 = FLOPs/M（AI は加えてパラメータ数/M）。**ベースライン = Sample & Hold**。観測窓の例: periodic CSI-RS で 5/10 ms・5/20 ms、aperiodic で 12/2 ms・8/2 ms・4/2 ms。予測窓の例: 1 instance/10 ms/gap 5 ms、4 instances/10 ms/gap 5 ms |
| Agreement | **コードブック構造の研究**: 低解像度/高解像度 CSI に対して **W₁W₂**（2 段構成）および **W₁W₂Wf**（周波数次元追加の 3 段構成）をベースラインに評価。各社は最大 rank 仮定・SD/FD 基底選択の前提・コードブックパラメータ・基底フォーマット・暗示的/明示的 CSI のどちらを対象 CSI とするか、複雑度分析を報告 |
| Agreement | **CJT 校正 CSI 報告の研究**: 複数 TRP 間の位相/遅延校正を支援するための CSI 報告を「サポートするか・どうサポートするか」を研究（CJT 協調品質の維持が目的） |
| Agreement | **AI ベース CSI 予測の汎化・スケーラビリティ評価**: 以下の 1 つ以上を横断して評価 — 展開シナリオ（UMa/InH 等）、キャリア周波数、屋内/屋外分布、BS アンテナ設定（素子間隔・仮想化・ポートレイアウト・ポート数）、サンプリング比率/パターン、UE パラメータ（速度・SNR/SINR・チャネル推定誤差・アンテナ設定・報告分解能） |
| Agreement | **AI ベース CSI 圧縮の汎化・スケーラビリティ評価**: TR 38.843 の評価方法をスタートポイントに、以下を対象に評価 — DL チャネル（展開シナリオ・屋内外比・アンテナ仮想化）、UL チャネル/干渉（AWGN/CDL/TDL/UMa、UL SNR 範囲、ノイズパターン）、UL リソースサイズ（CSI フィードバック RE 数）、NW/UE 実装（受信機・チェーン・RF 不完全性）、Tx/Rx ポート/レイヤ数、サブバンド数 |

> **DL CSI が今回最大の論点**になった理由: (a) 5G NR の Type II eType II より良くしないと 6G の意味がない、(b) Near-Field / SNS / 大規模アンテナ（256/512）は学術論文と仕様の最大ギャップ、(c) JSCM は 5G では存在しなかった新領域。

### 4.8 10.5.3.2 — 6GR UL CSI（CATT 主導）

| Agreement | SRS resource set / SRS resource の **階層構造**を検討 |
| Agreement | 同一 SRS で複数用途 |
| Agreement | SRS 系列設計: PAPR、系列プール、相関、長さ候補、RE マッピング、F-domain パラメータ柔軟性 |
| Agreement | **ZC / CGS** を出発点 |
| Agreement | アンテナポート数 = **{1,2,3,4,8}** |
| Agreement | P/AP-SRS をベースライン、SP-SRS は FFS |
| Agreement | 周波数ホッピング、partial frequency sounding |
| Agreement | comb 2/4/8 を出発点、非一様/疎パターンは検討 |
| Agreement | SRS リピティション、cross-slot |
| Agreement | 干渉緩和: シーケンス hop / start RB / comb offset / cyclic shift |
| Agreement | **272 PRBs 超**の SRS BW 拡張 |

### 4.9 10.5.3.3 — 6GR CSI other（joint DL/UL、tracking RS）

| Agreement | finer time/frequency tracking RS の周波数ドメイン構造（min BW、密度 x REs/RB）を研究 |
| Agreement | single-port と multi-port tracking RS |
| Agreement | QCL パラメータ不一致の影響を評価 |
| Agreement | 時間ドメイン挙動: periodic / aperiodic / semi-persistent、組合せ可 |
| Agreement | 周波数密度 x ∈ {2, 3, 4, 6, 12} REs/RB |
| Agreement | **joint DL/UL CSI acquisition の 2 ユースケース**: Use case 1 = SRS ベースを DL 測定/報告で支援、Use case 2 = SRS ベースで他の補助情報も使った MCS/rank 選択 |
| Agreement | 性能評価用の **SRS error model**: 推定チャネル = 真のチャネル + 白色 Gaussian（分散はスケーリング係数で）、SRS 干渉/不完全 OL 電力制御/UE Tx アンテナ利得不平衡を additionally 考慮可。数式: H̃_UL = γ(H + E)、σ²_E 例 = 1/(SINR × Δ) で Δ=9dB、γ = √(1/(1+σ²_E)) |
| Agreement | **アンテナ校正誤差モデル**: Ĥ_DL = diag(δᵢ·e^{jφᵢ}) × H_UL^T × diag(αᵢ·e^{jθᵢ})。振幅誤差 αᵢ の標準偏差例 = **0.35 dB**（Gaussian）、位相誤差 θᵢ の標準偏差例 = **5°**（Gaussian）。UE 側の δᵢ・φᵢ は各社報告。UE DL/UL 相反性の実現可能性も考慮 |
| Agreement | **挿入損失差モデル**: UL/DL 挿入損失差は Ĥ_DL = A × H_UL^T で表現。A = diag(β₁, β₂, …, β_N_UE)、βᵢ は最大電力アンテナを基準とした電力比（dB スケール）。生成方法は各社報告 |

## 5. 議論の背景と企業勢力（political dynamics）

### 5.1 Rel-19 → Rel-20 の継続性

- **Rel-18**: SI（FS_NR_AIML_Air、TR 38.843、rapporteur Juan Montojo / Qualcomm、2022-Q4 開始）
- **Rel-19**: 部分的 normative WI（CSI prediction、AI/ML beam management、AI/ML positioning）— **2025-06 (RAN#108) で functional freeze**
- **Rel-20**: 2 系統並走
  - **NR_AIML_air_Ph2 WI**: 5G-Advanced 上で **two-sided CSI compression "Case 0"** を初めて normative 化。RAN#108（2025-06）承認、Stage-2 完了は 2026-06、Stage-3 は 2027-03 ターゲット
  - **6GR Study Item**: 完全に新しい 6G 物理層（10.x agenda）。RAN#108 開始、本会合（#124bis）で技術的 deep-dive が本格化

### 5.2 Feature Lead 配置から読む勢力図

| 領域 | FL/Moderator | 戦略的意味 |
|:---|:---|:---|
| **Rel-19 AI/ML maint (8.1)** | Samsung (FL) + Ericsson (AdHoc) + Qualcomm (email mod) | 米/欧/韓の三社体制で Rel-19 を綺麗に閉じる |
| **Rel-20 AI/ML CSI Case 0 (9.1.1)** | Qualcomm 単独 | Rel-18 SI の rapporteur Montojo が継続。**CSI 圧縮の権威ポジションを Qualcomm が継承** |
| **Rel-20 Inter-vendor (9.1.2)** | Apple 単独 | これは 2025〜2026 における Apple の 3GPP 戦略の集大成。**端末ベンダーとして UE-側エンコーダの中身を秘匿しつつ NW と協調する仕組み**を主導することは、Apple 製品の差別化を守りつつ標準準拠を担保する |
| **Rel-20 NR MIMO Ph6 (9.2)** | MediaTek + CATT | RP-252936 rapporteur が MediaTek。**台湾モデムベンダ + 中国インフラの組合せ**は 4G LTE 時代の Samsung 単独覇権から大きな変化 |
| **6GR Sync/beam meas (10.5.1.1)** | Huawei + Xiaomi | 中国陣の連合。SSB 設計は 5G で Samsung 主導だったが 6G では中国に移行 |
| **6GR Beam management (10.5.2.4)** | ZTE + Apple | ZTE が中国インフラ、Apple が米端末。**ペア組成で対立軸を融合**させる 3GPP 議長の調整 |
| **6GR DL CSI (10.5.3.1)** | Samsung + vivo | 5G で Samsung が長らく握ってきたコードブック領域に **vivo（OPPO 系列の OEM）** が並ぶ。中国端末ベンダの台頭 |
| **6GR UL CSI (10.5.3.2)** | CATT 単独 | SRS は中国 CATT/CICT の伝統的得意領域 |
| **6GR CSI other (10.5.3.3)** | Lenovo 単独 | tracking RS は Lenovo が主導 |

### 5.3 観察される勢力構図

1. **Qualcomm**: 学術・SI フェーズの権威ポジションを維持。CSI compression（9.1.1）と Rel-19 maintenance（8.1）の両輪を握る。SEP 戦略上、**「two-sided model の量子化／UCI 構造／payload 構造」は Qualcomm が押さえ続ける可能性大**。
2. **Apple**: 6G 議論への深い関与。**inter-vendor training collaboration の FL を取った**ことは、UE-側エンコーダの IP を守りつつ標準連携可能なフレームを「自社主導で定義」する強烈なメッセージ。Apple は 5G では受動的だったが、6G では能動的。
3. **Samsung**: 6G DL CSI（10.5.3.1、最大論点）の co-FL を取得。Rel-19 maint 8.1 でも FL。コードブック領域の歴史的優位を 6G に持ち込む。
4. **中国陣（Huawei/HiSilicon、ZTE/Sanechips、Xiaomi、vivo、OPPO、CATT、Lenovo、CMCC、China Telecom、Pengcheng Lab、BUPT、X-NET、CAICT、CICTCI）**: 6GR 全 5 sub-WG 中、**Co-FL に 4 領域（10.5.1.1, 10.5.2.4, 10.5.3.1, 10.5.3.2）で参画**。NR Phase 6 でも CATT が SRS 担当 FL。学術機関の参加密度も中国系が圧倒。
5. **Ericsson / Nokia / NTT DOCOMO / KDDI / Orange / Rakuten Symphony / AT&T**: オペレータと欧州ベンダの discussion 寄書は健在だが、**FL ポジションはほぼ取れていない**。Ericsson は Rel-19 maint の Ad-Hoc Chair のみ。
6. **MediaTek**: Rel-20 5G-A の MIMO Phase 6 rapporteur と FL。モバイル SoC 視点での実装制約に強い影響力。
7. **学術 / 新興プレイヤー**: BeammWave AB、Pengcheng Lab、BJTU、IIT Kanpur、IMU+Turkcell、CEWiT、NICT、ITRI、Wistron など、**6G DL CSI（10.5.3.1）に大量参入**。論文段階のアイデアを 3GPP 仕様に押し込もうとする動き。

### 5.4 「論文の理想 vs 3GPP 制約」のギャップ — 本会合での具体例

| 領域 | 論文の理想 | 3GPP 制約（#124bis 合意） | 進歩性の余地 |
|:---|:---|:---|:---|
| CSI 量子化（9.1.1） | 連続値 / 任意 bit 数 | SQ {1/8, 3/8, 5/8, 7/8}、UCI 2 part 構造、最大 128 port / rank 4 / 19 subband | 量子化詳細・UCI mapping の最適化 |
| Inter-vendor (9.1.2) | 共通モデル前提 | payload pair {32,2}〜{192,2}、pairing ID = 1:1 mapping | データセット設計、performance target 構造 |
| 6G DL CSI ports（10.5.3.1） | 数百〜数千 port | 128/256/512 で down-select | Near-Field、SNS、CJT への対応 |
| 6G CSI-RS pattern | 任意 RE 配置 | CDM グループの集約、CDM 1/2/4/8/16、Localized vs Comb | 新 CDM タイプの設計、5G との RE 共有 |
| 6G beam management | 連続的 metric | L1-RSRP のみ最低限、L1-SINR は FFS、FLOPs/params で比較 | UEIBM のイベント定義、unified framework |
| 6G CPI（新概念） | チャネル特徴の自由表現 | scheduling/RS 設定/event-trigger 用に限定検討 | report quantity 設計、計算複雑度の制約 |
| 6G JSCM | 任意エンコーダ | QAM/APSK 系の固定コンステレーションへの写像、PAPR 制約 | コンステレーション設計、FL 的に PAPR 削減 |

## 6. 前世代との差分

- **5G Rel-15 NR**: Type I / Type II / eType II コードブック中心、AI/ML なし。CSI-RS は 32 port が上限。
- **5G-A Rel-18**: AI/ML が SI として登場（CSI feedback、BM、positioning の 3 use case）。実装制約は学術と乖離大。
- **5G-A Rel-19**: 上記 3 use case の partial normative。BM/positioning は WI 化、CSI feedback は 2 階段式（prediction の WI 化、compression は SI 継続）。
- **5G-A Rel-20 (Phase 2)**: **two-sided CSI compression が初めて normative 化**。Inter-vendor framework は完全な新規。LCM プロトコル（model pairing、activation、fallback、version sync）が TS 38.331 に追加。
- **6G Rel-20 (SI)**: 5G の物理層を **置き換える**新仕様。CSI-RS 最大 128/256/512 port、SRS 272 PRB 超、Near-Field/SNS/JSCM、unified BM/mobility framework。

## 7. 未解決課題（FFS / Down-select 待ち）

- **9.1.1**: 性能監視の L1 vs L3 シグナリング、量子化詳細
- **9.1.2**: pairing ID と RAN4 試験の関係（LS R1-2601756 で RAN2/SA5 と継続調整）
- **9.2**: aperiodic CSI-RS の QCL（Opt-1 vs Opt-2）、CSI-RS RB 制約 3 案、MAC-CE-in-MSG4 での dynamic indication
- **10.5.1.1**: SSB シンボル数、周期の数値合意は次回以降
- **10.5.2.4**: L1-SINR 採用、Set-A/Set-B 詳細、AI ベース予測と非 AI ベース手法のベンチマーク方法
- **10.5.3.1**: ポート数 128/256/512 down-select、CDM 設計、JSCM の testability（RAN4 LS が今後）。時間域 CSI 予測の観測窓/予測窓パラメータ確定。コードブック構造（W₁W₂ vs W₁W₂Wf）の採択。CJT 校正 CSI 報告の仕様化可否
- **10.5.3.2**: 5G に対する SRS BW 拡張方式（hopping vs sparse vs 再定義）の down-select
- **10.5.3.3**: tracking RS の具体パラメータ x, Y, N, Ssymb, Sslot。アンテナ校正誤差の分布パラメータ（X1/Y1/X2/Y2）の確定。挿入損失差モデルの βᵢ 生成方法の合意

## 8. 市場・知財余地

- **Two-sided CSI compression（9.1.x）**: SEP の宝庫。Qualcomm が量子化/UCI を、Apple が pairing/inter-vendor を握る。**JSCM**（10.5.3.1）は新概念で、誰もまだ強い特許を持っていない可能性 — 注目領域。
- **6G CSI-RS の CDM 集約 / RE 共有**: 5G との後方互換を保ちつつ拡張する設計は、回避設計（design-around）が難しく essential 化しやすい。
- **CPI（Channel Property Information）**: 全く新しい概念。define-then-patent の好例。**実装制約が確定する前に出願すべき**領域。
- **UEIBM の event 定義**: 端末側からのビーム管理開始は 5G では受動的 UE 報告のみ。UEIBM の 2 event（Event-1 = 自ビーム劣化、Event-2 = 候補ビーム良化）が 6G で正式化される。

## 9. 用語解説 — 本ノートで使われる専門用語

### 9.1 AI/ML maint（AI/ML maintenance）とは

**一言定義**: Rel-19 でフリーズ済みの AI/ML 仕様（TS 38.212 / TS 38.214）に Change Request（CR）を当てて品質を維持するフェーズ。

3GPP の標準化プロセスには、**functional freeze（機能フリーズ）** と **maintenance（保守）** の2段階がある。

| フェーズ | 目的 | 主な作業 |
|:---|:---|:---|
| **Study Item（SI）** | アイデアを技術報告（TR）にまとめる | 可能性調査、性能比較 |
| **Work Item（WI）** | 仕様書（TS）に normative テキストを書く | 新機能の追加・仕様化 |
| **functional freeze** | 新機能の追加を締め切る | WI 完結の区切り（Rel-19 = 2025-06、RAN#108） |
| **maintenance（maint）** | フリーズ後に発見される問題を修正 CR で対処 | spec バグ修正・曖昧さ解消・整合性維持 |

**maintenance でやること（具体例）**:
- **Spec error 修正**: 実装したら仕様の記述が矛盾していたことが判明 → CR で文言修正
- **Ambiguity resolution**: 2つの解釈が成立する記述を一意に確定
- **Edge case の救済**: 特定のパラメータ組合せ（例: PUCCH 上の 1〜2 ビット payload）で仕様が機能しないケース → ゼロパディング等のルール追記
- **実装フィードバック**: ベンダーの初期実装から発見した矛盾を 3GPP に持ち帰り、CR として処理

本会合（#124bis）の **agenda 8.1「Maintenance on AI/ML for NR Air Interface」**（Tdoc 14 件）は、この maintenance 作業を Rel-19 AI/ML について実施した。RAN1 functional freeze 後も **Samsung（FL）＋Ericsson（AdHoc Chair）＋Qualcomm（email moderator）** の 3 社体制でバグフィックス CR を処理し、Rel-19 仕様を成熟させている段階にある。

> **なぜ Samsung が FL か**: Samsung は Rel-18 SI から Rel-19 WI を通じて CSI prediction・BM・AI lifecycle の仕様化に深く関与しており、仕様内容の把握が最も深い企業として FL を引き受けた。maintenance FL は「仕様の責任を担う」という地位を標準化において継続的に持つことを意味し、SEP 戦略上も重要なポジション。

---

## 10. Samsung の技術提案詳細

Samsung は Malta 会合で **2 つの FL ポジション**（8.1 maint FL、10.5.3.1 co-FL）を担い、Rel-19 の後始末と 6G 物理層設計の両輪を同時に回している。

### 10.1 8.1 — Rel-19 AI/ML maintenance での Samsung の役割

Samsung が FL として提出・確定させた CR は以下の 2 件（いずれも本会合で endorsed）。

| CR 番号 | 対象 TS | 内容 | Why |
|:---|:---|:---|:---|
| **R1-2603378** | TS 38.212 §6.3.1.1.2 | P/SP CSI 報告が PUCCH 上で 1〜2 bit payload になるケースで **RS-PAI を 3 bit にゼロパディング**するルールを追記 | PUCCH のペイロードサイズ制約と AI 性能監視の1〜2 bit 報告が衝突するというバグ。Rel-19 の implementer が発見した spec error |
| **R1-2603379** | TS 38.214 §5.2.1.6 | ビーム管理向け **UE 側データ収集の CPU 持続時間（CPU duration）** の仕様化。UE-side training 用 periodic CSI 報告をサポート | 「UE が AI モデルをいつ・どれだけ計算してよいか」の仕様がなかった。CPU duration を明示することでチップ設計者が省電力設計できる |

**合意に至らなかった提案**:

> PDSCH の VRB マッピングで推論用 CSI report（Set A）の NZP CSI-RS 周辺 RE では rate matching を行わない案 — **不採用**。Rel-19 ではこの問題は閉じられず、Rel-20 での再議論候補。

**Samsung の戦略的意図**: バグフィックス CR 2 件を通じて (a) AI モデルの性能監視プロトコル（RS-PAI = Reference Signal for Performance Monitoring AI）と (b) UE 側訓練の計算資源管理の両方に Samsung の文言を刻んでいる。これらは将来の UE ベンダーが従わざるを得ない実装ルールであり、**SEP 主張の基盤**になり得る。

---

### 10.2 10.5.3.1 — 6GR DL CSI での Samsung の技術提案群

Samsung が 6G DL CSI（agenda 10.5.3.1）に持ち込んでいる技術提案の柱は 3 つ。

#### 10.2.1 JSCM（Joint Source-Channel Modulation）

**What**: 従来の「量子化→チャネル符号化→変調」という分離処理を廃止し、**ソース（CSI）圧縮・チャネル符号化・変調を一体で最適化**する AI ベースの CSI フィードバック方式。UE 側で CSI を量子化せずに複素値の圧縮シンボルとして直接 RE にマッピングし、gNB 側で AI/ML により CSI を再構成する。

**Why 6G で提案するか**: 5G NR の eType II コードブックは量子化による不可逆損失と cliff effect（SNR 劣化時の急激な性能崩壊）が問題。6G の大規模アンテナ（128〜512 port）では従来量子化コードブックのオーバーヘッドが爆発的に増大する。JSCM はオーバーヘッドを制御しながら eType II を上回る性能を実現できる。

**性能評価（Samsung Research 公開値）**:

| シナリオ | 指標 | JSCM の結果 |
|:---|:---|:---|
| Link-level（eType II 比） | SE（スペクトル効率） | **+94.4%** |
| SLS（sTRP） | UPT 改善 | 最大 **+3%**（OH = 60 RE） |
| SLS（mTRP CJT） | UPT 改善 | 最大 **+6%**（OH = 60 RE） |
| OH 削減 | 維持可能な OH 比率 | **60% 削減**（UPT 102% 維持） |
| UE 計算量（Rank=4） | eType II 比 | **2.9%** に削減 |

**3GPP での位置づけ**: 本会合（10.5.3.1）で JSCM は 6G AI ベース CSI 圧縮の**検討対象として agreement に採録**（§4.7 参照）。「Projection-matrix or encoder ベース、PAPR 制約、QAM/APSK 等への離散コンステレーション写像、誤り検出設計」という形で Research 課題が整理された段階。具体的パラメータの down-select は次回以降。

**実装制約の核心**: JSCM は UE→gNB 間の物理チャネルを「AI が暗黙的に最適化したコードワード」を流すことになるため、RAN4 試験（コンフォーマンス試験）の定義が技術的難題。**Testability（試験可能性）の設計が SEP の進歩性源泉**として Samsung が先行できる領域。

#### 10.2.2 CJT（Coherent Joint Transmission）との CSI 連携

**What**: 空間的に離れた複数 TRP が**位相同期したビームフォーミング**で同一データストリームを送信する方式。単一 TRP 比で平均 UPT **+40%** が Samsung の公開試験値。

**Rel-19 での Samsung 提案**（規格化済み）:
- **UE 支援キャリブレーションフィードバック**: 複数 TRP 間の時間オフセット・周波数オフセット・位相オフセットを UE が測定して報告するプロトコルを Rel-19 で仕様化。Samsung が主要提案者。
  - 遅延オフセット 5 bit 量子化で理想性能に近接
  - サブバンド報告が広帯域報告を大幅に上回る（TAE 65ns 時）

**6G での拡張提案**:
- セルハンドオーバーなしの動的 CJT 協調セット適応（7 セルシナリオで最大 +9% UPT、2 スロット処理 latency）
- AI 活用の CSI フィードバック圧縮（多 TRP 対応・大規模アンテナ対応）
- 層別 SD（空間領域）成分選択による細粒度最適化
- **Rel-18 で複雑化したコードブック設計を 6G で簡素化・再定義**（実装容易化と essentialSEP 主張の両立を狙う）

#### 10.2.3 コードブック設計（歴史的優位の継承）

Samsung は 5G NR における Type II / eType II コードブックの主要設計者であり、6G では：

- 128/256/512 port 時代の **CSI-RS CDM 集約パターン設計**（CDM タイプ拡張 fdCDM4, cdm8-FD4-TD2 等）
- **Near-Field / SNS（Spatial Non-Stationary）への対応コードブック** — 遠距離平面波仮定が崩れる距離（フレネル距離内）で有効な設計
- **CSI-RS RE 共有スキーム**（5G CSI-RS と 6G CSI-RS が同一 RE を共用できる後方互換設計）

これらは 10.5.3.1 の agreement テキストに「検討すべき設計軸」として収録されており、Samsung が co-FL として議題構造を設定した成果でもある。

---

### 10.3 Samsung の SEP 戦略上の狙い

| 提案 | 標準内での位置づけ | SEP 余地の理由 |
|:---|:---|:---|
| RS-PAI ゼロパディング（R1-2603378） | TS 38.212 に直接収録（CR 確定） | AI 性能監視の全実装が参照する必須手順。回避困難 |
| CPU duration 仕様（R1-2603379） | TS 38.214 に直接収録（CR 確定） | UE-side training の計算リソース管理は全 AI/ML モデルに適用 |
| JSCM | 6G 研究段階（FFS）、agreement 収録 | 5G には存在しない新領域。誰も強い特許を持っていない可能性 |
| CJT 向け UE 支援キャリブレーション | Rel-19 で normative 化済み | TDD multi-TRP の全実装が参照する必須手順 |
| 6G CSI-RS CDM 集約パターン | 6G 研究段階、agreement 収録 | コードブック設計の歴史的優位を 6G に持ち込む「define-then-patent」戦略 |

---

---

## 11. 合意の選択肢対比と価値基準分析

> 本セクションは Chair Notes _eom4 の合意テキスト（§4）と 3GPP における標準的な評価プロセスを組み合わせ、**「なぜその選択肢が選ばれたか」**を整理する。
> 一次情報（Chair Notes）から直接引用できる内容と、合意テキスト・業界慣行から導いた分析（`[分析]` と明記）を区別する。

### 11.1 3GPP RAN1 における汎用的な合意基準

本会合全体を貫く「下選び（down-select）の価値基準」の優先順序:

| 優先度 | 基準 | 本会合での使われ方（具体例） |
|:---:|:---|:---|
| 1 | **Testability（RAN4 試験定義可否）** | JSCM が FFS に留まった主因。MAC-CE in MSG4 必須化見送りの背景にも | 
| 2 | **シグナリングオーバーヘッド最小化** | Q=2（2 bit）量子化の採択、UCI two-part の継承 |
| 3 | **後方互換性（5G 実装への影響）** | SRS sequence に ZC/CGS ベースライン、CSI-RS RE 共有の 4 ユースケース設計 |
| 4 | **性能（SLS/LLS での優位）** | L1-RSRP をベースラインに L1-SINR を FFS とした判断 |
| 5 | **実装複雑度（FLOPs/パラメータ数）** | 10.5.2.4 で FLOPs/params 数を評価軸として明示採択 |
| 6 | **スケジューリング整合性** | CSI-RS density reduction の RB 制約オプション設計 |

> **観察**: 学術論文では「性能最大化」が第一だが、3GPP では「試験で確認できるか（Testability）」が事実上の第一関門。これが「論文 vs 3GPP」ギャップの根本的理由。

---

### 11.2 9.1.1 — Rel-20 AI/ML CSI Case 0 の選択肢対比

#### 11.2.1 量子化コードブック Q=2 の選定根拠

本会合前に存在したと推定される選択肢と採否の理由:

| 選択肢 | 内容 | 採否 | 理由 |
|:---|:---|:---:|:---|
| Q=1（1 bit） | {1/4, 3/4} の 2 点量子化 | 却下 | rank ≥ 2 の多層 BF では精度が不足。性能劣化が許容外 |
| **Q=2（2 bit）** | {1/8, 3/8, 5/8, 7/8} の 4 点均一量子化 | **採択** | UCI payload 効率と量子化精度のバランスが最適。Rel-19 で確定した RS-PAI 3 bit ゼロパディング（R1-2603378）との整合性も確保 |
| Q=3（3 bit） | 8 点量子化 | FFS/将来検討 | 精度は上がるが UCI overhead が倍増。PUCCH payload 制約に抵触するリスクが高い |

> [分析] 均一量子化（uniform SQ）を採択したのは試験容易性によるところが大きい。非均一量子化は性能が上がる場合があるが、「どのコードブックでも等しく試験できる」というRAN4 要件を満たしにくい。

#### 11.2.2 target CSI 量子化方式：Option 1a vs 1b のダウンセレクト

本会合以前に複数の選択肢が提案されていたと推定される。本会合では 1a・1b に絞り込んだが最終選択は先送り。

| 選択肢 | 表現方式 | 支持する企業論理 | 残った理由 |
|:---|:---|:---|:---|
| **Option 1a（real-imaginary）** | 複素数の実部・虚部で分解 | 行列演算（MRC/ZF）が直交成分ベースであり UE 実装と自然対応。NW 側 decoder の線形再構成に有利 | チャネル分布によって 1a・1b の優劣が逆転するケースがある |
| **Option 1b（amplitude-phase）** | 振幅・位相の極形式で分解 | eType II コードブックの WB/SB amplitude 設計との継承性がある。ビームフォーミング重みの「大きさ vs 向き」と直感的に対応 | 同上 |

**最終選択が先送りになった理由**: 「性能優劣が一義的に決まらない場合は FFS として両立」が 3GPP の標準的判断。十分なシミュレーション（チャネルモデル・SNR 分布の組合せ）を次会合以降に集めて決定する方針。

#### 11.2.3 UCI two-part 構造を継承した設計根拠

5G NR の Type II Large-codebook では UCI two-part（Part 1 = RI/CRI、Part 2 = PMI）が既に採用されている。本会合はこれを AI/ML two-sided model に継承することを合意した。

**継承の価値基準（3 点）**:

1. **スケジューリング先行性**: Part 1（CQI/RI）を Part 2（PMI）より先に受信することで、gNB は PDSCH 割当を PMI 受信前に確定できる。gNB の scheduling latency を削減する設計原則。
2. **HARQ との整合**: ACK/NACK と CQI が同一スロットに載る既存 PUCCH 構造を変更しない → Rel-15 以降の UE 実装を破壊しない。
3. **AI モデル出力の可変性対応**: PMI の bit 数はモデル複雑度に依存して可変（32〜192 bit の幅）。two-part に分離して Part 2 size を動的設定することでオーバーヘッドを柔軟に管理できる。

> PMI payload のレイヤ別 bit 数 {32,2}, {64,2}, ... はこの「可変性 × UCI budget 制約」を反映した合意値。

---

### 11.3 9.2 — NR MIMO Phase 6 の選択肢対比

#### 11.3.1 Early CSI-RS の QCL 参照信号：Option-1 vs Option-2

**本会合の結果**: 両 option 存続、RAN1#125 で down-select 予定。

| Option | QCL 参照信号 | QCL タイプ | 利点 | 欠点 |
|:---|:---|:---|:---|:---|
| **Option-1** | SSB | Type-C（時間オフセット + 周波数オフセットのみ） | SSB は初期アクセス時から UE が保持。AP-TRS の追加設定が不要。オーバーヘッド最小 | SSB 周期が長い（20ms〜160ms）ため、高速移動 UE では channel tracking 精度が劣化 |
| **Option-2** | AP-TRS | Type-A（遅延スプレッド、Doppler を含む full QCL） | 専用 TRS で精密なチャネル推定が可能。高速移動・室内 LOS 逆 Doppler シナリオで安定 | AP-TRS の新規 RRC 設定が必要。RACH 直後は AP-TRS が未配信で使えない transition 問題 |

**RAN1#125 での down-select に先送りした理由**: UE 速度（歩行者 3km/h vs 車両 120km/h）によって Option の性能逆転が起きることが各社の寄書から示された。「どのシナリオを 6G のターゲットとするか」の KPI 合意なしに下選びは困難。SLS 結果を次回持ち寄ることで合意。

#### 11.3.2 CSI-RS density reduction：3 案の設計哲学と対立

| 候補 | 設計原則 | 支持企業の想定論理 |
|:---|:---|:---|
| **Opt-1（ZP CSI-RS 整合）** | NZP CSI-RS の配置 RB を ZP CSI-RS の構造と一致させる | **干渉管理一貫性優先**: rate matching 設計と scheduler の complexity を最小化。Ericsson / Nokia 系の「整合性优先」思想 |
| **Opt-2（1〜2 連続 RB）** | 1 または 2 連続 RB 単位で CSI-RS を配置する | **スケジューリング粒度整合**: 5G NR の最小 PRB pair 単位に対応。MediaTek 等チップ実装視点での feasibility |
| **Opt-3（均等分散）** | 帯域内を均等間隔で CSI-RS を分散配置 | **チャネル推定精度優先**: 等間隔サンプリングは帯域全体の周波数応答を最も正確に補間できる。Samsung / 中国ベンダーの性能優先思想 |

**対立構図**: 「干渉管理（Opt-1）」vs「実装容易性（Opt-2）」vs「推定精度（Opt-3）」は三つ巴。3 社以上が強く異なる案を推した場合、3GPP は SLS 数値で決着をつける慣行がある。本会合ではシミュレーションが未収束のため 3 案並走のまま継続。

#### 11.3.3 MAC-CE-in-MSG4 必須化の見送り

**議論された選択肢**:

| Option | 内容 |
|:---|:---|
| **必須化（A 案）** | RACH 完了の MSG4（RRC Connection Setup/Resume）に aperiodic SRS-AS や TRS のトリガリング MAC CE を含める → 接続直後の CSI 収集を高速化 |
| **見送り（B 案）** | 接続後に別途 DCI でトリガリングする既存フロー。接続直後に MAC CE を使うのは実装者の任意 |

**B 案（見送り）の価値基準**:
- MSG4 は HARQ process 0 でのやりとりが多く、payload 制約が厳しい
- 初期段階の SRS-AS trigger が有効かどうかは UE アンテナ構成とチャネル状況に依存し、汎用 benefit が不明確
- 「全 UE に必須実装コストを課す」のは benefit/cost が一義的でない限り 3GPP では避ける慣習
- [分析] Ericsson / Nokia など欧州系が「十分なデータがなければ必須化しない」スタンスで慎重姿勢をとったと推察される。

---

### 11.4 10.5.2.4 — 6GR Beam Management の選択肢対比

#### 11.4.1 ビーム報告量：L1-RSRP をベースラインとした価値基準

| 報告量 | 内容 | 採否 |
|:---|:---|:---:|
| **L1-RSRP** | 受信信号電力（干渉を含まない） | **採択（ベースライン）** |
| L1-SINR | 信号対干渉雑音比（スループット予測に直結） | **FFS** |
| L1-RSRQ | 参照信号受信品質（RSRP / RSSI 比）、LTE 時代の指標 | **未採択** |

**RSRP をベースラインとした 3 つの理由**:
1. **Testability**: RSRP は受信電力の絶対値測定。RAN4 が ±5 dB 等の精度要件を明確に定義できる。SINR は干渉推定精度が UE 実装に大きく依存し、試験方法の合意が困難。
2. **後方互換性**: 5G NR の全 UE が L1-RSRP を実装済み。6G SI の評価ベースラインとして 5G 手法との比較が容易。
3. **段階的高度化の原則**: SI 段階ではシンプルな指標から始め、WI 化で高度化するのが 3GPP の慣習。SINR 追加は WI フェーズの議題として位置付け。

#### 11.4.2 UEIBM の 2 イベント設計の根拠

**UEIBM 導入の背景**: 5G では NW が定期ポーリングでビーム管理を主導（NW-initiated）。UE は「報告するだけ」。6G では UE が自律的にビーム切替を起動（UE-initiated）することで、NW 側のポーリング遅延を削減し、高速移動時のビーム切替レイテンシを短縮。

| イベント | トリガー条件 | 設計意図 | 5G との差分 |
|:---|:---|:---|:---|
| **Event-1** | サービングビームの予測品質が閾値を**下回る** | 「守りのビーム管理」: 通信品質劣化を UE 側で先行検知し、NW のポーリング待ちなしに報告トリガー | 5G では NW タイマーによる定期ポーリングのみ |
| **Event-2** | 候補ビームの予測品質が閾値を**上回る** | 「攻めのビーム管理」: より良いビームを発見した UE が積極的に切替を要求 | 5G では UE 起点の切替要求なし |

**2 イベントの独立設定を採用した理由**: 単一 Event（「サービングビームが悪化 かつ 候補ビームが改善」）では条件が厳しすぎてトリガーされない局面が生じる。2 Event を独立に設定することで「Event-1 のみ有効化（防御的 BM）」「両方有効化（積極的 BM）」のポリシー柔軟性を持たせた設計。

#### 11.4.3 FLOPs / パラメータ数を評価軸に採用した意義

「AI ベース予測と非 AI ベース手法を FLOPs / モデルパラメータ数で比較する」という合意は、**6G における AI 手法の価値基準を明示的に定義**した重要な転換点。

- **FLOPs**: UE の計算リソース制約（バッテリー寿命・発熱）を定量化する指標
- **パラメータ数**: モデルサイズ = メモリ消費 + OTA アップデートコスト

5G まで: 「性能が良ければ採択」という 1 次元評価  
6G から: 「性能 / 複雑度のトレードオフ曲線で評価」という 2 次元評価

この基準の採択は、**「計算量的に重すぎる AI モデルは 6G 標準には入れない」という暗黙のゲートキーパー**を設定することを意味する。SEP 観点では「FLOPs 効率の高い AI BM アルゴリズム」は採択されやすく、その特許は essential 化しやすい。

---

### 11.5 10.5.3.1 — 6GR DL CSI の選択肢対比

#### 11.5.1 CSI-RS ポート数 128 / 256 / 512 の三択並走の理由

**5G との対比**:

| 世代 | 最大ポート数 | 備考 |
|:---|:---:|:---|
| 5G NR Rel-15 | 32 | Type II コードブック上限 |
| 5G-A Rel-18 | 64 | eType II 拡張 |
| **6G Rel-20 SI（候補）** | **128 / 256 / 512** | 本会合で 3 択として並走 |

**3 案を down-select せず並走させた理由**:

| 候補 | 想定シナリオ | ハードウェア実現性 |
|:---|:---|:---|
| **128 port** | sub-6 GHz の地上 BS。現在の 32〜64 port array の延長。近未来で最も実現性が高い | 既存 antenna array 技術の延長で対応可能 |
| **256 port** | mmWave massive MIMO。密な array が可能な近距離シナリオ（indoor、dense urban） | 位相制御 IC の集積度上昇が必要 |
| **512 port** | 分散 MIMO / Cell-Free シナリオを想定。単独 BS には過大で、複数 TRP 協調前提 | 現状のチップセットでは困難。6G 後期か研究用途 |

SI 段階では「どのシナリオを 6G の primary target とするか」が未確定。周波数帯（sub-6 GHz、FR2、sub-THz）ごとに実現可能なポート数が大きく異なるため、シミュレーション完了後に down-select。

#### 11.5.2 L1 vs L2 CSI 報告比較軸（A1〜A7、B1〜B4）の採用背景

5G NR では「CSI 報告は全て L1（PHY）内で完結」が原則だった。6G では L2（RLC/MAC 層）への機能分散も本格検討。この判断を構造化するために 11 の評価軸が合意された。

**A 軸（基本機能評価）**:

| 軸 | 評価内容 | L1 有利 | L2 有利 |
|:---|:---|:---|:---|
| A1: efficiency | スペクトル効率 | 低遅延でのリアルタイム BF 最適化 | AI 圧縮による高効率フィードバック |
| A2: latency | CSI フィードバック遅延 | PHY 内完結で最小遅延 | RLC/PDCP 層経由で遅延増 |
| A3: reliability | 報告の信頼性 | HARQ 再送による信頼性確保 | アプリ層での再送制御 |
| A4: UE 複雑度 | UE の演算・メモリコスト | PHY 処理のみ | 上位スタックも動作する必要あり |
| A5: NW 複雑度 | gNB 側処理コスト | scheduler への直接入力 | 上位層のプロトコル変換が必要 |
| A6: congestion | UCI 輻輳の管理 | PUCCH/PUSCH 容量に厳しい制約 | バッファ管理で柔軟対応 |
| A7: payload 範囲 | 可変 payload への対応 | 固定サイズが基本 | 可変長 payload に対応しやすい |

**B 軸（付加価値評価）**: B1=scheduling 制約緩和 / B2=multiplexing 簡素化 / B3=タイムライン緩和 / B4=可変 payload — いずれも L2 報告が相対的に有利な領域。

> この 11 軸は「どの条件なら L2 報告への移行が正当化できるか」の設計原則基盤。5G では「L1 に全てを詰め込む」が原則だったが、6G では L2 分散の可能性を構造的に検討する宣言でもある。**A2（latency）と A4（UE 複雑度）が競合するトレード空間に SEP 余地**がある。

#### 11.5.3 CDM 設計拡張の選択肢

| 設計要素 | 5G NR | 6G 検討候補（#124bis 合意） | 変更の動機 |
|:---|:---:|:---|:---|
| CDM サイズ | 1, 2, 4, 8 | 既存 + **16** | 128 port 以上では短い OCC では多重分離性能が劣化。CDM16 で 1 RE に 16 port を多重 |
| CDM タイプ | FD2, FD4, FD8 等 | 既存 + **fd-CDM4**（周波数方向 4 分割）、**cdm8-FD4-TD2**（周波数 4 × 時間 2） | 時間方向 CDM 拡張で時変チャネルへの対応 |
| 配置スタイル | Localized のみ | Localized **vs Comb** | Comb は周波数ダイバーシティ高くチャネル推定精度が上がるが、スケジューリングが複雑化 |

**Localized vs Comb の設計トレード**:
- Localized: 連続 RB に集約 → スケジューリング単純、干渉局所化
- Comb: 飛び飛び RB に配置 → 周波数ダイバーシティ高く広帯域推定精度が高い
→ 両方 FFS として継続（シナリオ依存のため一義的に優劣が決まらない点は 11.3.2 の CSI-RS density reduction と同構造）

#### 11.5.4 JSCM が「FFS」で agreement テキストに入った意義と残るハードル

**FFS ながら採録された理由**: Samsung Research 公開値（eType II 比 +94.4% SE、UE 演算 2.9%）が議論を通過するだけの説得力を持ち、「SI での検討対象」として門前払いにはできなかった。

**FFS 継続（本格採択に至らなかった）の具体的ハードル**:

| ハードル | 内容 | 3GPP 上の影響 |
|:---|:---|:---|
| **Testability** | AI エンコーダ出力が「標準コードブック」でないため RAN4 が「正しい出力か」を試験できない | コンフォーマンス試験の枠組み自体の再定義が必要 |
| **PAPR 制約** | JSCM の複素コンステレーションが UE RF 送信の PAPR 上限に収まるかの試験方法が未確定 | UE の RF 設計・試験に根本的影響 |
| **コンステレーション固定問題** | 3GPP は変調方式（QAM/APSK）のコンステレーション点を仕様で固定する慣習がある。「AI が最適化した任意コンステレーション」はこの慣習と根本的に相容れない | 最終的には QAM/APSK 系の離散グリッドへの丸め込みが必要になり、JSCM の本来の性能が損なわれる可能性 |
| **ベンダー依存性** | AI モデルは学習データ依存。Samsung の JSCM モデルと Ericsson の JSCM モデルが異なる動作をすると、UE-gNB 異ベンダー組合せの相互接続性が保証できない | inter-vendor interoperability の定義が未解決 |

> **知財観点のインプリケーション**: 上記 4 ハードルへの具体的解決策（例:「学習データに依存しない構造的 PAPR 制約の設計」「ベンダー非依存の等価コンステレーション定義」）は、まだ誰も強い特許を持っていない可能性がある「define-then-patent」領域。

---

## Next Steps

- [ ] **9.1.2 Apple FL summary 全 4 ラウンド精読**: `R1-2602690〜R1-2602693`（Inbox/drafts/9.1.2/）から Direction A 〜 D の細部を抽出 → Apple の戦略文書として知財余地マップを作る
- [ ] **9.1.1 Qualcomm FL summary 全 4 ラウンド精読**: `R1-2602996〜R1-2602999` → SQ コードブックの選定ロジックと UCI mapping の bit 順序の根拠を確認
- [ ] **10.5.3.1 FL summary #1〜#10 通読**: Samsung+vivo の議論進化を追跡（66 Tdoc が #1〜#10 でどう収斂したか）
- [ ] **TR 38.843**（Rel-18 SI 報告書）と本会合 9.1.x 合意の差分マッピング — Rel-19 → Rel-20 で何が新しくなったかを spec-mapping
- [ ] **RP-252936** WID（NR MIMO Phase 6, MediaTek）と **NR_AIML_air_Ph2** WID（rapporteur 要確認）を `portal.3gpp.org/WorkItems` から取得
- [ ] **10.5.3.1 の JSCM 寄書** を企業別にスキャン（Samsung Research の 6G AI/ML for Physical-layer Part II - JSCM ブログとの突合）→ Section 10.2.1 の数値を Tdoc で裏付け
- [ ] **Chair Notes _eom4 の各 agenda の Conclusion** を抽出し「合意できなかったもの = 進歩性の源泉候補」リストを作る
- [ ] 次回 RAN1#125 の予告（agenda.csv の `down-select in RAN1#125` 文言を全件抽出）→ Malta で先送りされた論点リスト
- [ ] **Rel-19 → Rel-20 の Apple/Qualcomm/Samsung の Tdoc 提出パターン** を時系列で並べ、SEP 戦略の進化を可視化
- [ ] **Section 10.2.1 JSCM の Testability 問題**を深掘り — RAN4 LS が今後どのような形で来るか予測し、先行特許候補を整理

