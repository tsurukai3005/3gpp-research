---
title: "RAN1#124bis (Malta, 2026-04-13〜04-17) — DL CSI / Beam Management / AI-ML 寄書と議論の整理"
status: draft
confidence: high
created: 2026-04-27
updated: 2026-04-27
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
up: "[[260420_標準化特許申請のための調査戦略]]"
related:
  - "[[260422_Rel-15-NR-勉強会トピック調査ガイド]]"
  - "[[260420_NRフレーム構造とリソースブロックの進化まとめ]]"
---

# RAN1#124bis（Malta、2026-04-13〜04-17）— DL CSI / Beam Management / AI-ML

> 本ノートは「学術理想 vs 3GPP 実装制約」のギャップ可視化を目的とし、Malta 会合の Tdoc / Chair Notes（end-of-meeting v4 = `eom4`）から RAN1 が実際に何を合意したかを整理する。本会合は **2026-04-13〜04-17（5 日間）**、登録 1,724 件の Tdoc が提出された。
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
| Agreement | 性能評価用の **SRS error model**: 推定チャネル = 真のチャネル + 白色 Gaussian（分散はスケーリング係数で）、SRS 干渉/不完全 OL 電力制御/UE Tx アンテナ利得不平衡を additionally 考慮可 |

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
- **10.5.3.1**: ポート数 128/256/512 down-select、CDM 設計、JSCM の testability（RAN4 LS が今後）
- **10.5.3.2**: 5G に対する SRS BW 拡張方式（hopping vs sparse vs 再定義）の down-select
- **10.5.3.3**: tracking RS の具体パラメータ x, Y, N, Ssymb, Sslot

## 8. 市場・知財余地

- **Two-sided CSI compression（9.1.x）**: SEP の宝庫。Qualcomm が量子化/UCI を、Apple が pairing/inter-vendor を握る。**JSCM**（10.5.3.1）は新概念で、誰もまだ強い特許を持っていない可能性 — 注目領域。
- **6G CSI-RS の CDM 集約 / RE 共有**: 5G との後方互換を保ちつつ拡張する設計は、回避設計（design-around）が難しく essential 化しやすい。
- **CPI（Channel Property Information）**: 全く新しい概念。define-then-patent の好例。**実装制約が確定する前に出願すべき**領域。
- **UEIBM の event 定義**: 端末側からのビーム管理開始は 5G では受動的 UE 報告のみ。UEIBM の 2 event（Event-1 = 自ビーム劣化、Event-2 = 候補ビーム良化）が 6G で正式化される。

## Next Steps

- [ ] **9.1.2 Apple FL summary 全 4 ラウンド精読**: `R1-2602690〜R1-2602693`（Inbox/drafts/9.1.2/）から Direction A 〜 D の細部を抽出 → Apple の戦略文書として知財余地マップを作る
- [ ] **9.1.1 Qualcomm FL summary 全 4 ラウンド精読**: `R1-2602996〜R1-2602999` → SQ コードブックの選定ロジックと UCI mapping の bit 順序の根拠を確認
- [ ] **10.5.3.1 FL summary #1〜#10 通読**: Samsung+vivo の議論進化を追跡（66 Tdoc が #1〜#10 でどう収斂したか）
- [ ] **TR 38.843**（Rel-18 SI 報告書）と本会合 9.1.x 合意の差分マッピング — Rel-19 → Rel-20 で何が新しくなったかを spec-mapping
- [ ] **RP-252936** WID（NR MIMO Phase 6, MediaTek）と **NR_AIML_air_Ph2** WID（rapporteur 要確認）を `portal.3gpp.org/WorkItems` から取得
- [ ] **10.5.3.1 の JSCM 寄書** を企業別にスキャン（Samsung Research の 6G AI/ML for Physical-layer Part II - JSCM ブログとの突合）
- [ ] **Chair Notes _eom4 の各 agenda の Conclusion** を抽出し「合意できなかったもの = 進歩性の源泉候補」リストを作る
- [ ] 次回 RAN1#125 の予告（agenda.csv の `down-select in RAN1#125` 文言を全件抽出）→ Malta で先送りされた論点リスト
- [ ] **Rel-19 → Rel-20 の Apple/Qualcomm/Samsung の Tdoc 提出パターン** を時系列で並べ、SEP 戦略の進化を可視化

