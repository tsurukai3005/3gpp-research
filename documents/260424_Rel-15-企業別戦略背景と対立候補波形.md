---
title: "Rel-15 NR 企業別戦略の背景と対立候補波形 — なぜ Qualcomm は 2^n スケーラブル OFDM を推したか"
status: draft
confidence: medium
created: 2026-04-24
updated: 2026-04-24
axes:
  technology-layer: [phy-mimo, cross-layer]
  generation: [rel-15]
  value: [throughput, latency, energy-efficiency, coverage]
  market: [consumer-xr, b2b-industrial, fwa]
  adoption-factors: [standard-convergence, backward-compat, operator-roi, economies-of-scale]
  ip: [novelty, inventive-step, spec-mapping]
sources:
  - url: https://www.qualcomm.com/media/documents/files/whitepaper-making-5g-nr-a-reality.pdf
    title: "Qualcomm — Making 5G NR a Reality (Dec 2016)"
    accessed: 2026-04-24
  - url: https://www.qualcomm.com/news/releases/2006/01/qualcomm-completes-acquisition-flarion-technologies
    title: "Qualcomm — Completes Acquisition of Flarion Technologies (Jan 2006)"
    accessed: 2026-04-24
  - url: https://en.wikipedia.org/wiki/Qualcomm
    title: "Wikipedia — Qualcomm (CDMA/UMB/LTE history, 4G SEP share)"
    accessed: 2026-04-24
  - url: https://businessmodelanalyst.com/qualcomm-business-model/
    title: "Business Model Analyst — Qualcomm QTL/QCT revenue breakdown"
    accessed: 2026-04-24
  - url: https://www.ericsson.com/en/blog/2017/5/in-the-race-to-5g-cp-ofdm-triumphs
    title: "Ericsson blog — In the race to 5G, CP-OFDM triumphs (May 2017)"
    accessed: 2026-04-24
  - url: https://www.ericsson.com/en/reports-and-papers/research-papers/waveform-and-numerology-to-support-5g-services-and-requirements
    title: "Ericsson Zaidi et al. — Waveform and Numerology to Support 5G Services (IEEE ComMag Nov 2016)"
    accessed: 2026-04-24
  - url: https://www.ericsson.com/en/reports-and-papers/books/5g-nr-the-next-generation-wireless-access-technology
    title: "Ericsson — 5G NR: The Next Generation Wireless Access Technology (Dahlman/Parkvall/Skold)"
    accessed: 2026-04-24
  - url: https://www.comsoc.org/peiying-zhu
    title: "IEEE ComSoc — Peiying Zhu profile (Huawei Fellow, f-OFDM lead)"
    accessed: 2026-04-24
  - url: https://ieeexplore.ieee.org/document/7227001/
    title: "Abdoli/Jia/Ma — Filtered OFDM: A New Waveform for Future Wireless (IEEE PIMRC 2015)"
    accessed: 2026-04-24
  - url: https://www.huawei.com/en/press-events/news/2016/11/World-First-5G-Large-Scale-Field-Trial
    title: "Huawei-DOCOMO 4.5 GHz 5G field trial using f-OFDM (Nov 2016)"
    accessed: 2026-04-24
  - url: https://www.nokia.com/about-us/news/releases/2016/01/14/nokia-celebrates-first-day-of-combined-operations-with-alcatel-lucent/
    title: "Nokia — First day of combined operations with Alcatel-Lucent (Jan 2016)"
    accessed: 2026-04-24
  - url: https://www.nokia.com/bell-labs/publications-and-media/publications/waveform-contenders-for-5g-suitability-for-short-packet-and-low-latency-transmissions/
    title: "Nokia Bell Labs — Waveform Contenders for 5G"
    accessed: 2026-04-24
  - url: https://metis-ii.5g-ppp.eu/wp-content/uploads/deliverables/METIS-II_D4.1_V1.0.pdf
    title: "5G PPP METIS-II D4.1 — 5G RAN design (Nokia technical manager)"
    accessed: 2026-04-24
  - url: https://www.innovations-report.com/science-tech/information-technology/trend-setting-research-project-5gnow-on-the-future-of-mobile-communications-rated-excellent/
    title: "5GNOW project final results (FP7 2012-2015)"
    accessed: 2026-04-24
  - url: https://blog.3g4g.co.uk/2016/03/5g-study-item-si-for-ran-working-groups.html
    title: "3G4G blog — RP-160671 NR SID NTT DOCOMO rapporteur (2016-03)"
    accessed: 2026-04-24
  - url: https://www.nttdocomo.co.jp/english/info/media_center/pr/2015/0302_03.html
    title: "NTT DOCOMO — 15 GHz outdoor 10 Gbps MIMO trial with Ericsson (2015)"
    accessed: 2026-04-24
  - url: https://www.olympics.com/ioc/news/fans-of-the-olympic-winter-games-2018-to-experience-world-s-first-broad-scale-5g-network
    title: "PyeongChang 2018 — world's first broad-scale 5G network (Samsung/KT/Intel, 28 GHz)"
    accessed: 2026-04-24
  - url: https://patents.google.com/patent/WO2018203717A1/en
    title: "Samsung WO2018203717A1 — BWP configurations (priority 2017-05-04)"
    accessed: 2026-04-24
  - url: https://www.mediatek.com/press-room/mediatek-unveils-new-m80-5g-modem-with-support-for-mmwave-and-sub-6-ghz-5g-networks
    title: "MediaTek M80 5G Modem — Dynamic BWP branding"
    accessed: 2026-04-24
  - url: https://www.cohere-tech.com/wp-content/uploads/2017/06/R1-167593-Performance-evaluation-of-OTFS-in-single-user-scenarios-am.pdf
    title: "R1-167593 Cohere Technologies — OTFS performance evaluation (RAN1#86)"
    accessed: 2026-04-24
  - url: https://ar5iv.labs.arxiv.org/html/1609.02427
    title: "Liu et al. — Waveform Candidates for 5G Networks: Analysis and Comparison (arXiv 2016)"
    accessed: 2026-04-24
  - url: https://link.springer.com/article/10.1186/s13638-016-0792-0
    title: "Hong et al. — The 5G candidate waveform race (EURASIP JWCN 2016)"
    accessed: 2026-04-24
  - url: https://www.sharetechnote.com/html/5G/5G_Phy_Candidate_Overview.html
    title: "ShareTechNote — 5G waveform candidates overview"
    accessed: 2026-04-24
  - url: https://www.rfwireless-world.com/terminology/5g/fbmc-vs-ufmc-vs-gfdm-5g-waveforms
    title: "RF Wireless World — FBMC vs UFMC vs GFDM comparison"
    accessed: 2026-04-24
  - url: https://www.rfwireless-world.com/terminology/cp-ofdm-vs-dft-s-ofdm-5g
    title: "RF Wireless World — CP-OFDM vs DFT-s-OFDM"
    accessed: 2026-04-24
  - url: https://mcns5g.com/first-6g-agreement-reached-cp-ofdm-and-dft-s-ofdm-confirmed-but-is-this-really-the-future-of-6g/
    title: "6G first agreement — CP-OFDM + DFT-s-OFDM confirmed (2025)"
    accessed: 2026-04-24
  - url: https://www.lightreading.com/6g/cohere-technologies-fights-to-keep-6g-doors-open-for-something-new
    title: "Light Reading — Cohere fights for 6G OTFS consideration"
    accessed: 2026-04-24
  - url: https://www.freepatentsonline.com/y2018/0131487.html
    title: "Qualcomm US 2018/0131487 — Decoupling of sync raster and channel raster"
    accessed: 2026-04-24
related:
  - Rel-15-物理リソース仕様策定の議論変遷.md
  - TS38.211-Section4-原文準拠和訳.md
  - TS38.101-1-Section5-原文準拠和訳.md
  - NR周波数リソース構造の発表資料ドラフト.md
---

# Rel-15 NR 企業別戦略の背景と対立候補波形

> **本ノートの問い**:
> 1. 各企業が Rel-15 で推した方針は分かったが、その**背景**は何か？ なぜ Qualcomm は 2^n スケーラブル OFDM を推したのか？
> 2. CP-OFDM + 2^n スケーリングの**対立候補**はあったのか？ あったとすれば、なぜ採用されなかったのか？
>
> **前提ノート**: [Rel-15-物理リソース仕様策定の議論変遷.md](./Rel-15-物理リソース仕様策定の議論変遷.md) で「何が、いつ、どの会議で合意されたか」を扱った。本ノートは「なぜ、各社がそれを推したか」に焦点を絞る。

---

## 1. サマリー（結論先出し）

### Qualcomm が 2^n スケーラブル OFDM を推した理由

**3層構造**で整理できる:

| 層 | 動機 |
|:---|:---|
| **技術層** | 2^n スケーリングでは FFT サイズも 2^n でスケールし、**単一の FFT パイプラインと単一のクロックツリーで全 SCS をカバー**できる。Snapdragon モデムの SKU 統合に直結する |
| **事業層** | Qualcomm 収益の構造: QCT（チップ）+ QTL（ライセンス）の二本柱。ライセンス課金対象デバイスが **新用途（mmWave/URLLC/IoT）に拡張されるほど QTL 収入が増える**。スケーラブル numerology はライセンス面積そのもの |
| **歴史層** | Qualcomm は 3G 期 CDMA（cdma2000/UMB）の敗北から立ち直り、2006 年の **Flarion 買収（約 8 億ドル）で OFDMA 特許ポートフォリオを獲得**、LTE 期に OFDM プレイヤーとして再生。5G NR はその延長線上で「自社設計思想をデファクト化する」戦略となる |

### 対立候補波形

CP-OFDM 以外に少なくとも **6つの 5G 候補波形**が研究され、3GPP/EU/アカデミアで評価された:

| 候補 | 主推進 | 本質的理由で敗北？ |
|:---|:---|:---|
| **f-OFDM** | Huawei Canada Research | 実装依存で送信側に残存 → 実質的には「負けて勝った」|
| **FBMC-OQAM** | Nokia Bell Labs, Orange, CEA-Leti, 5G PPP | ◎ Yes — MIMO 非互換（OQAM 実数直交性） |
| **UFMC / UF-OFDM** | Alcatel-Lucent Stuttgart (Schaich/Wild/ten Brink) | ◎ Yes — RX 複雑、利得不足 |
| **GFDM** | TU Dresden (Fettweis) | ◎ Yes — 非直交、自己干渉、MIMO 困難 |
| **OTFS** | Cohere Technologies | ✕ タイミング問題 — 高モビリティ用途でニッチ、6G NTN で再浮上 |
| **DFT-s-OFDM** | Qualcomm / Ericsson（LTE 流用）| △ UL のみ採用（カバレッジ制約時）— 完全には負けていない |

**2^n スケーリングの対立候補は存在したか？** 公開情報の範囲では、**3^n や不規則比を 3GPP に正式提案した Tdoc は見つからなかった** `[要確認]`。固定 15 kHz（LTE 流用）は議論段階で mmWave 位相雑音と広帯域要件により早期排除。

---

## 2. Qualcomm — スケーラブル OFDM は垂直統合戦略

### 2.1 歴史層: CDMA から OFDM への大転換

Qualcomm は元々 **CDMA** 陣営の旗手だった:
- **IS-95 / cdma2000**（2G/3G）の発明・標準化
- **UMB (Ultra Mobile Broadband)** を 4G 候補として推進（OFDMA ベースだが CDMA 後方互換性がなく、どのキャリアも採用せず）
- 2005 年に UMB 開発中止、**LTE 支援に方針転換**

転換を決定づけたのが **2006 年 1 月の Flarion Technologies 買収**（約 6 億ドル + マイルストン含め総額 約 8.05 億ドル）。これにより OFDMA の主要特許ポートフォリオを一気に獲得し、「CDMA 企業が LTE で OFDM 特許プレイヤーに化ける」基盤を作った。Wikipedia 引用によれば 2012 年時点で **4G LTE 必須特許の 12.46%（81 seminal patents）**を保有。

Qualcomm にとって 5G NR のスケーラブル OFDM 推進は、**LTE 期に確立した OFDM 技術優位性を、新規ユースケース全域に持ち込む**ための論理的延長線だった。

### 2.2 事業層: QCT + QTL 二本柱とライセンス面積の拡大

Qualcomm の収益構造 (FY2024):
- **QCT（Snapdragon 等のチップ）**: $33.20B (85.6%)
- **QTL（ライセンス）**: $5.57B (14.4%)

ただし EBT マージンは QTL が Q3 FY25 で **71%** と突出して高い（Business Model Analyst, Nasdaq）。

この構造の意味:
- ライセンス収入 = **課金対象デバイス数 × 単価**
- 課金対象デバイス数は「3GPP 仕様に準拠するデバイス」すべて
- **用途が広がるほど QTL が伸びる**

スケーラブル numerology は、**一つの物理層設計で sub-6 GHz から mmWave・URLLC・IoT までカバー**する設計思想。つまり:

> Qualcomm にとって「2^n で全用途をカバー」は、自社の設計思想を全デバイスの物理層に埋め込み、ライセンス収入の課金面積を最大化する戦略。

### 2.3 技術層: FFT パイプライン共用による SKU 統合

**2^n スケーリングの直接的な技術効果**（Qualcomm "Making 5G NR a Reality" 2016-12 より）:

> "Invention #1: Scalable OFDM numerology with 2^n scaling of subcarrier spacing"

主張の骨子:
1. サブキャリア間隔がチャネル帯域幅にスケール
2. **FFT サイズもスケール**し、広帯域でも処理複雑度が不必要に増えない
3. SCS × FFT = サンプリング周波数 が 2^n 倍関係

実装上の帰結:
- **単一の FFT ハードウェアパイプライン**で全 SCS (15/30/60/120/240 kHz) をカバー可能
- クロックツリーを分周比で切替えるだけで対応
- **Snapdragon X シリーズの SKU 統合**: 単一モデムチップが sub-6 GHz FDD + sub-6 GHz TDD + mmWave 全てに対応

これは Qualcomm にとって **製造コスト・在庫管理・市場投入速度すべてで競合優位**をもたらす。MediaTek のような後発ベンダが同じ設計思想に乗るのは歓迎すべき副作用（エコシステムが広がる）でもあった。

### 2.4 Rel-15 における Qualcomm の成果

| 望んだもの | 結果 |
|:---|:---|
| 2^n スケーラブル OFDM | ◎ 採用 (TS 38.211 Table 4.2-1) |
| mini-slot / URLLC | ◎ 採用 (2/4/7 シンボル) |
| Flexible TDD / SFI | ◎ 採用 (DCI 2_0, 3層階層) |
| BWP（省電力視点） | ◎ 採用 |
| Sync/Channel raster 分離 | ◎ 採用（特許 US 2018/0131487 で根拠）|

**完勝**。Qualcomm の Rel-15 SEP 寄与度は評価機関（IPlytics/LexisNexis/GreyB）で順位が揺れるが、Huawei と並び常にトップ 1-2 位。

---

## 3. 対立候補波形 — なぜ CP-OFDM が勝ったか

### 3.1 候補波形の全体マップ

| 波形 | 主推進 | 核となる主張 | 致命的弱点 |
|:---|:---|:---|:---|
| **CP-OFDM** | Qualcomm, Ericsson, Samsung, Intel, Nokia（現実派）| MIMO 親和、LTE エコシステム再利用、位相雑音頑健 | 高 PAPR、OOB リーク |
| **f-OFDM** | Huawei Canada（Jianglei Ma, Peiying Zhu, Ming Jia）| サブバンド単位のフィルタで OOB 抑制、ガードバンド 10%→1% | TX フィルタ追加、サブバンド非厳密直交 |
| **FBMC-OQAM** | Nokia Bell Labs, Orange, CEA-Leti, 5GNOW/FANTASTIC-5G | 最良の OOB、CP 不要、CFO 頑健 | **OQAM 実数直交性 → MIMO 困難**、フィルタ tail が低レイテンシを阻害 |
| **UFMC / UF-OFDM** | Alcatel-Lucent Stuttgart (Schaich, Wild, ten Brink) | CP-OFDM と FBMC の中間案 | RX 複雑、~0.3 dB ノイズ増大 |
| **GFDM** | TU Dresden (Fettweis) | ブロック単位の柔軟パルス整形、スペクトル効率 | 非直交 → 自己干渉、MIMO 困難 |
| **OTFS** | Cohere Technologies | 遅延-ドップラー領域、高モビリティで 2.1 dB 利得 (64QAM @ 120 km/h) | 新規 RX アーキ、エコシステム未成熟、SEP 集中 |
| **DFT-s-OFDM** | Qualcomm/Ericsson（LTE 流用）| ~2-3 dB PAPR 改善 → UL カバレッジ | 単レイヤ、MIMO 劣化 |
| **ZT-DFT-s-OFDM** | Ericsson Research (Berardinelli 2013-2015) | 可変 tail 長 → CP オーバヘッド柔軟 | 小さな BLER ペナルティ、ベースライン不採用 |

### 3.2 CP-OFDM が勝った 4 つの理由

**① MIMO 互換性（技術的・構造的）**

CP-OFDM は**複素数体での直交性**を各サブキャリアで満たすため、per-tone MIMO 等化が単純な行列逆変換で済む。FBMC-OQAM は**実数体でのみ直交**（OQAM 本質的虚数干渉）なため:
- 対策として記号拡散・双直交フィルタ再設計・後処理が必要
- 4×4, 8×8 massive MIMO での RX 複雑度とブロック誤り率が劣化

**NR の中核機能（CSI-RS, DM-RS, MU-MIMO, プリコード SRS）はすべて複素数体直交性を前提**に設計されている。FBMC/GFDM を採用すると標準全体を書き直す必要があり、タイミング的に不可能。

**② mmWave での位相雑音頑健性**

Ericsson Zaidi et al. 2016 IEEE ComMag:
> "CP-OFDM is more robust to oscillator phase noise and Doppler than other multicarrier waveforms."

28 GHz 以上では LO 位相雑音が EVM を支配する。CP-OFDM は **DM-RS で per-subcarrier CPE (Common Phase Error) 補償**ができ実装が単純。FBMC の OQAM 構造は位相雑音補償が構造的に異なり、IEEE ICC 2017 の比較では CP-OFDM が低受信電力域で EVM 優位。

**③ 時間局在性（低レイテンシ + TDD）**

FBMC の典型プロトタイプフィルタ（PHYDYAS）はシンボル長の **4 倍**の tail を持つ。URLLC の 0.5 ms スロットに収まらない。Liu et al. 2016 の表現では「data transmission will be postponed」。

**④ エコシステムとタイミング**

- **LTE ベースバンド DSP の再利用**: 主要チップベンダ（Qualcomm, Intel, MediaTek, Samsung LSI）は LTE の IFFT/FFT エンジン、CP 処理、チャネル推定パイプラインに**数十億ドル規模**の投資済み
- **2018 年商用化の締切**: NSA 完成 2017-12、初回商用 NR 2019 早期（Verizon/AT&T/KT/SKT）というハードロック
- **5G PPP 研究の成熟度不足**: 5GNOW (FP7, 2012-2015) と FANTASTIC-5G (H2020, 2015-07 〜 2017-06) はシミュレーション結果と実験室プロトタイプ止まりで、Qualcomm/Huawei の OTA テストベッドに並ぶ実証がなかった

Ericsson 公式ブログ (2017-05) の表現:
> "there are well-established simple techniques to reduce PAPR...and improve frequency localization."

つまり「CP-OFDM の欠点（PAPR・OOB）は送信側の既知手法で解決可能、逆に他波形の欠点は本質的」という見解で収束した。

### 3.3 f-OFDM — 「負けて勝った」特殊例

Huawei Canada Research（オタワ、Jianglei Ma, Peiying Zhu, Ming Jia 主導）の f-OFDM は、表面的には「採用されなかった」が、実態は異なる:

- 3GPP は**送信側のフィルタ/ウィンドウ処理を実装依存（implementation-specific）**と規定
- Mandatory は CP-OFDM（DL/UL）+ DFT-s-OFDM（UL オプション）
- → **Huawei の f-OFDM はそのまま実装可能**、標準違反にならず、かつ Huawei 独自の差別化特許として残存

結果として Huawei の gNB 実装では f-OFDM 的 TX ウィンドウ処理が内部で動く。「ミキシド numerology 時のガードバンド 10% → 1%」というメリットは Huawei gNB の実運用で享受される。

**副作用**: Rel-15 の SEP としては f-OFDM 特許は**非該当**（標準記述に無いため）。実装差別化特許としてのみ価値を持つ。

### 3.4 FBMC — 本質的敗北

Nokia Bell Labs は **Alcatel-Lucent 買収（2015-04 発表、2016-01-14 統合運用開始、2016-11-03 完全クローズ）**で Bell Labs を手中に収めた。Bell Labs の特許ファミリは約 3.1 万件、ノーベル賞 8 件という研究資産。

Nokia は **EU 5G PPP の METIS-II 技術マネージャ**として RAN 設計と周波数管理 WP をリード。FBMC は **FP7 PHYDYAS プロジェクト (2008-2010)** のプロトタイプフィルタを継承し、**5GNOW** と **FANTASTIC-5G** で 5G 候補として検討された。

しかし Nokia 自身が出版した「Waveform Contenders for 5G」でも、短パケット・低レイテンシ用途では FBMC が劣後することが示され、NR 不採用となった。

**FBMC IPR の行き先**:
- Rel-15 の SEP には**非該当**
- 現在の研究フロンティアは **NTN（非地上系ネットワーク、衛星）** で CFO 頑健性が効く場面、および **コグニティブ無線**
- 完全には死蔵されておらず、6G の衛星系で復活する可能性はある

### 3.5 OTFS — タイミングが悪かった、6G NTN で再浮上

**Cohere Technologies**（2011 年創業、Ronny Hadani, Anton Monk 等）は **R1-167593**（RAN1#86, 2016-08）で OTFS を提案。主張:
- 遅延-ドップラー領域で情報を配置
- 高モビリティで **2.1 dB 利得 (64QAM @ 120 km/h vs OFDM)**
- 衛星・HST・自動車ユースケースで OFDM の ICI 問題を回避

なぜ採用されなかったか:
- **新規 RX アーキ**でエコシステム未成熟
- **2.1 dB 利得は高速移動コーナーケース**のみ、NR の主戦場 sub-100 km/h eMBB では利得なし
- **SEP が一社（Cohere）に集中**。Qualcomm/Ericsson/Huawei など大手は、小規模企業が SEP で巨額課金する可能性を警戒

現在の動き:
- Cohere は OTFS/Delay-Doppler/Zak-OTFS で **300 件超の特許**を保有
- **6G NTN（LEO 衛星、HST）議論で再浮上**。2025 年の RAN1 6G 議論で ZAC-OTFS を提案したが、暫定的に CP-OFDM/DFT-s-OFDM 継続決定（"First 6G agreement reached" MCNS5G 報道）
- Cohere は現在も 6G で OTFS 採用を働きかけ（Light Reading "Cohere fights to keep 6G doors open"）

### 3.6 DFT-s-OFDM — UL のみ生存

完全敗北ではなく、**UL 限定で mandatory**として採用された LTE 流用波形。理由:

- UE 送信電力は PA バックオフで制約される（PC3 で PA ヘッドルーム ~23 dBm）
- CP-OFDM PAPR ~11-12 dB → DFT-s-OFDM PAPR ~8-9 dB → **~2-3 dB バックオフ改善**
- セルエッジ・深屋内・mmWave で決定的

DL では不採用:
- gNB PA は 40-50 dBm、バックオフ予算潤沢、DPD で補正可能
- DL は純粋 CP-OFDM

DFT-s-OFDM の採用は **UE パワー制限時のみ**（RRC 設定 + DCI スケジューリングで動的切替）、かつ**単レイヤのみ**（MIMO 劣化するため高 SNR では CP-OFDM 優先）。

Rel-15 では **π/2-BPSK + DFT-s-OFDM** も追加され、mMTC / 極端カバレッジで PAPR がさらに ~2-3 dB 低下、ほぼ単一搬送波包絡となる。

---

## 4. 2^n スケーリング対立候補の検証

### 4.1 検証した候補

| 候補 | 状況 |
|:---|:---|
| **固定 15 kHz（LTE 流用）** | 議論段階で早期排除。mmWave 位相雑音と広帯域 (>100 MHz) 要件に対応不可 |
| **3^n スケーリング** | 公開 3GPP 寄書で正式提案を確認できず `[要確認]` |
| **17.5 kHz / 17 kHz anchor** | 初期ホワイトボード議論に出た形跡はあるが公開 Tdoc 未確認 `[要確認]` |
| **不規則比** | アカデミックの非 2 冪 FFT 研究はあるが 3GPP 正式提案を確認できず `[要確認]` |

### 4.2 2^n が勝った理由（公開情報による整理）

**① FFT ハードウェア効率**
- radix-2 / radix-4 FFT が最も成熟したシリコン IP
- 2^n ならサイズを 2 倍・1/2 で容易にスケール
- 非 2^n（例 3 倍）は別 FFT ブロックかリサンプリングが必要 → 面積・電力コスト

**② ミキシド numerology のスロット境界整列**
- 2^n スケーリングでは、Δf = 15 kHz の 1 シンボル = Δf = 15·2^μ kHz の 2^μ シンボル
- 同一キャリア上で eMBB + URLLC を FDM 多重した際、**スロット境界で決定的に整列**
- これにより scheduling が単純化

**③ LTE 15 kHz アンカー**
- Qualcomm "Making 5G NR a Reality" (2016-12): LTE 15 kHz を μ=0 の anchor とすべし
- Ericsson Zaidi et al. (2016-11): 同じ主張
- FR1 共存 / refarming / LTE UE 併存スケジューリング（DSS の前身）が自然になる

**非 2^n 案の公開情報不足**: 3GPP ウェブ検索と主要ベンダ白書の範囲では、3^n / 17 kHz / 不規則比を**3GPP RAN1 に正式寄書として提出した記録は見つからない**。これは `[要確認]` だが、少なくとも主要候補として議論された形跡がない。

### 4.3 Rel-17 での 480 / 960 kHz 追加

Rel-15 時点では 240 kHz までだが、Rel-17 で **480 / 960 kHz**が追加された（FR2-2, 52.6–71 GHz 拡張）。これは 2^n 枠組みの**自然な延長**として実現しており、Rel-15 の設計決定が拡張性を持っていたことの証左。

---

## 5. 他主要プレイヤーの動機マップ（要点）

### Ericsson — ベースバンド DSP 統一による gNB コスト最小化

- gNB 世界トップクラスインフラベンダ、LTE RAN ~40% シェア
- **CP-OFDM を DL・UL 共通**にすることで送受信 FFT/IFFT ブロックとスケジューラ DSP を統一 → gNB コスト削減
- **研究伝統**: Erik Dahlman / Stefan Parkvall / Johan Sköld（3G/4G/5G 正典書籍著者）の連続性が「LTE 哲学の発展」を志向
- 2016-04 RAN1 NR 初回会合で CP-OFDM 提案、同年 11 月 IEEE ComMag 掲載 → 規制当局・ITU-R への**事前シグナリング**として機能、「CP-OFDM は既に業界合意」ナラティブを先行形成

### Huawei — f-OFDM 差別化 + 中国キャリア SUL 要求

- インフラ + チップ（HiSilicon Balong）を両方持つ
- **Huawei Canada Research（オタワ）**の Peiying Zhu（Huawei Fellow、150+ granted patents）チームが f-OFDM 開発
- 差別化 IPR プレイだが実装依存合意で「実質勝利」
- **SUL 推進**: China Mobile の n41 + n79 TDD 展開で UL カバレッジがボトルネック、低バンド UL 補助が本質的要求

### Nokia — Bell Labs 研究伝統 + 5G PPP アラインメント

- ALU 買収で Bell Labs 傘下化（約 3.1 万特許ファミリ、ノーベル賞 8 件）
- **METIS-II 技術マネージャ**として EU 5G PPP に深く関与
- FBMC/UFMC は本質的敗因（MIMO 非互換、レイテンシ問題）で不採用
- **Mixed numerology TDM/FDM 推進**で柔軟性を担保する立場に移行

### NTT DOCOMO — オペレータ・ラポータの調停役

- **RP-160671 NR SID のラポータ**就任（2016-03, RAN #71 Gothenburg）
- ベンダ中立の立場でベンダ間対立を調停
- **1 ms サブフレーム維持**: LTE リファーミング段階移行を重視
- **日本 MIC スペクトラム政策**整合: 4.5 GHz (n79) + 28 GHz (n257) 両獲得
- DOCOMO-Ericsson 15 GHz トライアル (2014-2015 横須賀)、DOCOMO-Nokia 70 GHz トライアル (2015-10 六本木ヒルズ) が mmWave 標準化押上げの交渉力

### Samsung — チップ × インフラ × ハンドセット垂直統合

- **Exynos モデム + Networks + Galaxy**の唯一の三位一体ベンダ
- **BWP 早期特許化**: WO2018203717A1 (2017-05-04 優先) で Qualcomm に先行
- **FR2 400 MHz 推進**: PyeongChang 2018 冬季五輪 28 GHz 実証（Samsung + KT + Intel、ピーク 20 Gbps/cell）を根拠に
- **Spatial QCL Type D**: ハイブリッドビームフォーミング gNB + RX ビーム端末の両面要求

### MediaTek — コスト層モデムにとって BWP は存亡機能

- グローバル #2 モデムベンダ、コスト志向・新興国市場強い
- **BWP = SKU が成り立つ前提**: 広帯域 RF を自社再現するコストが不成立、狭 RF + BWP 切替で対応
- M80 5G Modem で **Dynamic BWP**を明示機能名化
- "Carrier Bandwidth Part" 用語の自社由来主張 `[要確認 — 一次証拠なし]`

### オペレータ群

| オペレータ | スペクトラム | Rel-15 での主な押し |
|:---|:---|:---|
| **China Mobile** | n41 (2.5 GHz 160 MHz) + n79 (4.8 GHz) | n41/n79、**SUL 主要ユースケース**（TDD UL カバレッジ補完）|
| **Verizon** | n261 (28 GHz) $505M FCC 落札 | mmWave NR/FWA、dynamic TDD |
| **AT&T** | n260 (39 GHz) + 24 GHz $982M + FiberTower | mmWave FWA/モバイル |
| **T-Mobile US** | 600 MHz $8B 落札（全米平均 31 MHz）| **n71 広域低バンド**、ルーラルカバレッジ |
| **DT/Orange/Telefonica** | 欧州 CEPT C-band | n78 (3.5 GHz) 主軸、FR2 は n258 |
| **Cohere Technologies** | スペクトラム保有なし（スタートアップ）| **OTFS**（高速移動・衛星）→ 6G NTN で復活画策 |

---

## 6. IPR / SEP 地図（粗い整理）

| 領域 | 主要 SEP 集中 | 備考 |
|:---|:---|:---|
| **CP-OFDM コア** | 広く交差ライセンス済、原典（Cimini 1985, Chang 1966）はパブリックドメイン | 現行 SEP は DMRS 配置・CP 長選択・PT-RS・numerology などの**利用特許** |
| **CP-OFDM 利用特許（NR PHY）**| Qualcomm, Huawei, Samsung, LG, Ericsson, Nokia, ZTE | 具体シェアは評価機関で揺れる `[要確認]` |
| **DFT-s-OFDM (SC-FDMA)** | Qualcomm, Ericsson（LTE 期特許が NR UL に継承）| `[要確認]` |
| **f-OFDM** | Huawei | Rel-15 SEP には非該当（実装依存のため）→ 実装差別化特許 |
| **FBMC/UFMC/GFDM** | Nokia Bell Labs、TU Dresden スピンオフ、Orange、CEA | 非標準のため Rel-15 SEP 非該当。6G NTN・衛星で潜在資産 |
| **OTFS** | **Cohere Technologies 単独集中（300+ 特許）** | SEP 集中リスクが大手警戒要因に。6G NTN で再浮上画策 |
| **BWP** | Samsung (WO2018203717A1), MediaTek, Qualcomm, Intel | Rel-15 の大型 IPR 領域 |
| **Mini-slot / URLLC** | Qualcomm, Samsung, LG | 2/4/7 シンボル PDSCH、front-loaded DM-RS |
| **SFI / Dynamic TDD** | **Qualcomm (US 2018/0279304)**, ZTE, Samsung | Group-common PDCCH、3層階層 |
| **QCL Type D** | Samsung, Qualcomm, Ericsson | FR2 ビーム管理、TCI state |
| **Sync/Channel raster 分離** | **Qualcomm (US 2018/0131487)** | GSCN 数値テーブル設計 |
| **SUL** | **Huawei**, Qualcomm | UL/DL 非対称キャリア組合せ、SUL スイッチング DCI |

---

## 7. Rel-15 の構造的ギャップ — 論文 vs 実装（原則 2）

| 学術論文の仮定 | Rel-15 実装制約 | 進歩性の源泉 |
|:---|:---|:---|
| 波形は自由選択可能 | **CP-OFDM 固定**（実装依存で TX 整形のみ可変）| f-OFDM 的 TX フィルタの実装差別化 |
| 連続 SCS 可 | **5 値のみ** (15/30/60/120/240 kHz, 240 は SSB 専用) | 離散 SCS 制約下のシステム最適化 |
| 任意スケール比 | **2^n のみ** | FFT ハードウェア共用、スロット境界整列 |
| UL MIMO 任意 | DFT-s-OFDM UL は**単レイヤのみ** | カバレッジ vs MIMO のスイッチング戦略 |
| OTFS 自由採用可 | 6G で検討中、5G NR では**非採用** | 高モビリティ特化の差分特許（Cohere 集中）|
| 理想エコシステム | **2018 商用化締切**というタイミング制約 | 成熟度リスクを避けた保守設計 |

---

## 8. 未解決課題 / 検証できなかったこと

### 8.1 Tdoc / 一次情報未検証

- 3^n / 17 kHz / 不規則比スケーリングの 3GPP 正式提案 Tdoc（見つからず、`[要確認]`）
- f-OFDM IPR の Rel-15/16/17 具体仕様条番号での再利用
- Nokia mixed numerology 主張の個別 RAN1 Tdoc 番号
- MediaTek "CBP" 用語自社由来の一次証拠
- 各社の Rel-15 SEP 正確シェア（IPlytics/LexisNexis/GreyB で順位差）
- Ericsson mini-slot 慎重姿勢の RAN1 寄書証拠
- Qualcomm 10-K における 5G モデム戦略の具体表現

### 8.2 構造的に不明

- Huawei f-OFDM 撤回の票数・日付
- 「2^n = 単一 FFT パイプライン」設計結論の Qualcomm 内部文書（ホワイトペーパーは FFT スケーリングを述べるが SKU 統合インセンティブは明文化していない）
- FBMC の敗因配分（MIMO vs レイテンシ vs エコシステム）の定量化

### 8.3 環境的制約（前ノートと共通）

- 3GPP FTP の `/ftp/tsg_ran/WG1_RL1/TSGR1_*/Docs/` が WebFetch から **HTTP 403**
- 3GPP Portal の認証アクセスが必要

---

## 9. Next Steps

### 9.1 追加検証タスク

- [ ] **R1-165425**（Huawei f-OFDM RAN1#85）の原文取得と f-OFDM 提案の具体内容確認
- [ ] **R1-167593**（Cohere OTFS RAN1#86）の評価結果の追加精査（性能主張の検証）
- [ ] **RP-160671**（NR SID）全文読み込み（NTT DOCOMO ラポータ原文）
- [ ] **IPlytics / GreyB / LexisNexis** の 5G SEP ランキング最新版取得と比較
- [ ] Qualcomm 10-K (FY2018-2024) の「5G modem strategy」関連記述抽出

### 9.2 関連トピックへの展開

- [ ] **6G 波形議論（2025 年〜）** の調査 — OTFS / Zak-OTFS / AFDM / OCDM が 6G NTN で再浮上する可能性 → `/survey-topic 6G waveform candidates`
- [ ] **Cohere Technologies の IPR 戦略** — 単独企業集中 SEP のケーススタディ → `/survey-topic OTFS IPR strategy`
- [ ] **DSS (Dynamic Spectrum Sharing) の Rel-15 技術的基盤** — LTE 15 kHz 基点維持が enable した事例
- [ ] **f-OFDM 的 TX 整形の gNB 実装差別化** — 標準に入らない技術の事業的意味
- [ ] **FBMC の 6G NTN 復活可能性** — 衛星系での CFO 頑健性再評価

### 9.3 発表資料への反映候補

- [NR周波数リソース構造の発表資料ドラフト.md](./NR周波数リソース構造の発表資料ドラフト.md) の Q&A 想定問答に、本ノート Sec 2-4 を「なぜその設計になったか」として組み込み可能
- 特に「なぜ 2^n か」「なぜ CP-OFDM か」「なぜ FBMC/GFDM は負けたか」は発表中の深掘り質問で出る可能性が高い

---

## 10. 信頼度の総評

| セクション | 信頼度 | 根拠 |
|:---|:---|:---|
| Qualcomm 事業モデル（QCT/QTL）| high | 公開財務資料 |
| Flarion 買収タイムライン・金額 | high | Qualcomm 公式プレス |
| 2^n スケーリング技術根拠 | medium-high | Qualcomm/Ericsson 公式白書・論文 |
| SKU 統合インセンティブ | medium | 業界通説、Qualcomm 内部文書未確認 |
| 波形候補比較（FBMC/UFMC/GFDM/OTFS）| medium-high | Liu 2016、Hong 2016 の複数査読論文で収束 |
| f-OFDM 実装依存合意 | high | Ericsson blog、ShareTechNote で一致 |
| OTFS の 2.1 dB 利得主張 | medium | Cohere 自社主張、独立検証は限定的 |
| 非 2^n 案の不在 | low-medium | 公開情報の範囲では見つからないが、全件検証していない `[要確認]` |
| Nokia/Orange/CEA の FBMC 研究 | high | 5G PPP 公式文書・Nokia Bell Labs 出版 |
| 各社 SEP シェア | low | 評価機関間で揺れ |
| オペレータ動機 | medium | スペクトラム保有は公開、動機は公開情報からの推論 |
