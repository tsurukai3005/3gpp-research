---
up: "[[../README|framework]]"
related:
  - "[[../3gpp-ftp-cookbook|3gpp-ftp-cookbook]]"
  - "[[../sources|sources]]"
  - "[[../skill-contract|skill-contract]]"
---

# framework/catalog/ — メタデータカタログ

3GPP RAN1 の **会合 / アジェンダ / WI・SI** を YAML で構造化する。
スキル `/trace-evolution` 等が **自然言語クエリ → 安定 ID** に解決する際の参照元。

> 親: [[../README|framework]]
> 関連: [[../3gpp-ftp-cookbook|3GPP FTP cookbook]] / [[../sources|sources]] / [[../skill-contract|skill-contract]]

## 1. ファイル構成

| ファイル | 役割 | キー |
|:---|:---|:---|
| [meetings.yaml](./meetings.yaml) | 会合略号 → 日付・場所・FTP フォルダ・AI 番号マップ | 会合略号（例: `RAN1#124bis`） |
| [agenda-items.yaml](./agenda-items.yaml) | 安定 AI ID → 機能名・aliases・親 WI/SI | 機能ベース安定 ID（例: `ai_6gr_mimo_dl_pdcch`） |
| [work-items.yaml](./work-items.yaml) | WI/SI 略号 → 親 Rel・rapporteur・配下 AI | WI/SI 略号（例: `NR_AIML_air_Ph2`） |

## 2. 設計思想

### 2.1 安定 AI ID と会合別 AI 番号の分離

3GPP の AI 番号は **会合ごとに変動する**（例: AI/ML CSI は #123 で 9.1.1、#124bis で 9.1.2 のように変わりうる）。
そのため:

- **キー = 機能ベースの安定 ID**（`agenda-items.yaml`）
- **会合ごとの番号 = `meetings.yaml` の `ai_map` で吸収**

```yaml
# agenda-items.yaml
ai_nr_aiml_csi_compression_r19:
  title: "NR AI/ML CSI compression (Rel-19)"
  aliases: ["CSI 圧縮", "AI CSI compression", ...]

# meetings.yaml
"RAN1#124bis":
  ai_map:
    ai_nr_aiml_csi_compression_r19: "9.1.2"  # ← この会合での番号
"RAN1#125":
  ai_map:
    ai_nr_aiml_csi_compression_r19: "9.1.3"  # ← 番号が変わってもキーは不変
```

### 2.2 自然言語ヒット率を `aliases` で稼ぐ

ユーザーは「CSI 圧縮」「Type-II AI」「JSCC CSI」等、表記揺れの自然言語で投げてくる。
`aliases` 配列に **英語と日本語の両方** を載せ、Claude の fuzzy match の取りこぼしを減らす。

### 2.3 完全網羅は目指さない

- **触っているトピックから先に埋める**。空欄が多くてもカタログとして機能する設計
- 未確認のフィールドは `[要確認]` と明記し、`/trace-evolution` 実行時に「不足」として報告される

## 3. 運用ルール

### 3.1 aliases の追加（最重要）

`/trace-evolution` がトピック語の解決に失敗 or 候補曖昧でユーザーに確認したとき、
**その場で aliases に 1〜2 個追加**して PR にする。catalog は使いながら太らせる。

例:
```diff
 ai_nr_aiml_csi_compression_r19:
   aliases:
     - "CSI 圧縮"
     - "AI CSI compression"
+    - "two-sided model CSI"     # ← 2026-04-30 ユーザー指示で追加
+    - "DL CSI compression AI"
```

### 3.2 新会合の追加

会合終了後、最低限以下を埋める:

1. `meetings.yaml` に新エントリ（日付・場所・FTP フォルダ名）
2. `Chair-Notes-RAN1-<会合>.md` を `references/` に取得（[[../3gpp-ftp-cookbook]] の curl 手順）
3. agenda.csv を取得し、**追跡対象の AI のみ** `ai_map` に追記（全 AI を埋める必要はない）

### 3.3 `[要確認]` フィールド

未確認のフィールドは `[要確認]` と明記する。これは原則 5（confidence）に準拠した運用。
`/trace-evolution` は `[要確認]` を「不足」として報告する。

## 4. 関連ノート

- [[../3gpp-ftp-cookbook|3GPP FTP cookbook]] — `meetings.yaml` の `ftp_folder` から実 URL を組み立てる手順
- [[../sources|sources]] — catalog 補強のために巡回する情報源
- [[../skill-contract|skill-contract]] — このカタログを参照するスキルの行動規範

> 設計上の謝辞（着想元の表記）はリポジトリルート [README.md](../../README.md) #謝辞 を参照。
