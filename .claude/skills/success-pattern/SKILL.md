---
name: success-pattern
description: Learn adoption factors from past-generation (3G/4G/5G) successes and failures, and project them onto 6G study items. 過去世代（3G/4G/5G）の成功・失敗事例から普及要因を学び 6G の検討課題に照射。
user-invocable: true
---

# success-pattern

## Motivation

Technical excellence alone does not get a feature standardized. 4G LTE succeeded by syncing
a killer app (smartphones) with standard convergence; 5G has struggled with immature B2B and
excessive CAPEX. By projecting these historical patterns onto the current topic, this skill
asks structurally **what is required for 6G adoption**.

## Usage

```
/success-pattern <トピック名>
```

## Inputs and prerequisites

- **Required input**: a topic name (precision improves if a note exists in `documents/`, but is not required)
- **Prerequisites**: none (but generation-by-generation notes in `documents/` are leveraged when present)
- **Cannot proceed when**: never (historical facts are collectable from public sources)

## Execution flow

1. Read existing generation-by-generation notes from `documents/` if any
2. Read `framework/templates/generation-comparison.md` and confirm the matrix shape
3. Read `framework/axes/05-adoption-factors.md` and confirm the five adoption-factor items
4. Project the target topic onto past generations and build a 5-column × 7-row matrix:
   - Columns: 3G UMTS / 4G LTE / 5G NR / 5G-Advanced / 6G 構想
   - Rows: technical options / problem solved / problem newly created / killer app / operator ROI / adoption factors / IP players
5. Centered on the adoption-factors axis (Axis 5), ask:
   - Do the structural factors that made 4G LTE succeed apply to this topic?
   - Are the factors that caused 5G to struggle at risk of repeating here?
   - What scenarios would make operator ROI viable?
6. Distill the conclusion into 3 points in the form "Conditions for 6G success"
7. Write **Next Steps**

**When the matrix has unfillable cells**: when no equivalent technology existed in the past generation, write 「該当なし（この世代では未登場）」, and mark inferences from similar technologies as `[推論]`.

## Output

- **Format**: chat output (default). File save if requested
- **Save location**: `documents/<yymmdd>_<slug>_success-pattern.md` (flat)
- **frontmatter**: follows the common schema (place the target-topic note under `up:` as a wikilink)
- **status**: `draft`
- **Links**: place the target topic's survey note under `up:`, and any generation-specific notes under `related:` ([`framework/linking-policy.md`](../../../framework/linking-policy.md))

## Skill-specific notes

- **Write the three conditions in a verifiable form** — not 「良い技術であること」 but 「FWA 市場で既存 5G CPE との後方互換性を維持できること」
- **Treat 5G's struggle as a lesson, not a dogma** — always consider that 5G and 6G may face different market conditions
- **Record the point-in-time of sources** — market data shifts; record the reference date
- The "6G 構想" column reflects current proposals, not finalized information; state so explicitly

## Related skills

- ← `/survey-topic` — technical background of the target topic
- ↔ `/demand-reverse` — complement "success for whom" with the persona perspective
- → `/analyze-gap` — gaps that must close to meet the success conditions