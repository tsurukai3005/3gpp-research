---
title: "NR Operating Bands and Channel Arrangement (TS 38.101-1 Section 5)"
axes:
  technology_layer: [phy-waveform]
  generation: [rel-15, rel-16, rel-17, rel-18, rel-19]
  value: [throughput, coverage, energy-efficiency]
  market: [consumer-xr, b2b-industrial, fwa, ntn, ambient-iot]
  adoption: [backward-compat, standard-convergence, economies-of-scale]
  ip: [spec-mapping]
status: draft
confidence: high
created: 2026-04-21
updated: 2026-04-21
sources:
  - url: https://www.3gpp.org/dynareport/38101-1.htm
    title: "3GPP TS 38.101-1 — NR; User Equipment (UE) radio transmission and reception; Part 1: Range 1 Standalone"
    accessed: 2026-04-21
  - url: https://www.etsi.org/deliver/etsi_ts/138100_138199/13810101/16.05.00_60/ts_13810101v160500p.pdf
    title: "ETSI TS 138 101-1 V16.5.0 (PDF)"
    accessed: 2026-04-21
  - url: https://www.sharetechnote.com/html/5G/5G_FR_Bandwidth.html
    title: "ShareTechNote — 5G FR/Bandwidth"
    accessed: 2026-04-21
  - url: https://www.nrexplained.com/raster
    title: "NR Explained — Raster"
    accessed: 2026-04-21
  - url: https://www.nrexplained.com/bandwidth
    title: "NR Explained — Bandwidth"
    accessed: 2026-04-21
  - url: https://www.sqimway.com/nr_band.php
    title: "Sqimway — NR Band"
    accessed: 2026-04-21
  - url: https://5g-tools.com/5g-nr-frequency-band/
    title: "5G-Tools — NR Frequency Band"
    accessed: 2026-04-21
related:
  - frame-structure.md
  - gap-202604.md
  - ../../docs/presentations/nr-frame-structure.md
---

# NR Operating Bands and Channel Arrangement (TS 38.101-1 Section 5)

> **対象仕様**: 3GPP TS 38.101-1 — NR; User Equipment (UE) radio transmission and reception; Part 1: Range 1 Standalone
> **対象セクション**: Section 5 "Operating bands and channel arrangement"
> **スコープ**: FR1（410 MHz〜7125 MHz）のスタンドアロン動作

---

## 1. 定義と背景（Why）

### この仕様セクションは何か

TS 38.101-1 Section 5 は、NR UE が FR1（Frequency Range 1）で動作する際の**周波数配置の全ルール**を定義する。具体的には:

- どの周波数帯域で NR を運用できるか（Operating Bands）
- 各帯域でどのチャネル帯域幅が使えるか（Channel Bandwidth）
- キャリアの中心周波数をどこに置けるか（Channel Raster）
- UE が初期セルサーチで探す周波数はどこか（Synchronization Raster）
- 隣接キャリアとの間隔はどう決めるか（Channel Spacing）
- 送信帯域幅の端と隣接チャネルの間にどれだけの保護帯域が必要か（Guardband）

### なぜ必要とされたか

NR は LTE の 44 バンド（Rel-8〜14 累計）を大幅に超える数の周波数帯域をサポートし、かつ各帯域で複数のサブキャリア間隔（SCS）と帯域幅の組合せを許容する。この柔軟性を**相互運用性を保ちながら実現する**ために、以下のルールが必要になった:

1. **グローバルな周波数統一管理**: 各国の周波数割当が異なる中で、NR-ARFCN（絶対無線周波数チャネル番号）による統一的な周波数指定
2. **効率的なセルサーチ**: 広大な周波数空間から素早く同期信号を見つけるための粗い同期ラスター
3. **隣接チャネル干渉の防止**: ガードバンドと最大送信帯域幅構成の厳密な定義
4. **多様なデプロイメントの共存**: FDD / TDD / SDL / SUL / CA / DC の各構成に対応

---

## 2. セクション構造の全体像

Section 5 のサブセクション構造を以下に示す。基本セクション（5.x）がスタンドアロン単一キャリアの定義を担い、A/B/C/D/K/M 等の接尾辞が CA・DC・SUL 等の拡張構成を担う。

```
5       Operating bands and channel arrangement
5.1     General
5.2     Operating bands
5.2A    Operating bands for CA (Carrier Aggregation)
  5.2A.1  Intra-band CA
  5.2A.2  Inter-band CA
5.2B    Operating bands for DC (Dual Connectivity)
5.2C    Operating bands for SUL (Supplementary Uplink)
5.2D    Operating bands for UL MIMO
5.2K    Operating bands for simultaneous Rx/Tx in multiple directions
5.2M    Operating bands for LP-WUS/WUR [Rel-18+]
5.3     UE channel bandwidth
  5.3.1   General
  5.3.2   Maximum transmission bandwidth configuration
  5.3.3   Minimum guardband and transmission bandwidth configuration
  5.3.4   RB alignment
  5.3.5   Channel bandwidths for each NR band
5.3A    UE channel bandwidth for CA
5.3B    UE channel bandwidth for DC
5.3C    UE channel bandwidth for SUL
5.3D    Channel bandwidth for UL MIMO
5.3K    Channel bandwidth for simultaneous Rx/Tx in multiple directions
5.3M    UE channel bandwidth for LP-WUS/WUR [Rel-18+]
5.4     Channel arrangement
  5.4.1   Channel spacing
    5.4.1.1  Channel spacing for adjacent NR carriers
  5.4.2   Channel raster
    5.4.2.1  NR-ARFCN and channel raster
    5.4.2.2  Channel raster to resource element mapping
    5.4.2.3  Channel raster entries for each operating band
  5.4.3   Synchronization raster
    5.4.3.1  Synchronization raster and numbering
    5.4.3.2  Synchronization raster to SS block resource element mapping
    5.4.3.3  Synchronization raster entries for each operating band
5.4A    Channel arrangement for CA
5.4B    Channel arrangement for DC
5.4C    Channel arrangement for SUL
5.5     TX-RX frequency separation
5.5A    Configurations for CA
  5.5A.1  Intra-band contiguous CA
  5.5A.2  Intra-band non-contiguous CA
  5.5A.3  Inter-band CA
5.5B    Configurations for DC
5.5C    Configurations for SUL
5.5D    Configurations for UL MIMO
5.5K    Configurations for simultaneous Rx/Tx in multiple directions
```

**設計思想**: 基本セクション（5.2〜5.5）でスタンドアロン単一キャリアのルールを完結させ、接尾辞付きセクション（A=CA, B=DC, C=SUL, D=UL MIMO, K=多方向同時 Rx/Tx, M=LP-WUS）で拡張構成を追加定義する。この構造により、各拡張は基本ルールを「差分」として参照できる。

---

## 3. サブセクション詳細

### 5.1 General — 概要

Section 5 全体のスコープを定義。FR1（410 MHz〜7125 MHz）のスタンドアロン NR UE が対象であること、FR2 は TS 38.101-2 で扱うことを明記。

**背景知識**: TS 38.101 シリーズは 4 パートに分かれる:
- **Part 1 (-1)**: FR1 スタンドアロン ← **本セクションの対象**
- **Part 2 (-2)**: FR2 スタンドアロン
- **Part 3 (-3)**: FR1 + FR2 のインターバンド動作（CA/DC 等）
- **Part 4 (-4)**: 性能要件

---

### 5.2 Operating Bands — NR 運用周波数帯

NR で使用可能な周波数帯域（Operating Band）を定義する。各バンドには "n" プレフィックスの番号が付与される（LTE の "Band" と区別）。

#### デュプレックスモード別分類

**FDD バンド**（上り・下りが異なる周波数）:

| バンド | UL 周波数 (MHz) | DL 周波数 (MHz) | 帯域幅 (MHz) | 主な地域・用途 |
|:-------|:---------------|:---------------|:------------|:-------------|
| n1 | 1920–1980 | 2110–2170 | 60 | グローバル（IMT コア） |
| n2 | 1850–1910 | 1930–1990 | 60 | 北米 PCS |
| n3 | 1710–1785 | 1805–1880 | 75 | グローバル（DCS/AWS） |
| n5 | 824–849 | 869–894 | 25 | 北米 850 MHz |
| n7 | 2500–2570 | 2620–2690 | 70 | グローバル IMT-E |
| n8 | 880–915 | 925–960 | 35 | 欧州・アジア 900 MHz |
| n12 | 699–716 | 729–746 | 17 | 北米 700 MHz |
| n13 | 777–787 | 746–756 | 10 | 北米 FirstNet 隣接 |
| n14 | 788–798 | 758–768 | 10 | 北米 FirstNet |
| n18 | 815–830 | 860–875 | 15 | 日本 800 MHz |
| n20 | 832–862 | 791–821 | 30 | 欧州 800 MHz（DD） |
| n24 | 1626.5–1660.5 | 1525–1559 | 34 | L バンド（衛星隣接） |
| n25 | 1850–1915 | 1930–1995 | 65 | 北米 PCS 拡張 |
| n26 | 814–849 | 859–894 | 35 | 北米 ESMR + 850 |
| n28 | 703–748 | 758–803 | 45 | APT 700 MHz |
| n30 | 2305–2315 | 2350–2360 | 10 | 北米 WCS |
| n31 | 452.5–457.5 | 462.5–467.5 | 5 | 450 MHz（ユーティリティ） |
| n65 | 1920–2010 | 2110–2200 | 90 | n1 拡張 |
| n66 | 1710–1780 | 2110–2200 | 70/90 | 北米 AWS 拡張 |
| n68 | 698–728 | 753–783 | 30 | 欧州 700 MHz |
| n70 | 1695–1710 | 1995–2020 | 15/25 | 北米 AWS-3 |
| n71 | 663–698 | 617–652 | 35 | 北米 600 MHz |
| n74 | 1427–1470 | 1475–1518 | 43 | L バンド |
| n85 | 698–716 | 728–746 | 18 | n12 拡張 |
| n87 | 410–415 | 420–425 | 5 | 410 MHz（IoT） |
| n88 | 412–417 | 422–427 | 5 | 410 MHz（IoT） |
| n91 | 832–862 | 1427–1432 | 30/5 | UL=n20, DL=L バンド |
| n92 | 832–862 | 1432–1517 | 30/85 | UL=n20, DL=L バンド |
| n93 | 880–915 | 1427–1432 | 35/5 | UL=n8, DL=L バンド |
| n94 | 880–915 | 1432–1517 | 35/85 | UL=n8, DL=L バンド |
| n105 | 663–703 | 612–652 | 40 | 600 MHz 拡張 |
| n106 | 896–901 | 935–940 | 5 | 900 MHz 狭帯域 |

**TDD バンド**（上り・下りが同一周波数を時分割）:

| バンド | 周波数 (MHz) | 帯域幅 (MHz) | 主な地域・用途 |
|:-------|:------------|:------------|:-------------|
| n34 | 2010–2025 | 15 | IMT TDD |
| n38 | 2570–2620 | 50 | IMT-E TDD |
| n39 | 1880–1920 | 40 | 中国 TD-SCDMA 再利用 |
| n40 | 2300–2400 | 100 | グローバル 2.3 GHz |
| n41 | 2496–2690 | 194 | グローバル 2.5 GHz（C バンド隣接） |
| n46 | 5150–5925 | 775 | 5 GHz 非免許帯（NR-U） |
| n48 | 3550–3700 | 150 | 北米 CBRS |
| n50 | 1432–1517 | 85 | L バンド SDL/TDD |
| n51 | 1427–1432 | 5 | L バンド |
| n53 | 2483.5–2495 | 11.5 | S バンド |
| n77 | 3300–4200 | 900 | **C バンド（グローバル主力 TDD）** |
| n78 | 3300–3800 | 500 | C バンド（n77 のサブセット） |
| n79 | 4400–5000 | 600 | 4.5 GHz（日本等） |
| n90 | 2496–2690 | 194 | n41 と同一（SUL 組合せ用） |
| n96 | 5925–7125 | 1200 | **6 GHz 帯（Rel-17+、NR-U / Wi-Fi 6E 隣接）** |

**SDL（Supplementary Downlink）バンド**:

| バンド | DL 周波数 (MHz) | 帯域幅 (MHz) |
|:-------|:---------------|:------------|
| n29 | 717–728 | 11 |
| n67 | 738–758 | 20 |
| n75 | 1432–1517 | 85 |
| n76 | 1427–1432 | 5 |

**SUL（Supplementary Uplink）バンド**:

| バンド | UL 周波数 (MHz) | 帯域幅 (MHz) | ペアとなる DL バンド |
|:-------|:---------------|:------------|:------------------|
| n80 | 1710–1785 | 75 | n3 の UL と同一 |
| n81 | 880–915 | 35 | n8 の UL と同一 |
| n82 | 832–862 | 30 | n20 の UL と同一 |
| n83 | 703–748 | 45 | n28 の UL と同一 |
| n84 | 1920–1980 | 60 | n1 の UL と同一 |
| n86 | 1710–1780 | 70 | n66 の UL と同一 |
| n89 | 824–849 | 25 | n5 の UL と同一 |
| n95 | 2010–2025 | 15 | n34 と同一 |

#### 用語解説

- **Operating Band**: NR 運用が認められた周波数帯域の定義。UL/DL の周波数範囲とデュプレックスモードの組合せ
- **FDD**: 上り（UL）と下り（DL）に異なる周波数帯を使用。常時双方向通信が可能だが、ペア帯域が必要
- **TDD**: 同一周波数を時間的に UL/DL で共有。ペア帯域が不要だが、ガードタイム（GP）が必要
- **SDL**: DL のみの補助帯域。別バンドの UL と組み合わせて DL 容量を増強
- **SUL**: UL のみの補助帯域。高周波 TDD バンド（n77/78 等）の UL カバレッジを低周波帯で補完

#### 背景知識: なぜバンド番号が飛び飛びか

NR バンドの番号体系は LTE バンドとの対応関係を反映している。例えば n1 = LTE Band 1、n3 = LTE Band 3 のように、同一周波数帯を共有する LTE バンドと番号を揃えている。n77〜n79 のように NR で新設された帯域は新番号が付与される。これは **LTE-NR DSS（Dynamic Spectrum Sharing）** を行う際の管理上の整合性と、規制当局との対応関係を維持するため。

---

### 5.2A Operating Bands for CA — キャリアアグリゲーション

CA で組み合わせ可能なバンドの組合せを定義。

- **5.2A.1 Intra-band CA**: 同一バンド内の複数キャリアを束ねる（Contiguous / Non-contiguous）
- **5.2A.2 Inter-band CA**: 異なるバンドのキャリアを束ねる（例: n3 + n78）

CA 組合せは `CA_nX-nY` の形式で表記される（例: `CA_n78A-n78A` = n78 の 2CC intra-band CA）。

### 5.2B Operating Bands for DC — デュアルコネクティビティ

EN-DC（E-UTRA NR Dual Connectivity）および NR-NR DC で組み合わせ可能なバンド構成を定義。EN-DC は TS 38.101-3 で主に扱われるが、NR-NR DC の構成がここに記載される。

### 5.2C Operating Bands for SUL

SUL バンドとペアとなる TDD/FDD バンドの有効な組合せを定義。

**背景知識: SUL の設計動機**: C バンド（n77/78、3.5 GHz 帯）は広帯域が利用可能だが、パスロスが大きいため UE の送信電力（最大 23 dBm）ではカバレッジが不足する。低周波帯（n80/81/82/83 等）を UL のみの補助帯として追加することで、DL は C バンドの広帯域、UL は低周波の良好なカバレッジという組合せが実現する。

### 5.2D Operating Bands for UL MIMO

UL で複数アンテナ送信（UL MIMO）をサポートするバンドを定義。

### 5.2K Operating Bands for Simultaneous Rx/Tx in Multiple Directions

同時に複数方向で送受信を行う構成のバンドを定義（例: NTN + 地上の同時運用シナリオ）。

### 5.2M Operating Bands for LP-WUS/WUR [Rel-18+]

**LP-WUS（Low-Power Wake-Up Signal）/ WUR（Wake-Up Receiver）** をサポートするバンド。Rel-18 で導入された省電力技術で、UE がメイン受信機をスリープさせたまま低電力受信機で起動信号を監視する。

---

### 5.3 UE Channel Bandwidth — UE チャネル帯域幅

#### 5.3.1 General — 概要

NR UE がサポートするチャネル帯域幅の定義。FR1 では **5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 MHz** が定義されている（3 MHz は Rel-17+ で sidelink / RedCap 向けに追加）。

**背景知識: LTE との違い**: LTE では最大 20 MHz だったチャネル帯域幅が NR FR1 では **100 MHz** まで拡大された。これは n77/78/79 等の TDD バンドで広帯域を活用するため。ただし、全バンドで 100 MHz が使えるわけではなく、バンドごとに許容される帯域幅が異なる（5.3.5 で定義）。

#### 5.3.2 Maximum Transmission Bandwidth Configuration — 最大送信帯域幅構成

チャネル帯域幅と SCS の各組合せに対して、利用可能な最大 RB 数（N_RB）を定義する。

| SCS | 3 MHz | 5 MHz | 10 MHz | 15 MHz | 20 MHz | 25 MHz | 30 MHz | 35 MHz | 40 MHz | 45 MHz | 50 MHz | 60 MHz | 70 MHz | 80 MHz | 90 MHz | 100 MHz |
|:----|:------|:------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:--------|
| 15 kHz | 15 | 25 | 52 | 79 | 106 | 133 | 160 | 188 | 216 | 242 | 270 | — | — | — | — | — |
| 30 kHz | — | 11 | 24 | 38 | 51 | 65 | 78 | 92 | 106 | 119 | 133 | 162 | 189 | 217 | 245 | 273 |
| 60 kHz | — | — | 11 | 18 | 24 | 31 | 38 | 44 | 51 | 58 | 65 | 79 | 93 | 107 | 121 | 135 |

**読み方の例**: 30 kHz SCS で 100 MHz チャネル帯域幅 → 最大 273 RB = 273 × 12 = 3,276 サブキャリア。実際の占有帯域 = 273 × 30 kHz × 12 = 98.28 MHz。残り約 1.72 MHz が両端のガードバンド。

**設計上の注目点**:
- 15 kHz SCS は **50 MHz まで**しか対応しない（270 RB が上限。275 RB 制限に近い）
- 30 kHz SCS が FR1 の主力で、**100 MHz まで対応**
- 60 kHz SCS は 100 MHz 対応だが RB 数が半減（135 RB）→ 周波数スケジューリング粒度が低い
- 最大 RB 数 **275** は仕様上の上限（TS 38.211 で定義）。これを超える RB 数のサポートは 6G cmWave で FFS

#### 5.3.3 Minimum Guardband and Transmission Bandwidth Configuration — 最小ガードバンド

チャネル帯域の端と実際のデータ送信帯域の間に設ける最小限の保護帯域を定義。

**ガードバンドの計算式**:

```
Minimum GB = (BW_channel × 1000 - N_RB × SCS × 12) / 2 - SCS / 2  [kHz]
```

**SCS = 15 kHz の例（抜粋）**:

| チャネル BW | 5 MHz | 10 MHz | 20 MHz | 50 MHz |
|:-----------|:------|:-------|:-------|:-------|
| ガードバンド | 242.5 kHz | 312.5 kHz | 452.5 kHz | 692.5 kHz |

**SCS = 30 kHz の例（抜粋）**:

| チャネル BW | 10 MHz | 20 MHz | 50 MHz | 100 MHz |
|:-----------|:-------|:-------|:-------|:--------|
| ガードバンド | 665 kHz | 805 kHz | 1045 kHz | 845 kHz |

**背景知識: ガードバンドの役割**:
- **隣接チャネル干渉（ACI）の防止**: 送信スペクトラムの端は急峻にロールオフできないため、隣接チャネルへの漏洩を抑制するマージンが必要
- **フィルタ実装の制約**: 実際の送受信フィルタは理想的なブリックウォール特性を持たない。ガードバンドはフィルタのロールオフ特性を吸収する
- **SCS 依存性**: SCS が大きいほど各サブキャリアのスペクトラム幅が広く、ロールオフの影響が大きいため、一般にガードバンドが広くなる

#### 5.3.4 RB Alignment — RB 整列

異なるニューメロロジーの BWP が同一キャリア内で共存する際の RB グリッド整列ルールを定義。

**背景知識**: 15 kHz SCS の RB（180 kHz 幅）と 30 kHz SCS の RB（360 kHz 幅）は、30 kHz RB の境界が 15 kHz RB の 2 つ分に対応するよう整列される。これにより、CRB（Common Resource Block）ナンバリングが全ニューメロロジーで一貫性を持つ。

#### 5.3.5 Channel Bandwidths for Each NR Band — バンド別チャネル帯域幅

各 NR バンドでサポートされるチャネル帯域幅と SCS の組合せを個別に定義する、**実運用上最も参照頻度が高いテーブル**。

**主要バンドの例**:

| バンド | SCS | サポートされる BW (MHz) |
|:-------|:----|:----------------------|
| n1 | 15 kHz | 5, 10, 15, 20, 25, 30, 40, 45, 50 |
| n3 | 15 kHz | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |
| n5 | 15 kHz | 3, 5, 10, 15, 20, 25 |
| n8 | 15 kHz | 5, 10, 15, 20, 25, 30, 35 |
| n20 | 15 kHz | 5, 10, 15, 20 |
| n28 | 15 kHz | 3, 5, 10, 15, 20, 25, 30, 40 |
| n41 | 15/30 kHz | 5〜100（全 BW） |
| n48 | 15/30 kHz | 5〜100 |
| n71 | 15 kHz | 5, 10, 15, 20, 25, 30, 35 |
| n77 | 15/30 kHz | 10〜100 |
| n78 | 15/30 kHz | 10〜100 |
| n79 | 15/30 kHz | 10〜100 |
| n96 | 30/60 kHz | 20, 40, 60, 80, 100 |

**パターンの法則性**:
- **低周波 FDD バンド**（n5, n8, n20 等）: 15 kHz SCS のみ、狭い BW（帯域幅自体が小さいため）
- **中周波 FDD バンド**（n1, n3, n7 等）: 15 kHz SCS、最大 50 MHz 程度
- **広帯域 TDD バンド**（n41, n77, n78, n79）: 15 kHz + 30 kHz SCS、最大 100 MHz
- **6 GHz 帯**（n96）: 30 kHz + 60 kHz SCS、20 MHz 以上のみ

**設計上の意味**: 低周波バンドで 30 kHz SCS をサポートしないのは、CP 長の短縮（2.34 μs）が低周波帯の大セル環境で遅延拡散をカバーしきれないため。逆に広帯域 TDD バンドで 15 kHz SCS をサポートするのは、LTE-NR DSS（Dynamic Spectrum Sharing）のためと、50 MHz 以下の狭帯域デプロイメントへの対応。

---

### 5.4 Channel Arrangement — チャネル配置

#### 5.4.1 Channel Spacing — チャネル間隔

##### 5.4.1.1 Channel Spacing for Adjacent NR Carriers

隣接する NR キャリア間の中心周波数の間隔（Nominal Channel Spacing）を定義。

**計算式**:

```
Nominal Channel Spacing = (BW_channel,1 + BW_channel,2) / 2  [MHz]
```

ただし、実際のチャネル間隔はチャネルラスターの倍数に丸められる。また、オペレーターはこの値より小さい間隔を使用可能（ガードバンドの一部を犠牲にして帯域利用効率を上げるため）。

#### 5.4.2 Channel Raster — チャネルラスター

キャリアの中心周波数を配置できる離散的な位置の集合。

##### 5.4.2.1 NR-ARFCN and Channel Raster — NR-ARFCN とグローバル周波数ラスター

NR-ARFCN（NR Absolute Radio Frequency Channel Number）は、任意の NR キャリア中心周波数を一意に指定する整数値。

**グローバル周波数ラスター**:

| 周波数範囲 | ΔF_Global | F_REF-Offs | N_REF-Offs | N_REF 範囲 |
|:----------|:---------|:-----------|:-----------|:----------|
| 0 – 3,000 MHz | 5 kHz | 0 MHz | 0 | 0 – 599,999 |
| 3,000 – 24,250 MHz | 15 kHz | 3,000 MHz | 600,000 | 600,000 – 2,016,666 |
| 24,250 – 100,000 MHz | 60 kHz | 24,250.08 MHz | 2,016,667 | 2,016,667 – 3,279,165 |

**変換式**:

```
F_REF = F_REF-Offs + ΔF_Global × (N_REF - N_REF-Offs)  [kHz]
```

**用語解説**:
- **NR-ARFCN (N_REF)**: グローバルに一意な周波数チャネル番号。LTE の EARFCN に相当
- **ΔF_Global**: グローバルラスターの最小ステップ幅。周波数が高いほど粗い（5 → 15 → 60 kHz）
- **F_REF**: NR-ARFCN に対応する実際の RF 周波数

**例**: n78（3500 MHz 付近）のキャリア中心周波数 3600 MHz を NR-ARFCN に変換:
- 3000–24250 MHz 帯 → ΔF_Global = 15 kHz, F_REF-Offs = 3000 MHz, N_REF-Offs = 600,000
- N_REF = 600,000 + (3,600,000 - 3,000,000) / 15 = 600,000 + 40,000 = **640,000**

##### 5.4.2.2 Channel Raster to Resource Element Mapping

チャネルラスター上の中心周波数と、実際のリソースグリッド（サブキャリア）の対応関係を定義。キャリア中心周波数は必ずしもサブキャリアの中心に一致する必要はなく、半サブキャリア分のオフセットが許容される。

##### 5.4.2.3 Channel Raster Entries for Each Operating Band

各バンドで有効な NR-ARFCN の範囲とステップサイズ（ΔF_Raster）を定義。

**背景知識**: ΔF_Raster はバンドごとに異なり、ΔF_Global 以上の値を取る。

- **100 kHz ラスター**: 多くの sub-3 GHz バンド（n1, n3, n5 等）
- **15 kHz ラスター**: 3 GHz 以上のバンド（n77, n78 等）
- **一部のバンドではサブセットラスターを定義**: 特定の周波数位置のみ有効（規制上の制約や既存システムとの共存のため）

**設計上の意味**: ラスターが粗いほど UE のセルサーチが高速化する（走査する周波数候補が減る）が、キャリア配置の自由度が下がる。ラスターの粒度は「セルサーチ速度」と「スペクトラム利用効率」のトレードオフで決まる。

#### 5.4.3 Synchronization Raster — 同期ラスター

UE が初期セルサーチで SS/PBCH ブロック（同期信号）を探す周波数位置の集合。チャネルラスターよりもはるかに粗い。

##### 5.4.3.1 Synchronization Raster and Numbering — GSCN

**GSCN（Global Synchronization Channel Number）** を用いて SS/PBCH ブロックの中心周波数を指定する。

| 周波数範囲 | 計算式 | パラメータ | GSCN 範囲 |
|:----------|:------|:---------|:---------|
| 0 – 3,000 MHz | N × 1200 kHz + M × 50 kHz | N=1–2499, M∈{1,3,5} | 2 – 7,498 |
| 3,000 – 24,250 MHz | 3,000 MHz + N × 1.44 MHz | N=0–14,756 | 7,499 – 22,255 |
| 24,250 – 100,000 MHz | 24,250.08 MHz + N × 17.28 MHz | N=0–4,383 | 22,256 – 26,639 |

**用語解説**:
- **GSCN**: SS/PBCH ブロックの中心周波数を指定するグローバル番号
- **SS/PBCH ブロック（SSB）**: PSS + SSS + PBCH で構成される 4 シンボル × 20 RB の同期信号ブロック（TS 38.211 定義）

**背景知識: なぜ同期ラスターは粗いのか**

UE が電源 ON 直後に行うセルサーチでは、全チャネルラスター位置を走査するのは時間がかかりすぎる。同期ラスターは以下のトレードオフで設計されている:

- **ステップ幅の選定**:
  - 0–3 GHz: 約 1.2 MHz ステップ（M のバリエーションで 50 kHz 分の微調整可能）
  - 3–24.25 GHz: 1.44 MHz ステップ
  - 24.25–100 GHz: 17.28 MHz ステップ
- **粗い理由**: UE のセルサーチ時間を許容範囲（数百 ms〜数秒）に収めるため
- **チャネルラスターとのオフセット**: SSB の中心周波数はキャリアの中心周波数と必ずしも一致しない。オフセットは SIB1 で通知される

##### 5.4.3.2 Synchronization Raster to SS Block Resource Element Mapping

GSCN で指定された周波数と、SS/PBCH ブロックのサブキャリアの対応関係を定義。SSB の SCS パターン（Case A/B/C）に依存する。

##### 5.4.3.3 Synchronization Raster Entries for Each Operating Band

各バンドで有効な GSCN の範囲と、対応する SS ブロック SCS パターンを定義。

**SS ブロック SCS パターン**:

| パターン | SSB SCS | 適用バンドの例 | 背景 |
|:--------|:-------|:-------------|:-----|
| **Case A** | 15 kHz | n1, n2, n3, n5, n8, n20, n28, n71 等 | 低周波 FDD バンド |
| **Case B** | 30 kHz | n41（一部） | 一部の中周波バンド |
| **Case C** | 30 kHz | n41, n48, n77, n78, n79, n96 等 | 高周波 TDD バンド |

**設計上の意味**: SSB の SCS パターンはバンドごとに固定であり、データチャネルの SCS とは独立。例えば n78 でデータに 15 kHz SCS を使っていても、SSB は Case C（30 kHz SCS）で送信される。これは SSB の標準化された検出手順を簡素化するため。

---

### 5.5 TX-RX Frequency Separation — 送受信周波数分離

FDD バンドにおける UL と DL の中心周波数の差分（デュプレックス間隔）を定義。

**主要バンドの例**:

| バンド | TX-RX 分離 (MHz) |
|:-------|:----------------|
| n1 | 190 |
| n3 | 95 |
| n5 | 45 |
| n7 | 120 |
| n8 | 45 |
| n20 | -41（UL > DL なので負） |
| n28 | 55 |
| n66 | 400 |
| n71 | -46（UL > DL） |

**背景知識**: TX-RX 分離が大きいほどデュプレクサ（送受信分離フィルタ）の設計が容易だが、周波数資源の利用効率が下がる。n20 や n71 のように UL 周波数が DL 周波数より高い「逆デュプレックス」バンドも存在する。

### 5.5A Configurations for CA

CA 構成時の TX-RX 分離と帯域幅の組合せを定義。

- **5.5A.1 Intra-band Contiguous CA**: 同一バンド内の隣接キャリアを束ねる構成
- **5.5A.2 Intra-band Non-contiguous CA**: 同一バンド内だが隣接しないキャリアを束ねる構成
- **5.5A.3 Inter-band CA**: 異なるバンドのキャリアを束ねる構成

### 5.5B–5.5K

DC, SUL, UL MIMO, 多方向同時 Rx/Tx の各構成を同様に定義。

---

## 4. パラメータ間の相互関係

各パラメータがどのように依存し合っているかの全体構造:

```
Operating Band (Table 5.2-1)
  ├── 周波数範囲を決定
  ├── デュプレックスモード (FDD/TDD/SDL/SUL) を決定
  │
  ├──→ サポートされる Channel Bandwidth を制約 (Table 5.3.5-1)
  │     └──→ SCS との組合せで N_RB（最大 RB 数）が決定 (Table 5.3.2-1)
  │           └──→ Guardband が導出 (Table 5.3.3-1)
  │
  ├──→ Channel Raster の粒度を決定 (Table 5.4.2.3-1)
  │     └──→ 有効な NR-ARFCN の範囲とステップ
  │
  ├──→ Synchronization Raster を決定 (Table 5.4.3.3-1)
  │     ├──→ 有効な GSCN の範囲
  │     └──→ SS Block SCS パターン (Case A/B/C)
  │
  └──→ TX-RX Frequency Separation (FDD のみ) (Table 5.5-1)
```

**設計上のキーポイント**:

1. **Operating Band が全ての起点**: バンドが決まると、他の全パラメータが連鎖的に制約される
2. **ラスターの階層性**: Synchronization Raster（最も粗い）> Channel Raster ≧ Global Frequency Raster（最も細かい）。UE はまず粗い同期ラスターでセルを発見し、次に細かいチャネルラスターでキャリアに同調する
3. **SCS の三重の役割**: データチャネルの SCS、SSB の SCS、チャネルラスターの粒度の 3 つが独立に決まる。SSB SCS はバンド固定、データ SCS は BWP 設定による
4. **N_RB × SCS × 12 ≦ BW_channel**: この不等式がガードバンドの存在を保証する

---

## 5. 前世代との差分

### LTE vs NR の Operating Bands / Channel Arrangement 比較

| 観点 | LTE (TS 36.101) | NR (TS 38.101-1) |
|:-----|:----------------|:-----------------|
| バンド番号プレフィックス | "Band"（例: Band 1） | "n"（例: n1） |
| 周波数チャネル番号 | EARFCN | NR-ARFCN |
| グローバルラスター粒度 | 100 kHz 固定 | 5 / 15 / 60 kHz（周波数帯依存） |
| 最大チャネル帯域幅 | 20 MHz | **100 MHz**（FR1） |
| SCS 選択肢 | 15 kHz 固定 | **15 / 30 / 60 kHz** |
| 同期ラスター | なし（EARFCN = セル中心周波数） | **GSCN（SSB 位置用の独立ラスター）** |
| SUL | なし | **あり**（低周波 UL 補完） |
| バンド数（FR1 相当） | ~44（Rel-14 時点） | **60+**（Rel-18 時点、増加中） |
| SDL/SUL | 一部 SDL のみ | SDL + SUL |

### 主要な進化ポイント

1. **同期ラスターの分離**: LTE では EARFCN がセル中心とセルサーチの両方を兼ねたが、NR では Channel Raster と Synchronization Raster を分離。これにより SSB の配置自由度が上がり、セルサーチ効率と帯域配置効率を独立に最適化できるようになった
2. **SUL の導入**: 高周波帯の DL 容量と低周波帯の UL カバレッジを組み合わせる概念は NR で初めて標準化
3. **広帯域チャネルのサポート**: 100 MHz チャネル帯域幅は LTE の 5 倍。ガードバンド設計や N_RB テーブルが大幅に拡張された
4. **LP-WUS/WUR バンド**: Rel-18 で追加された新概念。LTE には存在しない

---

## 6. 未解決課題

### 3GPP 内の残課題

- **n96（6 GHz 帯）の規制調和**: 地域により Wi-Fi 6E との共存規則が異なり、NR-U の実運用条件が流動的 [要確認: WRC-23 後の各国規制動向]
- **cmWave (6–8 GHz) の新バンド定義**: Rel-20 SI で検討中。n96 の上限 7125 MHz を超える帯域の追加が議論されている
- **RedCap (Reduced Capability) 向け帯域幅制約**: Rel-17/18 の RedCap UE は最大 20 MHz（FR1）。バンドごとのサポート BW リストへの影響が段階的に追加中
- **N_RB 上限 275 の緩和**: cmWave で 400 MHz チャネル帯域幅を 30 kHz SCS でサポートする場合、275 RB を超える N_RB が必要（約 16,384 FFT ポイント）。Rel-20 で FFS

### 6G に向けた課題

- **Sub-7 GHz 帯の再編**: 既存 FDD バンドの TDD 転用（FDD→TDD リファーミング）の可能性
- **同期ラスター設計の 5G-6G 共存**: 6G SSB を 5G UE が無視できるラスター設計
- **LP-WUS の進化**: Ambient IoT（ゼロエネルギーデバイス）向けのさらなる低電力化と対応バンド拡大

---

## 7. 市場・普及の見込みと知財余地

### 市場への影響

| セグメント | Operating Bands の関連性 |
|:----------|:----------------------|
| **Consumer (eMBB)** | n77/78（C バンド）が全世界で 5G eMBB の主力帯域。100 MHz BW がスループットの鍵 |
| **B2B (URLLC)** | n48 (CBRS) がプライベート 5G の主力。狭帯域 FDD (n5, n8) もカバレッジ重視で使用 |
| **FWA** | n41, n77/78 の広帯域で固定回線代替。n28, n71 の低周波で農村部カバレッジ |
| **NTN** | n24 (L バンド)、n256 (S バンド、FR2 仕様) が衛星直接通信の候補 |
| **Ambient IoT** | n87/88 (410 MHz) のような狭帯域低周波バンドが候補 |

### 知財余地

| 理想仮定 | 実装制約 | 知財機会 |
|:---------|:--------|:--------|
| 任意の中心周波数配置 | チャネルラスターに量子化 | ラスター制約下でのスペクトラム利用最適化 |
| シームレスなバンド切替 | 異なるバンドの RF フロントエンド切替遅延 | バンド間切替の遅延最小化手順 |
| 全バンドで全 BW サポート | バンドごとに BW/SCS が制約 | 制約下での CA/DC 組合せ最適化 |
| 理想的なデュプレクサ | TX-RX 分離が小さいバンドでの自己干渉 | 自己干渉キャンセル技術と組み合わせた新バンド設計 |
| SUL 瞬時切替 | UL パスの切替遅延 | SUL/TDD UL の動的選択手順 |

---

## 既存ノートとの関連性

### [frame-structure.md](frame-structure.md) との関係

frame-structure.md はフレーム構造（時間軸のスロット/シンボル構造）とリソースグリッドの設計を扱う。本ノートとの接点:

- **SCS の共有**: frame-structure.md で解説される SCS (15/30/60 kHz) が、本ノートの N_RB テーブル（Table 5.3.2-1）とガードバンドに直結する。SCS が変わると同じチャネル帯域幅でも利用可能な RB 数が変わる
- **BWP との関係**: frame-structure.md の BWP 概念は、本ノートの Channel Bandwidth の部分集合として機能する。BWP の周波数範囲はキャリア帯域幅（Table 5.3.5-1 で定義）内に収まる必要がある
- **SSB と同期ラスター**: frame-structure.md で解説される SSB のビームスイープ設計は、本ノートの GSCN（Table 5.4.3.3-1）で定義される周波数位置に配置される
- **最大 RB 数 275**: frame-structure.md のリソースグリッド定義における上限が、本ノートの N_RB テーブルに反映されている

### [gap-202604.md](gap-202604.md) との関係

ギャップ分析ノートとの接点:

- **B-2: 広帯域ニューメロロジー**: 本ノートの N_RB 上限 275 と、cmWave 400 MHz チャネル帯域幅のギャップがまさに B-2 の課題。30 kHz SCS で 400 MHz → 約 13,333 サブキャリア → 約 1,111 RB が必要だが、現行上限は 275 RB
- **C-1: INI 抑制**: 本ノートのガードバンド設計（Table 5.3.3-1）が、異なる SCS 間の干渉抑制の物理的基盤。ギャップ分析で「固定ガードバンドを動的に最適化する手法」が知財機会として挙げられている
- **B-1: 5G-6G 統一フレーム構造**: 本ノートの同期ラスター設計が、6G SSB の後方互換配置に直接影響する

### [nr-frame-structure.md](../../docs/presentations/nr-frame-structure.md) との関係

発表資料との接点:

- 発表資料の「主張2: フレーム構造は格子の階層化とシグナリング管理の設計」で述べられる **周波数方向の階層化**（Carrier → BWP → RB → SC）の具体的パラメータが、本ノートの Section 5.3 で定義される
- 発表資料の **Point A と CRB/PRB ナンバリング**（根拠 2.2）は、本ノートの Channel Raster（5.4.2）と直接対応する。Point A はチャネルラスター上の位置から導出される
- 発表資料の **FR1/FR2 定義**は本ノートの Operating Band 分類の基盤
- 発表資料のニューメロロジー一覧表の「最大帯域幅概算」列は、本ノートの Table 5.3.2-1 から導出されている

---

## Next Steps

- [ ] 3GPP ポータルで TS 38.101-1 の最新版（V19.x）の Section 5 を直接確認し、Rel-19 で追加された新バンドを反映
- [ ] n96（6 GHz 帯）の規制動向と NR-U 運用条件を `/survey-topic` で個別調査
- [ ] cmWave (6–8 GHz) の新バンド定義に関する Rel-20 SI Tdoc を 3GPP ポータルで検索（キーワード: "cmWave" "operating band" "FR1 extension"）
- [ ] `/analyze-gap` で「Operating Bands × cmWave 拡張」のギャップ分析を実施
- [ ] SUL の運用実態（どのオペレーターが実際にデプロイしているか）を GSMA Intelligence で調査
- [ ] TS 38.101-2（FR2）の Section 5 を別ノートとして調査し、FR1 との設計思想の差分を整理
- [ ] LP-WUS/WUR（Rel-18 新機能）の対応バンドと省電力効果を `/survey-topic` で個別調査
- [ ] RedCap UE のバンドごとの BW 制約一覧を TS 38.101-1 の最新版から抽出
