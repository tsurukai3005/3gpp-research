---
title: "ギャップ分析: フレーム構造 — 学術 vs 3GPP vs 実装制約"
parent: frame-structure.md
gap-type: [A, B, C]
axes:
  technology_layer: [phy-waveform, higher-layer, cross-layer]
  generation: [rel-20, rel-21]
  ip: [novelty, inventive-step, spec-mapping]
status: draft
confidence: medium
updated: 2026-04-21
sources:
  - url: https://the-mobile-network.com/2025/08/6g-meeting-settles-on-same-old-air-interface/
    title: "6G meeting settles on same old air interface — RAN1#119 報告"
    accessed: 2026-04-21
  - url: https://arxiv.org/html/2508.08225v1
    title: "Industrial Viewpoints on RAN Technologies for 6G (arXiv 2508.08225)"
    accessed: 2026-04-21
  - url: https://arxiv.org/html/2602.08163
    title: "AFDM: Evolving OFDM Towards 6G+ (arXiv 2602.08163)"
    accessed: 2026-04-21
  - url: https://arxiv.org/html/2602.09834
    title: "6G NTN Waveforms: OTFS, AFDM and OCDM Comparison (arXiv 2602.09834)"
    accessed: 2026-04-21
  - url: https://www.sciencedirect.com/science/article/pii/S2352864824001482
    title: "User-Based Numerology and Waveform approach (DCN, 2024)"
    accessed: 2026-04-21
  - url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12694481/
    title: "AI-Native PHY-Layer in 6G Orchestrated Spectrum-Aware Networks (2025)"
    accessed: 2026-04-21
  - url: https://arxiv.org/html/2510.04413v1
    title: "The Role of ISAC in 6G Networks (arXiv 2510.04413)"
    accessed: 2026-04-21
  - url: https://www.nokia.com/asset/f/214991/
    title: "Nokia — Physical Layer Foundations Powering 6G"
    accessed: 2026-04-21
  - url: https://www.ericsson.com/en/blog/2024/5/future-6g-radio-access-network-design-choices
    title: "Ericsson — Future 6G RAN design choices (2024)"
    accessed: 2026-04-21
  - url: https://www.qualcomm.com/news/onq/2025/06/3gpp-release-20-completing-5g-advanced-evolution-preparing-for-global-6g-standardization
    title: "Qualcomm — 3GPP Release 20"
    accessed: 2026-04-21
  - url: https://research.samsung.com/blog/Physical-Layer-Innovations-Driving-6G-Evolution
    title: "Samsung — Physical Layer Innovations Driving 6G Evolution"
    accessed: 2026-04-21
  - url: https://jwcn-eurasipjournals.springeropen.com/articles/10.1186/s13638-024-02350-y
    title: "Gaussian phase noise in DFT-s-OFDM for sub-THz (EURASIP, 2024)"
    accessed: 2026-04-21
  - url: https://arxiv.org/html/2505.06816
    title: "CLI mitigation with over-the-air pilot forwarding (arXiv, 2025)"
    accessed: 2026-04-21
  - url: https://www.mdpi.com/1099-4300/26/11/994
    title: "GFB-OFDM: Low-Complexity Waveform for Ultra-Wide Bandwidth (MDPI, 2024)"
    accessed: 2026-04-21
  - url: https://www.ericsson.com/en/news/2026/2/ericsson-qualcomm-advance-6g-toward-commercialization
    title: "Ericsson-Qualcomm 6G prototype demo (MWC 2026)"
    accessed: 2026-04-21
related:
  - frame-structure.md
  - operating-bands-channel-arrangement.md
  - ../../40_ideas/frame-structure-ip-opportunities.md
---

# ギャップ分析: フレーム構造

> **分析対象**: フレーム構造・ニューメロロジー・リソース割当の設計
> **基盤ノート**: [frame-structure.md](frame-structure.md)

---

## 3GPP Rel-20 の現状（2026年4月時点）

ギャップ分析の前提となる最新状況:

- **RAN1#119（2025年8月、ベンガルール）**: 6G の DL 波形に **CP-OFDM**、UL に **DFT-s-OFDM** を基本とすることで合意。ただし「新波形の可能性は排除しない」との附帯条件あり
- **Rel-20 SI スコープ（RAN#108 承認、2025年6月）**: 拡張 OFDM 波形・変調、統一フレーム構造（5G-6G 共存）、広帯域ニューメロロジー、ISAC を Day-1 機能として含む
- **Sub-THz は WRC-2027 議題外**: WRC-31（2031年頃）で初めて検討の可能性。学術研究との乖離は極めて大きい
- **Ericsson-Qualcomm MWC 2026 デモ**: 400 MHz CC + 30 kHz SCS を 6-8 GHz cmWave で実証

---

## Gap A: 学術で解決済みだが 3GPP に未取込

### A-1. 遅延ドップラー領域波形（OTFS / AFDM / ODDM）

**ギャップの内容**: 学術界では OFDM の根本的限界（高ドップラー環境での性能劣化）を克服する遅延ドップラー領域波形が活発に研究されている。特に AFDM（Affine Frequency Division Multiplexing）は「OFDM 互換のハードウェアパイプラインを維持しながら軽量な chirp 回転を加えるだけ」で実装可能と主張されている。

**学術での成熟度**:
- OTFS: 理論・シミュレーション成熟。NTN（LEO 衛星）シナリオで OFDM を大幅に凌駕（arXiv 2602.09834）
- AFDM: OFDM 互換パスを重視した設計で産業界への訴求力あり（arXiv 2602.08163）
- ODDM: マルチパス+ドップラーの同時解消を理論的に証明

**3GPP の状況**: RAN1#119 で Jio Platforms が ZAC-OTFS を提唱したが、**シミュレーション不足**を理由に保留。CP-OFDM 基本方針が確定。

**取り込まれていない理由**:
1. **後方互換性**: OFDM ベースのエコシステム（チップ・基地局）との互換性が不透明
2. **コンセンサス未形成**: 主要ベンダー（Ericsson, Qualcomm, Nokia）が OFDM 継続で一致
3. **シミュレーション不足**: 3GPP 評価方法論（TDL/CDL チャネルモデル）での公正比較が未完了
4. **タイミング**: Sub-THz（OTFS が最も有利な帯域）が WRC-2027 議題外

**知財評価**:
- novelty: 低（OTFS/AFDM 自体は既に特許出願多数）
- inventive-step: 中（OFDM→OTFS/AFDM の移行手順、後方互換性確保に余地）
- spec-mapping: **現時点では低**（3GPP 採用の見込みが薄い）→ Rel-21 以降で状況変化の可能性

**関連軸**: 技術レイヤー（phy-waveform）、世代（rel-21+）、市場（ntn, b2b-industrial）

---

### A-2. AI/ML ベースの動的ニューメロロジー選択

**ギャップの内容**: NR では SCS はセル/BWP 単位で半静的に設定される。学術では UE 個別に環境（遅延拡散、ドップラー、SNR）に応じてニューメロロジーを動的に選択する手法が提案されている。

**学術での提案**:
- DNN による最適ニューメロロジー推定（パワー遅延プロファイル + 速度 + 雑音電力から学習）（arXiv 2011.04247）
- User-Based Numerology and Waveform (UBNW): ユーザーごとに波形 + SCS を割当て、INI を抑制（DCN, 2024）
- AI ネイティブ PHY: SCS/FFTサイズ/スロット長/CP種別を上位層シグナリングなしで推定（PMC, 2025）

**3GPP の状況**: Rel-18/19 で AI/ML の CSI フィードバックや位置推定は SI 化されたが、**ニューメロロジー選択への AI 適用は SI/WI に含まれていない**。

**取り込まれていない理由**:
1. **シグナリング設計の困難**: UE 個別の SCS を動的に切り替えるための DCI/RRC 設計が未整理
2. **INI 問題の拡大**: 同一セル内で異なる SCS の UE が混在すると INI が深刻化
3. **実装複雑性**: UE 側に複数ニューメロロジーの同時受信能力が必要

**知財評価**:
- novelty: 中（AI/ML × ニューメロロジーの組み合わせ自体はまだ先行技術が少ない）
- inventive-step: **高**（「AI が出力した SCS をどう DCI で通知するか」「切替時の中断回避」に実装制約ギャップ）
- spec-mapping: 中（Rel-21 以降の AI ネイティブ PHY で仕様化の可能性あり）

**関連軸**: 技術レイヤー（cross-layer）、価値（latency, energy-efficiency）

---

### A-3. ISAC フレーム設計（ペイロードベースセンシング）

**ギャップの内容**: 従来の ISAC 研究はパイロット信号をセンシングに流用する設計だが、最新の学術研究では**データペイロード自体をセンシングに使う**パラダイムシフトが提案されている。

**学術での提案**:
- Payload-Based Sensing: パイロット不要のセンシングで spectral efficiency を維持（ResearchGate, 2024）
- OFDM レーダー/通信のリソース分割最適化（Springer, 2025）
- ISAC 向けフレーム構造: センシング専用シンボルの動的挿入

**3GPP の状況**: ISAC は Rel-20 SI で Day-1 機能に指定。ただしフレームレベルのリソース分割設計（通信シンボル vs センシングシンボルの配分）は**まだ具体的議論に入っていない**。

**取り込まれていない理由**:
1. **タイミング**: SI 開始直後（2025年8月〜）で詳細設計フェーズに至っていない
2. **KPI 未確定**: センシング精度と通信品質のトレードオフ評価基準が未合意

**知財評価**:
- novelty: **高**（ペイロードベースセンシングのフレーム構造設計は先行技術が少ない）
- inventive-step: **高**（データシンボルからセンシング情報を抽出する際の実装制約が豊富）
- spec-mapping: **高**（Rel-20/21 で仕様化される見込み。"shall" 文言に対応するクレーム設計が可能）

**関連軸**: 技術レイヤー（phy-waveform, cross-layer）、市場（b2b-industrial）、知財（spec-mapping）

> **特許戦略上の最重要ギャップ**: ISAC は 3GPP で確実に仕様化される方向であり、かつフレーム設計の詳細が未確定。学術提案と実装制約の差を埋める特許が SEP になる確率が最も高い。

---

## Gap B: 3GPP で FFS / 議論中かつ学術でも活発

### B-1. 5G-6G 統一フレーム構造（スペクトラム共有）

**ギャップの内容**: Rel-20 SI スコープに「unified frame structure for 5G-6G spectrum sharing」が含まれている。5G NR と 6G が同一帯域を共有する際のフレーム構造の共存設計。

**議論の状況**:
- 3GPP: SI 段階で詳細設計はこれから [要確認: RAN1#120 以降の Chairman's Notes]
- 学術: 5G/6G 共存シナリオの研究は限定的。DSS (Dynamic Spectrum Sharing) の 4G/5G 版からの延長が主

**論点**:
- 同一キャリアで異なるニューメロロジーの 5G UE と 6G UE が共存できるか
- 6G 新機能（ISAC シンボル等）を 5G UE が無視できるフレーム設計
- SSB（同期信号ブロック）の設計変更と後方互換性

**知財評価**:
- novelty: **高**（5G-6G 共存フレームは新しいテーマ）
- inventive-step: **高**（後方互換性 + 新機能導入のトレードオフに豊富な制約）
- spec-mapping: **最高**（Rel-20/21 で確実に仕様化。SI→WI の過程で "shall" 文言が生まれる）

---

### B-2. 広帯域ニューメロロジー（FR1 拡張 / cmWave）

**ギャップの内容**: 6-8 GHz cmWave 帯での 200 MHz 以上のキャリア帯域幅をサポートするニューメロロジーの設計。Ericsson-Qualcomm が MWC 2026 で 400 MHz CC + 30 kHz SCS のデモを実施。

**議論の状況**:
- 3GPP: Rel-20 SI スコープに含まれる。具体的 SCS / 最大 RB 数は FFS
- 産業界: Ericsson は「8k FFT で既存ニューメロロジーセットを維持」を提唱。cmWave に最適な SCS は 30 kHz が有力
- 学術: Adaptive OFDM Numerology + Carrier Aggregation for THz（IEEE, 2023）

**論点**:
- 30 kHz SCS で 400 MHz → 必要 FFT サイズ = 約 16k（実装可能か？）
- 新しいμ値を追加するか、既存μ=1 (30 kHz) を広帯域に拡張するか
- 最大 RB 数 275 の制約を緩和するか

**知財評価**:
- novelty: 中（ニューメロロジーの広帯域拡張は自然な延長）
- inventive-step: 中〜高（大 FFT サイズでの実装制約、位相雑音、PA 線形性）
- spec-mapping: **高**（Rel-20 WI で確実にパラメータが確定）

---

### B-3. DFT-s-OFDM の DL 利用と SU-MIMO 対応

**ギャップの内容**: NR では DFT-s-OFDM は UL single-layer のみに限定される。Nokia が 6G では DL にも DFT-s-OFDM を使い、かつ SU-MIMO マルチレイヤに対応させることを提案。

**学術/産業の提案**:
- Nokia: FDSS-SE（Frequency Domain Spectrum Shaping with Spectrum Extension）により最小 PAPR を実現。DFT-s-OFDM の SU-MIMO 多層対応が 6G で新規（Nokia White Paper）
- Samsung: 1D geometric constellation shaping で高次変調の効率改善

**3GPP の状況**: Rel-20 SI で「enhanced OFDM-based waveforms」の範囲に含まれる。DFT-s-OFDM の DL 適用は議論の入口段階。

**知財評価**:
- novelty: **高**（DFT-s-OFDM の DL マルチレイヤ送信は NR にない新概念）
- inventive-step: **高**（低 PAPR と MIMO 空間多重の両立に技術的困難がある）
- spec-mapping: 高（Rel-20/21 で仕様化の可能性）

---

## Gap C: 実装制約ギャップ（進歩性の最大の源泉）

### C-1. インターニューメロロジー干渉（INI）の抑制

| 論文の仮定 | 実装制約 |
|-----------|---------|
| UE ごとに波形 + SCS を動的に割当て可能 | BWP 単位の半静的設定。同時アクティブ BWP は 1 つのみ |
| 適応的ガードバンドで最適化 | **固定ガードバンド**で保守的に対処（帯域利用効率低下） |
| クロスレイヤ最適化で INI を理論的に最小化 | DCI/RRC のビット数制約で細粒度制御不可能 |

**具体的な制約差分**:
- NR は異なる SCS の BWP 間に**固定の guard band**（SCS 依存、数 RB 分）を設ける
- 学術の UBNW 手法はユーザー単位で波形を変えるが、NR の DCI format では**BWP 内は単一 SCS**が前提
- 6G で SCS の選択肢が増えれば INI 問題はさらに深刻化

**知財機会**: 「固定ガードバンドを動的に最適化する手法」「異なる SCS 間の干渉推定・補償をシグナリングオーバーヘッド最小で実現する方法」

**知財評価**:
- novelty: 中（INI 研究自体は多い）
- inventive-step: **高**（DCI ビット制約内で動的制御する工夫に進歩性）
- spec-mapping: 高（TS 38.211/214 のガードバンド設計に直接対応）

---

### C-2. Sub-THz 位相雑音とフレーム設計の両立

| 論文の仮定 | 実装制約 |
|-----------|---------|
| DNN ベースの位相雑音補償（無限計算資源） | UE 側の演算リソースは限定的。リアルタイム DNN 推論は消費電力制約 |
| OTFS/AFDM は本質的に位相雑音耐性が高い | 3GPP は OFDM 継続を決定。OTFS は不採用 |
| 理想的な発振器特性を仮定 | Sub-THz ではガウシアン位相雑音が支配的（相関構造を持たない → 補償困難） |
| 連続値の位相補正 | PT-RS (Phase Tracking RS) のシンボル密度は DCI で設定。ビット制約あり |

**具体的な制約差分**:
- 3GPP の主な位相雑音対策は **SCS 拡大**（ICI 低減）+ **PT-RS**（位相追跡）
- SCS 拡大は ADC/DAC サンプリングレートの比例的増加を要求 → **消費電力が指数的に増加**
- Sub-THz（100 GHz+）ではシンボル長が μs 以下になり、**CP 長が遅延拡散をカバーできない**可能性
- ガウシアン位相雑音（白色成分）は相関構造がなく、既存の PT-RS ベース補償は効率が悪い

**知財機会**: 「SCS 拡大に依存しない位相雑音補償と組み合わせた CP 設計」「PT-RS 密度の動的適応（位相雑音レベルに応じた DCI シグナリング）」「ガウシアン位相雑音に特化した低複雑度補償アルゴリズム」

**知財評価**:
- novelty: **高**（sub-THz 特有のガウシアン位相雑音対策は先行技術が少ない）
- inventive-step: **最高**（論文の理想仮定と実装制約の差が最も大きい領域）
- spec-mapping: 中（sub-THz は WRC-31 待ち。ただし FR2-2 (52.6-71 GHz) では Rel-20/21 で適用可能）

> **原則2 の体現**: 「論文は理想発振器を仮定するが、sub-THz では位相雑音がガウシアン的で従来手法が効かない」という差分こそが進歩性の核心。

---

### C-3. 動的 TDD クロスリンク干渉（CLI）管理

| 論文の仮定 | 実装制約 |
|-----------|---------|
| セル単位で自由に TDD パターンを変更可能 | 隣接セルの CLI を考慮すると**ネットワーク全体の同期が前提** |
| マルチエージェント DRL で最適パターン探索 | O-RAN rApps/xApps での推論遅延、バックホール遅延 |
| 完全 CSI + 完全 CLI 情報 | CLI 測定（SRS-for-CLI）のオーバーヘッド、限られた測定リソース |
| OTA パイロット転送で CLI を相殺 | パイロット転送のための新シグナリング未規格化 |

**具体的な制約差分**:
- 現実の商用網では**全セル同一 TDD パターン**が主流（CLI 回避のため）→ トラフィック非対称性に対応不可
- 3GPP Rel-16 で CLI 測定（SRS-for-CLI, CLI-RSSI）は導入されたが、**測定に基づく動的パターン変更手順は未規格化**
- 学術の DRL 手法は数十〜数百セルの協調を仮定するが、セル間シグナリングの遅延（X2/Xn 経由）がボトルネック

**知財機会**: 「CLI 測定結果に基づくスロットフォーマットの半動的適応手順」「限られた X2 シグナリングで隣接セル TDD パターンを協調する方法」「CLI-aware なスロットフォーマット選択テーブル」

**知財評価**:
- novelty: 中（CLI 緩和手法は多数）
- inventive-step: **高**（バックホール遅延 + 測定オーバーヘッドの制約下での実用解に進歩性）
- spec-mapping: **高**（TS 38.213 のスロットフォーマット設定に直接関連。Rel-20 で強化の可能性）

---

### C-4. BWP 切替遅延と URLLC の両立

| 論文の仮定 | 実装制約 |
|-----------|---------|
| BWP 切替は瞬時（0 ms） | NR では **Type 1: 0.5-1 ms、Type 2: 最大数 ms** の中断 |
| 共同最適化（DRX + BWP タイマー + トラフィック予測） | DRX サイクルと BWP 不活性タイマーの**独立動作**（協調 API なし） |
| 任意の BWP に即座に遷移 | 最大 4 BWP の制約。切替は DCI または不活性タイマーのみ |

**具体的な制約差分**:
- BWP 再構成は 80-100 ms（RRC 再構成含む）。URLLC の 1 ms 要件と相容れない
- 切替中はデータ送受信が中断 → パケットロスの原因
- 学術の joint optimization は DRX + BWP + スケジューリングの三位一体だが、NR ではこれらが**異なるレイヤ/タイマーで独立動作**

**知財機会**: 「BWP 切替中のデータバッファリング + 即時再送手順」「予測ベースの事前 BWP プリロード（DCI で次の BWP を予告）」「URLLC トラフィック検出時の高速 BWP フォールバック」

**知財評価**:
- novelty: 中（BWP 切替最適化は既存研究あり）
- inventive-step: 中〜高（URLLC 要件との両立に制約あり）
- spec-mapping: 高（TS 38.213/214 の BWP 操作に直接対応）

---

### C-5. エネルギー効率駆動のフレーム設計

| 論文の仮定 | 実装制約 |
|-----------|---------|
| シンボル単位の精密なスリープ制御 | DRX はサブフレーム/スロット単位。シンボル粒度の省電力は未対応 |
| AI/ML で最適なスリープスケジュール | AI/ML ベースの省電力は 3GPP で SI 段階（Rel-18 AI/ML for NR） |
| ネットワーク側のエネルギー最適化 | 3GPP は主に UE 側省電力に注力。基地局省電力は運用上の実装依存 |
| ゼロエネルギーデバイス対応フレーム | Ambient IoT は Rel-19 で Type 1 のみ。フレーム設計は限定的 |

**知財機会**: 「PDCCH モニタリング不要期間のシンボルレベル通知」「ネットワークエネルギー効率を考慮した SSB 送信パターン適応」「ゼロエネルギーデバイス向け超簡易フレーム構造」

**知財評価**:
- novelty: 中（省電力フレーム研究は多い）
- inventive-step: 中（シンボル粒度制御 + シグナリング設計に制約差分あり）
- spec-mapping: 高（Rel-20 でネットワークエネルギー効率が主要 KPI に昇格）

---

## ギャップ間の相互関係

```
A-2 (AI ニューメロロジー) ──→ C-1 (INI 悪化)
     動的 SCS 切替が INI を拡大。C-1 の解決なしに A-2 は実現困難

A-3 (ISAC フレーム) ──→ B-1 (5G-6G 共存)
     ISAC シンボルを 5G UE が無視できるフレーム設計が必要

C-2 (位相雑音) ──→ B-2 (広帯域ニューメロロジー)
     cmWave/sub-THz の広帯域化は位相雑音問題を伴う

C-3 (CLI) ──→ C-5 (省電力)
     動的 TDD は省電力（不要 DL シンボル停止）と表裏一体

B-3 (DFT-s-OFDM DL) ──→ C-2 (位相雑音)
     低 PAPR 波形は sub-THz 位相雑音環境で有利
```

---

## 知財優先度ランキング

| 順位 | ギャップ | 理由 |
|------|---------|------|
| **1** | **A-3: ISAC フレーム設計** | 3GPP 仕様化が確実 + 詳細未確定 + 学術提案と実装制約の差が豊富 |
| **2** | **B-1: 5G-6G 統一フレーム** | Rel-20 で確実に仕様化 + 後方互換性の制約が進歩性の源泉 |
| **3** | **C-2: Sub-THz 位相雑音×フレーム設計** | 理想仮定と実装制約の差が最大 + 先行技術少 |
| **4** | **B-3: DFT-s-OFDM DL マルチレイヤ** | 新規概念 + MIMO との両立に進歩性 |
| **5** | **C-3: CLI 管理** | 実用的需要大 + Rel-20 で強化見込み |
| **6** | **C-1: INI 動的制御** | 6G でニューメロロジー増加により重要性増大 |
| **7** | **B-2: 広帯域ニューメロロジー** | パラメータ確定時に SEP 可能だが自然な延長 |
| **8** | **A-2: AI ニューメロロジー** | 革新的だが 3GPP 採用時期が不透明 |
| **9** | **C-4: BWP 切替遅延** | 改善余地あるが既存解がある程度機能 |
| **10** | **C-5: 省電力フレーム** | 重要だがコア技術よりは周辺 |

---

## ベンダーポジション対照表

| ベンダー | 波形 | フレーム設計の力点 | 注目提案 |
|---------|------|------------------|---------|
| **Ericsson** | OFDM 継続。新波形不要 | 8k FFT、既存 SCS セット維持 | cmWave 400 MHz CC + 30 kHz SCS |
| **Qualcomm** | OFDM 基盤 + 測位対応波形 | スペクトラム閉じ込め、FDD/TDD 協調 | 6-8 GHz cmWave に注力 |
| **Nokia** | CP-OFDM + 拡張 DFT-s-OFDM | **DFT-s-OFDM の DL/MIMO 対応** | FDSS-SE で最小 PAPR |
| **Samsung** | OFDM + 符号化/変調革新 | LDPC 省エネ最適化、PAC 符号 | 1D geometric constellation shaping |
| **Huawei** | THz 通信 + NTN | [要確認: 具体的フレーム提案] | 6G 特許出願数で世界リード |
| **Jio** | ZAC-OTFS 推進 | OFDM 代替を主張 | RAN1#119 で保留に |

---

## Next Steps

- [ ] 3GPP ポータルで RAN1#120〜#122 の Chairman's Notes を確認し、ISAC フレーム設計の FFS 項目を特定
- [ ] `/digest-paper` で AFDM 論文 (arXiv 2602.08163) を詳細分析 — OFDM 互換パスの実装制約を評価
- [ ] `/digest-paper` で Nokia の FDSS-SE DFT-s-OFDM white paper を分析 — DL MIMO 対応の技術的課題を整理
- [ ] arXiv で "ISAC frame design 3GPP" を検索し、最新の仕様化提案を収集
- [ ] `/connect-dots` で「ISAC フレーム設計 × MIMO ビーム管理」の組合せ価値を分析
- [ ] `/demand-reverse` で「工場自動化ペルソナ × 動的 TDD」の需要接点を確認
- [ ] ETSI IPR データベースで "frame structure" "numerology" "ISAC" 関連の SEP 宣言を検索し、特許ランドスケープを把握
- [ ] TR 38.913 後継の 6G 要件 TR（RAN#112 予定）のドラフトを追跡
