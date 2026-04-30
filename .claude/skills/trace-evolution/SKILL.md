---
name: trace-evolution
description: 自然言語のトピック語から RAN1 議論変遷を縦に追い、会合横断のタイムラインを documents/ に生成する
user-invocable: true
---

# trace-evolution

## モチベーション

特定トピック（例: CSI 圧縮、Type-II codebook、6GR PDCCH）について
**「いつ・どの会合で・誰が・何を主張し・何が合意されたか」** を縦に追うのは、
個別 Tdoc / Chair Notes を会合ごとに横並びで読んでも見えない。

このスキルは [`framework/catalog/`](../../../framework/catalog/) と既存 `references/` の
Chair Notes を横串で串刺しし、**会合を跨いだ議論の系譜** を Markdown に描く。

埋め込み検索ではなく **構造化メタデータ + Markdown→Markdown 抽出** を選ぶ理由:

- 議論の継続性は AI 番号の系譜・FL 記名・revision pointer などの構造情報で追える
- 引用元 Tdoc / Chair Notes に wikilink で戻れる方が SEP 探索に有用
- 取得済み資料の不足は **「不足を報告」** できる方が、誤った要約を出すより価値が高い

## 使い方

```
/trace-evolution <自然言語のトピック語>
/trace-evolution <自然言語のトピック語> --meetings RAN1#124,RAN1#124bis,RAN1#125
/trace-evolution --ai-id <安定 AI ID>
/trace-evolution <トピック語> --from RAN1#123 --to RAN1#125
```

例:

- `/trace-evolution CSI 圧縮`
- `/trace-evolution type-II codebook`
- `/trace-evolution 6GR の DL 制御チャネル --meetings RAN1#124bis,RAN1#125`
- `/trace-evolution --ai-id ai_6gr_mimo_dl_pdcch`

## 入力と前提

- **必須入力**: 以下のいずれか
  - 自然言語のトピック語（agenda-items.yaml の `aliases` と fuzzy match）
  - `--ai-id <安定 ID>`（agenda-items.yaml のキーを直接指定）
- **オプション**:
  - `--meetings`: 対象会合をカンマ区切りで絞り込み
  - `--from <会合>` / `--to <会合>`: 範囲指定
  - `--persona <persona-file>`: ペルソナ視点で評価
- **前提条件**:
  - [`framework/catalog/meetings.yaml`](../../../framework/catalog/meetings.yaml) が存在
  - [`framework/catalog/agenda-items.yaml`](../../../framework/catalog/agenda-items.yaml) が存在
- **実行不可の条件**: トピックが catalog の aliases に該当せず、ユーザーから補足情報も得られない場合

## 実行フロー

### Phase A: トピック解決（自然言語 → 安定 AI ID）

1. [`framework/skill-contract.md`](../../../framework/skill-contract.md) と [`framework/principles.md`](../../../framework/principles.md) を読み、Global Will / Will Not を確認する
2. [`framework/catalog/agenda-items.yaml`](../../../framework/catalog/agenda-items.yaml) を読み、入力トピック語を以下に対して fuzzy match する:
   - 各エントリの `aliases` 全件
   - `title` の主要語
3. マッチ件数で分岐:
   - **0 件**: 候補語をユーザーに提示し、最寄りの安定 ID を確認する。`agenda-items.yaml` への aliases 追加提案も併記
   - **1 件**: そのまま採用
   - **2 件以上**: ユーザーに「どれを追跡しますか？」と確認（候補のスコープ説明も併せて提示）

### Phase B: 会合範囲の解決

4. 採用された安定 AI ID をキーに、[`framework/catalog/meetings.yaml`](../../../framework/catalog/meetings.yaml) の全会合を走査して `ai_map` にそのキーを含む会合を抽出する
5. `--meetings` / `--from` / `--to` の絞り込みを適用する
6. 会合数が 0 件 ⇒ ユーザーに「`ai_map` に未登録です。catalog 拡張が必要」と報告し、追加候補会合を提示する

### Phase C: 資料の収集状況を点検

7. 各会合について `references/` の取得状況を確認する:
   - **Chair Notes**: `references/Chair-Notes-RAN1-<会合>.md` の存在を Glob で確認
   - **個別 Tdoc**: `references/R1-<番号>.md` のうち frontmatter `agenda_item` がその会合の AI 番号と一致するもの（無いことが多い）
8. **未取得資料は fetch しない**。代わりに **「未取得」セクション** に URL（[`framework/3gpp-ftp-cookbook.md`](../../../framework/3gpp-ftp-cookbook.md) §2.2 から組み立て）と取得手順を列挙する
   - これは「指示→解釈→ツール」の柔軟性を保つため。Claude が必要に応じて curl で取りに行くか、ユーザーに取得を促すかを都度判断する

### Phase D: 会合ごとの抽出

9. 取得済み会合について以下を抽出する:
   - **a. Chair Notes 該当章**: 該当 AI 番号の章を抽出（pandoc で md 化済みなら見出し検索、未抽出ならフルパスを `framework/3gpp-ftp-cookbook.md` §2.4 の docx 解析手順で取り出す）
   - **b. 主要 Tdoc**: 利用可能な `references/R1-*.md` から該当 AI のものを列挙（FL Summary 優先）
   - **c. キーフレーズ**: `noted` / `agreed` / `revised` / `endorsed` / `working assumption` の動詞を拾う
   - **d. 提案企業**: 可能なら Tdoc 一覧の `Source` 列から集計（不要なら省略）

### Phase E: タイムライン組立

10. 会合横断のタイムラインを Markdown に組み立てる:
    - **冒頭サマリー**（H1 直下）:
      - 議論の到達点（合意済み事項）
      - 継続審議事項
      - 主要対立軸（企業ペア / 技術ペア）
      - 次会合での見どころ
    - **各会合 = H2 セクション**（時系列順）:
      - **i. 概況**: 提案企業数、主要 FL
      - **ii. 主要争点**: 1〜3 行で要約
      - **iii. 合意事項**: `agreed` / `endorsed` / `working assumption` の逐語列挙
      - **iv. 残課題**: `noted` / `revised` / FFS（For Further Study）の項目
      - **v. 引用 Tdoc**: `[[R1-XXXXXXX]]` 形式の wikilink リスト
    - **未取得資料セクション**: 取得すべき URL と curl コマンドの目安

### Phase F: 保存とリンク

11. ノートを `documents/<yymmdd>_<topic-slug>_変遷.md` に保存する
12. **リンクを必ず張る** ([`framework/linking-policy.md`](../../../framework/linking-policy.md)):
    - frontmatter `up:` ⇒ 該当 WI/SI の親ノート（既に `documents/` にあれば）。無ければ `framework/catalog/work-items.yaml` から導出して `next:` に placeholder を入れる
    - frontmatter `related:` ⇒ 各会合の調査ノート（既に `documents/` にあるもの）
    - frontmatter `references:` ⇒ 引用した Chair Notes / Tdoc の wikilink リスト
    - 本文中でも初出の関連ノート・Tdoc は `[[ファイル名]]` で wikilink を埋める
    - 既存 `documents/` ノート側にも逆方向リンク（`related:` に新規ノートを追記）

### Phase G: 運用上の判断分岐

- catalog の aliases が薄かった場合 ⇒ 末尾に **「catalog 拡張提案」** セクションを書く（追加すべき alias を列挙）
- 既存ノートと内容が重複しそう ⇒ `.tmp/<yymmdd>_<topic-slug>_変遷_draft.md` に下書きしてから差分をユーザーに見せる
- ユーザーから「もう少し企業ごとの主張を厚めに」等の追加指示があれば、その指示を反映して再生成

## 出力

- **形式**: ファイル保存 + チャットにサマリー
- **保存先**: `documents/<yymmdd>_<topic-slug>_変遷.md`（フラット、サブフォルダ禁止）
- **frontmatter**: 共通スキーマ + 以下の追加フィールド
  ```yaml
  trace:
    ai_id: "ai_nr_aiml_csi_compression_r19"   # 採用した安定 ID
    meetings_in_scope: ["RAN1#124", "RAN1#124bis", "RAN1#125"]
    completeness:
      chair_notes_obtained: ["RAN1#124bis"]   # 手元にある Chair Notes
      chair_notes_missing: ["RAN1#124", "RAN1#125"]  # 未取得（fetch 候補）
      tdocs_obtained: 0                       # 個別 Tdoc は基本未取得運用
  ```
- **status**: `draft`

## このスキル固有の注意点

- **完全自動化しない** — catalog のヒット曖昧時は必ずユーザーに確認する
- **未取得資料は「未取得」と素直に書く** — 推測で埋めない（原則 5）。
  Chair Notes が無いのに合意事項を書くのは禁止
- **AI 番号は会合ごとに変わるため、必ず `meetings.yaml` の `ai_map` 経由で解決** する
- **fetch はこのスキルでは行わない** — `framework/3gpp-ftp-cookbook.md` の curl 手順をユーザー or 別タスクで実行
- **同トピックの再実行は許容** — 新会合が増えるたび上書きせず、`--from` で増分追記するのが望ましい。差分は `.tmp/` で下書きしてユーザー確認
- **catalog の更新提案を必ず残す** — alias 不足、ai_map 未登録、新会合発見など、運用中に気付いた catalog の改善点は本ノートの末尾に列挙する（catalog は使いながら太らせる方針、`framework/catalog/README.md` §3.1）

## 関連スキル

- ← `/survey-topic` — 新規トピックの基本情報（変遷追跡の前提となる初期調査）
- ↔ `/connect-dots` — 横の繋がり（変遷追跡が **縦の深堀**、connect-dots が **横の組合せ**）
- → `/analyze-gap` — 変遷から見えたギャップを学術 / 3GPP / 実装制約で分類
- ↔ `/digest-paper` — 変遷で言及された個別 Tdoc / 論文を深掘り
