---
title: "Two-sided CSI 圧縮（Case-0）の inter-vendor 互換性 — RAN1#124 → #124bis → #125 議論変遷"
status: draft
confidence: medium
created: 2026-05-01
updated: 2026-05-01
axes:
  technology-layer: [phy-mimo, cross-layer]
  generation: [rel-19, rel-20, rel-20-6g]
  value: [throughput, ai-integration, energy-efficiency]
  market: [consumer-xr, b2b-industrial, fwa]
  adoption-factors: [standard-convergence, backward-compat, ecosystem-readiness, operator-roi]
  ip: [novelty, inventive-step, spec-mapping]
sources:
  - url: https://arxiv.org/abs/2507.18538
    title: "AI/ML Life Cycle Management for Interoperable AI Native RAN（NR_AIML_air_Ph2 解説）"
    accessed: 2026-05-01
  - url: https://arxiv.org/html/2507.18538v2
    title: "AI/ML Life-Cycle Management — HTML v2（Direction I/II 定義）"
    accessed: 2026-05-01
  - url: https://arxiv.org/abs/2502.17459
    title: "Study on Downlink CSI compression: Are Neural Networks the Only Solution?（IIT Madras、PCA ベース）"
    accessed: 2026-05-01
  - url: https://arxiv.org/abs/2506.21796
    title: "Demonstrating Interoperable Channel State Feedback Compression with Machine Learning（Nokia + Qualcomm 実機実証）"
    accessed: 2026-05-01
  - url: https://research.samsung.com/blog/6G-AI-ML-for-Physical-layer-Part-II-CSI-Compression-with-JSCM
    title: "Samsung Research — 6G AI/ML for PHY Part II: CSI Compression with JSCM"
    accessed: 2026-05-01
  - url: https://research.samsung.com/blog/Enable-JSCC-based-CSI-Feedback-for-B5G-6G-Design-Standardization-and-Prototype
    title: "Samsung Research — Enable JSCC-based CSI Feedback for B5G/6G"
    accessed: 2026-05-01
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/
    title: "RAN1#124 FTP root（Gothenburg、2026-02）"
    accessed: 2026-05-01
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom4.docx
    title: "Chair notes RAN1#124bis_eom4.docx — End-of-Meeting (final)"
    accessed: 2026-05-01
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/
    title: "RAN1#125 FTP root（フォルダ実在のみ確認済み、内容未公開）"
    accessed: 2026-05-01
  - url: https://www.3gpp.org/technologies/ai-ml-nr
    title: "AI/ML for NR Air Interface — 概要（rapporteur: Juan Montojo, Qualcomm）"
    accessed: 2026-05-01
  - url: https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1060078
    title: "WI #1060078 — FS_NR_AIML_air_Ph2（[要確認] アクセス制限あり）"
    accessed: 2026-05-01
  - url: https://ofinno.com/the-standards-readout-2/6g-takes-shape-in-gothenburg-and-goa-first-solutions-emerge-as-3gpp-moves-past-problem-identification/
    title: "Ofinno — 6G Takes Shape in Gothenburg and Goa（RAN1#124 概況）"
    accessed: 2026-05-01
references: []
up: "[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]"
related:
  - "[[260430_RAN1-124-125-13トピック議論変遷]]"
  - "[[260428_RAN1-124bis-MIMO-operation-10.5.2]]"
  - "[[260424_Rel-15-物理リソース仕様策定の議論変遷]]"
trace:
  ai_id: "ai_nr_aiml_csi_compression_r19"
  meetings_in_scope: ["RAN1#124", "RAN1#124bis", "RAN1#125"]
  completeness:
    chair_notes_obtained: []  # references/ には未配置
    chair_notes_indirect:     # 既存 documents/ ノートで要約済み
      - "RAN1#124bis (via [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.2 / §4.3)"
    chair_notes_missing: ["RAN1#124", "RAN1#125"]
    tdocs_obtained: 0
    web_secondary_sources: 7
---

# Two-sided CSI 圧縮（Case-0）の inter-vendor 互換性 — RAN1#124 → #124bis → #125 議論変遷

> **位置づけ**: [[260430_RAN1-124-125-13トピック議論変遷]] §5（CSI セクション）の **inter-vendor pairing 軸での縦の深堀**。本ノートは「**両ベンダーが互いのモデル中身を見せずにどう pair させるか**」という Two-sided AI/ML CSI 圧縮の最大の実装制約を、Rel-19 NR_AIML_air_Ph2 WI（Case-0 = 現スロット空間-周波数 CSI 圧縮、時間方向予測なし）に焦点を当てて整理する。
> **confidence: medium** — RAN1#124bis の合意事項は [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]（一次情報 Chair Notes eom4 を参照済み）から **high** で引用、#124 と #125 については **二次情報のみで low〜medium**。具体合意文言の逐語確認は §未取得資料 §10 の URL を fetch して別途行う。
> **本ノートの新規性**: ユーザー指定の 3 焦点（inter-vendor 訓練連携メカニズム、non-AI/ML 並列評価、6GR スケーラビリティ接続）に絞り、**SEP 仮説 5 件**を§9 で提案する。

---

## 0. 背景 — なぜ inter-vendor 互換性が最大の障害か

### 0.1 Two-sided model の構造的問題

```
[UE]                          [gNB]
 入力チャネル H              復元チャネル Ĥ
   │                            ▲
   ▼                            │
 UE-side encoder         gNB-side decoder
 （Apple/Qualcomm/        （Ericsson/Nokia/
   Samsung/MediaTek 等）    Huawei/Samsung 等）
   │                            ▲
   └────── 圧縮 bitstream ──────┘
            （PUCCH/PUSCH UCI に乗せる）
```

- **UE と gNB が異なるベンダー** であることが当然の世界（UE: Apple/Samsung/Xiaomi… ／ gNB: Ericsson/Nokia/Huawei/Samsung…）
- **両方の AI モデルが互いに整合**しないと、復元 CSI が崩れて MU-MIMO のスケジューリングが破綻する
- 一方、**両者ともモデルパラメータ・訓練データ・量子化方式は知財**であり、開示したくない

> 学術論文（[arXiv 2502.17459](https://arxiv.org/abs/2502.17459)、IIT Madras）はこの「**inter-vendor compatibility 問題**」を AI/ML CSI 圧縮の *the* 障害として提示し、「**PCA ベースの transformation matrix を毎報告で送る**」という対案で AI モデル不要を主張するほどに深刻視されている（[要確認] 本研究は 3GPP 寄書化の痕跡なし）。

### 0.2 アジェンダ分担（#124bis 確定）

| AI 番号 | タイトル | FL（#124bis） | 主導性格 |
|:---|:---|:---|:---|
| **9.1.1** | CSI spatial/frequency compression without temporal aspects ("Case-0") | **Qualcomm（Juan Montojo）単独 FL** | 量子化・UCI 構造・payload 設計 |
| **9.1.2** | Inter-vendor training collaboration for two-sided AI/ML models | **Apple 単独 FL** | pairing メカニズム・データセット形式・性能ターゲット |

> 出典: [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §3.1〜§3.2、§5.2 表、§4.2〜§4.3。
> **戦略的解読**: Qualcomm が「中身（量子化・UCI）」、Apple が「外側（pairing API）」という分業。Apple は UE-side encoder を**秘匿しながら**標準連携できるフレームを自社主導で定義しに来ている。

---

## 1. RAN1#124（Gothenburg, 2026-02-09 〜 02-13）

### 1.1 概況（confidence: low、二次情報のみ）

- **会場**: Gothenburg, Sweden（[Ofinno](https://ofinno.com/the-standards-readout-2/6g-takes-shape-in-gothenburg-and-goa-first-solutions-emerge-as-3gpp-moves-past-problem-identification/)）
- **Tdoc 一次情報**: 未取得（Chair Notes / agenda.csv とも本リポジトリ未配置）
- **Ofinno blog の議論カバー**: PAPR 削減・RAN2 modular RRC・SA2 シグナリングが中心で、**CSI 圧縮の合意事項は同 blog では言及なし**（[要確認]）

### 1.2 9.1.1 / 9.1.2 で取り上げられたとされる論点（二次情報集約）

> 以下は [[260430_RAN1-124-125-13トピック議論変遷]] §5.2、Apex Standards 寄書要旨、および arxiv:2507.18538v2 の整理から再構成。**逐語の合意は確認できていない**。

| 論点 | 内容（二次情報） | 一次確認の必要性 |
|:---|:---|:---|
| データセット形式の標準化 | 「standardized dataset formats」を共通基盤として議論。Option 1a (real-imaginary) / 1b (amplitude-phase) の二択が #124 時点で残存 | **要 Chair Notes** |
| Inter-vendor 訓練連携の方向性 | TR 38.843 の Type 1〜3（Rel-18 SI 由来）を Direction I/II（または A/B/C）に再編する動き | **要 R1-26xxxx FL summary** |
| non-AI/ML 並列評価義務 | 「AI/ML proposal は **non-AI/ML 並列評価**が義務」が #122〜#124 で再確認 | **要 RAN#108 WID** |

> **既知の数値レンジ**（#122〜#124 平均、Samsung・Nokia 等の寄書集計; 二次情報）: CSI feedback overhead 削減 **8〜79%**、user throughput **0〜17%** 増（[[260430_RAN1-124-125-13トピック議論変遷]] §5.2 表）。

### 1.3 引用 Tdoc（推定リスト、未取得）

- `R1-26xxxxx`（Apple, FL summary 9.1.2 #1〜#4 の前会合版） — [要確認]
- `R1-26xxxxx`（Qualcomm, FL summary 9.1.1 #1〜#4 の前会合版） — [要確認]

> #124 の Tdoc 番号体系は agenda.csv 未取得のため特定不能。`R1-26<連番>`（FTP/TSGR1_124/Docs/ 配下）を**§10 の URL リスト**から取得すること。

---

## 2. RAN1#124bis（Saint Julians, Malta, 2026-04-13 〜 04-17）

> 本会合は本リポジトリで Chair Notes eom4 を直接参照済み（[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]）。confidence: high。

### 2.1 概況

| 項目 | 内容 |
|:---|:---|
| Tdoc 件数（9.1.1 + 9.1.2 のみ） | **84 件**（9.1.1: 43、9.1.2: 41） |
| FL/Email moderator | 9.1.1: Qualcomm（Juan Montojo）／9.1.2: Apple |
| 9.1.2 ラウンド数 | FL summary #1〜#4（Apple 単独起草） |

### 2.2 Inter-vendor training collaboration（9.1.2）— 合意の核心

> 出典: [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.3、Chair Notes RAN1#124bis_eom4.docx。

| Agreement | 内容 |
|:---|:---|
| **Payload pair**（Direction A = reference model 共有） | target CSI = port-subband 領域の precoding matrix のとき、レイヤ毎に **{32,2}, {64,2}, {96,2}, {128,2}, {192,2}, {32,1}** をサポート（Layer 1〜3）。Layer 4 は {32,2}, {64,2}, {96,2}, {32,1}。NW は subset のみ交換可 |
| **Pairing ID** | pairing ID とデータセットは **1:1 対応**、**データセット間にリンクなし**（独立した model pair が複数併存可能） |
| **性能ターゲット** | レイヤ毎・CSI feedback set 毎に交換 |
| **RAN2 連携 LS** | `R1-2601756`（RAN2/Ericsson 起草）で「pairing ID for two-sided models」を SA5（管理面）にも展開 |

### 2.3 Direction A / B / C の現状（命名揺れに注意）

> **重要な命名揺れ**: arxiv:2507.18538v2 は **Direction I/II の 2 区分**で記述する一方、本リポジトリの既存ノートおよび Apple FL summary 系は **Direction A/B/C の 3 区分**を採用。3GPP 公式合意では下記の対応関係で読み替える:

| 現行表記 | arxiv 2507.18538v2 表記 | TR 38.843（Rel-18 SI）由来 | 内容 |
|:---|:---|:---|:---|
| **Direction A** | Direction I | (Type 1 から派生) | **Reference model 共有**：完全に標準化された reference encoder/decoder と parameter を提供 |
| **Direction B** | （Direction II の前半） | (Type 3 派生：encoder param) | **Encoder parameter 交換**：UE-side オフラインエンジニアリングを可能にする encoder パラメータ + target CSI |
| **Direction C** | （Direction II の後半） | (Type 3 派生：dataset alignment) | **Dataset 整列**：{target CSI, feedback CSI} の dataset 共有のみ |

> **#124bis での実態**: Apple FL summary は **「Direction A の payload pair down-select」を最初に通した**。Direction B/C は構造的合意（pairing ID = dataset 1:1 対応）に留まり、具体 API は FFS（[要確認] FL summary 起草者の Apple は Direction A を最重視）。

### 2.4 Case-0 圧縮本体（9.1.1）— 量子化・UCI・payload

> 出典: [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.2。

| Agreement | 内容 |
|:---|:---|
| **量子化コードブック** | NW がコードブックを交換しない場合の標準 SQ コードブック: **Q=2 で {1/8, 3/8, 5/8, 7/8}**、**Q=1 で {1/4, 3/4}** をサポート |
| **PMI スコープ** | precoding matrix feedback via two-sided model: **最大 128 ports / rank ≤ 4 / subbands ≤ 19** |
| **UCI 構造** | **two-part UCI** を採用。Part 1 = CQI/RI/CRI、Part 2 = PMI（全レイヤ）。レイヤを Group 1 / Group 2 に分割し、レイヤ強度順（強→弱）に bit を並べる |
| **NW 側データ収集** | target CSI 量子化方式は **Option 1a（real-imaginary）と 1b（amplitude-phase）の二択にダウンセレクト** |
| **性能監視** | paired CSI feedback と target CSI sample で監視。L3 シグナリング (Option 1) と L1 シグナリング (Option 2) のさらなる検討 |

### 2.5 引用 Tdoc

- `R1-2601750` — Draft Agenda of RAN1#124bis（議長提出、出典 [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]）
- `R1-2601756` — LS on pairing ID for two-sided models（RAN2/Ericsson）
- `R1-2603378` — Rel-19 maint TS 38.212 §6.3.1.1.2 TP（PUCCH 1〜2 ビット payload 救済）
- `R1-2603379` — Rel-19 maint TS 38.214 §5.2.1.6 TP（CPU duration 仕様化）
- Samsung 寄書（既知）: `R1-2400723`、`R1-2505588`、`R1-2509516`（[要確認] §3 で別途扱う）

> **重要**: 上記以外の 9.1.1/9.1.2 の **個別 Tdoc 84 件は本リポジトリ未取得**。FL summary（Apple/Qualcomm 単独起草）の中身も `references/` 未配置。Tdoc レベルの企業別主張比較は §10 の URL fetch 後に追補。

---

## 3. 6GR DL CSI（10.5.3.1）— Rel-19 Two-sided と並走する Samsung JSCM の差別化

### 3.1 JSCM（Joint Source-Channel Modulation）の構造

出典: [Samsung Research blog (2025-12-30)](https://research.samsung.com/blog/6G-AI-ML-for-Physical-layer-Part-II-CSI-Compression-with-JSCM)、[Samsung Research blog (2025-10)](https://research.samsung.com/blog/Enable-JSCC-based-CSI-Feedback-for-B5G-6G-Design-Standardization-and-Prototype)、[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.7。

| 観点 | 通常の Two-sided AI/ML CSI（Case-0） | Samsung JSCM |
|:---|:---|:---|
| 信号処理パイプライン | source coding（量子化）→ channel coding → modulation | **3 ステップを joint 最適化**、量子化を avoid（unquantized 信号に直接動作） |
| UE 計算複雑度 | 中〜大（Transformer/CNN encoder） | **Type-II 比 2.9%**（行列演算のみ）と Samsung 主張 |
| Inter-vendor pairing | 9.1.2 で Direction A/B/C を新規構築 | **NW-sided model** に重心を寄せ、UE は JSCM の固定変換のみで「pairing 問題を回避」 |
| Cliff effect | あり（圧縮率に応じた quality cliff） | 「graceful degradation」を主張 |

> **戦略的解読**: Samsung JSCM は「**Rel-19 Case-0 の inter-vendor pairing 問題そのものを 6G では発生させない**」というアプローチで差別化を狙う。Rel-19 では UE-side encoder を主役にする 9.1.2 と真正面から競合せず、6GR の 10.5.3.1（DL CSI、本会合最大 66 Tdoc）に並走させる戦略。

### 3.2 6GR スケーラビリティとの接続（256〜512+ CSI port）

> 出典: [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.7、[[260430_RAN1-124-125-13トピック議論変遷]] §5.4。

| 観点 | Rel-19 (Case-0) | 6GR (10.5.3.1) |
|:---|:---|:---|
| **CSI-RS 最大ポート数** | 32（5G Rel-15 上限）、Two-sided で precoding matrix feedback は 128 port まで | **Alt-1=128 / Alt-2=256 / Alt-3=512** から down-select 候補 |
| **コードブック構造** | 5G Type-II eType-II 系（W₁W₂） | **W₁W₂Wf**（周波数次元追加の 3 段構成）も評価対象 |
| **JSCM 採用** | 採用なし（Apple/Qualcomm の Direction A 軸） | **JSCM ベース CSI 圧縮**を AI ベース上に追加検討（Projection-matrix or encoder ベース） |
| **対応シナリオ** | UMa/InH 中心 | + Near-Field / SNS（Spatial Non-Stationary）/ CJT |

> **接続の仮説**: Rel-19 で確立される「pairing ID + payload pair」フレームは、6GR で **CSI-RS port 数が 4×〜16× にスケール**しても延伸可能か？　Apple Direction A の payload pair `{32,2}`〜`{192,2}` は port=128 に対応するが、port=512 を想定すると **payload pair の dimensionality 爆発**が起こる。**ここに進歩性余地**（§9 SEP 仮説 H-3 参照）。

### 3.3 関連 6GR 合意事項（10.5.3.1 から CSI 圧縮 inter-vendor 文脈で重要なもの）

| Agreement（出典 [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.7） | 解釈 |
|:---|:---|
| AI ベース CSI 圧縮の汎化・スケーラビリティ評価を **TR 38.843 の評価方法をスタートポイント**に行う | **Rel-19 の Direction A/B/C の延伸性を 6GR で評価する明示的な紐付け** |
| Channel Property Information (CPI) を新概念として導入 | 「pairing ID」とは別レイヤで NW-UE 間に **チャネル特徴の事前共有**を可能にする概念 |
| CJT 校正 CSI 報告の研究（複数 TRP の位相/遅延校正） | **D-MIMO 環境での pairing ID の複数化**問題を提起 |

---

## 4. RAN1#125（[要確認] 2026-05〜06 想定）

### 4.1 会合情報（公開二次情報のみ）

| 項目 | 内容 | confidence |
|:---|:---|:---|
| 日程 | **[要確認]** 2026-05〜06 期想定（公開ソース未確定） | low |
| 開催地 | **[要確認]**（ATIS Calgary 2026 は別会合の可能性） | low |
| FTP folder | `TSGR1_125`（実在のみ確認、内容未公開） | high |

> 出典: [[260430_RAN1-124-125-13トピック議論変遷]] §0.1、[3GPP meetings page](https://www.3gpp.org/dynareport?code=Meetings-R1.htm)（403 で本セッションでは取得失敗）。

### 4.2 #124bis から持ち越された open issue（#125 の見どころ）

| 領域 | 持ち越し論点 | down-select / agreement の見込み |
|:---|:---|:---|
| **9.1.1 量子化** | 性能監視の L1 vs L3 シグナリング | down-select 候補（Apple/Qualcomm/Samsung 三つ巴） |
| **9.1.1 PMI** | port=128 / rank=4 / subband=19 を超える拡張 | おそらく FFS 継続（6GR 接続待ち） |
| **9.1.2 Direction B/C** | encoder parameter 交換 / dataset 整列の API 仕様 | **#125 で初の具体合意の可能性大**（Apple FL #5〜#8 が見込まれる） |
| **9.1.2 RAN2/SA5 連携** | pairing ID の管理面（model storage / activation / fallback） | RAN2 LS 応答待ち |
| **9.1.2 RAN4 試験** | 標準テストデコーダ / 性能ベンチマーク条件 | **#125 で RAN4 LS 発射の可能性** |
| **10.5.3.1 6GR スケーラビリティ** | port=128 / 256 / 512 down-select | おそらく FFS、#126 持ち越し |
| **10.5.3.1 JSCM testability** | Samsung JSCM の RAN4 LS | 同上 |

### 4.3 想定される企業別主張（推測、confidence: low）

| 企業 | #125 で予想される主張 |
|:---|:---|
| **Apple** | Direction A の payload pair 完全合意 → Direction B/C への進入 |
| **Qualcomm** | 9.1.1 量子化詳細を Rel-20 normative に固める |
| **Samsung** | 9.1.2 で NW-sided / one-sided 派生（JSCM 系）を主張、6GR 10.5.3.1 で JSCM の testability を提起 |
| **Nokia** | 「separate training framework」（CENTRIC 由来）を Direction C の事例として補強 |
| **Huawei** | 中国陣として 6GR DL CSI を主導、Rel-19 では受身 |
| **MediaTek + CATT** | Rel-20 NR MIMO Phase 6（9.2）の implementation 制約を pairing 議論にも持ち込み |
| **Ericsson** | RAN2/SA5 LS の応答取りまとめ（pairing ID の管理面） |

> 出典補強: [Nokia CENTRIC blog (2023)](https://centric-sns.eu/2023/12/12/centric-separate-training-framework-for-aiml-based-csi-compression/) は Nokia の separate training framework を Type 3 collaboration として主張、これは Direction C の原型。

---

## 5. 議論変遷の要約（縦のタイムライン）

### 5.1 議論到達点（Rel-19 Case-0、#124bis 時点）

| 軸 | 合意済み（A） | 継続審議（FFS） | 主要対立軸 |
|:---|:---|:---|:---|
| **量子化** | SQ Q=2 {1/8,3/8,5/8,7/8} / Q=1 {1/4,3/4} | より高分解能の VQ 採用 | Qualcomm vs Samsung |
| **UCI 構造** | two-part、Part 1=CQI/RI/CRI、Part 2=PMI | レイヤ Group 分割の動的化 | Qualcomm 主導 |
| **PMI スコープ** | 128 port / rank≤4 / subband≤19 | 6GR への延伸 | 全社 |
| **Pairing ID** | 1:1 dataset 対応、独立 pair 併存可 | RAN2/SA5 管理面、RAN4 試験条件 | Apple 主導、Ericsson 折衝 |
| **Payload pair (Direction A)** | {32,2}〜{192,2} で down-select | Direction B/C の API 化 | Apple 主導 |
| **non-AI/ML 並列評価** | 義務化（#122〜#124 継承） | 比較ベースラインの統一性 | Type-II eType-II 主体 |
| **target CSI quantization** | Option 1a / 1b の二択 | 最終 down-select | NW vendor 内部論争 |

### 5.2 主要対立軸の整理

```
            UE 端末ベンダー                   NW インフラベンダー
            ─────────────────                ───────────────────
            Apple              ←9.1.2→       Ericsson + Nokia
            Qualcomm           ←9.1.1→       Samsung（NW + UE 両足）
            Samsung（端末）    ←JSCM→        Samsung（NW）  ※自社内競合

            MediaTek + Xiaomi  ←9.2 / 10.5→  Huawei + ZTE + CATT + vivo
            （台湾 + 中国端末）              （中国インフラ）
```

> **観察**: Samsung は **UE と NW の両側で 3GPP に顔を出す**ため、JSCM のような NW-sided 寄りの提案で**自社内対立**を含む。Apple は端末特化のため Direction A を強く推進。

### 5.3 次会合（#125）での見どころ（再掲、§4.2 から）

1. **Direction B/C の API 化**（Apple 主導の見込み）
2. **RAN4 LS 発射**による pairing ID 試験条件
3. **性能監視 L1 vs L3** の down-select
4. **6GR 10.5.3.1 port 数 down-select**（Rel-19 の延伸枠を決める前提）

---

## 6. Inter-vendor training collaboration の具体メカニズム — 焦点深堀

> 本ノートの最重要セクション。ユーザー指定焦点1。

### 6.1 標準化されたデータセット形式の合意状況（#124bis 時点）

| 項目 | 状態 | 詳細 |
|:---|:---|:---|
| **target CSI 表現** | down-select 中 | **Option 1a (real-imaginary) / 1b (amplitude-phase)** の二択（[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.2） |
| **データセットサイズ** | 未合意 | 各社が「typical 数十〜数百万サンプル」と主張（二次情報、[要確認]） |
| **チャネル分布** | 未合意 | TR 38.901 UMa/UMi/InH が出発点、6GR 拡張は 10.5.3.1 で議論 |
| **pairing ID の発行・管理** | 1:1 dataset 対応のみ合意 | 発行主体、有効期限、衝突処理は **RAN2/SA5 LS で継続審議** |
| **dataset 配布チャネル** | 未合意 | offline FTP / online API / OAM 経由 / SA5 管理 — 全て候補 |

### 6.2 Model exchange / pairing API の提案企業と対立軸

| 提案 | 提案企業（推定） | 対立企業 | コア論点 |
|:---|:---|:---|:---|
| **Direction A: 完全 reference model 共有** | Apple, Ericsson | Samsung（JSCM 派）, Huawei | UE 製造ベンダーの IP 保護 vs インフラベンダーの実装自由度 |
| **Direction B: encoder parameter + target CSI 交換** | Qualcomm, Nokia | Apple（過度な開示懸念） | encoder の中身（重み）をどこまで標準化するか |
| **Direction C: dataset 整列のみ** | Nokia (CENTRIC), Samsung (NW 側) | Qualcomm, Apple | NW 側でも UE 側でも完全独立学習を許す妥協案 |

> **対立軸の本質**: UE-side encoder の **重みを公開するか・しないか**。Direction A は重みを reference model として公開する代わりに UE は「fork して独自最適化」する余地を持つ。Direction B は重み交換の仕組みを定義するが、**両者間の信頼関係（NDA / SLA）を仕様外**に置く。Direction C は重み交換せず、共通データセットでの独立学習に賭ける。

### 6.3 共有 vs 個別学習の論点

| 観点 | 共有学習（joint training） | 個別学習（separate training） |
|:---|:---|:---|
| 性能 | 高（end-to-end 最適） | 中〜低（divergence あり） |
| IP 保護 | 困難（モデル同期に重み交換必要） | 容易（API のみ） |
| 運用 | model version 同期の負担大 | dataset 整合のみで OK |
| 3GPP の好み | TR 38.843 では Type 1（fully joint）として評価 | Type 3（fully separate）として評価 |
| #124bis 主流 | Direction A は joint training 寄り | Direction B/C は separate training 寄り |

> **既存実証**: [arXiv 2506.21796](https://arxiv.org/abs/2506.21796)（Nokia + Qualcomm 実機実証）は **Direction C（multi-vendor training）** に該当し、SGCS 0.815〜0.823、throughput 30〜100% 増を達成。**個別学習でも実用域に届く**ことを実機で示した点が重要（ただし 3GPP 寄書化の痕跡なし、[要確認]）。

---

## 7. non-AI/ML との並列評価義務 — 焦点深堀

> ユーザー指定焦点2。

### 7.1 並列評価の運用原則

- **WID 由来の義務**: NR_AIML_air_Ph2 WID（RAN#108、2025-06）で「AI/ML 提案は **non-AI/ML ベースライン**との並列評価が必須」と明記（[要確認] WID 番号 1060078、[3GPP Portal](https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1060078)）
- **#122〜#124 で再確認**: [[260430_RAN1-124-125-13トピック議論変遷]] §5.2

### 7.2 比較ベースラインの選定状況

| AI/ML 提案 | 並列評価ベースライン | 数値レンジ（既知） |
|:---|:---|:---|
| Direction A two-sided（Apple 系） | **Type-II eType-II codebook（Rel-16/17）** | overhead -8〜-79%、UPT 0〜+17%（複数社平均、二次情報） |
| Direction C separate（Nokia/CENTRIC） | Type-II eType-II + 任意の手作り encoder | SGCS 0.81〜0.82（[arXiv 2506.21796](https://arxiv.org/abs/2506.21796)） |
| 非 AI 代案（PCA） | Type-II eType-II | 「neural net と同等」を主張（[arXiv 2502.17459](https://arxiv.org/abs/2502.17459)、IIT Madras） |
| Samsung JSCM | Type-II + 通常 Two-sided | 「UE 複雑度 Type-II 比 2.9%」（Samsung 自社） |

### 7.3 性能ゲイン vs 複雑度のトレードオフ提示の運用

| 提示軸 | 9.1.1 / 9.1.2 で要求される報告 |
|:---|:---|
| **複雑度（FLOPs / M）** | 推論時の演算量。AI ベースは追加で **モデルパラメータ数 / M** を併記 |
| **性能（NMSE / SGCS）** | 中間 metric |
| **UPT（平均・5%tile）** | システム metric（10.5.3.1 と整合、[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.7） |
| **CSI 報告オーバーヘッド** | UCI bit 数 |
| **遅延** | encoder/decoder の serialization 含む実装遅延 |

> **#124bis での合意の特徴**: 6GR DL CSI（10.5.3.1）の評価枠組み（Sample & Hold をベースライン、観測窓/予測窓の数値例 5/10ms 等）が**Rel-19 Case-0 にも応用可能**な形で揃った。これにより 9.1.1 の non-AI 並列評価の「**ベースラインの数値統一**」が #125 以降に進む見込み。

---

## 8. 6GR 側の CSI スケーラビリティとの接続 — 焦点深堀

> ユーザー指定焦点3。詳細は §3 の表に集約済み。本節は SEP 観点でのリスク/機会を整理。

### 8.1 Rel-19 設計の延伸性評価

| Rel-19 設計要素 | 6GR (256〜512 port) で延伸可か？ | リスク |
|:---|:---|:---|
| Payload pair `{X, layer}`（X∈{32,…,192}） | **延伸困難**：port=512 だと {Y, layer} の Y の選び方で組合せ爆発 | 設計のやり直しが必要 |
| Pairing ID 1:1 dataset | 延伸可能だが dataset サイズが port²〜port³ で増大 | dataset 配布が現実的でない |
| Two-part UCI (Part 1=CQI/RI/CRI, Part 2=PMI) | 延伸可能（payload を増やせばよい） | UCI bit 数が暴発、Polar 復号負荷 |
| Direction A reference model | port=512 では reference model が肥大化 | **UE 計算負荷が爆発、Apple 戦略に逆風** |
| Direction C separate training | 個別 dataset で対応可能 | NW-UE 性能 divergence が拡大 |
| **Samsung JSCM** | スケーラブル（行列演算ベース） | **inter-vendor pairing 問題の構造変更が必要** |
| **CPI（Channel Property Information）** | 新概念、6GR 設計と同期可能 | 仕様化スコープが未確定 |

### 8.2 Samsung JSCM の差別化軸（再整理）

- **5G Rel-19 では「avoid」**：JSCM は 9.1.1 の Case-0 ではなく 6GR 10.5.3.1 で本格議論
- **NW-sided model に重心**：UE 側は固定変換のみ → **inter-vendor pairing 問題を構造的に回避**
- **連続値で動作**：Type-II の量子化 vs Two-sided AI の SQ {1/8,…} の対立から離脱
- **6GR の port=256〜512 想定**で「JSCM ベース CSI 圧縮を AI ベース上に追加検討」が #124bis で合意（[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.7）

> **戦略含意**: Samsung は Apple/Qualcomm の**Rel-19 Direction A 軸を尊重しつつ、6GR で別軸を立てる**ダブルトラック。Rel-19 の SEP は Apple/Qualcomm が押さえても、**6GR の SEP は Samsung が JSCM で取りに行く**可能性。

---

## 9. SEP 仮説 — Inter-vendor pairing 周辺の進歩性候補

> 本セクションはユーザー指定の主要出力。**法的助言ではなく**、調査・考察の範囲での進歩性候補。クレーム起草は別途。

### H-1. Pairing ID と dataset の 1:M / M:N マッピング機構

- **背景**: #124bis で「pairing ID と dataset は 1:1」と合意されたが、UE が複数 NW（serving + neighbor）と pair する MR-DC / dual-connectivity / handover 時に**1 ID では足りない**
- **進歩性余地**: pairing ID を**スコープ付き（cell / TRP / NW vendor 別）**に拡張する DCI/RRC シグナリングと UE 動作（active set 管理）
- **根拠**: [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.3 + §4.7（CJT 校正 CSI 報告の研究 → 複数 TRP の pairing ID）
- **回避困難性**: pairing ID は WID 必須項目、normative 化された場合 essential 化しやすい
- **confidence**: medium（#125 で Apple/Ericsson から類似提案が予想される）

### H-2. Direction B における encoder parameter 差分エンコード

- **背景**: Direction B（encoder parameter 交換）は API 仕様未合意。**重み全体の交換**は 100MB 級で現実的でない
- **進歩性余地**: **base model + delta encoding**（reference model からの差分のみ送信）、量子化・スパース化と組み合わせた効率的 parameter 配信プロトコル
- **根拠**: arxiv:2502.17459 の PCA「transformation matrix を毎回送る」発想を AI モデルに転用、TR 38.843 の Type 3 派生
- **回避困難性**: Direction B が normative 化されれば配信プロトコルは仕様階層 0 に来る
- **confidence**: medium

### H-3. Layer / Port スケーラブル payload pair 構造

- **背景**: #124bis 合意の payload pair `{32,2}〜{192,2}` は port=128 想定。6GR で port=256/512 になると組合せ爆発
- **進歩性余地**: **基底（basis）×係数構造**で payload を分解し、port 数増加に対し log スケールで増えるよう設計
- **根拠**: [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.7（W₁W₂Wf の 3 段構成研究）と組合せ可能
- **回避困難性**: payload 構造は UCI bit ordering と直結、normative 必須
- **confidence**: medium-high（6GR の port down-select で必然的に必要）

### H-4. Channel Property Information (CPI) を pairing trigger とする動的切替

- **背景**: 6GR で導入される CPI（[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.7）は「scheduling/RS 設定/event-trigger 用」と定義されたが、**pairing ID 切替の trigger** 用途は未定義
- **進歩性余地**: チャネル特性（Doppler, delay spread, near-field flag）に応じて**動的に pairing ID を切り替える**条件と DCI/MAC-CE シグナリング
- **根拠**: CPI は新概念、6GR で normative 化される見込み、Rel-19 への back-port も可能
- **回避困難性**: CPI 自体が新領域、SEP の宝庫
- **confidence**: medium（define-then-patent の好例）

### H-5. Non-AI baseline（Type-II eType-II）と AI Direction A/B/C の **runtime fallback 制御**

- **背景**: WID で non-AI 並列評価が義務、性能監視で L1/L3 シグナリング検討中
- **進歩性余地**: AI モデル inference 失敗時（モデル divergence、cliff effect）に ****eType-II にロールバックする UE 動作と NW 指示**。fallback 判定基準（NMSE 閾値、CRC failure rate）の標準化
- **根拠**: [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] §4.2（性能監視 Option 1/2）、Rel-19 maint 8.1 の RS-PAI 救済（R1-2603378）
- **回避困難性**: fallback はロバスト性必須、normative になりやすい
- **confidence**: high（Apple/Qualcomm 双方が利害を持つ領域）

### SEP 仮説まとめ表

| ID | テーマ | 主要回避困難性 | 競合提案企業（推定） | confidence |
|:---|:---|:---|:---|:---|
| H-1 | Multi-pairing-ID active-set 管理 | normative（CJT 必須） | Apple, Ericsson | medium |
| H-2 | Direction B 差分 encoder 配信 | API 階層 0 | Qualcomm, Nokia | medium |
| H-3 | Scalable payload pair 構造 | UCI 必須 | Qualcomm, MediaTek, Samsung | medium-high |
| H-4 | CPI を pairing trigger に拡張 | 新概念 | Samsung, Huawei | medium |
| H-5 | AI ↔ Type-II fallback 制御 | ロバスト性必須 | Apple, Qualcomm | high |

---

## 10. 未取得資料 — 取得すべき Tdoc 番号・URL

> 取得は別タスクで実行（[`framework/3gpp-ftp-cookbook.md`](../framework/3gpp-ftp-cookbook.md) §2.2 参照）。本セッションでは URL のみ列挙。

### 10.1 RAN1#124（Gothenburg、2026-02）

| 用途 | URL |
|:---|:---|
| 会合 root | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/` |
| Agenda CSV | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Agenda/agenda.csv` |
| Tdoc list（最終日） | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Tdoc_list/`（ファイル名は `TDoc_List_Meeting_RAN1#124 (260213).xlsx` 等を試行） |
| Chair Notes 最終 | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/`（`_eom*.docx` を確認） |
| FL Summary 9.1.1 (Qualcomm 起草) | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/drafts/9.1.1*/` 配下 |
| FL Summary 9.1.2 (Apple 起草) | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/drafts/9.1.2*/` 配下 |

### 10.2 RAN1#124bis（Malta、2026-04）— Tdoc レベル

> Chair Notes は既存ノート [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] で参照済み。個別 Tdoc 84 件（9.1.1: 43, 9.1.2: 41）は未取得。

| 用途 | URL |
|:---|:---|
| 9.1.1 全 Tdoc | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/`（Tdoc_list xlsx の "Agenda item" = 9.1.1 でフィルタ） |
| 9.1.2 全 Tdoc | 同上（Agenda item = 9.1.2） |
| Apple FL summary #1〜#4 | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/drafts/9.1.2*/` 配下 |
| Qualcomm FL summary #1〜#4 | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/drafts/9.1.1*/` 配下 |
| RAN2 LS R1-2601756 | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2601756.zip` |

### 10.3 RAN1#125（[要確認] 2026-05〜06）

| 用途 | URL |
|:---|:---|
| 会合 root | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/` |
| Agenda CSV（公開され次第） | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Agenda/agenda.csv` |
| Chair Notes（会期終了後） | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/` |
| Tdoc list（会期内更新） | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Tdoc_list/` |

### 10.4 関連 WI 情報

| 用途 | URL | 注 |
|:---|:---|:---|
| WI 1060078 (FS_NR_AIML_air_Ph2) | `https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1060078` | curl `-A "Mozilla/5.0"` 必要 |
| AI/ML for NR Air Interface | `https://www.3gpp.org/technologies/ai-ml-nr` | rapporteur Juan Montojo |
| TR 38.843 toc | `https://www.tech-invite.com/3m38/toc/tinv-3gpp-38-843_b.html` | Type 1/2/3 collaboration の出典 |

### 10.5 Samsung JSCM 関連寄書（[要確認]）

| Tdoc 番号（既存ノートから） | 推定対応会合 | URL（推定） |
|:---|:---|:---|
| `R1-2400723` | RAN1#118bis 〜 #119 想定 | 該当 TSGR1_<n>/Docs/ で fetch |
| `R1-2505588` | RAN1#121 〜 #122 想定 | 同上 |
| `R1-2509516` | RAN1#123 〜 #124 想定 | 同上 |

> Tdoc 番号の桁数（5 桁）から RAN1 内番号、年表記なし。**会合特定には RAN1 portal の Tdoc DB 検索が必要**（curl ベース）。

### 10.6 取得手順（再掲）

```bash
# RAN1#124 Chair Notes 一覧確認
curl -s -A "Mozilla/5.0" \
  "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/" \
  | grep -oE 'Chair[^"]+\.docx'

# Apple FL summary #1〜#4 (9.1.2) を取得
curl -A "Mozilla/5.0" -O \
  "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/drafts/9.1.2*/...FL%20Summary%23N...docx"

# pandoc で Markdown 化
pandoc -f docx -t markdown_strict \
  "Chair notes RAN1#124_eomX.docx" \
  -o references/Chair-Notes-RAN1-124.md
```

---

## 11. 既存リポジトリへの統合（catalog 拡張提案）

### 11.1 `framework/catalog/agenda-items.yaml` への追加 alias

```yaml
ai_nr_aiml_csi_compression_r19:
  aliases:
    # 既存に追加
    - "Case-0"
    - "Case 0 CSI"
    - "9.1.1 CSI compression"
    - "9.1.2 inter-vendor"  # 9.1.2 を別 entry にすべきかは要検討
    - "inter-vendor pairing"
    - "Direction A"
    - "Direction B"
    - "Direction C"
    - "pairing ID"
    - "two-part UCI CSI"
    - "payload pair"
```

### 11.2 別エントリ化の提案

> **提案**: 9.1.2 (Inter-vendor training collaboration) を **`ai_nr_aiml_inter_vendor_r19`** として別エントリ化する。理由:
> - 9.1.1 (Case-0 圧縮本体) と 9.1.2 (pairing メカニズム) は **FL が別企業（Qualcomm vs Apple）**
> - SEP 戦略上も論点が独立
> - #125 以降の議論で **Direction A/B/C の API 化が独自進路**を取る見込み

```yaml
ai_nr_aiml_inter_vendor_r19:
  title: "NR AI/ML Inter-vendor training collaboration (Rel-19/20 9.1.2)"
  parent_wi: "NR_AIML_air_Ph2"
  parent_ai: "ai_nr_aiml_csi_compression_r19"  # 上位は CSI 圧縮
  current_phase: "WI (specification)"
  aliases:
    - "9.1.2"
    - "Inter-vendor training"
    - "Inter-vendor pairing"
    - "model exchange"
    - "Direction A"
    - "Direction B"
    - "Direction C"
    - "pairing ID"
  description: |
    UE-side encoder と gNB-side decoder の two-sided AI モデル間で、
    モデル中身を秘匿しつつ標準連携可能にするフレーム。Apple FL（Rel-20）。
```

### 11.3 `framework/catalog/meetings.yaml` の更新提案

```yaml
"RAN1#124":
  ai_map:
    ai_nr_aiml_csi_compression_r19: "9.1.1"  # [推定、要確認]
    ai_nr_aiml_inter_vendor_r19: "9.1.2"     # [推定、要確認]

"RAN1#124bis":
  ai_map:
    ai_nr_aiml_csi_compression_r19: "9.1.1"  # [確認済み、本ノート §2]
    ai_nr_aiml_inter_vendor_r19: "9.1.2"     # [確認済み、本ノート §2]
```

---

## 12. Next Steps

- [ ] `references/Chair-Notes-RAN1-124.md` を作成（§10.1 の URL から curl + pandoc）— 現状 #124 は二次情報のみ
- [ ] `references/Chair-Notes-RAN1-124bis.md` を作成（個別ノートで参照済みだが references/ への正式配置）
- [ ] Apple FL summary 9.1.2 #1〜#4（#124bis）を取得・Markdown 化し、Direction A/B/C の**Apple 自身の説明文**を確認
- [ ] Qualcomm FL summary 9.1.1 #1〜#4（#124bis）を取得し、量子化の対立点を抽出
- [ ] Samsung 寄書 `R1-2400723` / `R1-2505588` / `R1-2509516` の会合特定（RAN1 Tdoc DB 検索）
- [ ] arXiv 2506.21796（Nokia + Qualcomm 実機実証）の本文を read、Direction C の実装詳細を [`references/arXiv-2506.21796.md`](../references/arXiv-2506.21796.md) として保存
- [ ] arXiv 2502.17459（IIT Madras PCA）の本文 read、Type-II 比較の数値があれば抽出
- [ ] RAN1#125 の日程・場所が公開され次第、`framework/catalog/meetings.yaml` を更新
- [ ] `framework/catalog/agenda-items.yaml` に §11 の alias 追加と新エントリ `ai_nr_aiml_inter_vendor_r19` 検討
- [ ] **#125 終了後（2026-06〜07 想定）に本ノートを `--from RAN1#125 --to RAN1#126` で増分更新**

---

## 13. 用語解説（本ノート固有）

| 用語 | 定義 |
|:---|:---|
| **Case-0** | Two-sided AI/ML CSI 圧縮の基本ケース。**現スロットのみの空間-周波数領域 CSI**（時間方向の予測なし）を UE-side encoder で圧縮、gNB-side decoder で復元 |
| **Direction A / I** | Reference model 共有方式。完全標準化された encoder/decoder と parameters を提供（Apple 主導） |
| **Direction B** | Encoder parameter + target CSI 交換方式（Qualcomm/Nokia 系） |
| **Direction C** | Dataset 整列のみ方式（Nokia CENTRIC 系） |
| **Pairing ID** | UE-side encoder と gNB-side decoder の組合せを識別する ID。1:1 dataset 対応で独立 pair が併存可能 |
| **Payload pair** | precoding matrix feedback の {bits, layers} ペア。例: {32,2}, {64,2}, {96,2}, {128,2}, {192,2}, {32,1} |
| **JSCM** | Joint Source-Channel Modulation（Samsung 提案）。源符号化・チャネル符号化・変調を joint 最適化 |
| **JSCC** | Joint Source-Channel Coding（JSCM の前段、量子化なしの圧縮） |
| **Two-part UCI** | Part 1 = CQI/RI/CRI、Part 2 = PMI（全レイヤ）の二部構成 UCI |
| **CPI** | Channel Property Information。6GR で導入される新概念で、RS 設定支援 / scheduling 連携 / event-triggered CSI / CSI 予測支援に使うチャネル特徴情報 |
| **Cliff effect** | AI 圧縮で SNR / 圧縮率が閾値を下回ると性能が崖のように落ちる現象。JSCM が「graceful degradation」で対処を主張 |
