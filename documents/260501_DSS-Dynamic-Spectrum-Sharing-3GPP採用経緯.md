---
title: "Dynamic Spectrum Sharing (DSS) — 3GPP 採用経緯と発表ドラフト範囲との接続"
status: draft
confidence: medium
created: 2026-05-01
updated: 2026-05-01
axes:
  technology-layer: [phy-mimo, cross-layer]
  generation: [rel-15, rel-16, rel-17]
  value: [coverage, throughput, backward-compat]
  market: [fwa, b2b-industrial]
  adoption-factors: [backward-compat, operator-roi, standard-convergence]
  ip: [spec-mapping]
sources:
  - url: https://www.3gpp.org/technologies/nr-dynamic-spectrum-sharing-in-rel-17
    title: "3GPP — NR Dynamic spectrum sharing in Rel-17 (Technologies page)"
    accessed: 2026-05-01
  - url: https://images.samsung.com/is/content/samsung/assets/global/business/networks/insights/white-papers/0122_dynamic-spectrum-sharing/Dynamic-Spectrum-Sharing-Technical-White-Paper-Public.pdf
    title: "Samsung — Dynamic Spectrum Sharing Technical White Paper (Jan 2021)"
    accessed: 2026-05-01
  - url: https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/5g-nr-evolution
    title: "Ericsson Technology Review — 3GPP releases 16 & 17 overview: 5G NR evolution"
    accessed: 2026-05-01
  - url: https://newsletter.mediatek.com/hubfs/mediatek5gprogress/Dynamic-Spectrum-Sharing-WhitePaper-PDFDSSWP-031320.pdf
    title: "MediaTek — 5G NR and 4G LTE Coexistence White Paper (Mar 2020)"
    accessed: 2026-05-01
  - url: https://blog.3g4g.co.uk/2020/05/5g-dynamic-spectrum-sharing-dss.html
    title: "3G4G Blog — 5G Dynamic Spectrum Sharing (DSS) (May 2020)"
    accessed: 2026-05-01
references:
  - "[[Samsung_DynamicSpectrumSharing_2021]]"
  - "[[3GPP_NR-DSS-in-Rel-17]]"
up: "[[260421_NR周波数リソース構造の発表資料ドラフト]]"
related:
  - "[[260421_TS38.101-1-Section5-Operating-Bandsの体系整理]]"
  - "[[260421_TS38.211-Section4-BWPとCarrier-Aggregationの体系整理]]"
  - "[[260424_Rel-15-物理リソース仕様策定の議論変遷]]"
  - "[[260424_Rel-15-企業別戦略背景と対立候補波形]]"
  - "[[260420_NRフレーム構造とリソースブロックの進化まとめ]]"
lang: ja
---
# Dynamic Spectrum Sharing (DSS) — 3GPP 採用経緯と発表ドラフト範囲との接続

> **本ノートの問い**: 発表ドラフト [[260421_NR周波数リソース構造の発表資料ドラフト|NR 周波数リソース構造]]（TS 38.101-1 Sec 5 + TS 38.211 Sec 4）の範囲は DSS と関係しているか。Yes — むしろ **発表ドラフトの主要な設計判断のほとんどが DSS 互換性を前提に決まっている**。本ノートでは (1) DSS の3GPP 採用経緯、(2) 発表範囲のどの概念がどう DSS と直結するか、(3) 4G→5G 移行で「うまくいかなかった」と言われる根拠、を整理する。

---

## 0. ユーザー前提の検証

ユーザー仮説:

> 4G の空き周波数に 5G の信号をねじ込んで同じ周波数帯を共有する仕組みだったが、調整のオーバーヘッドが大きかった

→ 一次情報で検証:

- Samsung 白書 [[Samsung_DynamicSpectrumSharing_2021]] Table 2 によれば、最悪ケース（4 CRS port）で **NR 側に対する LTE CRS+PDCCH の固定オーバーヘッドが ~23 %**。最小ケース（2 CRS, 1 LTE PDCCH）でも ~14 %。
- LTE Always-on signal (CRS) は基地局が起動している限り NR 利用率に常に減算項として効く。
- LTE-NR 間はリアルタイム協調が必須で、ベンダー独自 IF または統合スケジューラに依存する（マルチベンダー DSS は実質困難）。

ユーザー仮説は **概ね正しい**。ただし「ねじ込んだ」というより「LTE グリッドに NR を整列させる前提で NR 全体が設計された」というのが実態に近い（後述 §3）。

---

## 1. 定義と背景（Why）

### 1.1 DSS とは

**DSS (Dynamic Spectrum Sharing)** = 同一キャリア（同一中心周波数・同一占有帯域）を LTE と NR で**時間-周波数リソース単位で動的に分割**して共用する技術。LTE/NR スケジューラが負荷に応じて RB / シンボルを毎サブフレーム単位で割り振る。

旧来の「世代移行 = キャリア単位の re-farming」は、NR 利用者がまだ少ない初期市場では **NR キャリアのリソース過剰 + LTE キャリアのリソース不足** を生んでしまう。DSS はこの "transition mismatch" を埋めるために導入された（Samsung Figure 5）。

### 1.2 採用動機（オペレーター視点）

1. **C-band/mmWave のカバレッジ不足を補う**: NR 単独で 3 GHz 超の TDD バンドに展開すると、UE 送信電力 23 dBm の制約により UL カバレッジホールが発生（Samsung Figure 3）。低周波 FDD バンド（n1, n3, n5, n8, n20 等）は LTE 占有のため、re-farming するとそこの LTE ユーザーを犠牲にしてしまう。DSS なら LTE を残しながら NR カバレッジを獲得できる。
2. **新規スペクトル割当不要での 5G 早期展開**: 規制当局からの新規割当を待たずに、既存 LTE ライセンス上で SA NR を提供できる。
3. **LTE-NR 移行のソフトランディング**: トラフィック移行に応じて段階的に NR に振り分けを増やせる。

### 1.3 Rel-15 NR 設計が DSS を前提に置いた決定

これが本調査の核心。Rel-15 NR の物理層仕様策定は当初から「LTE FDD バンドを refarming できる / 共存できる」ことを必須要件として組み込んでいた。[[260424_Rel-15-物理リソース仕様策定の議論変遷|Rel-15 議論変遷ノート]] §1 でも 3 つの強制約のうちの 1 つとして `LTE との共存・相互運用性 — FDD 低周波帯の refarming（DSS の萌芽）と EN-DC（NSA Option-3）を必須とするオペレーター要求` を挙げている。

具体的には:
- **15 kHz SCS を基点として維持** → LTE OFDM サブキャリア間隔と完全一致 → グリッド整列可能
- **PRB = 12 サブキャリア** → 15 kHz SCS では 180 kHz、これは LTE PRB と同サイズ
- **100 kHz チャネルラスター（sub-3 GHz バンド）** → LTE FDD バンドと共有可能
- **SSB を MBSFN サブフレームに置けるよう設計余地を確保**

→ 発表ドラフトの「主流の数値（15 kHz SCS、100 kHz ラスター、特定の N_RB）」のほぼ全てに DSS の影が落ちている。

---

## 2. 技術要点（What） — 3GPP 採用経緯

### 2.1 採用経緯のタイムライン

| 時期 | リリース | 内容 | 主要根拠 |
|:---|:---|:---|:---|
| 2016 Q1〜2018 Q2 | Rel-15 SI/WI | NR 設計時点で LTE-NR 共存を必須要件として組み込み（NR 100 kHz raster, UL 7.5 kHz shift, CRS rate matching, MBSFN-based SSB, flexible CORESET, alternative DMRS 13th symbol） | Samsung WP §"LTE-NR Co-Existence Support in 3GPP Release 15"; TR 38.912 |
| 2018 Jun | Rel-15 ASN.1 freeze | LTE-CRS rate matching 1パターン、NR と LTE が同一帯域幅の場合のみ | TS 38.214 / 38.331 Rel-15 |
| 2019 Q4〜2020 Q3 | Rel-16 | **複数 (最大3) CRS rate matching pattern**（NR が LTE 側 CA に重なる場合）、PDSCH mapping type B 拡張（10 シンボル等） | Samsung WP §"Enhancement in 3GPP Release 16" |
| 2021 Q3〜2022 Q1 | Rel-17 NR_DSS WI（UID 860043 / Core 860143、approval RP-211345） | **SCell から sPCell への cross-carrier scheduling**。共有キャリアで NR PDCCH 容量逼迫を SCell PDCCH で補う | [[3GPP_NR-DSS-in-Rel-17]] / TR 21.917 §15 / RP-220464 |
| Rel-18 / Rel-19 | 継続 | Mid-band TDD DSS への展開、TDD バンド向け新ラスター定義 | Samsung WP §"Mid-band TDD DSS" |

### 2.2 Rel-15 の 6 つの共存メカニズム（[[Samsung_DynamicSpectrumSharing_2021]] §"3GPP Standards for DSS"）

1. **NR 100 kHz channel raster for FDD bands** — LTE と同一 RF チャネル位置に NR キャリアを配置可能にする。Slide 8 (5.4.2.3) のチャネルラスターの 100 kHz が **DSS 互換のために設定された値**。
2. **Optional NR UL 7.5 kHz shift (FDD)** — LTE UL は SC-FDMA 専用で DL に対して 7.5 kHz シフト。NR UL も OFDMA 系を使うため、オプションで 7.5 kHz シフトを取って LTE UL グリッドと整列。
3. **NR PDSCH with rate matching of LTE CRS** — RRC で CRS port 数 / 位置 / LTE BW を NR UE に通知し、PDSCH を LTE CRS 占有 RE に当てない（puncture or RE-level skip）。
4. **NR PDSCH alternative additional DMRS symbol location** — 追加 DMRS を 12 番目 → 13 番目シンボルへ移すオプションで CRS 衝突回避。
5. **NR flexible CORESET/PDCCH** — CORESET の RB/シンボル配置を柔軟化し、LTE PDCCH（first 1〜3 symbols）と NR PDCCH を同じ最初の 3 シンボル内で時分割共有。オプションで 4 番目以降にも CORESET 配置可能（PDSCH mapping type B 連携）。
6. **MBSFN サブフレーム上の SSB / SIB1 / RAR / OSI / Paging** — 初期アクセス段階の UE は CRS rate match を仮定できないため、CRS が制御領域のみに限定される MBSFN サブフレームで一括送信。SSB は 20 RB × 4 OFDM symbol。

### 2.3 Rel-16 拡張

- **複数 CRS rate matching pattern**（最大 3 つ）: NR キャリアが LTE 側の複数 CC（10 + 20 MHz など）に重なるケースを救済。
- **PDSCH mapping type B 拡張**: Rel-15 では 2/4/7 シンボル長のみだった type B に 10 シンボル長等を追加。CORESET を 1〜3 シンボルより後ろに置いた場合の残スロットを使い切れる。

### 2.4 Rel-17 NR_DSS WI（cross-carrier scheduling）

3GPP 公式 [[3GPP_NR-DSS-in-Rel-17]] によれば、NR 端末が増えると共有キャリアの NR PDCCH 容量が不足するため:

- SCell の PDCCH で sPCell の PDSCH/PUSCH をスケジュール可能に
- ただし「sPCell の PDCCH は他セルをスケジュールできない」「cross-carrier scheduling 対象 SCell は 1 つのみ」「monitoring candidates と CCE 数を sPCell/SCell で RRC 設定の scaling factor で分割」と制約あり
- 影響範囲: TS 38.211 / 212 / 213 / 214 / 331 / 300 / 306

これは「Rel-15 の DSS 設計が PDCCH 容量で破綻する」ことを 3GPP が事後に認めて補修した形。

---

## 3. 実装制約（How） — 発表ドラフト範囲との接続点

ユーザーの「周波数帯域の定義をつかさどっているので無関係ではない」という予想は **完全に正しい**。発表ドラフトのスライド毎に DSS との接続を整理:

| 発表ドラフトのスライド | 該当概念 | DSS との接続 |
|:---|:---|:---|
| **Slide 1b**: SCS = 15 × 2^μ kHz、μ=0 (15 kHz, FR1 低帯域) | 基点 SCS を 15 kHz とした理由 | **LTE OFDM サブキャリア間隔と完全一致**させ、LTE PRB（180 kHz= 12×15 kHz）と NR PRB を同サイズに揃えるため。これにより LTE グリッド上に NR を直交整列できる（Samsung WP §3GPP Rel-15 冒頭）。Slide 1b の "FR1 低帯域、LTE 共存" 注記がこれ。 |
| **Slide 2**: Operating Bands (n1=LTE B1, n3=B3, ...) | バンド番号体系 | NR バンド番号を LTE バンドと揃えたのは **同一周波数帯で DSS する際の管理整合性** が一因（[[260421_TS38.101-1-Section5-Operating-Bandsの体系整理|Operating Bands 体系整理]] §"なぜバンド番号が飛び飛びか"）。Slide 2 の「★口頭で一言触れる」注記を、本ノートの背景として強化できる。 |
| **Slide 5**: N_RB テーブル | SCS×Channel BW → N_RB | 15 kHz SCS の N_RB（5/10/15/20 MHz で 25/52/79/106）は **LTE の N_RB^DL と同じ値**。DSS では NR PRB が LTE PRB と RE 単位で整列する前提。 |
| **Slide 6**: ガードバンド計算式 `-SCS/2` 補正 | キャリア中心 vs CRB グリッド中心の半 SC オフセット | LTE は DC サブキャリアあり、NR DL も DC RE が rate match で扱われる。半 SC オフセット規則は LTE 整合のための補正。 |
| **Slide 7b (5.3.5)**: バンド別 SCS×BW の許容組合せ | 低周波 FDD は 15 kHz SCS のみ、最大 BW も狭い | **3 つの理由のうち 1 つが「LTE DSS で 15 kHz 必須」**（発表ドラフト Slide 7b/Q&A に既記）。DSS 互換のため低周波 FDD では 30 kHz SCS をサポートしない。 |
| **Slide 8 (5.4.2.3)**: チャネルラスター粒度 | sub-3 GHz: 100 kHz / C-band (n77/78): 15 kHz | **100 kHz は LTE FDD ラスターと同一**（[[Samsung_DynamicSpectrumSharing_2021]] §"NR 100 kHz channel raster for FDD bands"）。これにより同一中心周波数で DSS 可能。一方 C-band の 15 kHz ラスターは TDD で LTE 共存ニーズが薄い前提。「mid-band TDD DSS」が困難なのはこのラスター差異が一因。 |
| **Slide 9 (5.4.1.2)**: NR-LTE 隣接チャネル間隔の式 | DSS というよりキャリア間隔の話 | DSS が「同一中心周波数」シナリオなのに対し、5.4.1.2 は LTE と NR が**隣接配置**される refarming 部分共有のシナリオ。同じ仕様セクションが両ケースをカバー。 |
| **Slide 11 (5.4.3)**: 同期ラスター GSCN | SSB 配置の離散位置 | DSS では SSB を **MBSFN サブフレーム** に置く前提があり、GSCN がその位置を受け入れられる粒度であることが要請される。0-3 GHz の 100/1000 kHz ステップは LTE グリッドと整合。 |
| **Slide 11b**: Point A 決定経路、kSSB | キャリア中心と SSB 中心のオフセット | DSS で LTE キャリア中心と NR キャリア中心を一致させても、SSB は LTE CRS と衝突しない位置に置く必要がある。kSSB（半 SC 単位）でこの微調整が可能になっている。 |
| **Slide 12**: セルサーチ手順（GSCN → PSS/SSS → PBCH → SIB1） | 初期アクセス | DSS では SSB / SIB1 が MBSFN サブフレーム上にしかない。UE は当初 DSS 共有か純 NR か判別できず、CRS rate match を仮定せずに初期アクセスする必要がある。SIB1 取得後に CRS 設定 (`rateMatchPatternLTE-CRS`) が RRC で通知されて以降の PDSCH に適用される。 |
| **Slide 14〜18**: BWP（4.4.5） | UE 動作帯域の動的制御 | DSS 環境では LTE BW（典型 20 MHz）に揃えた **狭い NR BWP** を Initial / Active として運用するシナリオが想定される。BWP のニューメロロジー単一化（1 BWP = 1 SCS）も LTE 15 kHz と整合。 |
| **Slide 19〜21**: CA / 2 段階活性化 | キャリア集約と SCell | Rel-17 NR_DSS WI の cross-carrier scheduling（SCell → sPCell）が **発表ドラフト Slide 19〜21 の CA アーキテクチャを直接拡張**する。発表ドラフトに「Rel-17 で SCell から PCell へのクロスキャリアスケジューリングが追加」と一言加えると鮮度が上がる。 |
| **Slide 22**: 依存構造図（Operating Band → SCS → N_RB / BWP / GSCN）| 全体像 | 「Operating Band がサポートされる SCS を制約する」最大の理由が **DSS / refarming 互換**。FDD 低周波は 15 kHz 必須、TDD 中高周波は 30/60 kHz 可。 |

要約すると、**発表ドラフトの全体構造の "なぜその数値・なぜその制約" の背景に、ほぼ常に DSS が居る**。発表で DSS を独立トピックとして扱う必要はないが、各スライドの「補足／Q&A 予想」に DSS 動機を 1 行ずつ仕込むと、聴衆（発表者より詳しい部署）の質問に深く答えられるようになる。

---

## 4. 前世代（3G/4G）との差分

| 観点 | 4G LTE | 5G NR / DSS |
|:---|:---|:---|
| 世代移行方式 | キャリア単位の re-farming（GSM/UMTS → LTE） | RB / シンボル単位の動的共有（DSS） + 段階的 re-farming |
| 共存層 | RAT 間（DSDA / DSDS で UE が物理的に切り替え） | 同一物理チャネル内での LTE-NR multiplex |
| 必須 SCS | 15 kHz（固定） | 15 / 30 / 60 / 120 kHz（**ただし DSS 環境では実質 15 kHz 固定**） |
| Always-on 信号 | CRS（4 ports 最悪、サブフレーム内に分散） | SSB（20 ms 周期、MBSFN サブフレーム配置可）+ TRS（on-demand） |
| 制御チャネル | 先頭 1〜3 シンボルに集中（PDCCH） | 柔軟な CORESET 配置、ただし DSS では LTE PDCCH と先頭 3 シンボルを共有 → 容量制約 |

**3G→4G の re-farming は 4G の RAN 設計に大きな制約を与えなかったが、DSS は逆に NR 物理層仕様全体を制約した**点が決定的に異なる。これは「ローエンドカバレッジの確保が NR 単独では困難」という物理的制約と、「オペレーターが新規スペクトルを買えない」という商業的制約の合算による。

---

## 5. 主要プレイヤー

- **オペレーター推進派**: AT&T / Verizon / NTT DOCOMO / 欧州キャリア群（早期 5G 提供のための低帯域確保）→ DSS の3GPP 要件提出を主導
- **ベンダー実装派**: Ericsson（Spectrum Sharing 製品）, Samsung（同社白書 [[Samsung_DynamicSpectrumSharing_2021]] が業界標準の解説）, Nokia, Huawei, ZTE
- **チップセット**: Qualcomm（Snapdragon X55 で DSS 対応）, MediaTek（[MediaTek DSS 白書](https://newsletter.mediatek.com/hubfs/mediatek5gprogress/Dynamic-Spectrum-Sharing-WhitePaper-PDFDSSWP-031320.pdf)）
- **3GPP RAN1 Feature Lead**: Rel-17 NR_DSS WI [要確認: RP-211345 の rapporteur 企業を 3GPP work plan で確認] → Samsung または Ericsson の可能性が高い
- **Rel-16 LTE-CRS rate matching pattern enhancement**: Ericsson / Qualcomm 提案が中心 [要確認: Rel-16 RAN1 Tdoc を WhatTheSpec.net 等で確認]

---

## 6. 未解決課題・"うまくいかなかった" と評価される根拠

### 6.1 仕様レベルの未解決

- **PDCCH 容量問題**: Rel-17 NR_DSS の cross-carrier scheduling は緩和策だが、根本解決ではない（[[3GPP_NR-DSS-in-Rel-17]] が「sufficient scheduling capacity for NR UEs on the shared carriers」を Rel-17 でようやく対処したと明記）。
- **Mid-band TDD DSS の不全**: n41 等 TDD バンドは 100 kHz ラスターを持たず 15/30 kHz ラスターのみ。LTE-NR 中心周波数の整列が単純にできない（Samsung WP §"Mid-band TDD DSS"）。3GPP は同一物理周波数範囲に新バンドを追加で定義した。
- **URLLC との非互換**: 30/60 kHz SCS による低遅延が、DSS 下では 15 kHz 縛りで使えない（Samsung WP §"Deployment and Operation"）。

### 6.2 オペレーター/実運用上の負債

[[Samsung_DynamicSpectrumSharing_2021]] が同社製品売り込み資料でありながら明示している懸念:

1. **常時 14〜23 % のオーバーヘッド** (Table 2): 4 CRS port + 2 LTE PDCCH 構成で 23 %。re-farm 後の純 NR 環境では発生しない。
2. **ピークレート劣化**: 静的 LTE/NR 二分割なら DC でピークまで到達できるが、DSS だとオーバーヘッドが常時減算される。
3. **PDCCH 容量制約**: 4 CRS LTE 構成で NR PDCCH が 1 シンボルしか取れず、aggregation level 8 を要する weak channel UE が **1 セルあたり 1 端末** しかサポートできない極端ケース（Samsung Figure 18a）。
4. **HW/SW 移行コスト**: legacy radio unit 置換、新 baseband 追加、LTE-NR リアルタイム協調 IF の整備、commit 済 LTE 機能を DSS 対応版に再開発。
5. **隣接セル CRS 干渉**: 隣接セル CRS と自セル NR データが衝突。re-farm 後には消える問題。
6. **ベンダーロックイン**: LTE-NR の動的協調は専有スケジューラに依存。マルチベンダー運用はほぼ不可能。

これらが合わさって「DSS は移行ツールとしては必要だが、長く使うと複合デメリットが大きい → 早期に re-farming を進める方が合理的」というのが 2021 年以降の業界コンセンサス。本ノートのソースである Samsung 自身が "may be contradictory that DSS is considered as a promising technology for seamless transition to 5G" と書いている。

### 6.3 Beyond 5G / 6G への含意

- 6G で「LTE/5G との同時共存」を物理層に組み込むかは未決定。前世代と物理層で密結合する設計は、今回の DSS が示した通り**容量上限とベンダーロックインの代償**を払う。
- 一方、AI ベース動的スケジューリング・O-RAN の SMO による RAT 横断オーケストレーション・SBFD（Sub-band Full Duplex）等で、より少ないオーバーヘッドの "soft sharing" を実現できる可能性。

---

## 7. 市場・知財余地

### 7.1 知財ポジションの観点

DSS は **仕様マッピング (spec-mapping)** が主たる SEP 経路。具体的には:

- **CRS rate match パターン** (`rateMatchPatternLTE-CRS`) の表現方式と、複数パターンの組み合わせ方（Rel-16 で最大 3 パターン）
- **MBSFN サブフレーム上の SSB/SIB1/RAR 配置**の符号化方法
- **Cross-carrier scheduling SCell→sPCell** の RRC scaling factor 算出（Rel-17）
- **PDCCH symbol allocation**（first 3 symbols 内での LTE-NR 共有）

これらは Rel-15〜17 で大きな提案戦が起きた領域であり、Tdoc レベルで個別企業の主導が見える。**[要確認]** Rel-16 R1-19xxxxxx / Rel-17 R1-21xxxxxx の rate matching pattern 関連 Tdoc のリストを 3GPP FTP から取得し、提出企業の集中を分析するのが次のアクション。

### 7.2 市場視点

- DSS の主要展開地域: 米国（AT&T / Verizon の n5, n66 上）、欧州（Vodafone, Deutsche Telekom の n1, n3 上）、日本（DOCOMO の n1, n3, n28 上で限定的に）。
- 韓国 / 中国は当初から TDD mid-band（n41, n78）に大量スペクトルを確保していたため DSS 採用は限定的。
- 移行ツールとしての賞味期限: 2025〜2027 頃に主要市場で re-farming 完了 → DSS は段階的に役目を終える見通し。Rel-18/19 で更なる仕様強化が議論されているのは、この賞味期限を延長する/中・mmWave に拡大する方向（Samsung WP §"Mid-band TDD DSS"）。

---

## 8. 発表ドラフトへの反映提案（任意）

[[260421_NR周波数リソース構造の発表資料ドラフト]] への加筆候補（口頭でも可）:

1. **Slide 1b (SCS)**: 「2 のべき乗倍」の動機 3 つに加えて「**LTE 15 kHz と完全に整合させ DSS / EN-DC を可能にするため**」を 4 つ目として追加。
2. **Slide 2 (Operating Bands)**: 既に注記済の DSS 言及を、本ノートを参照しつつ Q&A 想定として強化。質問例「DSS とは何で、なぜバンド番号を LTE と揃えたか」への答えを準備。
3. **Slide 7b (5.3.5)**: 既に「LTE DSS で15kHz必須」と書いてある。MBSFN サブフレーム配置の話を口頭で補足できる。
4. **Slide 8 (5.4.2.3)**: 「100 kHz ラスターは LTE FDD ラスターと同一」を明示。「TDD バンドが 15 kHz ラスターなのは DSS 必要性が薄いため」を補足。
5. **Slide 12 (セルサーチ手順)**: DSS 環境では SSB が MBSFN サブフレーム上にしかない、と一言追加すると Q&A の幅が広がる。
6. **Slide 19〜21 (CA / 2 段階活性化)**: Rel-17 で **SCell→sPCell の cross-carrier scheduling**（NR_DSS WI、UID 860043）が追加されたことを前向き要素として軽く触れる。

---

## 9. Next Steps

- [ ] 3GPP Work Plan Excel（<https://www.3gpp.org/ftp/Information/WORK_PLAN/>）から `DSS` を含む全 WI/SI（Rel-15〜Rel-19）を抽出し、UID・Tdoc 番号・rapporteur を一覧化する。
- [ ] Rel-16 の "Multiple CRS rate matching patterns" 提案の Tdoc 起点を WhatTheSpec.net または ShareTechNote の Agreements ログで特定する（提案企業の集中を確認）。
- [ ] [[Samsung_DynamicSpectrumSharing_2021]] と MediaTek 白書（<https://newsletter.mediatek.com/hubfs/mediatek5gprogress/Dynamic-Spectrum-Sharing-WhitePaper-PDFDSSWP-031320.pdf>）を比較し、オーバーヘッド数値の独立検証を行う。
- [ ] 3G4G Blog の DSS 解説（<https://blog.3g4g.co.uk/2020/05/5g-dynamic-spectrum-sharing-dss.html>）から欧州オペレーター視点の追加情報を取り込む。
- [ ] TS 38.214 の `rateMatchPatternLTE-CRS` 関連条文（Rel-15 / 16 / 17 の差分）を `references/` に取り込み、`/digest-paper` で構造比較する。
- [ ] 6G で「LTE/5G との物理層共存」を再設計するか／するならどう改善するかを、本調査の結論をもとに `/connect-dots` で関連トピックと結びつける。
