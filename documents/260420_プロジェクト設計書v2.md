# 3GPP標準化調査のための Claude × GitHub 学習リサーチ基盤 設計書(改訂版)

## 0. 設計方針の転換

当初案は自動化(GitHub Actions、sub-agents、スクリプト連携)に寄りすぎていました。
本改訂版は以下の前提に絞り込みます。

- **私的な勉強プロジェクト**。公開情報のみを扱う。
- **自動化は最小限**。定期取込スクリプトや Actions は持たない。
- **中核は「調査の基準軸(AI のルール)」**。Claude が何をどの観点で調べ、どう記録するかを定める。
- **よく参照する情報源は CLAUDE.md / skill にリンクを仕込む**。Claude が迷わず信頼できる一次情報を引けるようにする。
- **GitHub は「差分管理された個人ノートブック」として使う**。Actions 等は不要。

目的は「自動化された調査工場」ではなく、**「自分の思考と AI の調査が同じ基準軸で走るノート基盤」**です。

---

## 1. 調査の6つの基準軸(AI のルールの核心)

アップロードされた戦略文書から抽出できる「情報を整理するレンズ」は6つあります。
Claude が調査・要約・記録を行うときは、**必ずこの6軸を意識し、可能なら軸ごとに記述を分ける** —
これを CLAUDE.md の最上位ルールに据えます。

### 軸1: 技術レイヤー(何の技術か)
物理層(MIMO / チャネルコーディング / 波形・変調) / 高位層(制御・スケジューリング・RRC) / クロスレイヤ
→ RAN1 の担当範囲は物理層中心だが、シグナリング設計は高位層と切り離せない。

### 軸2: 世代軸(いつの技術か)
3G UMTS → 4G LTE(Rel-8~14) → 5G NR(Rel-15/16/17) → 5G-Advanced(Rel-18/19) → 6G(Rel-20/21~)
→ 新しい技術を見るときは「前世代では何が限界だったか」を必ず対比する。

### 軸3: 価値軸(何を改善するか)
スループット(peak/cell-edge) / 遅延 / 接続数 / **エネルギー効率** / **カバレッジ** / 信頼性 / **AI統合度**
→ 戦略文書4節で強調される通り、6Gは「スループット至上主義からの脱却」。太字項目が今後の主戦場。

### 軸4: 市場軸(誰が使うか)
Consumer(eMBB/XR) / B2B(Industry 4.0, 自動運転) / **FWA** / **NTN**(衛星・HAPS) / Ambient IoT
→ 4Gはconsumer、5GはFWAで辛うじて成功、6Gはどのセグメントに賭けるか。

### 軸5: 普及要因軸(なぜ広まるか / 広まらないか)
- キラーアプリとの合致(4Gのスマホ革命 vs 5GのB2B未成熟)
- 単一標準への収束(LTE vs WiMAX の歴史)
- 事業者ROI(CAPEX/OPEX と収益の釣り合い)
- 規模の経済(チップセットコスト低減)
- 後方互換性とマイグレーションコスト

→ **この軸は過去世代の比較レンズそのもの**。20_history/ で重点的に扱う。

### 軸6: 知財軸(特許化できるか)
- 新規性(既存論文・Tdoc・公報との差)
- 進歩性(**論文の理想仮定から 3GPP の実装制約への落とし込み差分**)
- 規格マッピング可能性(TS の必須要件 "shall" に対応させられるか)

→ 戦略文書5.2節の通り、学術論文は理想チャネルを前提にしがち。
実際のOFDMフレーム、限られたDCIビット、同期ズレ耐性といった**泥臭い制約**との差にこそ
進歩性が潜む。

---

## 2. CLAUDE.md(プロジェクトルートに置くファイル、そのまま使える完成版)

````markdown
# 3GPP Research — Claude の行動指針

## プロジェクトの目的

私的な勉強として、3GPP RAN1(MIMO・チャネルコーディング)の動向を体系的に把握し、
特許アイデアのベースとなる知見をストックする。**公開情報のみを扱う個人プロジェクト**。

戦略の背景は `00_framework/strategy-summary.md` を参照。

## 調査の6つの基準軸(最重要ルール)

情報を記録・要約・分析するときは、以下の6軸を意識し、該当する軸を明示する。
トピックページの frontmatter には必ず `axes: [...]` で該当軸を記録する。

1. **技術レイヤー**: 物理層 / 高位層 / クロスレイヤ
2. **世代軸**: 3G / 4G / 5G / 5G-Advanced(Rel-18/19) / 6G(Rel-20/21~)
3. **価値軸**: スループット / 遅延 / 接続数 / エネルギー効率 / カバレッジ / 信頼性 / AI統合度
4. **市場軸**: Consumer / B2B / FWA / NTN / Ambient IoT
5. **普及要因軸**: キラーアプリ / 標準収束 / ROI / 規模の経済 / 後方互換性
6. **知財軸**: 新規性 / 進歩性(実装制約差分) / 規格マッピング可能性

詳細と各軸の問いかけテンプレは `00_framework/axes.md` にある。

## 不変原則

1. **一次情報の出典を必ず記録する**: URL + 文書番号 + アクセス日。二次情報で止めない。
2. **「論文の理想仮定 vs 3GPPの実装制約」を常に意識する**。ここが進歩性の源。
3. **過去世代の成功/失敗と対比する**。5Gの苦戦を踏まえて6Gに何が必要かを毎回考える。
4. **記述は3層で分ける**: 目的(Why) → 手法の最小構成(What) → 実装制約・パラメータ(How)
5. **知らない・確信がないことは明記する**。曖昧な推測は `[要確認]` とマークする。

## 定番の情報源(調査はここから始める)

### 3GPP 一次情報
- 3GPP ポータル(全文書検索): https://portal.3gpp.org/
- 3GPP 仕様書一覧: https://www.3gpp.org/specifications-technologies
- RAN1 会合カレンダー: https://www.3gpp.org/dynareport?code=Meetings-R1.htm
- 3GPP ニュース: https://www.3gpp.org/news-events

### 学術論文
- arXiv cs.IT(情報理論): https://arxiv.org/list/cs.IT/recent
- arXiv eess.SP(信号処理): https://arxiv.org/list/eess.SP/recent
- IEEE Xplore: https://ieeexplore.ieee.org/

### 要件定義・需要側(戦略文書5.1節より)
- NGMN Alliance: https://www.ngmn.org/publications.html
- ITU-R WP5D(IMT): https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/
- Next G Alliance(北米): https://nextgalliance.org/white_papers/
- 6G-IA(欧州): https://6g-ia.eu/publications/
- one6G: https://one6g.org/publications/
- XG Mobile Forum(日本): https://xgmf.jp/

### 標準化組織と主要ベンダーの技術発信
- ETSI: https://www.etsi.org/
- Qualcomm OnQ Blog: https://www.qualcomm.com/news/onq
- Ericsson Research: https://www.ericsson.com/en/reports-and-papers
- Nokia Bell Labs: https://www.nokia.com/bell-labs/
- Samsung Research: https://research.samsung.com/

### 市場・普及データ(軸5の分析用)
- GSMA Intelligence: https://www.gsmaintelligence.com/research/
- 5G Americas White Papers: https://www.5gamericas.org/resources/white-papers/
- Ericsson Mobility Report: https://www.ericsson.com/en/reports-and-papers/mobility-report

### 特許・SEP(軸6の分析用)
- ETSI IPR データベース: https://ipr.etsi.org/
- Google Patents: https://patents.google.com/
- WIPO: https://www.wipo.int/

## Claude のリサーチ機能の使い分け

| 機能 | 用途 | 呼び出し方 |
|:---|:---|:---|
| **Web Search(通常対話)** | 個別の事実確認、最新ニュース、用語の意味 | 普通に質問 |
| **Research 機能** | 1トピックを6軸で体系的に横断調査 | 「Research」をオンにして問う |
| **Claude Code** | ローカルノートの整理、差分管理、skill起動 | ターミナルから `claude` |

どのモードでも、**上記「定番の情報源」を優先して参照する**こと。

## 記述スタイル

各ノートの frontmatter:

```yaml
---
title: トピック名
axes: [技術レイヤー, 世代軸, 価値軸, 知財軸]
generation: [rel-19, rel-20]
status: exploring | stable | obsolete
updated: YYYY-MM-DD
sources:
  - url: https://...
    accessed: YYYY-MM-DD
related:
  - ../topics/mimo/ai-csi-feedback.md
---
```

本文は「Why(なぜ必要か) → What(最小構成) → How(実装制約)」の3階層で書く。
````

**CLAUDE.md の意図**: 毎セッションで読み込まれるので、「6軸」「不変原則」「定番URL」「機能の使い分け」だけに絞り、詳細は `00_framework/` に逃がす。これで Claude は毎回同じレンズで調査する。

---

## 3. リポジトリ構造(シンプル版)

```
3gpp-research/                       ← private repo(個人GitHub)
├── CLAUDE.md                        ← 上記の行動指針
├── README.md
│
├── .claude/
│   └── skills/                      ← 4個だけ、中身は「質問テンプレ」
│       ├── survey-topic/SKILL.md
│       ├── analyze-gap/SKILL.md
│       ├── success-pattern/SKILL.md
│       └── digest-paper/SKILL.md
│
├── 00_framework/                    ← 調査の基準軸(ルール定義)
│   ├── axes.md                      ← 6軸の詳細と各軸の問いかけテンプレ
│   ├── question-templates.md        ← 定型質問集
│   ├── sources.md                   ← 情報源リンク集(CLAUDE.mdより詳細)
│   └── strategy-summary.md          ← アップロード戦略文書の要約
│
├── 10_topics/                       ← トピック別知識ベース
│   ├── mimo/
│   │   ├── cell-free-mmimo.md
│   │   ├── ai-csi-feedback.md
│   │   ├── ris.md
│   │   ├── near-field-xl-mimo.md
│   │   └── sub-thz-mimo.md
│   ├── channel-coding/
│   │   ├── ldpc-polar-foundations.md
│   │   ├── grand.md
│   │   ├── semantic-djscc.md
│   │   └── ai-native-coding.md
│   └── cross-cutting/
│       ├── energy-efficiency.md
│       ├── ntn-integration.md
│       └── ai-native-air-interface.md
│
├── 20_history/                      ← 過去世代に学ぶ(6軸で整理)
│   ├── 3g-umts.md
│   ├── 4g-lte.md
│   ├── 5g-nr.md
│   └── cross-generation-lessons.md  ← 世代間比較マトリクス
│
├── 30_meetings/                     ← 会合動向(手動記録)
│   └── ran1-NNN/
│       ├── overview.md              ← 会合全体の読解メモ
│       └── ffs.md                   ← 残された FFS 項目
│
├── 40_ideas/                        ← アイデアメモ(私的勉強レベル)
│   └── IDEA-YYYYMM-NNN.md
│
└── 50_sources/                      ← 読んだ文献のメモ
    ├── papers/                      ← 論文ごとのノート
    └── whitepapers/                 ← ホワイトペーパー要約
```

各ディレクトリの役割:

| 番号 | 役割 | 更新頻度 |
|:---|:---|:---|
| 00 | 調査ルールの定義(これ自体は Claude の行動を縛るメタ情報) | 半年に一度 |
| 10 | トピック別の体系的な知識ベース(「教科書」側) | 月次 |
| 20 | 過去世代の分析(軸5の成功要因分析) | 半年 |
| 30 | 会合ごとのスナップショット(「動向」側) | 会合ごと |
| 40 | 自分のアイデア | 不定期 |
| 50 | 一次情報のメモ(引用元) | 読むたび |

**10 と 30 の違い**: 10 は「時系列を超えた概念整理」、30 は「この会合でこう動いた」という時点情報。
10 は Wikipedia 的、30 は Git log 的。

---

## 4. 00_framework/ の中身(AI のルール本体)

### 4.1 `00_framework/axes.md`(6軸の詳細と問いかけテンプレ)

各軸について「Claude がトピックを調査するときに自問すべき質問」を列挙します。

```markdown
# 調査の6軸とその問いかけテンプレ

## 軸1: 技術レイヤー
- このトピックは物理層のどの機能(波形/符号化/MIMO/基準信号)に属するか?
- 高位層(スケジューリング, RRC)とどう結合しているか?
- シグナリング(DCI/MAC CE/RRC)の負担はあるか?

## 軸2: 世代軸
- 前世代(4G LTE, 5G Rel-15/16/17)では何が限界だったか?
- このトピックは現行リリースのどの Work Item / Study Item に属するか?
- Rel-20(6G SI)での位置づけは?

## 軸3: 価値軸
- このトピックが改善する KPI は何か?(スループット/遅延/エネルギー/カバレッジ/...)
- トレードオフは何か?(ある KPI を改善すると別の KPI を悪化させるか?)
- 事業者 OPEX(運用コスト)への影響は?

## 軸4: 市場軸
- 想定ユースケースは consumer か B2B か FWA か NTN か?
- そのユースケース市場は成熟しているか、これから立ち上がるか?

## 軸5: 普及要因軸
- 4G で似た技術課題をどう解決したか?
- 5G で類似の試みが苦戦したならその理由は?
- エコシステム(チップセットベンダ、端末、事業者)の受容性は?
- 後方互換性コストは受容可能か?

## 軸6: 知財軸
- 既存論文・Tdoc・公開特許公報で類似アイデアはあるか?
- **論文の理想仮定と 3GPP の実装制約の差**はどこにあるか?
  - 理想チャネルの想定 → 実際の同期ズレ、遅延拡散、ドップラー
  - 連続値パラメータ → DCI の数ビット量子化
  - 完全情報仮定 → 限られたフィードバック帯域
- 規格の "shall" 文言に落とし込める形で記述できるか?
```

### 4.2 `00_framework/question-templates.md`(定型質問)

Claude への問いかけそのもののテンプレ集。skill から参照する。

```markdown
# 定型質問テンプレ

## トピック新規調査テンプレ

以下の観点で [トピック名] を調査してください。情報源は CLAUDE.md の
「定番の情報源」を優先し、一次情報の URL を必ず記録してください。

1. **定義と背景**: このトピックは何で、なぜ必要とされたか
2. **技術要点**: 最小構成(What)と実装時の制約(How)
3. **前世代との差分**: 4G/5G と比較して何が新しいか
4. **主要プレイヤー**: 学術(IEEE)、3GPP(Tdoc提出企業)、要件定義(NGMN等)
5. **未解決課題**: FFS に残されているもの、学術でも未解決のもの
6. **市場・普及の見込み**: どのセグメントで誰が使うか
7. **知財余地**: 論文と 3GPP 実装制約のギャップ

## ギャップ分析テンプレ

[トピック名] について、以下を3つのバケットで整理してください。

- **Gap A**: 学術で解決済みだが 3GPP に未取込
- **Gap B**: 3GPP FFS に残っており学術でも議論中
- **Gap C**: 実装制約ギャップ(同期/後方互換/シグナリング負担)

各ギャップについて、出典と、どの基準軸に該当するかを記載してください。

## 世代比較テンプレ

[トピック/技術要素] について、3G/4G LTE/5G NR/5G-Advanced/6G構想 の
5列でマトリクスを作り、以下の行で比較してください。

- 技術選択肢
- 解決した課題
- 新たに生じた課題
- 普及面での評価(軸5)
- 知財活動の主要プレイヤー

## 論文読解テンプレ

[論文] について以下を抽出してください。

- メタ: 著者/年/会議 or ジャーナル/DOI
- 主張(Contribution): 3-5点
- **前提仮定**: チャネル、SNR、複雑性、CSI精度など
- **3GPP実装時のギャップ**: 前提仮定 vs NR 仕様の制約の差
- 関連トピック(`10_topics/` のどれに紐づくか)
```

### 4.3 `00_framework/sources.md`

CLAUDE.md の「定番の情報源」を詳細化したもの。各ソースについて
「いつ見るか」「何が載っているか」を書く。Claude Code の skill から参照させる。

---

## 5. Skills の設計(4個、すべて「質問と観点のテンプレ」)

どの skill も **自動化スクリプトを持たず**、Claude への問いかけのテンプレと参照URLを
まとめた Markdown ファイルです。`/skill-name` で呼び出すと、そのテンプレに沿って
Claude が動きます。

### 5.1 `.claude/skills/survey-topic/SKILL.md`

```markdown
---
name: survey-topic
description: 指定したトピックを6軸で体系的に調査し、10_topics/ 配下の Markdown として記録する
user-invocable: true
---

# survey-topic

## 使い方
`/survey-topic <トピック名>` で起動。

## 手順
1. `00_framework/axes.md` と `00_framework/question-templates.md` を参照する
2. CLAUDE.md の「定番の情報源」から優先順に web_search / web_fetch で情報を収集する:
   - まず 3GPP ポータル / NGMN / arXiv を引く
   - 次にベンダー(Qualcomm/Ericsson/Nokia/Samsung)の technical blog
3. トピックを「定型質問テンプレ:トピック新規調査テンプレ」の7項目で整理する
4. 6軸のうち該当する軸を frontmatter `axes:` に明示する
5. **過去世代(3G/4G/5G)との対比**を必ず1セクション設ける
6. 結果を `10_topics/<category>/<slug>.md` に保存する
7. 関連する他のトピックへのリンクを `related:` に追加

## 禁止事項
- 一次情報のURLなしに事実を記載しない
- 不確実な情報は `[要確認]` と明示する
```

### 5.2 `.claude/skills/analyze-gap/SKILL.md`

```markdown
---
name: analyze-gap
description: 指定トピックについて学術/3GPP/実装制約のギャップを3バケットで可視化する
user-invocable: true
---

# analyze-gap

## 手順
1. 対象トピックの `10_topics/` ノートを読み込む
2. 最新の関連論文(arXiv)と 3GPP の該当 WI/SI の状況を web_search で確認する
3. `question-templates.md` の「ギャップ分析テンプレ」に沿って Gap A/B/C を抽出
4. 各ギャップに **軸6(知財軸)** の評価を付ける:進歩性の源泉として強いか弱いか
5. 結果をチャットに出力し、永続化する場合は `10_topics/<slug>/gap-YYYYMM.md` に保存

## 重要な問いかけ
「論文の理想仮定」と「3GPP の実装制約」の間にあるギャップを言語化する。
戦略文書5.2節の通り、ここが進歩性の源。
```

### 5.3 `.claude/skills/success-pattern/SKILL.md`

```markdown
---
name: success-pattern
description: 過去世代(3G/4G/5G)の成功・失敗事例から普及要因を学び、6Gの検討課題に照射する
user-invocable: true
---

# success-pattern

## 手順
1. `20_history/` 配下の世代別ノートを読む
2. `question-templates.md` の「世代比較テンプレ」で現在のトピックを過去世代に投影する
3. **軸5(普及要因軸)** を中心に、以下を問う:
   - 4G LTE が成功した構造的要因(キラーアプリとの同期、標準収束、規模の経済)は
     このトピックでも機能するか?
   - 5G が苦戦した要因(B2B未成熟、CAPEX過大、SA移行遅延)は繰り返されるか?
   - 事業者 ROI が成立するシナリオは何か?
4. 結論を「6Gで成功するための条件」の形で3点に絞って出力する

## 参考情報源
- GSMA Intelligence, 5G Americas, Ericsson Mobility Report(軸5のデータ)
- Qualcomm OnQ, BCG / Bain レポート(事業者経済の分析)
```

### 5.4 `.claude/skills/digest-paper/SKILL.md`

```markdown
---
name: digest-paper
description: 論文を読み、3GPP実装制約との差分を強調した構造化メモを 50_sources/papers/ に保存する
user-invocable: true
---

# digest-paper

## 手順
1. 論文 PDF または URL を受け取る
2. `question-templates.md` の「論文読解テンプレ」で抽出する
3. **前提仮定 vs 3GPP 実装制約のギャップ**のセクションに特に字数を使う
4. `50_sources/papers/YYYY-MM-DD__author__slug.md` に保存
5. 該当する `10_topics/<slug>.md` の `related` セクションにリンクを追記する
```

**どれも自動化スクリプトを持たず、「Claude への問いかけのルール」そのものです。**
これが今回のご指示の核心で、基準軸を AI のルールとして定めるという本来の目的に合致します。

---

## 6. 20_history/ — 過去世代に学ぶ部分の設計

ご指示の「過去の 3G/4G の成功した部分に学ぶ」が重要なので独立章にします。

### 6.1 各世代ノートの共通構造

`20_history/4g-lte.md` の例:

```markdown
---
title: 4G LTE の成功要因分析
generation: 4g
axes: [世代軸, 価値軸, 市場軸, 普及要因軸]
updated: YYYY-MM-DD
---

## 1. 技術的要点(軸1・3)
- OFDMA / SC-FDMA の採用
- All-IP ネットワーク
- MIMO のマス化(2x2 → 4x4 → 8x8)

## 2. 市場文脈(軸4)
- 2009年頃のスマートフォン爆発的普及との完全な同期
- モバイルビデオ/SNSという消費者のキラーアプリ

## 3. 普及を成立させた構造的要因(軸5)
- WiMAX との標準競争に勝利 → 世界単一標準化
- エコシステムの規模の経済(チップセットの急激なコストダウン)
- 事業者 ROI が明確(ARPU 向上)
- GSM/UMTS からの連続性と後方互換

## 4. 残した教訓
- 「技術単体」ではなく「アプリと同期した技術」が普及する
- 単一標準への収束は規模の経済を生む最大のドライバ
- 消費者需要が明確だと事業者投資が加速する

## 5. 6G に投影すると(軸5 × 軸2)
- 6G のキラーアプリ候補(AIネイティブサービス、没入型XR、統合センシング)は
  4Gのスマホ革命ほど明確か? → **[要確認] 現時点では不明瞭**
- 標準収束は進むか? → 3GPP がグローバル標準の中心でありほぼ確実
- 事業者 ROI が成立する設計はエネルギー効率と NTN 統合にかかっている

## 出典
- [GSMA Intelligence ...](https://...) (accessed YYYY-MM-DD)
- [BCG 2015 The Mobile Revolution ...](https://...) (accessed YYYY-MM-DD)
- 戦略文書 section 4
```

### 6.2 `20_history/cross-generation-lessons.md`(世代横断マトリクス)

3G/4G/5G/6G構想の4列で、軸1-6の各行について比較マトリクスを作る。
これが「過去から学ぶ」の中心ドキュメント。例:

| | 3G UMTS | 4G LTE | 5G NR | 6G構想 |
|:---|:---|:---|:---|:---|
| 価値軸での主眼 | データ通信の一般化 | 高速大容量 | 三つの柱(eMBB/URLLC/mMTC) | エネルギー/カバレッジ/AI |
| キラーアプリ | モバイルインターネット黎明 | スマホ/ビデオ/SNS | FWA(局所成功) | 未確定 |
| 標準収束 | WCDMA優位 | LTE単一 | 5G単一 | 3GPP主導で継続 |
| 事業者ROI | ○ | ○ | △(B2B未成熟) | 成功条件=OPEX削減 |
| 物理層革新 | CDMA | OFDMA/MIMO | Massive MIMO/LDPC/Polar | Cell-Free/RIS/AI-native |
| 残した課題 | 遅延大 | カバレッジ穴 | CAPEX過大 | 未知 |

このマトリクスを **Claude が `success-pattern` skill で毎回参照** する。

---

## 7. Claude のリサーチ機能の使い分け(具体的な運用)

### 7.1 Claude.ai Web Search(通常の対話)

- **用途**: 単発の事実確認、用語、最新ニュース
- **例**: 「RAN1 #122 の開催地と開催期間は?」「RIS の最新の商用化事例は?」
- **運用**: 特別な準備は不要。ただし CLAUDE.md の「定番の情報源」をユーザー側で
  常に意識し、必要ならチャット冒頭に「NGMN の最新 white paper から引いて」と明示する。

### 7.2 Claude.ai Research 機能(深い調査)

- **用途**: 1トピックを6軸で横断的に調べて包括的レポートを得る
- **呼び出し**: Claude.ai で Research を ON
- **プロンプトの定型**:
  ```
  トピック: [AI-assisted CSI feedback]

  以下を調査してください。

  優先情報源:
  - 3GPP ポータル https://portal.3gpp.org/
  - arXiv eess.SP / cs.IT
  - NGMN https://www.ngmn.org/publications.html
  - Qualcomm OnQ, Ericsson Research

  出力観点(6軸):
  1. 技術レイヤー: 物理層のどの機能か、シグナリング負担
  2. 世代軸: Rel-18/19での扱い、Rel-20での位置づけ
  3. 価値軸: 改善するKPIとトレードオフ
  4. 市場軸: 想定ユースケース
  5. 普及要因軸: 4G/5Gの類似試みと対比
  6. 知財軸: 論文と3GPP実装制約のギャップ

  一次情報のURLを必ず記載してください。
  ```
- **運用**: このテンプレは `00_framework/question-templates.md` にも置いておく。

### 7.3 Claude Code(ローカルノート整理)

- **用途**: リポジトリ内のノートを読み・書き・リンクし合う作業
- **呼び出し**: ターミナルで `claude`
- **どの skill をいつ使うか**:
  - 新しいトピックを立てる → `/survey-topic`
  - 既存トピックのギャップを洗う → `/analyze-gap`
  - 世代比較を深める → `/success-pattern`
  - 論文を読んだ → `/digest-paper`

### 7.4 使い分けの判断フロー

```
事実を1つ確認したい         → Claude.ai + Web Search
体系的なレポートがほしい     → Claude.ai + Research機能(6軸テンプレ使用)
ノートを作成・更新・整理したい → Claude Code + skill
```

---

## 8. GitHub の使い方(最小限)

- **リポジトリ**: private(公開情報のみ扱うが個人ノートなので非公開で運用)
- **ブランチ**: 原則 main 直コミットでも可。複数トピック並行で書くときだけ feature ブランチ
- **Issue**: **使わなくてよい**。トピック自体が `10_topics/*.md` というファイル
- **Actions**: **使わない**
- **差分の価値**: 
  - ある会合のあとで `30_meetings/ran1-NNN/ffs.md` にどの FFS が追加されたか
  - トピックノートの結論がどう変わったか
  - これらを git log / git blame で振り返れる

**GitHub は「差分が追える個人ノートブック」として使う**。それ以上の機能は今回は使わない。

---

## 9. 最初にやること(具体的なスタート手順)

1. GitHub で `3gpp-research`(private)リポジトリを作成
2. このドキュメントの「2. CLAUDE.md」をそのままコピーして配置
3. `00_framework/` の4ファイルを作成:
   - `axes.md`(4.1節の内容)
   - `question-templates.md`(4.2節の内容)
   - `sources.md`(CLAUDE.md のリンク集を詳細化)
   - `strategy-summary.md`(アップロードされた戦略文書の要約を Claude に作らせる)
4. `.claude/skills/` に4個の SKILL.md を配置(5節の内容)
5. `20_history/` の4ファイルを Claude Code の `/success-pattern` を使って埋める
   (3G/4G/5G それぞれのノート + cross-generation-lessons.md)
6. `10_topics/mimo/` と `10_topics/channel-coding/` の主要トピックを
   `/survey-topic` で1個ずつ作り、挙動を確認する

**最初の1日**でここまで到達できます。自動化が一切ないので、セットアップコストが低い。

---

## 10. 分からないこと / 今後の検討余地

- **Claude.ai の Research 機能の最適な使い方**は運用してみないと見えてこない部分がある。
  最初は 1 トピックで試し、出力の質と時間コストを見て、定型プロンプトを調整する。
- **`10_topics/` のトピック分割粒度**は、書き進めるうちに「細かすぎた」「大きすぎた」が見える。
  最初は戦略文書に出てきた単位で切り、半年後にリファクタリングする前提でよい。
- **3GPP ポータルの検索性**は限界があり、`WhatTheSpec.net` や `Apex Standards` のような
  サードパーティツールの補助が実務上は必要になる場合がある。
  ただし最初は 3GPP 公式で足りる範囲に留めるのが無難。

---

## 11. 次に具体化するなら

どれか一つを選べば1セッションで完了します:

- **A.** `00_framework/axes.md` を完全に書き起こす(6軸の問いかけテンプレを各軸10項目ずつに拡充)
- **B.** `20_history/` の4ファイル(3G/4G/5G/世代横断マトリクス)を完成させる
- **C.** `10_topics/` の初期構造と主要トピック(MIMO 4件 + チャネルコーディング 4件)の
  スケルトン(タイトルと6軸タグだけ)を作る
- **D.** `question-templates.md` を拡充し、Claude.ai の Research 機能に貼り付けるだけで
  使える定型プロンプトを5〜10本用意する
- **E.** この設計自体のさらなる改善点の議論

C と D は「明日から使える」に直結するので実用性が高いです。
B は戦略文書の4節(過去世代の分析)を本設計の中核資産に昇格させる作業で、
「過去から学ぶ」というご指示に最も直接応えます。
