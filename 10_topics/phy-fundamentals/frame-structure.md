---
title: フレーム構造とリソースブロック — 4G LTE から 5G NR、6G への進化
axes:
  technology_layer: [phy-waveform, higher-layer]
  generation: [rel-8, rel-15, rel-17, rel-20]
  value: [latency, energy-efficiency, throughput]
  market: [consumer-xr, b2b-industrial, ntn]
  adoption: [backward-compat, standard-convergence]
  ip: [inventive-step, spec-mapping]
status: draft
confidence: high
updated: 2026-04-20
sources:
  - url: https://www.etsi.org/deliver/etsi_ts/138200_138299/138211/18.02.00_60/ts_138211v180200p.pdf
    title: "ETSI TS 138 211 V18.2.0 — NR Physical channels and modulation"
    accessed: 2026-04-20
  - url: https://www.3gpp.org/specifications-technologies/releases/release-20
    title: "3GPP Release 20 公式ページ"
    accessed: 2026-04-20
  - url: https://www.qualcomm.com/media/documents/files/whitepaper-making-5g-nr-a-reality.pdf
    title: "Qualcomm — Making 5G NR a Reality (2016)"
    accessed: 2026-04-20
  - url: https://www.ericsson.com/en/blog/2017/8/three-design-principles-of-5g-new-radio
    title: "Ericsson — Three Design Principles of 5G New Radio (2017)"
    accessed: 2026-04-20
  - url: https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/designing-for-the-future-the-5g-nr-physical-layer
    title: "Ericsson Technology Review — Designing for the Future: The 5G NR Physical Layer"
    accessed: 2026-04-20
  - url: https://arxiv.org/abs/2306.09183
    title: "Waveforms for sub-THz 6G: Design Guidelines"
    accessed: 2026-04-20
  - url: https://www.interdigital.com/post/paving-the-path-to-6g-key-takeaways-for-3gpp-release-20
    title: "InterDigital — Paving the Path to 6G: Key Takeaways for 3GPP Release 20"
    accessed: 2026-04-20
  - url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8038383/
    title: "5G Numerologies Assessment for URLLC in Industrial Communications"
    accessed: 2026-04-20
  - url: https://www.sharetechnote.com/html/5G/5G_FrameStructure.html
    title: "ShareTechNote — 5G Frame Structure"
    accessed: 2026-04-20
  - url: https://www.keysight.com/blogs/en/inds/2018/09/07/5g-flexible-numerology-defining-what-it-is-and-explaining-why-you-should-care
    title: "Keysight — 5G Flexible Numerology"
    accessed: 2026-04-20
related:
  - ../cross-cutting/waveform-design.md
  - ../phy-fundamentals/resource-allocation.md
  - operating-bands-channel-arrangement.md
---

## 1. 定義と背景（Why）

### フレーム構造とは

無線通信では、時間軸と周波数軸を格子状に区切って送受信を管理する。この格子の区切り方を**フレーム構造**と呼ぶ。フレーム構造は以下を規定する:

- **時間方向**: フレーム → サブフレーム → スロット → OFDM シンボル
- **周波数方向**: サブキャリア → リソースブロック (RB) → 帯域幅パート (BWP)
- **時間×周波数の最小単位**: リソースエレメント (RE) = 1 サブキャリア × 1 OFDM シンボル

### なぜ必要とされたか

4G LTE のフレーム構造は **固定的** だった（15 kHz SCS、1 ms TTI）。5G NR では以下の要求が生じた:

1. **多様なユースケース**: eMBB（大容量）、URLLC（超低遅延）、mMTC（大量接続）を1つの基盤で
2. **広帯域化**: mmWave（ミリ波）での 400 MHz 帯域幅をサポート
3. **低遅延**: 1 ms 以下の無線区間レイテンシ
4. **前方互換性**: 将来のリリースで新機能を追加可能な設計

これらを実現するために **スケーラブル・ニューメロロジー**（可変サブキャリア間隔）と**柔軟なスロット構成**が設計された。

---

## 2. 技術要点（What）

### 2.1 NR フレーム階層構造

```
Radio Frame (10 ms)
├── Half-frame 0 (5 ms)
│   ├── Subframe 0 (1 ms)
│   │   ├── Slot 0   [14 OFDM symbols]  ← μ=0 なら 1 スロット/サブフレーム
│   │   ├── Slot 1   [14 OFDM symbols]  ← μ=1 なら 2 スロット/サブフレーム
│   │   └── ...
│   ├── Subframe 1
│   └── ...Subframe 4
├── Half-frame 1 (5 ms)
│   └── Subframe 5〜9
```

- **フレーム**: 10 ms（LTE と同じ）
- **サブフレーム**: 1 ms（LTE と同じ。互換性のアンカー）
- **スロット**: 14 OFDM シンボル（Normal CP）。持続時間はニューメロロジーに依存

### 2.2 スケーラブル・ニューメロロジー

NR の最大の設計革新。サブキャリア間隔 (SCS) を `15 × 2^μ kHz` のべき乗でスケーリングする。

| μ | SCS (kHz) | スロット長 | スロット/サブフレーム | スロット/フレーム | 主な用途 |
|---|-----------|-----------|---------------------|-----------------|---------|
| 0 | 15 | 1 ms | 1 | 10 | FR1 低帯域、LTE との共存 |
| 1 | 30 | 0.5 ms | 2 | 20 | FR1 中帯域（主流） |
| 2 | 60 | 0.25 ms | 4 | 40 | FR1/FR2 境界、Extended CP 対応 |
| 3 | 120 | 125 μs | 8 | 80 | FR2 mmWave |
| 4 | 240 | 62.5 μs | 16 | 160 | SS/PBCH のみ（FR2） |

> **Rel-17 以降の拡張**: μ=5 (480 kHz)、μ=6 (960 kHz) が FR2-2（52.6〜71 GHz）向けに追加。

**SCS 選択のトレードオフ**:
- SCS ↑ → スロット短縮 → **低遅延化** + **位相雑音耐性向上**（高周波帯で重要）
- SCS ↑ → シンボル長短縮 → **CP 長短縮** → **マルチパス耐性低下**
- SCS ↑ → 帯域幅あたりの RB 数減少 → **周波数選択性スケジューリングの粒度低下**

### 2.3 OFDM シンボルとサイクリックプレフィックス (CP)

| μ | シンボル長 (μs) | Normal CP 長 (μs) | CP オーバーヘッド |
|---|----------------|-------------------|-----------------|
| 0 | 66.67 | 4.69 | ~7% |
| 1 | 33.33 | 2.34 | ~7% |
| 2 | 16.67 | 1.17 | ~7% |
| 3 | 8.33 | 0.57 | ~7% |

- **Normal CP**: 14 シンボル/スロット（全ニューメロロジー）
- **Extended CP**: 12 シンボル/スロット（μ=2 のみ。大遅延拡散環境用）

### 2.4 ミニスロット（非スロットベーススケジューリング）

スロット全体を待たずに送信を開始できる仕組み。

- 長さ: **2、4、または 7 OFDM シンボル**
- スロット内の**任意のシンボル位置から開始可能**
- 主なユースケース:
  - **URLLC**: 低遅延が必要な場合、次のスロット境界を待たない
  - **プリエンプション**: 進行中の eMBB 送信を中断して URLLC を挿入
  - **Unlicensed band (NR-U)**: LBT (Listen Before Talk) 後の即時送信

### 2.5 スロットフォーマット

TDD で DL/UL のシンボル配分を柔軟に制御する仕組み。

- 各 OFDM シンボルを **D**（下り）、**U**（上り）、**F**（柔軟）に設定
- 61 の定義済みスロットフォーマット（TS 38.213 Table 11.1.1-1）
- SFI (Slot Format Indicator) を DCI format 2_0 で動的に指定可能
- 例: `DDDDDDDDDDDDFU` = 13 DL + 1 flexible + 最後の GP/UL

### 2.6 リソースブロック (RB) とリソースグリッド

#### 基本定義

| 概念 | 定義 |
|------|------|
| **リソースエレメント (RE)** | 1 サブキャリア × 1 OFDM シンボル（最小単位） |
| **リソースブロック (RB)** | 12 連続サブキャリア（周波数方向のみ） |
| **リソースグリッド** | 特定のニューメロロジーにおける周波数×時間の2次元格子 |

> **LTE との違い**: LTE では RB = 12 サブキャリア × 7 シンボル（時間含む）だったが、NR では RB は**周波数方向のみ**で定義。時間方向はスロット/ミニスロット単位でスケジューリング。

#### Point A と CRB ナンバリング

- **Point A**: CRB 0 のサブキャリア 0 の中心周波数（絶対基準点）
- **CRB (Common Resource Block)**: Point A から連番。キャリア帯域外にも存在し得る
- **PRB (Physical Resource Block)**: BWP 内でのローカル番号
- 変換式: `CRB = PRB + N_start_BWP`

#### Bandwidth Part (BWP)

キャリア帯域幅の**連続部分集合**に単一ニューメロロジーを割り当てる仕組み。

- UE あたり最大 **4 BWP** 設定可能（DL/UL 各々）
- 同時アクティブは **1 BWP のみ**
- 目的:
  - **省電力**: 狭い BWP で受信帯域を削減
  - **能力適応**: 端末能力に応じた帯域幅設定
  - **混合ニューメロロジー**: 異なる SCS の BWP を切替

#### 最大 RB 数

| μ | SCS (kHz) | 最大 RB 数 | 最大帯域幅概算 | 周波数レンジ |
|---|-----------|-----------|-------------|------------|
| 0 | 15 | 275 | ~50 MHz | FR1 |
| 1 | 30 | 275 | ~100 MHz | FR1 |
| 2 | 60 | 275 | ~200 MHz | FR1/FR2 |
| 3 | 120 | 275 | ~400 MHz | FR2 |
| 4 | 240 | 138 | ~400 MHz | FR2 |

周波数レンジ定義:
- **FR1**: 410 MHz〜7125 MHz（最大キャリア帯域幅 100 MHz）
- **FR2**: 24.25〜52.6 GHz（最大 400 MHz）
- **FR2-2** (Rel-17): 52.6〜71 GHz

---

## 3. 実装制約（How）

### 3GPP 仕様への落とし込み

| 仕様書 | 内容 |
|--------|------|
| **TS 38.211** | フレーム構造、ニューメロロジー、リソースグリッド定義 |
| **TS 38.213** | スロットフォーマット設定、DCI/SFI |
| **TS 38.214** | PDSCH/PUSCH スケジューリング（ミニスロット含む） |
| **TS 38.101-1/2** | 帯域幅設定、最大 RB 数（FR1/FR2） |
| **TS 38.912** | NR スタディフェーズ結論 |
| **TR 38.913** | NR 要件（フレーム設計の駆動要因） |

### シグナリングの制約

- **DCI (Downlink Control Information)**: スロットフォーマット、BWP 切替、ミニスロットスケジューリングを数ビットで指定
- **RRC シグナリング**: BWP 設定、ニューメロロジー設定を半静的に通知
- **MAC CE**: BWP アクティベーション切替

### ハードウェア実装の制約

- **FFT サイズ**: SCS に応じて 4096（μ=0, 50 MHz）〜 4096（μ=3, 400 MHz）程度
- **ADC/DAC サンプリングレート**: 広帯域ほど高速サンプリング必要（消費電力増加）
- **位相雑音**: 高周波帯（FR2以上）では発振器品質がボトルネック → 広い SCS で対処
- **バッファリング**: ミニスロットスケジューリングは HARQ バッファ管理を複雑化

---

## 4. 前世代との差分

### LTE（4G）vs NR（5G）フレーム構造比較

| パラメータ | LTE (TS 36.211) | NR (TS 38.211) |
|-----------|----------------|----------------|
| SCS | **15 kHz 固定** | 15/30/60/120/240 kHz |
| フレーム | 10 ms | 10 ms |
| サブフレーム | 1 ms | 1 ms |
| スロット | 0.5 ms 固定 | 1 ms / 2^μ（可変） |
| シンボル/スロット | 7 (Normal CP) | 14 (Normal CP) |
| 最小スケジューリング単位 | 1 ms (サブフレーム) | **1 シンボル（ミニスロット）** |
| 最大キャリア帯域幅 | 20 MHz | 100 MHz (FR1) / 400 MHz (FR2) |
| 最大 RB 数 | 100 | 275 |
| RB 定義 | 12 SC × 7 sym | **12 SC（周波数のみ）** |
| BWP | なし | **あり（最大 4 per cell）** |
| TDD DL/UL | サブフレーム単位 | **シンボル単位** |
| 参照信号 | セル固有 CRS（常時送信） | **オンデマンド（リーン設計）** |

### LTE の限界と NR の解決策

| LTE の限界 | NR の解決策 | 効果 |
|-----------|-----------|------|
| 15 kHz 固定 → mmWave で位相雑音に弱い | スケーラブル SCS | mmWave 運用が可能に |
| 1 ms TTI → URLLC に不十分 | ミニスロット + 短スロット | 0.125 ms 以下のスケジューリング |
| 20 MHz 最大 → スループット上限 | 最大 400 MHz キャリア | ピーク 20 Gbps 級 |
| 固定 DL/UL 比 → TDD 効率低下 | シンボルレベル DL/UL | トラフィック非対称性に対応 |
| 常時 CRS 送信 → 電力浪費 | リーン設計（CSI-RS オンデマンド） | ネットワークエネルギー効率向上 |
| 単一帯域幅で動作 → 端末省電力困難 | BWP → 狭帯域モード切替 | 端末バッテリー寿命改善 |

### 3G UMTS からの進化の文脈

| 世代 | 多重方式 | 時間単位 | 帯域幅 |
|------|---------|---------|--------|
| 3G (WCDMA) | CDMA | 10 ms TTI | 5 MHz |
| 4G (LTE) | OFDMA | 1 ms TTI | 20 MHz |
| 5G (NR) | OFDMA + 柔軟ニューメロロジー | 62.5 μs〜1 ms | 400 MHz |

---

## 5. 主要プレイヤー

### 学術・標準化での貢献

| 企業 | 主な貢献 | 文書・発表 |
|------|---------|-----------|
| **Qualcomm** | スケーラブル OFDM ニューメロロジーの主提唱者。CP-OFDM + WOLA 窓関数。前方互換性の設計哲学 | "Making 5G NR a Reality" (2016年12月) |
| **Ericsson** | 3つの設計原則（Ultra-lean、前方互換性、ビーム中心）。CP-OFDM 合意形成のキーロール | "Three Design Principles of 5G New Radio" (2017年8月) |
| **Nokia Bell Labs** | 柔軟 TDD フレーム構造。f-OFDM（mixed numerology）。URLLC ミニスロット/プリエンプション | 各種 RAN1 Tdoc |
| **Samsung** | NR SI/WI でのスロット構造・TDD パターンへの貢献 | RAN1 寄書多数 |
| **Huawei** | フレーム構造議論（RAN1#86/86bis）。柔軟 UL/DL 配分の提案 | RAN1#86 関連 Tdoc |
| **InterDigital** | Rel-20 / 6G 物理層研究への活発な参加 | "Paving the Path to 6G" (2025) |

### 標準化の主要マイルストーン

| 時期 | 会合 | 決定事項 |
|------|------|---------|
| 2016年4月 | RAN1#84bis | NR Study Item 開始 |
| 2016年8月 | RAN1#86 | ニューメロロジー初期議論 |
| 2016年10月 | RAN1#86bis | **スケーラブルニューメロロジー枠組み合意**（15 kHz ベース、2のべき乗スケーリング） |
| 2016年11月 | RAN1#87 | DL/UL とも CP-OFDM に収束 |
| 2017年3月 | RAN#75 | NR Work Item 承認 |
| 2018年6月 | RAN#80 | Rel-15 NR 仕様凍結 |

---

## 6. 未解決課題

### 3GPP 内の残課題

- **FR2-2 (52.6〜71 GHz) のニューメロロジー最適化**: μ=5, 6 の実運用での性能検証が進行中
- **URLLC と eMBB のスロット共存**: プリエンプションの信頼性と eMBB スループット低下のトレードオフ
- **動的 TDD の干渉管理**: 隣接セル間で異なるスロットフォーマットを使用した場合のクロスリンク干渉
- **BWP 切替遅延**: BWP 間の切替に伴う中断時間の最小化

### 6G に向けた課題

- **Sub-THz（100〜300 GHz）のフレーム設計**: 960 kHz 以上の SCS が必要になる可能性。位相雑音が支配的
- **6G 波形選択**: CP-OFDM の高 PAPR が sub-THz で問題。KT-DFT-s-OFDM が有力候補 [要確認: Rel-20 SI での採否]
- **ISAC（通信とセンシングの統合）のためのフレーム設計**: センシング用シンボルの挿入方法
- **AI/ML ベースのニューメロロジー選択**: 環境に応じて動的に SCS を最適化する構想
- **エネルギー効率駆動のフレーム設計**: スリープモードとの連携、不要シンボルの送信停止

### 学術的未解決問題

- Sub-THz での最適 CP 長（遅延拡散と位相雑音のバランス）
- 混合ニューメロロジー間のインターニューメロロジー干渉 (INI) の実用的抑制法
- 超高密度ネットワークにおけるスロットフォーマット協調

---

## 7. 市場・普及の見込みと知財余地

### 市場セグメント別の影響

| セグメント | フレーム構造の関連性 |
|-----------|-------------------|
| **Consumer (eMBB/XR)** | 広帯域 SCS (30/60 kHz) + 大容量 RB でスループット確保 |
| **B2B (URLLC)** | ミニスロット + 短 SCS によるサブミリ秒スケジューリング |
| **FWA** | BWP による端末省電力が家庭用 CPE で重要 |
| **NTN (衛星)** | 大きな伝搬遅延に対する CP/タイミングアドバンスの拡張が課題 |

### 知財余地の分析

**論文の理想仮定と実装制約のギャップ（進歩性の源泉）**:

| 理想仮定 | 実装制約 | 知財機会 |
|---------|---------|---------|
| 連続的な SCS 選択 | 2のべき乗に量子化 | 量子化 SCS 間の切替手順、境界条件処理 |
| 瞬時 BWP 切替 | 数スロットの切替遅延 | 切替中のデータ損失回避手法 |
| 完全同期のミニスロット | タイミングアドバンスのズレ | ミニスロット境界での同期補正 |
| 理想的 TDD 切替 | ガードピリオドの必要性 | 効率的な GP 設計、動的 GP 調整 |
| Sub-THz で理想発振器 | 深刻な位相雑音 | 位相雑音補償と組み合わせたフレーム設計 |

**SEP 可能性が高い領域**:
1. **Rel-20 以降の新ニューメロロジー**: sub-THz 向け SCS の定義に伴う必須手順
2. **ISAC フレーム設計**: センシングと通信の時間リソース分割方法
3. **BWP 拡張**: AI/ML 駆動の動的 BWP 適応
4. **省電力フレーム設計**: PDCCH モニタリング削減と組み合わせたスロットフォーマット

---

## 前世代対比サマリー

| 観点 | 3G (WCDMA) | 4G (LTE) | 5G (NR) | 6G への課題 |
|------|-----------|---------|---------|------------|
| **多重方式** | CDMA | OFDMA | OFDMA + 柔軟 SCS | OFDM 継続 or SC at sub-THz? |
| **最小時間単位** | 10 ms TTI | 1 ms TTI | 1 シンボル (~4.2 μs @ 240 kHz) | さらなる短縮の必要性? |
| **帯域幅** | 5 MHz | 20 MHz | 400 MHz | GHz 級? |
| **柔軟性** | 固定 | ほぼ固定 | 高度に柔軟 | AI/ML で動的最適化? |
| **省電力** | なし | DRX | BWP + リーン設計 | ゼロエネルギーデバイス? |

---

## Next Steps

- [ ] TS 38.211 V18 のフレーム構造関連セクション（Section 4）を直接参照し、パラメータ表を検証
- [ ] 3GPP ポータルで "frame structure" "numerology" キーワードで Rel-20 SI 関連 Tdoc を検索
- [ ] arXiv で "sub-THz frame structure 6G" を検索し、最新の波形候補を確認
- [ ] `/analyze-gap` でフレーム構造の「学術 vs 3GPP vs 実装制約」ギャップを可視化
- [ ] `/success-pattern` で「3G→4G→5G のフレーム構造進化から6Gへの教訓」を抽出
- [ ] NTN 向けフレーム構造拡張（TS 38.211 の NTN 関連改定）を別トピックとして調査
- [ ] ISAC (Integrated Sensing and Communication) のフレーム設計を `10_topics/cross-cutting/` に記録
