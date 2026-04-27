# personas — 需要側の多面的モデル（Map of Content）

技術を「誰にとって価値があるか」で評価するためのペルソナ集。
3つの次元で分類する。

## 次元

| 次元 | サブフォルダ | 問い |
|:---|:---|:---|
| 地域 | `regions/` | その地域の通信インフラ事情と政策は？ |
| 産業 | `industries/` | その産業の技術ニーズとペインポイントは？ |
| ステークホルダー | `stakeholders/` | その立場の人が意思決定で重視することは？ |

## ペルソナ一覧

### 地域（regions/）

- [[regions/north-america|北米]]
- [[regions/europe|欧州]]
- [[regions/china|中国]]
- [[regions/japan|日本]]
- [[regions/southeast-asia|東南アジア]]

### 産業（industries/）

- [[industries/mno-operator|MNO（通信事業者）]]
- [[industries/chipset-vendor|チップセットベンダー]]
- [[industries/device-oem|デバイス OEM]]
- [[industries/vertical-automotive|垂直産業: 自動車]]

### ステークホルダー（stakeholders/）

- [[stakeholders/3gpp-chair|3GPP 議長/Feature Lead]]
- [[stakeholders/operator-cxo|オペレーター経営層（CxO）]]
- [[stakeholders/regulator|規制当局]]
- [[stakeholders/vendor-rd|ベンダー R&D 責任者]]

## 関連

- 親: [[../README|framework/README]]
- 連携: [[../axes/04-market|軸4 市場]] と密接（市場軸が分類、ペルソナが深掘り）
- 利用スキル: [[../templates/demand-reverse]]、[[../templates/connect-dots]]
- 政治経済的文脈は [[../lenses/political-economy]] と組み合わせて使う

## 使い方

- `/demand-reverse` スキルで「このペルソナのペインポイントに応える技術は？」と逆引き
- `/connect-dots --persona <file>` でトピック間の組合せをペルソナ視点で評価
- `/survey-topic` の分析で「市場軸」を深掘りする際に参照

## ペルソナの追加・削除

- 追加: 該当サブフォルダにファイルを置き、本ファイルの一覧に行を追加する
- 削除: ファイルを消し、本ファイルの一覧から行を削除する
- スキルは本ファイル経由ではなくディレクトリスキャンで発見するため、機能上は本一覧の更新は必須ではないが、Obsidian グラフでの可視性のために更新を推奨
