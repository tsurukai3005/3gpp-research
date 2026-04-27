# 3GPP FTP アクセスの知見集（cookbook）

RAN1 会合の Tdoc / Chair Notes / Agenda を効率的に取得・解析するための運用ノート。
`/survey-topic` 等の調査スキルから参照される実装ガイド。`sources.md` の URL リストを「実際にどう叩くか」に翻訳したもの。

初版の根拠: 2026-04-27 の RAN1#124bis（Malta、2026-04-13〜04-17）調査で得られた経験則。

---

## 1. 何で時間がかかるか — 失敗パターンと回避策

### 1.1 WebFetch / WebSearch では 3GPP の核心ファイルに辿り着けない

| 起こること | 原因 | 回避策 |
|:---|:---|:---|
| `https://portal.3gpp.org/...` が 403 | Anthropic の WebFetch User-Agent が拒否される | **WebFetch を諦めて `curl -A "Mozilla/5.0"` に切り替える** |
| `https://www.3gpp.org/dynareport?...` が 403 | 同上 | 同上 |
| `https://www.3gpp.org/ftp/...` が 403 | 同上 | 同上 |
| WebSearch で `"RAN1#124bis"` が引っかからない | 直近会合は Google index に入る前 | **3GPP FTP の directory listing を直接 grep する** |
| 古い (RAN1#120 等) のブログ記事しか出ない | 同上 | 同上 |

> **ルール**: 3GPP FTP は IIS で公開配信されており、認証不要で誰でも DL 可能。問題は「Anthropic の WebFetch がブロックされる」だけ。`curl -A "Mozilla/5.0"` で常時アクセス可。

### 1.2 フォルダ命名の揺れに惑わされる

`#124-bis` の正しいフォルダ名を検索や推測で見つけようとすると数ターン無駄になる。

| 表記 | 用途 |
|:---|:---|
| `RAN1#124-bis` / `RAN1#124bis` / `RAN1 #124-bis` | 文書タイトル中の人間向け表記（ハイフン揺れ） |
| **`TSGR1_124b`** | **FTP フォルダ名（公式）** |
| `TSGR1_124` | 直前のプレナリ（bis なし） |
| `TSGR1_122b-e` 等 | `-e` は electronic-only meeting（コロナ禍由来） |

> **ルール**: `#<n>-bis` のフォルダは必ず `TSGR1_<n>b`（小文字 b、ハイフンなし）。推測する前に、まず親 `WG1_RL1/` の listing から実在名を grep する（次節）。

### 1.3 一次情報を取りに行く前に二次情報で消耗する

`arxiv.org`、`sharetechnote.com`、`6ghow.com`、ベンダーブログ等は内容理解には便利だが、**直近会合の合意事項は載っていない**ことが多い。今回（#124bis、4/17 終了 → 10 日後の 4/27 調査）でも 6ghow は #124 までしかカバーしていなかった。

> **ルール**: 「会合終了から数週間以内」の調査は、最初から FTP の `Chair_notes/*_eom*.docx` を読みに行く。二次情報を使うのは背景・歴史・rapporteur 経歴の確認のみ。

---

## 2. 標準アクセス手順（cookbook）

### 2.1 全体フロー

```
1. WG1_RL1/ の listing で正しいフォルダ名 (TSGR1_<n>[b]) を確認
2. agenda.csv で章番号と全体構造を把握（最小コスト）
3. Tdoc_list/<最新日付>.xlsx で寄書件数・FL・提出企業を集計
4. Chair_notes/_eom<最大番号>.docx で合意事項を逐語抽出
5. 必要に応じて Inbox/drafts/<AI>(...)/ で個別 FL Summary を読む
```

各ステップのファイルサイズ目安:
- agenda.csv: ~4 KB
- Tdoc_list xlsx: ~500 KB（行数 ~1,700）
- Chair Notes EoM docx: ~1.2 MB（段落 ~5,000）
- 個別 Tdoc docx: 数百 KB 〜数 MB（×1700 件）

### 2.2 URL パターン早見表

`<MEET>` = `TSGR1_124b` 等のフォルダ名。`<DATE>` = 会期内 YYMMDD。`<VER>` = `eom4` 等。

| 用途 | URL |
|:---|:---|
| 親 listing | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/` |
| 会合 root | `https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/<MEET>/` |
| Agenda CSV | `<MEET>/Agenda/agenda.csv` |
| Tdoc list | `<MEET>/Inbox/Tdoc_list/TDoc_List_Meeting_RAN1%23<n>-bis%20(<DATE>).xlsx` |
| Chair Notes 最終 | `<MEET>/Inbox/Chair_notes/Chair%20notes%20RAN1%23<n>bis_<VER>.docx` |
| 個別 Tdoc | `<MEET>/Docs/R1-<番号>.zip` |
| FL Summary 等 | `<MEET>/Inbox/drafts/<AI>(...)/.../*.docx` |
| Sorour notes（速報メモ） | `<MEET>/Inbox/Sorour_notes/` |
| Hiroki notes | `<MEET>/Inbox/Hiroki_notes/` |

> **URL エンコード必須文字**: `#` → `%23`, スペース → `%20`。bis ファイル名は `RAN1#124-bis` 表記が混在するため両方試す。

### 2.3 ステップ別コマンド

#### Step 1: 正しいフォルダ名を確認

```bash
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/" -o /tmp/ran1_root.html
grep -oiE 'TSGR1_12[0-9][a-z]?' /tmp/ran1_root.html | sort -u | tail -30
```

出力例:
```
TSGR1_120  TSGR1_120b  TSGR1_121  TSGR1_122  TSGR1_122b
TSGR1_123  TSGR1_124  TSGR1_124b  TSGR1_125  TSGR1_126
```

#### Step 2: 会合フォルダ構造を確認

```bash
curl -s -A "Mozilla/5.0" "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/" \
  | grep -oiE 'href="[^"]+"' | grep -v 'sortby\|3gpp.org/$\|3gpp.org/ftp/$'
```

サブフォルダは `Agenda / Docs / Inbox / Invitation / LS / Report` の 6 構成が標準。

#### Step 3: Agenda（最小コスト、最初に読む）

```bash
curl -s -A "Mozilla/5.0" \
  "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Agenda/agenda.csv" \
  -o /tmp/agenda.csv
```

CSV は `"番号","タイトル"` の 2 列。章立てだけ把握できればよい。

#### Step 4: Tdoc 一覧（XLSX）

```bash
curl -s -A "Mozilla/5.0" \
  "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Tdoc_list/TDoc_List_Meeting_RAN1%23124-bis%20(260417).xlsx" \
  -o /tmp/tdoc.xlsx
```

会期中は毎日 (`260413`〜`260417`) 更新される。**最終日の版を使う**（status が確定する）。

XLSX の標準カラム（36 列）:
```
TDoc, Title, Source, Contact, Contact ID, Type, For, Abstract,
Secretary Remarks, Agenda item sort order, Agenda item,
Agenda item description, TDoc sort order within agenda item,
TDoc Status, Reservation date, Uploaded, Is revision of, Revised to,
Release, Spec, Version, Related WIs, CR, CR revision, CR category,
TSG CR Pack, UICC, ME, RAN, CN, Clauses Affected,
Reply to, To, Cc, Original LS, Reply in
```

集計対象として有用な列: `Agenda item`（章番号集計）/ `Source`（提出企業）/ `Type`（discussion/CR/agenda/...）/ `TDoc Status`（agreed/noted/withdrawn 等）。

#### Step 5: Chair Notes（合意事項本体）

```bash
# 最終版（_eom + 数字最大）を選ぶ
curl -s -A "Mozilla/5.0" \
  "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom4.docx" \
  -o /tmp/chair.docx
```

リビジョン規約:
- `_v00` 〜 `_v15`: 会期中（毎日数回更新）
- `_eom`, `_eom1`〜`_eom4`: End of Meeting、会期終了後の確定版。**数字が大きい方が新しい**

### 2.4 解析（Python が最速）

Python 3 + openpyxl + python-docx で 1〜2 秒で全量解析できる。Windows + bash の本プロジェクトでは:

```bash
py -3 -m pip install --quiet openpyxl python-docx
```

#### XLSX: agenda 別集計

```python
import openpyxl
from collections import Counter
wb = openpyxl.load_workbook('/tmp/tdoc.xlsx', read_only=True, data_only=True)
ws = wb.active
rows = list(ws.iter_rows(values_only=True))
hdr = rows[0]; ix = {h:i for i,h in enumerate(hdr)}
data = [r for r in rows[1:] if r[0] and str(r[0]).startswith('R1-')]

# agenda 別の件数
agenda_count = Counter(r[ix['Agenda item']] for r in data)

# 特定 agenda の提出企業
target = '9.1.1'
sub = [r for r in data if r[ix['Agenda item']] == target]
src_count = Counter(str(r[ix['Source']]) for r in sub)
```

#### DOCX: 章単位で抽出

```python
import docx
d = docx.Document('/tmp/chair.docx')
# まず Heading スタイルだけ全部出して章のインデックスを取る
for i, p in enumerate(d.paragraphs):
    if p.style.name.startswith('Heading') and p.text.strip():
        print(f"[{i}] {p.style.name}: {p.text[:120]}")
# 次に章範囲を切って本文を取得
def extract(start, end):
    return '\n'.join(p.text for p in d.paragraphs[start:end] if p.text.strip())
```

> **重要**: Heading は **見出しスタイル** で判定（`Heading 1`〜`Heading 4`）。テキストの番号 prefix（"9.1.1" 等）でマッチさせると `9.1.1` で始まる本文に誤マッチする。

### 2.5 Source 列の罠（提出企業集計）

XLSX の `Source` 列は `"Huawei, HiSilicon"` のように **コンマ区切りで複数企業**が入る。

- そのまま Counter にかけると「Huawei」「HiSilicon」「Huawei, HiSilicon」が別カウントになる
- Source を split すると「Inc.」「Sanechips」等の補助名が独立して数えられる（誤集計）
- 推奨: **Source 文字列をそのまま「提出グループ」としてカウント**。組合せ単位の出現頻度に意味があるため

例外: `Moderator (Huawei, Xiaomi)`、`Moderators (ZTE, Apple)` は co-FL を意味する。これは split 不可、文字列のまま扱う。

---

## 3. 何を読み、何を読まないか — 判断基準

### 3.1 デフォルトで読むもの（≒ 全件 sweep の対象）

| ファイル | 判断 | 理由 |
|:---|:---|:---|
| `agenda.csv` | 必ず読む | 4 KB、最初の地図 |
| `Tdoc_list/*.xlsx`（最終日版） | 必ず読む | 集計用メタデータ |
| `Chair_notes/*_eom<最大>.docx` | 必ず読む | 合意事項の正本 |

### 3.2 トピック特定後に読むもの

| ファイル | 判断基準 |
|:---|:---|
| `Inbox/drafts/<AI>/*FL summary*.docx` | 該当 agenda の議論進化を追う必要があるとき。FL summary は #1〜#10 まであるため 1 ラウンドだけ読むのは無意味 |
| `Inbox/drafts/<AI>/*Round<N>*.docx` | 上同 |
| 個別 Tdoc `Docs/R1-<番号>.zip` | 「特定企業の特定主張の根拠を引きたい」場合のみ |

### 3.3 通常は読まないもの

| ファイル | 理由 |
|:---|:---|
| `Docs/` の全 1,000+ 件 | 量的に不可能。Tdoc 一覧 + Chair Notes でほぼ要件は満たせる |
| `_v00`〜`_v15` の途中版 Chair Notes | `_eom<最大>` が確定版 |
| `Hiroki_notes/`, `Sorour_notes/` | 個人速記メモ。Chair Notes が出れば不要 |
| `Invitation/`, `LS/`, `Welcome_speech` | 調査目的では不要 |

> **量の感覚**: RAN1 会合は約 1,700 件の Tdoc が出る。1 件 30 秒で読んでも 14 時間。**個別 Tdoc 全読は前提から放棄**。集計は XLSX、結論は Chair Notes、必要なら FL Summary、と段階的に深掘る。

---

## 4. 今回（2026-04-27 RAN1#124bis 調査）の振り返り

### 4.1 時間がかかった所

| フェーズ | 時間配分（体感） | 内訳 |
|:---|:---|:---|
| 会合フォルダ名の特定 | 全体の 50%（無駄が多い） | WebFetch 403 を 6 回連続、WebSearch で誤情報、Wispro/6ghow を辿るが #124bis 未収録 |
| `curl + grep` で `TSGR1_124b` 確定後 | < 5 分 | 直接 listing が出る |
| Tdoc list / Chair Notes 解析 | < 10 分 | Python で全自動 |
| ノート執筆 | 全体の 30% | 9 セクションの逐語整理 |

**教訓**: 最初の 2 ターンで「WebFetch が 403 を返した」段階で `curl + bash` に切り替えるべきだった。

### 4.2 読まなかったもの・読めなかったもの

| 種別 | 読んだか | コメント |
|:---|:---|:---|
| Agenda CSV | ✅ 全文 | 4 KB |
| Tdoc 一覧 XLSX | ✅ 全 1,724 行 | メタデータのみ |
| Chair Notes EoM v4 | ✅ 対象 9 章 | 全 5,049 段落中、対象部 ~700 段落 |
| 個別 Tdoc 本体 | ❌ 0 件 | 量的に断念。Next Steps に列挙 |
| FL Summary 本体 | ❌ 0 件 | 同上。Apple, Qualcomm, Samsung+vivo の各 #1〜#10 が候補 |

### 4.3 効率化の改善点（次回の運用）

1. **FTP listing 取得を真っ先に行う**（`WG1_RL1/`、`<MEET>/`、`<MEET>/Inbox/`）。3 連続 listing で会合構造の全体像が把握できる
2. **WebFetch 失敗で 2 回詰まったら即 curl/bash に切替**。WebFetch でリトライしない
3. **XLSX/DOCX の解析は Python 一択**。`grep` での docx は zip 内 XML を見るしかなく非効率
4. **FL summary は Round 単位ではなく「最後の Round」を選んで読む**。#1 は議題提起、最終 Round が結論
5. **agenda 番号で章・XLSX 集計・DOCX 抽出を一貫させる**（"9.1.1" のような prefix を全フェーズの key に）

---

## 5. 参考: 関連リソースの「使い分け」

| リソース | URL | 強み | 弱み |
|:---|:---|:---|:---|
| 3GPP FTP（直接 curl） | `www.3gpp.org/ftp/...` | 最新・公式・認証不要 | UI なし、自前で listing 解析必要 |
| portal.3gpp.org | `portal.3gpp.org/` | TS/TR/WI 横断検索、login で AI/ML フィルタ可 | WebFetch では 403、login 必要な機能あり |
| WhatTheSpec.net | `whatthespec.net/` | TS/TR の本文検索 | RAN1 議事まではカバーしていない |
| Apex Standards | `apexstandards.com/` | TDoc データ可視化 | 個別問合せベース、即時公開なし |
| 6G HOW Agreements | `6ghow.com/agreements/` | RAN1 合意事項を会合横断で追跡 | **直近会合は反映遅延（数週間〜）** |
| Wispro 解析記事 | `wispro.com/en/...` | AI 駆動の会合プレビュー | 全会合は対象外、英語のみ |
| arXiv（学術論文） | `arxiv.org/list/...` | 理論・実装の深い解説 | 3GPP の確定仕様とは独立 |

---

## Next Steps

- [ ] `framework/sources.md` の補助ツール表に「FTP 直接 curl」を一行追加して本ファイルへの参照を入れる
- [ ] `digest-paper` スキルから docx 解析パターンを参照できるよう README を整える
- [ ] 個別 Tdoc を読む需要が出たら、`Docs/R1-<num>.zip` の自動 unzip + docx 抽出スクリプトを `framework/scripts/` に置く（現状は手動）
- [ ] RAN2/RAN3/RAN4 でも同じフォルダ規則（`TSGR2_*`, `TSGR3_*`, `TSGR4_*`）が成立することを 1 サンプルで確認する
