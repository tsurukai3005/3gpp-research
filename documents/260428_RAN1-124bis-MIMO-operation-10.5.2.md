---
title: "RAN1#124bis (Malta, 2026-04-13〜04-17) — 6GR MIMO Operation (10.5.2) 詳細調査"
status: draft
confidence: high
created: 2026-04-28
updated: 2026-04-28
axes:
  technology-layer: [phy-mimo, phy-pdcch, phy-pusch, cross-layer]
  generation: [rel-20-6g]
  value: [throughput, latency, energy-efficiency, spectral-efficiency]
  market: [consumer-xr, b2b-industrial, fwa, hst]
  adoption-factors: [standard-convergence, backward-compat, economies-of-scale]
  ip: [novelty, inventive-step, spec-mapping]
sources:
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom4.docx
    title: "Chair notes RAN1#124bis_eom4.docx — End-of-Meeting (final)"
    accessed: 2026-04-28
  - url: https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Agenda/agenda.csv
    title: "RAN1#124-bis Agenda CSV"
    accessed: 2026-04-28
up: "[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]"
related:
  - "[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]"
  - "[[260420_NRフレーム構造とリソースブロックの進化まとめ]]"
  - "[[260424_Rel-15-物理リソース仕様策定の議論変遷]]"
references: []
---

# RAN1#124bis — 6GR MIMO Operation（アジェンダ 10.5.2）詳細調査

> 本ノートは [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] の補足として、**6GR Multi-antenna System の MIMO Operation（AI 10.5.2）** を詳細化する。  
> 上位ノートでは 10.5.2.4（Beam Management）を扱ったが、**10.5.2.1（DL 制御チャネル）・10.5.2.2（DL 共有チャネル）・10.5.2.3（UL チャネル）** の分析が欠落していたため本ノートで補完する。

---

## 1. 定義と背景（Why）

### 1.1 10.5.2 MIMO Operation とは

3GPP の 6G Radio（6GR）Study Item における **AI 10.5.2「MIMO Operation」** は、
「データチャネル・制御チャネルをどのように送受信するか」という**物理層伝送方式の中核**を扱うアジェンダ群。

| サブ AI | タイトル | 対象チャネル |
|:---|:---|:---|
| **10.5.2.1** | Downlink transmission scheme(s) for downlink control channels | 6G PDCCH（制御情報の受け渡し） |
| **10.5.2.2** | Downlink transmission scheme(s) for downlink shared channels | 6G PDSCH（データ送信） |
| **10.5.2.3** | Uplink transmission scheme(s) for uplink channels | 6G PUSCH / PUCCH（UL データ + フィードバック） |
| **10.5.2.4** | Beam management for downlink and uplink | ビーム管理（別ノート参照） |

> **5G NR との継承と変革**: 5G NR では TS 38.211（物理チャネル）と TS 38.214（Layer 1 手順）で対応機能が規定される。6G ではこれらを **White-paper から書き直す形** で re-define する。会議のノート（AI 10.5.2 の Note 2）には「PDCCH の「どこ・どのように送るか」は 10.5.2.1、「何を送るか」は 10.5.4.1（スケジューリング）で扱う」と明記されており、機能が適切に分担されている。

### 1.2 なぜ今回（#124bis）が重要か

- RAN1#122（2025-08）では MIMO operation はまだ「将来の議題」として延期されていた
- RAN1#123（2025-11）〜 RAN1#124（2026-02）で EVM（Evaluation Model）の基礎を合意
- **本会合（#124bis）で伝送方式設計の詳細が初めて本格的に議論された最初の会議**
- 各サブアイテムで FL summary が複数ラウンド出たことが「設計議論の初深掘り」であることを示す

---

## 2. アジェンダ構造と Tdoc 件数

> 上位ノート [[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]] の Tdoc 件数表を補完。

| AI | タイトル | 件数（推計） | FL/Moderator |
|:---|:---|---:|:---|
| **10.5.0** | General aspects and frameworks | ~55 | **Huawei + Xiaomi**（Xinghua+Yanping） |
| **10.5.2.1** | DL 制御チャネル | ~40 | **Nokia (Dimitri)** |
| **10.5.2.2** | DL 共有チャネル | **55** | **Ericsson (Sven) + Google (Yushu)** |
| **10.5.2.3** | UL チャネル | ~35 | **NTT DOCOMO (Naoya) + Samsung (Youngrok)** |
| 10.5.2.4 | Beam management | 44 | ZTE (Bo) + Apple (Hong)（別ノート） |

### 2.1 FL Summary ラウンド数（= 議論の深度）

| AI | FL Summary 件数 | 備考 |
|:---|:---:|:---|
| 10.5.2.1 | **#1〜#3**（Nokia 単独） | PDCCH 構造の基礎を 3 ラウンドで確立 |
| 10.5.2.2 | **#1〜#5**（Ericsson + Google 共同） | PDSCH は最多 5 ラウンド = 本会合最大の論点の一つ |
| 10.5.2.3 | **#1〜#4**（NTT DOCOMO + Samsung 共同） | UL も 4 ラウンド。日韓共同 FL は珍しい組合せ |

---

## 3. 寄書企業と勢力図

### 3.1 10.5.2.1 — DL 制御チャネル（Nokia FL）

- **Nokia 単独 FL**：5G NR で Nokia が PDCCH 最適化の中心的提案者であった流れを継承
- 主要提出企業：Spreadtrum/UNISOC, TCL, Huawei/HiSilicon, vivo, CMCC, NEC, Samsung, China Telecom, Sony, Lenovo, OPPO, MediaTek, InterDigital, CATT/CICTCI, LG, Xiaomi, **Apple**, 1Finity, Rakuten Mobile, Panasonic, HONOR, ZTE/Sanechips, ETRI, ASUSTeK, Sharp, Google, Ericsson, Ofinno, **Qualcomm**, NTT DOCOMO, CSCN
- **オペレータ連合**：Bouygues Telecom + Vodafone + Orange + Telecom Italia + British Telecom + Deutsche Telekom + AT&T が共同提出（MRSS 観点）
- **観察**：制御チャネル設計は実装複雑度に直結するため、欧州ベンダ（Nokia, Ericsson）と大学系ではなく実装経験豊富な企業が中心

### 3.2 10.5.2.2 — DL 共有チャネル（Ericsson + Google FL）

- **Ericsson + Google の組み合わせ**：PDSCH は「ネットワーク（Ericsson）×端末/AI（Google）」という視点の融合
- 主要提出企業：FUTUREWEI, Spreadtrum/UNISOC, Nokia, ZTE/Beijing Digital Nebula/Sanechips, Huawei/HiSilicon, MediaTek, vivo, Ericsson, Tejas Networks, CMCC, NEC, LG Electronics, Lenovo, Samsung, Qualcomm, NTT DOCOMO, Ofinno ほか
- **新興：Tejas Networks Limited**（インド）が PDSCH 設計で積極的に寄書
- **AI/ML DMRS**: Google が推進する側面がある（AI/ML 受信機によるオーバーヘッド削減）

### 3.3 10.5.2.3 — UL チャネル（NTT DOCOMO + Samsung FL）

- **日韓共同 FL**：UL 送信方式は「UE 実装（Samsung）×ネットワーク最適化（NTT DOCOMO）」
- 主要提出企業：FUTUREWEI, ZTE/Sanechips, Samsung, Fainity Innovation（新興）, NEC, LG, Lenovo, Sharp, Sony, CATT/CICTCI, Panasonic, Apple, Ericsson, ETRI, NVIDIA, Ofinno, Qualcomm, NTT DOCOMO, Transsion Holdings, KDDI
- **NVIDIA が参加**：AI/ML 受信機と PUSCH DMRS 削減は NVIDIA の GPU 最適化アーキテクチャと親和性が高い
- **CPE（Customer Premises Equipment）**: FWA（固定無線アクセス）向け CPE 設計が独立の合意項目として議論されている

---

## 4. 議論内容と合意（Chair Notes eom4 から抽出）

### 4.1 10.5.2.1 — 6G PDCCH 伝送方式

> PDCCH（Physical Downlink Control Channel）は、スケジューリング情報・ MCS・RV・HARQ 番号などを UE に通知する制御チャネル。5G NR の CORESET / Search Space 設計をベースに 6G 向けに再定義。

#### 4.1.1 構造的合意

| Agreement | 内容 |
|:---|:---|
| **CORESET 定義** | 6GR 専用 CORESET を新規定義。最低限「時間・周波数リソース長さ」を定義 |
| **Search Space (SS) 定義** | 6GR 専用 SS Set を新規定義。UE がモニタすべき PDCCH 候補群を定義 |
| **REG 構造** | REG = 複数 RE / 1 OFDM シンボル。周波数方向の RE 割当は **FFS** |
| **CCE 構造** | CCE = REG の集合。REG/CCE 比、REG インデキシングは **FFS** |
| **PDCCH 候補** | 1 PDCCH 候補 = AL 個の CCE（AL = Aggregation Level）。繰り返しなし時は AL 個固定 |
| **REG バンドル** | Working Assumption（旧 RAN1#124 継続）: REG バンドル = REG の集合 |

#### 4.1.2 設計パラメータの合意

| Agreement | 内容 |
|:---|:---|
| **CCE-to-REG mapping** | 非インタリーブド（non-interleaved）とインタリーブド（interleaved）の**両方を研究** |
| **変調** | 最低 QPSK を使用。QPSK 以外の変調の必要性・実現可能性は **FFS** |
| **Aggregation Level (AL)** | 1, 2, 4, 8, 16 をベースラインとして研究。AL=32 の必要性・use-case も研究 |
| **PDCCH 繰り返し** | イントラスロット繰り返しとインタースロット繰り返しの必要性・use-case を研究 |
| **CORESET 持続時間** | 1, 2, 3 シンボルをベースライン。3 シンボル超の必要性・実現可能性も研究 |
| **CORESET 周波数割当** | 連続・非連続の両方を研究 |
| **CRC スクランブル** | RNTI によるスクランブルを研究 |
| **ペイロードスクランブル** | 変調前のビットレベルスクランブルを研究 |
| **Common SS / UE-specific SS** | CSS と USS の両方を定義。各 SS は最低 1 CORESET に紐付け |
| **Hash 関数** | 6G PDCCH 候補の CCE インデックスを決定するための Hash 関数を定義（設計は FFS） |
| **DMRS** | 少なくとも RE マッピング・系列生成・初期化の設計を研究 |
| **モニタリング** | スロット単位モニタリング（最小周期 1 スロット）を支援。非スロット単位は研究 |
| **送信ダイバーシティ** | 単一ポート DMRS ベースをベースライン。Non-transparent 方式の必要性と precoder 粒度を研究 |

#### 4.1.3 重要な Conclusion

| Conclusion | 内容 |
|:---|:---|
| **5G と 6G の CORESET は独立** | 「6GR UE は 6G ネットワーク内で 6GR CORESET のみを設定される」（RAT-specific 分離） |
| **MRSS（Multi-Radio Spectrum Sharing）** | 5G と 6G の PDCCH で時間-周波数リソースを動的共用または半静的割当するしくみを研究。**NW 観点のみ、UE に透明** |

---

### 4.2 10.5.2.2 — 6G PDSCH 伝送方式

> PDSCH（Physical Downlink Shared Channel）はダウンリンクのデータ本体。5G NR との最大の差分は「超広帯域（400 MHz）」「マルチ TRP」「AI/ML 受信機」という 3 軸。

#### 4.2.1 基本構造

| Agreement | 内容 |
|:---|:---|
| **FDRA（周波数割当）** | Type 0（ビットマップ）と Type 1（RIV ベース）の両方をサポート。動的切替もサポート。>275 PRB 対応の粒度は研究 |
| **TDRA（時間割当）** | 単一マッピングタイプ（スロット内）。開始シンボルの柔軟性あり。シンボル数・DMRS 位置・スロット境界越え PDSCH・PDSCH 繰り返しを研究 |
| **PT-RS** | FR2 では少なくとも PT-RS をサポート。FR1 / 7 GHz 帯での必要性を研究。設計は統一方針 |
| **位相雑音モデル** | TR38.803 の位相雑音モデルを採用（RAN4 に LS を送り更新確認） |

#### 4.2.2 DMRS 設計

| Agreement | 内容 |
|:---|:---|
| **MU-MIMO DMRS** | 共スケジューリング UE 向けに以下を研究: CDM グループ/ポート/密度/パターン/シンボル、NW 指示 OCC デスプレッド支援、DMRS 系列・変調次数・QCL/TCI 情報・PRG 割当のネットワーク指示 or UE 仮定 |
| **DMRS 系列設計** | PAPR・シーケンス間干渉・スクランブル ID 指示を研究 |
| **DMRS OCC 候補** | FD-OCC: {2, 3, 4, 6, 8, 12, 16, 24, x}、TD-OCC: {1, 2, 4, x}、CDM グループ数: {2, 3, 4, 6, 8, 12, x} |
| **CDM 構造** | Comb ベースまたはブロックベースを研究 |

> **5G NR との比較**: NR の最大 FD-OCC は 4、TD-OCC は 2、CDM グループ数は最大 8。6G ではそれぞれ大幅に拡張（FD-OCC 最大 24、CDM グループ 12）を検討。DMRS 設計の自由度が知財余地の一つ。

#### 4.2.3 AI/ML DMRS オーバーヘッド削減（新規）

| Agreement | 内容 |
|:---|:---|
| **AI/ML 受信機用 LLS EVM** | AI/ML ベース受信機による PDSCH DMRS オーバーヘッド削減を LLS で研究 |
| **性能 KPI** | 最終 KPI: BLER/SE/スループット |
| **複雑度 KPI** | **FLOPs とパラメータ数**（= 6G における AI モデル評価の標準軸） |

#### 4.2.4 コードワード・レイヤマッピング

| Agreement | 内容 |
|:---|:---|
| **CW-to-layer mapping 研究** | 各 rank でのコードワード数、最大コードワード数、コードワード当たりの最大 rank、レイヤ当たりの変調次数を研究 |
| **ベースライン** | NR 空間方向優先・周波数方向次・時間方向の映射（Spatial→Freq→Time）と NR CW-to-layer 映射をベースラインに評価 |
| **TB/CW マッピング研究** | 1 つ以上のトランスポートブロック（TB）を時間/周波数リソースにマップする方法とその CW-to-layer への影響を研究 |

#### 4.2.5 評価モデル（SLS / LLS EVM）— 非 HST

| パラメータ | 値 |
|:---|:---|
| キャリア周波数 | 0.7 GHz（FDD）、2 GHz（FDD）、4 GHz（TDD）、7 GHz（TDD）、30 GHz（TDD） |
| SCS | 15 kHz（FDD）、30 kHz（TDD, 2–7 GHz）、120 kHz（TDD, 30 GHz） |
| BS アンテナ（4 GHz 例） | 4 TXRUs/32 AEs〜64 TXRUs/192 AEs |
| BS アンテナ（30 GHz 例） | 4 TXRUs/1024 AEs〜16 TXRUs/2048 AEs |
| Multi-TRP シナリオ | Scenario 1（イントラセル 4 TRP）/ Scenario 2（イントラサイト 3 TRP）/ Scenario 3（N TRP）|
| MIMO スキーム | 各社報告 |
| 受信機 | MMSE-IRC（ベースライン）、R-ML（オプション） |

#### 4.2.6 評価モデル（SLS EVM）— HST シナリオ（追加合意）

| パラメータ | 値 |
|:---|:---|
| キャリア周波数 | 4 GHz / 7 GHz / 30 GHz（TDD） |
| UE 速度 | Rural macro: 350 km/h, 500 km/h（5G NR の最大 500 km/h と同等だが **複数 TRP 協調が追加**） |
| Multi-TRP 協調 TRP 数 | **最大 2, 4, 8, または 16**（5G NR では最大 2 TRP が主流） |
| UE 数 | 300 UE（1000 名の乗客 × 30% アクティビティ率） |

---

### 4.3 10.5.2.3 — 6G PUSCH / UL 伝送方式

> UL 送信は PUSCH（Physical Uplink Shared Channel）中心。6G では **AI/ML 受信機**、**FWA（CPE）向け設計**、**コードブック設計の柔軟化** が 5G NR との主要差分。

#### 4.3.1 基本構造

| Agreement | 内容 |
|:---|:---|
| **UE アンテナポート数** | {1, 2, 3, 4, 8}。その他は FFS |
| **SU-MIMO 最大レイヤ数** | CP-OFDM の場合、UE アンテナポート数と同じ（最大 8 レイヤ） |
| **FDRA** | 物理的に連続した割当を 1 物理キャリア内でサポート。粒度/単位を研究。非連続は FFS |
| **TDRA** | 柔軟な開始シンボル、シンボル数（1 シンボル粒度）、スケジューリング PDCCH からの時間オフセットを研究 |

> **5G NR との比較**: NR では 4 アンテナポート（実装上 2 panel の場合最大 8）だが、6G では 8 ポートを明示的に候補に含む。SU-MIMO 最大レイヤ数が 8 まで拡張されることで、高容量シナリオでのスループット向上が期待される。

#### 4.3.2 コードブックベース PUSCH（重要な設計議論）

| Agreement | 内容 |
|:---|:---|
| **コードブックベース PUSCH をサポート** | UL コードブックから UE がプリコーダを選択し、NW スケジューリングベースで送信 |
| **SRS ベースライン** | UL CSI 取得には SRS をベースラインとして使用（他の RS/方法は FFS） |
| **コードブック設計の研究軸** | 固定コードブック（仕様プリ定義）/ 設定可能コードブック（NW 設定）/ ハイブリッド方式。5G NR との性能・分解能・オーバーヘッド・コードブックサイズを比較。UE コヒーレンシ能力と Tx アンテナ構造の多様性を考慮 |

> **知財余地**: 5G NR では固定コードブック（Type 1/2）のみ。**6G では「NW が UE 向けにカスタマイズするコードブック」**（Configurable / Hybrid）が候補に入った。この設計空間は 5G にはなかった新規領域。

#### 4.3.3 AI/ML ベース PUSCH DMRS オーバーヘッド削減（新規）

| Agreement | 内容 |
|:---|:---|
| **LLS 評価テンプレート** | RAN1#125 でパラメータ値を収集するための以下のテンプレートを使用: |
| — 受信機仮定 (#1) | — |
| — モデル入力 (#2) | 次元含む |
| — モデル出力 (#3) | 次元含む |
| — ラベル (#4) | ラベリングエラーモデルはオプション報告 |
| — 訓練タイプ (#5) | — |
| — MIMO レイヤ数 (#6) | — |
| — **FLOPs 数 (#7)** | RB/スロット/レイヤ当たりのオプション報告 |
| — **AI モデルパラメータ数 (#8)** | — |
| — ベンチマーク (#9) | 非 AI 受信機（リアルな仮定） |
| — 汎化・スケーラビリティ性能 (#10) | — |

#### 4.3.4 CPE（固定無線アクセス）向け設計

| Agreement | 内容 |
|:---|:---|
| **CPE 事前選択基準** | Approach 0（ランダム indoor/outdoor 選択、ベースライン）/ Approach 1（品質基準による事前選択）/ Approach 2（最悪パフォーマンス世帯の室外 CPE 割当：最大 20%）|
| **CPE アンテナ設定** | AI 10.1（一般的枠組み）の合意に準拠 |
| **HST シナリオ** | PUSCH も HST（350/500 km/h）+ Multi-TRP（2/4/8/16 TRP）を SLS で評価 |

---

### 4.4 10.5.0 — General Aspects and Frameworks（補足）

> 上位ノートでは 55 Tdoc と記録されているが分析なし。本会合で合意された主要項目を整理する。

| Agreement | 内容 |
|:---|:---|
| **カバレッジギャップ計算** | 7 GHz 帯で 5G 中帯域（~3.5 GHz）サイトグリッドを再利用する際のカバレッジギャップ = MPL1 – MPL2 – PL_diff |
| **リンクバジェット整合** | 共通ビームのアンテナゲイン補正係数の共通理解を合意（BS DL/UL 共通ビーム利得が変わらない条件を明確化） |
| **評価対象信号** | DL: NR PSS/SSS, SSB, Common PDCCH, SIB1 PDSCH, Msg2/4 PDSCH / UL: PRACH formats, MSG3/5 PUSCH, MSG4 PUCCH Format 1 |
| **動的 TDD リンク方向** | Option 1（半静的 TDD + 柔軟シンボル）/ Option 2（動的 TDD パターン指示 + ガードシンボル）/ Option 3（ガードシンボルのみ + 動的パターン指示）を研究 |
| **最大 UE 帯域幅の削減** | eRedCap SI 結果に基づく複雑度削減分析（Alt 2 ≈ 10% 削減、Alt 3 ≈ 7-8% 削減） |
| **TB マッピング** | 200–400 MHz 幅での TB/CB/CBG 映射: Option A（TB が 400 MHz まで）vs Option B（TB が 200 MHz まで）FFS |

---

## 5. 前世代との差分

| 機能 | 5G NR（Rel-15〜19） | 6G（Rel-20 SI での議論） | 変化の意味 |
|:---|:---|:---|:---|
| **PDCCH: CORESET 分離** | 単一 RAT（NR のみ） | **RAT-specific 独立**（5G CORESET と 6G CORESET は独立） | MRSS（マルチ RAT 共存）のための設計転換 |
| **PDCCH: Aggregation Level** | 最大 AL=16 | AL=16 まで + **AL=32 を研究** | 大規模アンテナ・カバレッジ拡大に対応 |
| **PDCCH: 繰り返し** | スロット内繰り返しのみ（Rel-16 で一部） | **イントラ + インタースロット繰り返し**を研究 | カバレッジエッジ UE と high reliability ユースケース対応 |
| **PDSCH: 最大帯域幅** | 最大 275 PRBs @ 30kHz SCS ≈ 100 MHz | **400 MHz（TB が 400 MHz まで対応）** | 超高速通信への対応 |
| **PDSCH: クロススロット** | 単一スロット内のみ | **スロット境界越え PDSCH を研究** | 大きな TB サイズと遅延耐性トレードオフ |
| **PDSCH: DMRS OCC** | FD-OCC 最大 4、TD-OCC 最大 2、CDM グループ最大 8 | FD-OCC 最大 24、TD-OCC 最大 4、CDM グループ最大 12 | 大規模 MU-MIMO に対応（DMRS 多重化能力拡張） |
| **PDSCH: AI/ML 受信機** | なし（FFS で研究） | **FLOPs/パラメータ数 KPI で正式に研究** | AI 活用の複雑度評価軸を初めて明示 |
| **PUSCH: アンテナポート数** | 最大 4（一部実装で 8） | **{1, 2, 3, 4, 8} を仕様候補に明示** | UL 大規模 MIMO への第一歩 |
| **PUSCH: コードブック** | 固定コードブック（Type 1/2） | **固定/設定可能/ハイブリッドを研究** | UE 多様性（FWA, XR, IoT）への対応 |
| **PUSCH: AI/ML 受信機** | なし | **FLOPs/パラメータ数 KPI テンプレートを合意** | DMRS オーバーヘッド削減の AI 活用を標準化 |
| **HST Multi-TRP** | 主に 2 TRP 協調 | **最大 16 TRP 協調を SLS で評価** | 超高速鉄道向けの大規模 TRP 協調 |
| **UE 帯域幅** | 5〜100 MHz（RedCap は最小 5 MHz） | **eRedCap より更に削減（Alt 3: ~7% 複雑度削減）** | IoT 向け低コスト UE 設計 |

---

## 6. 論文の理想 vs 3GPP 実装制約のギャップ

| 領域 | 論文の理想 | 3GPP 制約（#124bis 合意） | 進歩性の余地 |
|:---|:---|:---|:---|
| **PDCCH 送信ダイバーシティ** | 任意マルチポート BF | 単一ポート DMRS をベースライン → 非透明方式を研究 | Non-transparent 送信ダイバーシティの方式設計、precoder 粒度 |
| **MU-MIMO DMRS 指示** | 完全チャネル推定を前提 | NW-UE 間の CDM/ポート情報のどこを規定するか（指示 vs UE 仮定） | 指示粒度と interoperability の最適化 |
| **AI/ML DMRS 削減** | 任意のニューラルネット | FLOPs/パラメータ数で上限規定。Testability 問題未解決 | Testability 可能な AI/ML DMRS の構造設計 |
| **コードワード数 vs rank** | 任意の CW-layer mapping | 研究段階（NR の 1CW/2CW の枠組み継承か否かは未確定） | 高 rank（8〜16）時の CW 設計最適化 |
| **超広帯域 FDRA** | 任意の RB 粒度 | Type 0/1 のダイナミック切替。400 MHz TB は研究段階 | 400 MHz 対応 FDRA の粒度設計 |
| **UL コードブック** | 任意プリコーダ行列 | Configurable codebook の設計方針が未確定 | NW-configurable UL codebook の設計 |
| **HST 16 TRP 協調** | 任意の TRP 数 | 最大 16 TRP を研究対象に合意。具体的 TRP 間の同期・補正は未合意 | 大規模 TRP 協調のキャリブレーション方式 |
| **動的 TDD** | 任意のスロット割当 | Option 1/2/3 三択を研究（5G のフレキシブルシンボルモデルの発展形） | ガードシンボル削減と UE 処理タイム設計 |

---

## 7. 未解決課題（FFS / 次回以降）

### 10.5.2.1（PDCCH）
- REG 周波数方向割当の詳細
- CCE → REG 映射: REG/CCE 比・REG インデキシング
- QPSK 以外の変調の採否（高 SNR 環境での高変調次数 PDCCH）
- Hash 関数の設計詳細
- AL=32 の必要性と実現可能性
- 3 シンボル超 CORESET の採否
- PDCCH 送信ダイバーシティの non-transparent vs transparent の選択
- 6G と 5G の PDCCH リソース共用（MRSS）の具体的方式

### 10.5.2.2（PDSCH）
- AI/ML DMRS オーバーヘッド削減の具体的 EVM パラメータ（RAN1#125 で収集）
- FD-OCC / TD-OCC / CDM グループ数の down-select
- クロススロット PDSCH の最大持続時間と最大 TB サイズ
- CW-to-layer mapping の最大 CW 数・最大 rank 数
- PT-RS の FR1 / 7 GHz 対応
- TB / CB / CBG の 400 MHz マッピング（Option A vs B）
- RAN4 位相雑音モデルの更新確認（LS 回答待ち）

### 10.5.2.3（PUSCH）
- AI/ML 受信機 DMRS 削減のパラメータ値（RAN1#125 で収集）
- Configurable/Hybrid UL コードブックの具体的設計
- FDRA 非連続割当の可否
- FWA CPE SLS の評価結果（各社報告）
- UE アンテナポート数の 8 以外の候補

### 10.5.0（General）
- 動的 TDD Option 1/2/3 の down-select
- UE 最大帯域幅（Alt 1/2/3）の down-select
- 7 GHz アンテナ設定（AI 10.1 の合意待ち）

---

## 8. 市場・知財余地

| 提案・機能 | 標準での位置づけ | SEP 余地の理由 |
|:---|:---|:---|
| **MRSS PDCCH リソース共用** | 5G/6G が同一スペクトルを共存するための新規メカニズム（研究段階） | 5G には存在しない。NW 観点で UE 透明なため実装しやすく、essential 化しやすい |
| **AI/ML DMRS 削減の Testability** | 6G 仕様に初めて FLOPs/params 評価軸が入った | 「AI モデルの試験方法」は 3GPP で未確立。最初に解決策を出した企業が SEP を取れる |
| **Configurable UL Codebook** | 5G の固定コードブックを超える新設計（研究段階） | NW が UE 向けにカスタマイズするコードブックの送信・更新プロトコルは define-then-patent |
| **クロススロット PDSCH** | スロット境界越え PDSCH の仕様化（研究段階） | 超大 TB / 超広帯域 PDSCH（400 MHz）では必須になる可能性大 |
| **HST 最大 16 TRP 協調** | EVM 合意済み、具体的プロトコルは未合意 | TRP 間同期・QCL 設定・キャリブレーションの仕様化は必須化リスク大 |
| **Non-transparent PDCCH 送信ダイバーシティ** | 研究段階（ベースラインは単一ポート） | UE が precoder を認識する方式の設計は 5G と異なる新規。高 reliability ユースケースに必須 |
| **PUSCH 8 ポート対応** | 候補に明示されたが詳細設計未合意 | UL 大規模 MIMO 向け UE アンテナ設計を規定するシグナリング（コードブック/SRS）が SEP 候補 |

---

## 9. 会社別戦略的意図

| 企業 | 役割 | 戦略的意図 |
|:---|:---|:---|
| **Nokia** | 10.5.2.1 FL 単独 | 5G NR PDCCH 設計の歴史的優位を 6G に継承。制御チャネル設計の必須特許を握り続ける |
| **Ericsson + Google** | 10.5.2.2 co-FL | Ericsson: NW 観点の PDSCH スケジューリング / Google: AI/ML 受信機（DMRS 削減）を主導。異なる専門性の融合 |
| **NTT DOCOMO + Samsung** | 10.5.2.3 co-FL | DOCOMO: ネットワーク観点の UL 最適化 / Samsung: UE 実装の codebook 設計。日韓連合で UL 送信方式の議題設定権を得る |
| **Huawei + Xiaomi** | 10.5.0 co-FL | 中国陣が 6G の「全体アーキテクチャ（カバレッジ・TDD・帯域幅設計）」を主導 |
| **NVIDIA** | 10.5.2.3 寄書 | AI/ML 受信機 (GPU 活用) の PUSCH DMRS 削減に関心。チップベンダが 3GPP に参画する珍しいケース |
| **Bouygues+Vodafone+Orange+Telecom Italia+BT+DT+AT&T** | 10.5.2.1 共同寄書 | オペレータ 7 社連合が MRSS を支持。5G/6G スペクトル共用は既存インフラ投資の保護に直結 |

---

## Next Steps

- [ ] **10.5.2.2 FL Summary #1〜#5 精読**: Ericsson+Google の `R1-2603209〜R1-2603213` → PDSCH DMRS OCC 設計の具体的な選択肢と採否論理を確認
- [ ] **10.5.2.3 FL Summary #1〜#4 精読**: NTT DOCOMO+Samsung の `R1-2602188〜R1-2602191` → Configurable UL codebook の各社提案の収斂を追跡
- [ ] **10.5.2.1 FL Summary #1〜#3 精読**: Nokia の `R1-2603244〜R1-2603248` → MRSS の具体的なリソース共用オプションと Nokia 案の特徴を確認
- [ ] **AI/ML DMRS Testability の深掘り**: PDSCH と PUSCH 両方の AI/ML DMRS に FLOPs/params KPI が入った → 「AI モデルを RAN4 でどう試験するか」という未解決問題に先行出願できないか検討
- [ ] **Configurable UL Codebook の学術論文調査**: "configurable codebook NR 6G uplink" arXiv 検索 → 6G UL コードブック設計で優位な特許余地を特定
- [ ] **MRSS の SEP 余地分析**: 5G/6G 共存スペクトルでの PDCCH リソース共用プロトコル → Nokia + オペレータ連合の具体提案を Tdoc で確認
- [ ] **RAN1#125 予告の抽出**: 本ノートの FFS 項目（PDCCH 設計パラメータ、PDSCH OCC down-select、UL コードブック）が次会合でどのアジェンダで議論されるかを確認
- [ ] **CW-to-layer mapping の高 rank 研究**: 5G の最大 8 レイヤ（SU-MIMO）が 6G で拡張されるかを確認 → レイヤ増加時の CW 構造設計が知財余地
