---
title: "Rel-15 NR 勉強会トピック調査ガイド"
status: draft
confidence: medium
created: 2026-04-22
updated: 2026-04-22
axes:
  technology-layer: [phy-mimo, phy-coding, higher-layer, cross-layer]
  generation: [rel-15]
  value: [throughput, latency, reliability, coverage, energy-efficiency]
  market: [consumer-xr, b2b-industrial, fwa]
  adoption-factors: [standard-convergence, backward-compat]
  ip: [spec-mapping]
sources:
  - url: https://www.3gpp.org/specifications-technologies
    accessed: 2026-04-22
  - url: https://portal.3gpp.org/
    accessed: 2026-04-22
related:
  - TS38.211-Section4-BWPとCarrier-Aggregationの体系整理.md
  - TS38.101-1-Section5-Operating-Bandsの体系整理.md
  - NRフレーム構造の発表資料ドラフト.md
  - フレーム構造のギャップ分析-学術vs3GPPvs実装制約.md
---

# Rel-15 NR 勉強会トピック調査ガイド

## 目的

Rel-15 NR の主要トピック（30件）について、勉強会で参照すべきスペック資料・概要・LTE からの変化点を一覧化する。各トピックを独立したノートに展開する前の **ロードマップ** として機能させる。

## トピック群の構成

30トピックを以下の7グループに分類し、スペック上の依存関係に沿った学習順序を示す。

| # | グループ | トピック数 | 主要スペック |
|---|---------|-----------|-------------|
| A | フレーム構造・二重化 | 2 | TS 38.211, TS 38.300 |
| B | 変調・符号化 | 3 | TS 38.211, TS 38.212 |
| C | 初期接続・同期 | 2 | TS 38.211, TS 38.213 |
| D | モビリティ・無線リンク管理 | 3 | TS 38.133, TS 38.213, TS 38.321 |
| E | DL/UL 制御・データチャネル | 8 | TS 38.211–214, TS 38.321 |
| F | MIMO・参照信号・CSI | 7 | TS 38.211, TS 38.214 |
| G | UL 固有 | 5 | TS 38.211, TS 38.213, TS 38.214 |

---

## グループ A: フレーム構造・二重化

### A-1. Frame Structure

**定義と背景（Why）**
NR は LTE の固定 1ms サブフレーム構造を超えて、スケーラブルな numerology（SCS: 15/30/60/120/240 kHz）を導入。URLLC の低遅延要件と eMBB の高スループットを同一フレーム内で共存させるため、柔軟なフレーム構造が必須となった。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §4.1–4.3 | フレーム構造定義、numerology、スロット/シンボル構造 |
| TS 38.300 | §5.1 | 全体アーキテクチャにおけるフレーム構造の位置づけ |
| TS 38.213 | §11.1 | スロットフォーマット indication |
| TR 38.802 | — | NR Study Item での検討経緯 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| サブキャリア間隔 | 15 kHz 固定 | 15/30/60/120/240 kHz（μ = 0–4） |
| スロット長 | 1 ms 固定 | 0.5 ms ÷ 2^μ（可変） |
| シンボル数/スロット | 7 or 6（Normal/Extended CP） | 14（Normal CP）/ 12（Extended CP, 60 kHz のみ） |
| Mini-slot | なし | 2/4/7 シンボルの柔軟スケジューリング |

**議論の変遷**
- RAN1#86bis (2016-10): numerology 候補の絞り込み。2^n スケーリングに合意
- RAN1#87 (2016-11): スロット構造の basic unit を 14 OFDM シンボルに合意
- RAN1#88 (2017-02): mini-slot（non-slot-based scheduling）の導入合意

**勉強会で注目すべきポイント**
- numerology の 2^n スケーリングがなぜ選ばれたか（実装の同期容易性）
- mini-slot の導入動機（URLLC の低遅延 vs. スケジューリング粒度のトレードオフ）

---

### A-2. Duplex

**定義と背景（Why）**
NR は FDD/TDD に加え、dynamic TDD（シンボル単位の UL/DL 切替）を導入。高周波帯（FR2）では TDD が前提であり、低周波帯（FR1）では従来 FDD が主流だが、SUL や flexible duplex が選択肢を広げた。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §4.3.1 | スロットフォーマット（DL/UL/Flexible シンボル） |
| TS 38.213 | §11.1 | SFI（Slot Format Indication）via DCI format 2_0 |
| TS 38.101-1 | §5 | FR1 の FDD/TDD バンド定義 |
| TS 38.101-2 | §5 | FR2 の TDD バンド定義 |
| TS 38.828 | — | Cross-link interference の study（Rel-16 への布石） |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| TDD パターン | 7 固定パターン（SA0–SA6） | シンボル単位の柔軟設定 |
| パターン設定 | SIB1 で semi-static | SIB1（semi-static）+ DCI（dynamic） |
| ガードピリオド | 固定 Special Subframe | Flexible シンボルで対応 |
| CLI 対策 | 同一パターン運用前提 | Cross-link interference は Rel-16 課題 |

**議論の変遷**
- RAN1#86bis: semi-static + dynamic TDD の2層構造に合意
- RAN1#88: Slot Format Indication (SFI) の DCI 設計議論
- Rel-16 以降: CLI（Cross-Link Interference）管理が本格化

**勉強会で注目すべきポイント**
- Dynamic TDD のシンボル粒度がなぜ必要か（URLLC と eMBB の共存）
- CLI 問題が Rel-15 で未解決のまま残された理由

---

## グループ B: 変調・符号化

### B-1. NR Modulation and Coding Schemes

**定義と背景（Why）**
NR は LTE のMCS テーブルを拡張し、256QAM の DL/UL 両方でのサポート、および URLLC 向けの低 code rate MCS テーブルを新設した。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.1.3（DL）, §6.1.4（UL） | MCS テーブル定義（Table 5.1.3.1-1/2/3, Table 6.1.4.1-1/2） |
| TS 38.211 | §7.3.1 | 変調方式の定義（QPSK, 16QAM, 64QAM, 256QAM） |
| TS 38.212 | §5–7 | チャネル符号化の全体構造 |
| TS 38.214 | §5.1.3.1 | MCS テーブル切替の条件（DCI field, RRC 設定） |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 最大変調次数 | DL: 256QAM (Rel-12), UL: 64QAM (Rel-8) / 256QAM (Rel-14) | DL/UL 共に 256QAM を初期サポート |
| MCS テーブル | 1種類 | 3種類（eMBB 64QAM, eMBB 256QAM, URLLC 低符号化率） |
| π/2-BPSK | なし | UL（DFT-s-OFDM 時）で追加、カバレッジ拡大 |
| チャネル符号化 | Turbo code (data), TBCC (control) | LDPC (data), Polar (control) |

**議論の変遷**
- RAN1#86–87: Turbo code vs LDPC vs Polar の大論争
- RAN1#88: data channel → LDPC, control channel → Polar に最終合意
- MCS テーブルの URLLC 用低符号化率テーブルは URLLC WI 内で議論

**勉強会で注目すべきポイント**
- MCS テーブルが3種類ある設計意図（ユースケース別の最適化）
- π/2-BPSK の導入理由（DFT-s-OFDM の PAPR 特性との関係）

---

### B-2. NR LDPC Codes

**定義と背景（Why）**
NR のデータチャネル（PDSCH/PUSCH）は LDPC 符号を採用。LTE の Turbo code と比較して、高スループット（10+ Gbps）でのデコーダ実装が容易であり、パイプライン並列処理に適した構造を持つ。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.212 | §5.2.2 | LDPC base graph 選択（BG1: 大 TBS, BG2: 小 TBS） |
| TS 38.212 | §5.3.2 | Rate matching for LDPC |
| TS 38.212 | §5.4.2 | Code block segmentation |
| TS 38.214 | §5.1.3 | MCS と Transport Block Size の決定 |
| R1-1611254 | — | Qualcomm の LDPC 構造提案（raptor-like） |

**LTE からの主な変化**

| 観点 | LTE (Turbo) | NR (LDPC) |
|------|-------------|-----------|
| 構造 | 再帰的畳み込み | Quasi-Cyclic LDPC (QC-LDPC) |
| 復号 | MAP/log-MAP（逐次） | Belief Propagation（並列可能） |
| 最大 TBS | ~75,376 bits | ~1,277,992 bits（BG1, 最大 code rate） |
| Base graph | — | BG1（大 TBS, code rate 1/3–8/9）, BG2（小 TBS, code rate 1/5–2/3） |
| Lifting size | — | Z = 2–384（51 種類、柔軟な TBS 対応） |

**議論の変遷**
- RAN1#86bis (2016-10): LDPC vs Turbo vs Polar の初期検討
- RAN1#87 (2016-11): data channel を LDPC とする方向に収束
- RAN1#88 (2017-02): Raptor-like LDPC 構造（Qualcomm 提案）を base に合意
- RAN1#88bis–89: Base graph 2 の設計、lifting size の詳細化

**勉強会で注目すべきポイント**
- BG1/BG2 の使い分け閾値（TBS, code rate の境界）
- HARQ-IR（Incremental Redundancy）との連携（rate matching の circular buffer）
- Raptor-like 構造が選ばれた理由（rate compatibility の良さ）

---

### B-3. NR Polar Codes

**定義と背景（Why）**
NR の制御チャネル（PDCCH/PUCCH の一部、PBCH）に Polar 符号を採用。情報理論的に容量達成可能な最初の実用符号であり、短ブロック長で Turbo/LDPC より優れた性能を示す。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.212 | §5.2.1 | Polar coding（符号化手順） |
| TS 38.212 | §5.3.1 | Rate matching for Polar |
| TS 38.212 | §7.1 | DCI の CRC 付加と Polar 符号化 |
| TS 38.212 | §7.3 | PBCH の Polar 符号化 |

**LTE からの主な変化**

| 観点 | LTE (TBCC) | NR (Polar) |
|------|------------|------------|
| 理論基盤 | 畳み込み符号 | チャネル容量達成符号（Arıkan, 2009） |
| 復号 | Viterbi | SCL（Successive Cancellation List）+ CRC-aided |
| CRC の役割 | 誤り検出のみ | 誤り検出 + Polar 復号の list 選択 |
| Distributed CRC | なし | あり（CRC ビットを情報ビット間に分散配置） |

**議論の変遷**
- RAN1#86bis–87: 制御チャネルの符号化方式としてPolar vs TBCC vs LDPC
- RAN1#87 (2016-11): DL control → Polar で合意（Huawei が強力に推進）
- RAN1#88 (2017-02): UL control も Polar で合意
- RAN1#88bis–89: Distributed CRC 設計、rate matching（puncturing vs shortening）の詳細

**勉強会で注目すべきポイント**
- SCL 復号の list size と性能/複雑度のトレードオフ
- Distributed CRC がなぜ性能向上に効くか
- Polar が control channel に限定された理由（大ブロック長での LDPC 優位性）

---

## グループ C: 初期接続・同期

### C-1. SSB (SS/PBCH Block)

**定義と背景（Why）**
NR のセル検出・初期同期に使用される信号ブロック。LTE では PSS/SSS/PBCH が毎サブフレームで送信されたが、NR では beam sweeping のために SSB を burst set として周期的に送信し、always-on 信号を削減（エネルギー効率向上）。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §7.4.3 | SS/PBCH block 構造（4 OFDM シンボル × 240 SC） |
| TS 38.213 | §4.1 | SSB の周期、burst set、candidate positions |
| TS 38.211 | §7.4.2.1 | PSS（Primary Synchronization Signal）系列 |
| TS 38.211 | §7.4.2.2 | SSS（Secondary Synchronization Signal）系列 |
| TS 38.211 | §7.4.3.1 | PBCH の DMRS |
| TS 38.213 | §4.1 | SSB index と timing の関係 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| PSS/SSS 配置 | 毎5ms, 帯域中央固定 | SSB burst set（5/10/20/40/80/160ms 周期） |
| ビーム | 全方向送信 | 最大 64 ビームで sweep（FR2） |
| セル ID | PCI = 3×N(1) + N(2), 504 個 | PCI = 3×N(1) + N(2), 1008 個 |
| PBCH | 毎10ms, 40ms TTI | SSB に統合、80ms TTI |
| Always-on overhead | 高い | SSB 周期の設定で削減可能 |

**議論の変遷**
- RAN1#86bis: SSB の物理構造（4 OFDM シンボル）の初期合意
- RAN1#88: SSB candidate position の設計（numerology 依存）
- RAN1#89: FR2 での最大 64 SSB beams に合意

**勉強会で注目すべきポイント**
- SSB の candidate position がなぜ half-frame 内に限定されるか
- SSB index から timing information をどう取得するか（PBCH payload）
- FR1 vs FR2 での SSB beam 数の違い（4/8 vs 64）

---

### C-2. PRACH

**定義と背景（Why）**
UE がネットワークに初期アクセスする際のランダムアクセスチャネル。NR では beam 環境での動作、多様な numerology への対応、short preamble の導入（URLLC 低遅延）が主要な変更点。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §6.3.3 | PRACH preamble（long/short sequence） |
| TS 38.213 | §8 | RA 手順（4-step / 2-step (Rel-16)） |
| TS 38.211 | Table 6.3.3.1-1/2 | Preamble format 定義（format 0–3, A1–C2） |
| TS 38.321 | §5.1 | Random Access 手順の MAC 層 |
| TS 38.213 | §8.1 | PRACH occasion と SSB の対応 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| Preamble format | Format 0–4（固定長） | Long: Format 0–3, Short: Format A1–C2（多様） |
| 系列長 | 839（long）, 139（short, Rel-15 では未使用） | 839（long）, 139（short） |
| Restricted set | Type A/B | Type A/B（long のみ） |
| SSB との対応 | なし（omnidirectional） | SSB-to-RO mapping（beam correspondence） |
| 2-step RA | なし | Rel-16 で導入（msgA/msgB） |

**議論の変遷**
- RAN1#87–88: Short preamble format の導入合意
- RAN1#89: SSB-to-PRACH occasion mapping の詳細設計
- Rel-16: 2-step RACH (msgA/msgB) が追加議論

**勉強会で注目すべきポイント**
- Long vs Short preamble の使い分け（セルサイズ、遅延要件）
- SSB-to-RO mapping が beam management にどう寄与するか
- PRACH occasion のリソース配置設計（時間/周波数の柔軟性）

---

## グループ D: モビリティ・無線リンク管理

### D-1. Mobility RRM (Radio Resource Management)

**定義と背景（Why）**
NR ではビーム管理が加わったことで、セルレベルの mobility に加えて beam レベルの mobility が必要。RRM 測定はSSB または CSI-RS ベースで行い、L3 mobility（ハンドオーバ）の判断に使用される。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.133 | §9 | RRM 測定要件（RSRP, RSRQ, SINR の精度・報告間隔） |
| TS 38.331 | §5.5 | MeasConfig, MeasObjects, ReportConfig |
| TS 38.215 | — | 物理層の測定定義（SS-RSRP, SS-RSRQ, SS-SINR, CSI-RSRP 等） |
| TS 38.300 | §9 | モビリティ手順の概要 |
| TS 38.214 | §5.1.6 | CSI-RS ベース RRM 測定のリソース設定 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 測定対象 | CRS ベース（always-on） | SSB ベース + CSI-RS ベース |
| 測定指標 | RSRP, RSRQ | SS-RSRP, SS-RSRQ, SS-SINR, CSI-RSRP 等 |
| ビーム管理 | なし | beam レベルの RSRP 報告 + cell レベルへの集約 |
| 測定ギャップ | 固定パターン | 複数の gap pattern + per-FR gap |
| Conditional HO | なし | Rel-16 で導入 |

**勉強会で注目すべきポイント**
- SSB ベース vs CSI-RS ベース測定の使い分け
- beam management（L1/L2）と mobility（L3）の連携

---

### D-2. RLM (Radio Link Monitoring)

**定義と背景（Why）**
UE がサービングセルとの無線リンク品質を監視し、radio link failure (RLF) を検出する仕組み。NR ではビーム障害（beam failure）の概念が加わり、RLF に至る前に beam recovery で救済する手段が導入された。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.213 | §12 | RLM 手順（IS/OOS 判定） |
| TS 38.321 | §5.17 | Beam failure detection / recovery（MAC 層） |
| TS 38.133 | §12 | RLM の性能要件 |
| TS 38.331 | §5.3.10 | RRC での RLF 検出と recovery 手順 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 監視対象 | CRS の BLER 推定 | SSB / CSI-RS の hypothetical BLER |
| Beam failure | なし | Beam failure detection + recovery (BFR) |
| Recovery | RLF → 再接続 | Beam recovery → 失敗なら RLF → 再接続 |
| RLM-RS | CRS（implicit） | SSB or CSI-RS（explicit 設定） |

**勉強会で注目すべきポイント**
- Beam failure recovery (BFR) の手順と RLF との関係
- RLM reference signal の設定とその測定周期

---

### D-3. Bandwidth Part (BWP)

**定義と背景（Why）**
UE が常にキャリア全帯域を処理する必要をなくし、UE 能力に応じた帯域幅で動作可能にする仕組み。省電力化と多様な UE カテゴリのサポートが主目的。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §4.4.5 | BWP の物理層定義 |
| TS 38.213 | §12 | Active BWP の切替手順 |
| TS 38.214 | §5.1.2.1 | BWP とリソース割当の関係 |
| TS 38.331 | §6.3.2 | BWP-Downlink / BWP-Uplink の RRC IE 定義 |
| TS 38.300 | §5.4 | BWP の概念説明 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| UE 帯域幅 | システム帯域幅全体を処理 | BWP（最大4 per CC）から active BWP を1つ使用 |
| Numerology 切替 | 不可 | BWP ごとに numerology を設定可能 |
| 省電力 | DRX のみ | DRX + BWP adaptation（狭帯域 BWP への切替） |
| Initial access | MIB → SIB1 → full bandwidth | MIB → initial BWP → dedicated BWP |

**勉強会で注目すべきポイント**
- BWP 切替の遅延（timer-based vs DCI-based）
- Initial BWP / Default BWP / Active BWP の関係
- BWP と CA の組み合わせ

---

## グループ E: DL/UL 制御・データチャネル

### E-1. Control Channel (PDCCH/CORESET)

**定義と背景（Why）**
NR の DL 制御チャネルは LTE の PDCCH（帯域全体の先頭 1–3 シンボル）から、CORESET（Control Resource Set）という柔軟なリソース割当に変更。Beam 管理と柔軟なスケジューリングをサポートするため。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §7.3.2 | PDCCH の物理構造 |
| TS 38.213 | §10.1 | CORESET 定義、search space |
| TS 38.213 | §10.2 | Search space set（USS/CSS） |
| TS 38.212 | §7.3 | DCI format 定義（0_0, 0_1, 1_0, 1_1 等） |
| TS 38.213 | §10.3 | PDCCH candidates と aggregation level |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 制御領域 | 帯域全体, 先頭 1–3 シンボル | CORESET: 周波数/時間/ビームで柔軟に設定 |
| Search space | Common + UE-specific | CSS + USS（最大 10 search space sets） |
| Aggregation level | 1, 2, 4, 8 CCE | 1, 2, 4, 8, 16 CCE |
| DMRS | CRS ベース | PDCCH-DMRS（CORESET ごと） |
| Blind decoding | 最大 44 candidates | 最大 44 candidates per slot（設定に依存） |

**勉強会で注目すべきポイント**
- CORESET #0（initial access）の特殊性
- Search space の monitoring periodicity と DCI format の対応

---

### E-2. HARQ Feedback / SR / CSI

**定義と背景（Why）**
UL フィードバック情報（HARQ-ACK, Scheduling Request, CSI）の報告手段と多重化の枠組み。NR では非同期 HARQ、柔軟なタイミング設定、CBG 単位 ACK など LTE にない自由度が導入された。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.213 | §9.1 | HARQ-ACK feedback timing（K1 パラメータ） |
| TS 38.213 | §9.2 | SR の PUCCH リソース設定 |
| TS 38.213 | §9.3 | CSI 報告設定 |
| TS 38.212 | §6.3 | UCI 符号化（HARQ-ACK, SR, CSI） |
| TS 38.321 | §5.4 | HARQ process 管理（MAC 層） |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| HARQ timing | 固定（DL: n+4） | DCI で K1 を動的指定 |
| HARQ process 数 | 8（FDD）, 最大 16 | 最大 16 |
| Codebook | Fixed size | Semi-static / Dynamic codebook |
| CBG-level ACK | なし | Rel-15 で導入 |
| SR 周期 | 固定セット | 柔軟設定（1–640 スロット） |

**勉強会で注目すべきポイント**
- K1（HARQ-ACK タイミング）の柔軟性と UE processing time の関係
- Semi-static vs Dynamic HARQ-ACK codebook
- HARQ/SR/CSI が同時発生した場合の優先制御

---

### E-3. PUCCH

**定義と背景（Why）**
UL 制御情報（UCI: HARQ-ACK, SR, CSI）を伝送する物理チャネル。NR では 5 つの PUCCH format を定義し、少ビット（1–2 bit ACK）から大容量 CSI 報告まで柔軟に対応。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §6.3.2 | PUCCH 物理構造（Format 0–4） |
| TS 38.213 | §9.2 | PUCCH リソース設定 |
| TS 38.212 | §6.3 | UCI on PUCCH の符号化 |
| TS 38.213 | §9.2.1 | PUCCH resource set と payload size の対応 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| Format 数 | Format 1/1a/1b/2/3/4/5 | Format 0/1/2/3/4（整理・統合） |
| Short PUCCH | なし | Format 0, 2（1–2 シンボル） |
| Long PUCCH | Format 1–5（1 スロット） | Format 1, 3, 4（4–14 シンボル） |
| 周波数ホッピング | Format 依存 | Intra-slot hopping（long format） |
| 多重化 | Format 1: CDM | Format 0: sequence, Format 1: time-domain OCC, Format 4: OCC |

**各 Format の概要**

| Format | シンボル数 | UCI bits | 用途 |
|--------|-----------|----------|------|
| 0 | 1–2 | 1–2 | SR, 少ビット HARQ-ACK（sequence selection） |
| 1 | 4–14 | 1–2 | SR, 少ビット HARQ-ACK（time-domain OCC, カバレッジ大） |
| 2 | 1–2 | >2 | 中～大ビット UCI（CSI 含む） |
| 3 | 4–14 | >2 | 大ビット UCI（CSI 含む, DFT-s-OFDM） |
| 4 | 4–14 | >2 | Format 3 + OCC 多重（多 UE） |

**勉強会で注目すべきポイント**
- Short PUCCH（Format 0/2）の導入動機（低遅延、TDD の self-contained slot）
- PUCCH resource set の選択ロジック（UCI payload size → resource set → resource）

---

### E-4. UCI Multiplexing

**定義と背景（Why）**
HARQ-ACK、SR、CSI が同一 UL スロットで発生した場合の多重化ルール。UCI on PUSCH（データと制御の多重）も含む。NR では優先度ベースの dropping/multiplexing ルールが整備された。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.213 | §9.2.5 | UCI の同時送信ルール（PUCCH 同士、PUCCH + PUSCH） |
| TS 38.212 | §6.3.2.4 | UCI on PUSCH の符号化 |
| TS 38.214 | §6.2.7 | UCI on PUSCH のリソース決定 |
| TS 38.213 | §9.2.5.1 | PUCCH の衝突解決 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| UCI on PUSCH | ACK/CSI を PUSCH に多重 | 同様 + 優先度ベースの beta offset |
| 同時 PUCCH | 不可（1 UL CC で 1 PUCCH） | 同一スロット内の衝突解決ルール |
| 優先度 | HARQ-ACK > SR > CSI | 同様の優先度 + 2段階 priority（URLLC 対応） |
| CSI dropping | Part 2 を全 drop | Part ごとの priority-based omission |

**勉強会で注目すべきポイント**
- PUCCH と PUSCH が重なった場合のルール
- CSI Part 1 / Part 2 の omission ルール

---

### E-5. Resource Allocation

**定義と背景（Why）**
PDSCH/PUSCH の時間・周波数リソース割当方法。NR では Type 0（bitmap）/ Type 1（連続 RB）の2方式に整理され、BWP 内での割当が基本単位。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.1.2 | DL resource allocation（Type 0, Type 1） |
| TS 38.214 | §6.1.2 | UL resource allocation（Type 0, Type 1） |
| TS 38.214 | §5.1.2.1 | Time-domain resource allocation（TDRA table, K0, SLIV） |
| TS 38.212 | §7.3.1 | DCI の RA field 定義 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 周波数割当 | Type 0/1/2 | Type 0（bitmap）/ Type 1（RIV） |
| 時間割当 | 固定（1 サブフレーム） | SLIV（Start and Length Indicator Value）+ K0/K2 |
| RBG サイズ | 帯域幅依存の固定テーブル | Configuration 1 / Configuration 2 |
| VRB-to-PRB mapping | Distributed + Localized | Interleaved + Non-interleaved |
| Mini-slot 割当 | なし | 2/4/7 シンボル単位の割当 |

**勉強会で注目すべきポイント**
- SLIV のエンコーディング方法（なぜこの圧縮方式か）
- Type 0 vs Type 1 の使い分け（UE category, traffic type）
- TDRA table の RRC 設定とデフォルトテーブル

---

### E-6. TBS Determination

**定義と背景（Why）**
Transport Block Size の決定手順。MCS index → modulation order + code rate → 割当 RE 数 → TBS の計算フロー。NR では手順が整理・明確化され、quantization ステップが導入された。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.1.3.2 | TBS determination 手順（DL） |
| TS 38.214 | §6.1.4.2 | TBS determination 手順（UL） |
| TS 38.212 | §5.4.2 | Code block segmentation（TBS → CB 分割） |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| TBS テーブル | TBS index × N_PRB のルックアップテーブル | 算術計算（N_RE × R × Qm × ν → quantize） |
| Quantization | TBS テーブル値 | 8の倍数に round（小 TBS）/ 段階的 granularity |
| DMRS overhead | 固定 | 設定に応じて variable |
| Scaling factor | なし | DL: PDSCH-to-RE ratio, UL: 同様 |

**勉強会で注目すべきポイント**
- テーブル方式から算術方式に変わった理由（柔軟性 vs 実装複雑度）
- TBS の quantization ステップの設計意図

---

### E-7. UE Processing Time

**定義と背景（Why）**
UE が DL 受信から UL 送信（HARQ-ACK 等）までに必要な処理時間の規定。NR では URLLC の低遅延要件に対応するため、capability 1 / capability 2 の2段階を定義。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.3 | PDSCH processing time |
| TS 38.214 | §6.4 | PUSCH preparation time |
| TS 38.213 | §9.2.3 | HARQ-ACK timing と processing time の関係 |
| TS 38.306 | §4 | UE capability（processing time capability） |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 最小処理時間 | 3 ms（Rel-15 short TTI で 2–3 OFDM sym） | Capability 1/2（SCS 依存、最小 ~0.19 ms @ 120 kHz） |
| Capability 報告 | なし（一律） | UE が processing time capability を報告 |
| PDSCH→ACK | n + 4 固定 | K1 で柔軟指定（processing time 以上） |
| PUSCH prep | n + 4 固定 | K2 で柔軟指定（preparation time 以上） |

**勉強会で注目すべきポイント**
- N1/N2（processing time in symbols）の SCS 別の値
- Capability 2 の要件（追加 DMRS 無し等の制約）

---

### E-8. Configured Grant / CBG-based Re-Tx

#### Configured Grant

**定義と背景（Why）**
UE が SR→UL grant の手順を踏まずに、事前設定されたリソースで UL 送信を行う仕組み。URLLC の低遅延、IoT の省シグナリングに有効。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §6.1.2.3 | Configured grant Type 1 / Type 2 |
| TS 38.321 | §5.8.2 | MAC 層での configured grant 手順 |
| TS 38.331 | §6.3.2 | ConfiguredGrantConfig の RRC IE |

**LTE からの主な変化**

| 観点 | LTE (SPS) | NR (Configured Grant) |
|------|-----------|----------------------|
| 名称 | Semi-Persistent Scheduling | Configured Grant |
| Type | 1種類 | Type 1（RRC のみ）, Type 2（RRC + DCI activation） |
| HARQ process | 1 | 複数（設定可能） |
| 繰返し | なし | repK（2/4/8 回繰返し） |

#### CBG-based Re-Tx

**定義と背景（Why）**
Transport Block 内の Code Block Group (CBG) 単位で HARQ 再送を行う仕組み。TB 全体の再送ではなく、エラーが発生した CBG のみを再送することで効率向上。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.1.7 | CBG-based transmission/retransmission（DL） |
| TS 38.212 | §7.3.1.2 | DCI format 1_1 の CBGTI / CBGFI field |
| TS 38.213 | §9.1.3 | CBG-level HARQ-ACK feedback |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 再送単位 | TB 全体 | CBG（2/4/6/8 CBG per TB） |
| HARQ-ACK | 1 bit per TB | 1 bit per CBG |
| DCI overhead | なし | CBGTI/CBGFI field 追加 |

**勉強会で注目すべきポイント**
- Configured Grant Type 1 vs Type 2 の使い分け
- CBG 数の設定と HARQ-ACK overhead のトレードオフ

---

## グループ F: MIMO・参照信号・CSI

### F-1. MIMO

**定義と背景（Why）**
NR MIMO は LTE MIMO を大幅に拡張。最大 256 アンテナポート（gNB）、DL 最大 8 レイヤ（SU-MIMO）、beam management の統合、柔軟な RS 設計が特徴。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §7.4 | DL RS（DMRS, CSI-RS, PT-RS） |
| TS 38.214 | §5.1 | DL MIMO 動作（transmission scheme, precoding） |
| TS 38.214 | §5.2 | CSI 報告 |
| TS 38.211 | §6.4 | UL RS（DMRS, SRS, PT-RS） |
| TS 38.214 | §6.1 | UL MIMO 動作 |
| TR 38.802 | §6 | NR MIMO の Study Item 検討 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 最大 DL レイヤ | 8（TM9/10） | 8（codebook-based / non-codebook-based） |
| 最大 UL レイヤ | 4（Rel-14） | 4 |
| アンテナポート | CRS ベース | DMRS ベース（always-on RS 廃止） |
| Beam management | なし | SSB/CSI-RS による L1/L2 beam 手順 |
| Transmission mode | TM1–TM10 | 単一フレームワーク（DCI + RRC で設定） |
| DMRS | Fixed pattern | Front-loaded + additional DMRS |

**勉強会で注目すべきポイント**
- LTE の TM（Transmission Mode）概念がなくなった理由
- Beam management (P1/P2/P3) 手順
- DMRS の front-loaded 設計の意義（低遅延復調）

---

### F-2. RS Design (Reference Signal)

**定義と背景（Why）**
NR は CRS（Cell-specific RS）を廃止し、用途別の RS を設計。これにより always-on overhead の削減、柔軟な beam 運用、UE 固有のチャネル推定が実現。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.211 | §7.4.1 | DL DMRS（PDSCH/PDCCH） |
| TS 38.211 | §7.4.1.5 | CSI-RS |
| TS 38.211 | §7.4.1.6 | PT-RS（Phase Tracking RS） |
| TS 38.211 | §6.4.1 | UL DMRS（PUSCH/PUCCH） |
| TS 38.211 | §6.4.1.4 | SRS |
| TS 38.214 | §5.1.6 | CSI-RS の設定と用途 |

**NR の RS 体系**

| RS | 用途 | LTE 対応 |
|----|------|----------|
| DMRS | チャネル推定（復調用） | LTE DMRS + CRS の役割を統合 |
| CSI-RS | チャネル状態測定、beam management、RRM | LTE CSI-RS を大幅拡張 |
| PT-RS | 位相雑音追跡（高周波帯） | なし（NR 新規） |
| SRS | UL チャネル推定、beam management | LTE SRS を拡張 |
| SSB (PSS/SSS/PBCH-DMRS) | 同期、セル検出 | LTE PSS/SSS/CRS |
| TRS (Tracking RS) | 時間/周波数追跡 | なし（CSI-RS の特殊設定として実現） |

**勉強会で注目すべきポイント**
- CRS 廃止の意義（overhead 削減、lean carrier 設計）
- DMRS Type 1 vs Type 2（CDM グループ数、最大ポート数）
- PT-RS の必要性（FR2 の位相雑音問題）

---

### F-3. TCI State (Transmission Configuration Indicator)

**定義と背景（Why）**
DL 信号/チャネルに対して、どの RS（SSB or CSI-RS）を spatial QCL source として使うかを UE に指示する仕組み。Beam indication の中核メカニズム。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.1.5 | PDSCH の TCI state 設定 |
| TS 38.213 | §10.1 | PDCCH の TCI state |
| TS 38.331 | §6.3.2 | TCI-State の RRC IE 定義 |
| TS 38.321 | §5.2 | TCI state の MAC CE activation |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| Beam indication | なし（omni 前提） | TCI state で DL beam を指示 |
| 設定方法 | — | RRC（候補リスト）+ MAC CE（activation）+ DCI（dynamic indication） |
| QCL 情報 | CRS ベースの暗黙的 QCL | 明示的 QCL TypeA/B/C/D |

**勉強会で注目すべきポイント**
- TCI state の 3 段階設定（RRC → MAC CE → DCI）
- QCL Type D（spatial）が beam management の要
- Rel-15 の制約（PDSCH の TCI は前スロットの DCI で指示）と Rel-16 以降の改善

---

### F-4. QCL (Quasi Co-Location) RS

**定義と背景（Why）**
ある RS と別の RS が同じ大規模チャネル特性を共有することを UE に通知する仕組み。UE がチャネル推定の際に、どの RS の情報を参照できるかを規定する。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.1.5 | QCL の定義と Type A/B/C/D |
| TS 38.211 | §5.1.5 | QCL assumption のアンテナポートへの適用 |

**QCL Type の定義**

| QCL Type | 共有するパラメータ | 主な用途 |
|----------|-------------------|---------|
| Type A | Doppler shift, Doppler spread, average delay, delay spread | DMRS のチャネル推定補助 |
| Type B | Doppler shift, Doppler spread | 高速移動時 |
| Type C | Doppler shift, average delay | PDSCH DMRS → SSB の参照 |
| Type D | Spatial Rx parameter | ビーム方向（FR2 で必須） |

**LTE からの主な変化**
- LTE でも QCL 概念は存在したが（TM10）、NR では 4 type に体系化
- Type D（spatial QCL）が NR の beam management の根幹

**勉強会で注目すべきポイント**
- QCL Type A–D の使い分け
- TCI state との関係（TCI state = QCL 情報のコンテナ）
- FR1 vs FR2 での QCL 適用の違い

---

### F-5. CSI Framework

**定義と背景（Why）**
NR の CSI 報告フレームワークは LTE より大幅に柔軟化。CSI-RS リソース設定、報告設定、測定設定を分離し、trigger state で動的に組み合わせる。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.2 | CSI 報告の全体構造 |
| TS 38.214 | §5.2.1 | CSI 報告設定（ReportConfig） |
| TS 38.214 | §5.2.2 | CSI-RS リソース設定（ResourceConfig） |
| TS 38.214 | §5.2.3 | CSI 報告量（reportQuantity） |
| TS 38.331 | §6.3.2 | CSI-MeasConfig, CSI-ReportConfig 等の RRC IE |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| CSI-RS | 周期的のみ → aperiodic/semi-persistent 追加 | Periodic / Semi-Persistent / Aperiodic の3モード |
| Report trigger | CQI request bit (1bit) | Trigger state（最大 128 states） |
| Report 内容 | CQI/PMI/RI 一体 | reportQuantity で個別指定可能 |
| 測定-報告の分離 | なし（暗黙） | ResourceConfig, ReportConfig を明示的に分離 |
| Codebook | Type I (Rel-10+) | Type I / Type II |

**勉強会で注目すべきポイント**
- ResourceConfig / ReportConfig / MeasConfig の3層分離設計
- Trigger state による aperiodic CSI の柔軟な起動

---

### F-6. Type I and Type II CSI Codebook

**定義と背景（Why）**
NR の PMI コードブックは2種類。Type I は LTE のコードブックを進化させたもの（低 overhead）。Type II は高精度のチャネル情報フィードバック（高 overhead）で MU-MIMO 性能向上を狙う。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.2.2.2.1 | Type I Single-Panel codebook |
| TS 38.214 | §5.2.2.2.2 | Type I Multi-Panel codebook |
| TS 38.214 | §5.2.2.2.3 | Type II codebook |
| TS 38.214 | §5.2.2.2.4 | Type II Port Selection codebook |

**Type I vs Type II の比較**

| 観点 | Type I | Type II |
|------|--------|---------|
| フィードバック粒度 | ビーム選択（1 beam） | 線形結合（L beams × 係数） |
| Overhead | 低（数十ビット） | 高（数百ビット） |
| 主な用途 | SU-MIMO | MU-MIMO |
| LTE 対応 | Class A codebook 相当 | 新規 |
| ベース構造 | DFT beam (i1, i2) | DFT beam 結合 (amplitude + phase) |
| L (beam 数) | 1 | 2 or 4 |

**勉強会で注目すべきポイント**
- Type II のビーム結合（linear combination）の仕組み
- Type II Port Selection（Rel-15 後期追加）の省 RS overhead 効果
- Rel-16 の Enhanced Type II（圧縮 CSI）への発展

---

### F-7. CSI Reporting Contents

**定義と背景（Why）**
CSI 報告に含まれる具体的な指標（CQI, PMI, RI, CRI, SSBRI, LI, L1-RSRP）の定義とその報告フォーマット。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §5.2.1 | reportQuantity の種類 |
| TS 38.214 | §5.2.2.1 | CQI 定義 |
| TS 38.214 | §5.2.2.2 | PMI 定義 |
| TS 38.214 | §5.2.2.3 | RI 定義 |
| TS 38.214 | §5.2.2.4 | CRI, SSBRI 定義 |
| TS 38.214 | §5.2.2.5 | LI（Layer Indicator）定義 |
| TS 38.212 | §6.3.1 | CSI Part 1 / Part 2 の分割 |

**報告量の一覧**

| 指標 | 説明 | LTE 対応 |
|------|------|----------|
| CQI | Channel Quality Indicator | あり（拡張） |
| PMI | Precoding Matrix Indicator | あり（拡張） |
| RI | Rank Indicator | あり |
| CRI | CSI-RS Resource Indicator | NR 新規 |
| SSBRI | SSB Resource Indicator | NR 新規 |
| LI | Layer Indicator（SU→MU の参考） | NR 新規 |
| L1-RSRP | 参照信号の受信電力 | NR 新規 |

**勉強会で注目すべきポイント**
- CSI Part 1 / Part 2 の分割理由（Part 1 で Part 2 のサイズを UE が報告）
- CRI / SSBRI の beam management での役割
- wideband vs subband reporting の使い分け

---

## グループ G: UL 固有

### G-1. UL MIMO

**定義と背景（Why）**
NR UL は codebook-based と non-codebook-based の2方式をサポート。最大4レイヤ送信。full-power transmission の実現が Rel-16 以降の課題。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.214 | §6.1.1 | UL transmission scheme（codebook / non-codebook） |
| TS 38.214 | §6.1.1.1 | Codebook-based UL MIMO |
| TS 38.214 | §6.1.1.2 | Non-codebook-based UL MIMO |
| TS 38.211 | §6.3.1 | PUSCH の物理構造 |
| TS 38.212 | §7.3.1.1 | DCI format 0_1 の precoding field |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 最大レイヤ | 4（Rel-14） | 4 |
| Precoding 方式 | Codebook-based のみ | Codebook-based + Non-codebook-based |
| Non-codebook | なし | SRS ベースで gNB が precoding を指示 |
| TPMI codebook | 固定テーブル | アンテナ数 1/2/4 対応、full/partial coherence |
| Coherence | Full | Full / Partial / Non-coherent |

**勉強会で注目すべきポイント**
- Codebook-based vs Non-codebook-based の使い分け
- UE antenna coherence（full/partial/non）の影響
- SRS を使った non-codebook UL MIMO の手順

---

### G-2. UL Power Control

**定義と背景（Why）**
NR の UL 電力制御は LTE の open-loop / closed-loop フレームワークを継承しつつ、BWP/beam ごとの設定、path-loss RS の柔軟な選択を追加。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.213 | §7.1 | PUSCH power control |
| TS 38.213 | §7.2 | PUCCH power control |
| TS 38.213 | §7.3 | SRS power control |
| TS 38.213 | §7.4 | PRACH power control |
| TS 38.331 | §6.3.2 | Power control の RRC IE |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| Path-loss RS | CRS（セル共通） | SSB or CSI-RS（beam 別に設定可能） |
| Power control set | 1 set | 複数 set（最大 p0/alpha combination） |
| SRI 連携 | なし | SRS Resource Indicator → power control parameter set の紐付け |
| BWP 依存 | なし | BWP ごとに power control parameter を設定 |
| P0/alpha | セル共通 + UE 固有 | 柔軟な組み合わせ |

**勉強会で注目すべきポイント**
- Beam ベースの path-loss 推定（なぜ CRS 廃止でこの設計になったか）
- Multiple power control parameter sets の使い分け

---

### G-3. Supplemental Uplink (SUL)

**定義と背景（Why）**
高周波帯（例: 3.5 GHz TDD）のカバレッジ不足を補うため、低周波帯（例: 900 MHz FDD UL）を補助 UL として使用する仕組み。CA とは異なり、UE は DL 1CC + UL 2CC（通常 + SUL）として動作。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.300 | §5.2 | SUL の概念（DL carrier + normal UL + SUL） |
| TS 38.213 | §15 | SUL の物理層手順 |
| TS 38.101-1 | Annex | SUL 対応バンド組合せ |
| TS 38.331 | §6.3.2 | SUL の RRC 設定 |

**LTE からの主な変化**

| 観点 | LTE | NR |
|------|-----|-----|
| 概念 | なし（CA で代替） | SUL 専用設計 |
| UL 切替 | — | DCI の SUL indicator で動的切替 |
| PRACH | — | normal UL と SUL 両方に PRACH 設定 |
| CA との違い | — | SUL は独立した DL CC を持たない |

**勉強会で注目すべきポイント**
- SUL vs UL CA の違い（SUL は DL carrier を共有）
- SUL の動的切替メカニズム

---

### G-4. Single UL Transmission

**定義と背景（Why）**
NR Rel-15 では、UE は同一時間に1つの UL キャリアでのみ送信する制約がある（SUL と normal UL の同時送信不可）。これは UE の RF 実装制約（PA 数、干渉）に起因する。

**参照スペック**

| 文書 | セクション | 内容 |
|------|-----------|------|
| TS 38.213 | §15 | UL 送信の切替ルール |
| TS 38.306 | §4 | UE capability（simultaneous Tx） |
| TS 38.101-3 | — | バンド組合せと同時送信能力 |

**議論の変遷**
- Rel-15: Single UL transmission を基本とする合意
- Rel-16 以降: Simultaneous UL transmission の検討開始（CA/DC シナリオ）

**勉強会で注目すべきポイント**
- なぜ Rel-15 で single UL に制限されたか（RF 実装の現実的制約）
- UL switching delay の規定

---

## スペック文書の全体マップ

勉強会で参照する主要 TS のカバレッジ一覧。

| TS | 名称 | カバーするトピック |
|----|------|-------------------|
| **TS 38.211** | Physical channels and modulation | Frame structure, BWP, RS design, PUCCH, PDCCH, SSB, PRACH |
| **TS 38.212** | Multiplexing and channel coding | LDPC, Polar, DCI format, UCI coding, TBS segmentation |
| **TS 38.213** | Physical layer procedures for control | CORESET, search space, HARQ timing, power control, TCI, RLM, SFI |
| **TS 38.214** | Physical layer procedures for data | MCS, TBS, resource allocation, MIMO, CSI framework, codebook |
| **TS 38.215** | Physical layer measurements | RSRP, RSRQ, SINR 定義 |
| **TS 38.300** | NR and NG-RAN overall description | アーキテクチャ、プロトコルスタック概要 |
| **TS 38.321** | MAC protocol | HARQ process, RA 手順, configured grant, BSR |
| **TS 38.331** | RRC protocol | RRC IE 定義（全設定パラメータ） |
| **TS 38.133** | Requirements for support of RRM | 測定精度、ハンドオーバ遅延要件 |
| **TS 38.101-1/2/3** | UE radio transmission and reception | バンド定義、RF 要件 |
| **TR 38.802** | Study on NR access technology | NR Study Item のまとめ（議論経緯） |
| **TR 38.912** | Study on NR access technology (RAN4) | RF feasibility study |
| **TR 38.913** | Study on scenarios and requirements | NR の KPI・要件定義 |

## 推奨学習順序

```
Phase 1: 基盤（フレーム構造を理解しないと全てが分からない）
  A-1 Frame Structure → A-2 Duplex → D-3 BWP

Phase 2: 物理チャネル基礎
  B-1 MCS → B-2 LDPC → B-3 Polar
  C-1 SSB → C-2 PRACH

Phase 3: 制御・データの仕組み
  E-1 Control Channel → E-5 Resource Allocation → E-6 TBS
  E-7 UE Processing Time

Phase 4: HARQ と UL 制御
  E-2 HARQ/SR/CSI → E-3 PUCCH → E-4 UCI Multiplexing
  E-8 Configured Grant / CBG

Phase 5: MIMO・CSI（最も深い領域）
  F-1 MIMO → F-2 RS Design → F-3 TCI → F-4 QCL
  F-5 CSI Framework → F-6 Codebook → F-7 CSI Reporting

Phase 6: UL 固有
  G-1 UL MIMO → G-2 UL Power Control
  G-3 SUL → G-4 Single UL Transmission

Phase 7: モビリティ（Phase 5 の beam 知識が前提）
  D-1 Mobility RRM → D-2 RLM
```

## Next Steps

- [ ] 各トピックの detailed note を個別ファイルに展開する（優先: Phase 1–2）
- [ ] TR 38.802 を通読し、NR Study Item での議論変遷をまとめる
- [ ] 3GPP ポータルで RAN1#86bis–#92 の議事録を確認し、主要合意事項を時系列化する
  - 検索: https://portal.3gpp.org/ → Meeting: R1-86b, R1-87, R1-88, R1-88b, R1-89
- [ ] ShareTechnote (https://www.sharetechnote.com/) の NR 解説ページを補助資料として活用
- [ ] 各トピックの Qualcomm / Ericsson / Samsung 技術ブログ記事を収集
- [ ] `/analyze-gap` で Phase 5（MIMO/CSI）のギャップ分析を実施（知財の重点領域）
