---
up: "[[../README|personas]]"
related:
  - "[[chipset-vendor]]"
  - "[[mno-operator]]"
  - "[[vertical-automotive]]"
---

# 産業ペルソナ: 端末 OEM

> 親: [[../README|personas]] | 兄弟（産業）: [[mno-operator|MNO]] / [[chipset-vendor|チップセットベンダー]] / [[vertical-automotive|自動車]]

## 基本的な立場

スマートフォン、IoT デバイス、車載端末を製造する。
エンドユーザーとの接点を持ち、ユーザー体験（UX）を重視する。

## 代表企業

- Apple, Samsung, Xiaomi, OPPO, vivo
- 車載: Continental, Harman, LG Electronics

## ペインポイント

- **バッテリー寿命**: 新機能追加による消費電力増を許容できない
- **端末コスト**: 中低価格帯で新機能を搭載するコスト
- **アンテナ設計**: 筐体内のアンテナスペース制約
- **発熱管理**: モデムの消費電力 → 発熱 → UX 低下

## 技術に求めること

- 端末側の消費電力を増やさない（または削減する）技術
- UE 側の計算負荷が小さい MIMO / コーディング方式
- Ambient IoT のような超低コスト端末の実現
- AI/ML をデバイスエッジで効率的に動かす仕組み

## 標準化での影響力

- Apple は直接の Tdoc 提出は少ないが、市場での採否が決定的
- UE の能力（UE capability）報告の設計に強い関心

## この産業が重視する価値軸

- エネルギー効率（端末バッテリー）
- コスト（BOM コスト）
- 遅延（UX に直結）
