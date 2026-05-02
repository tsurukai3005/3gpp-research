---
name: analyze-gap
description: For a given topic, classify academic / 3GPP / implementation-constraint gaps into three buckets and visualize them. 指定トピックの学術/3GPP/実装制約ギャップを3バケットで可視化。
user-invocable: true
---

# analyze-gap

## Motivation

A topic survey alone can organize "what is known", but it leaves
**"what has not yet been solved"** out of focus.
By classifying gaps explicitly into three categories, this skill identifies the
unsolved problems that become seeds for IP.
In particular, Gap C (the implementation-constraint gap) is the strongest source of
inventive step, as Principle 2 indicates.

## Usage

```
/analyze-gap <トピック名>
```

## Inputs and prerequisites

- **Required input**: a note on the target topic must exist under `documents/`
- **Prerequisites**: basic information must already be organized via `/survey-topic` (or equivalent)
- **Cannot proceed when**: no note exists for the target topic → propose running `/survey-topic` first

## Execution flow

1. Read the note for the target topic from `documents/`
2. Read `framework/templates/gap-analysis.md` and confirm the three-bucket definition and the questions to ask
3. Read `framework/axes/06-ip.md` and confirm the IP-evaluation criteria
4. Confirm the latest information:
   - **arXiv**: in the last year, are there relevant papers that newly solve any issue?
   - **3GPP**: confirm FFS items in the latest Chairman's Notes for the WI/SI
5. Classify gaps into three buckets:
   - **Gap A (academic → 3GPP lag)**: solved in academia but not yet adopted by 3GPP. Estimate **why it has not been adopted** (implementation complexity / lack of consensus / timing / backward-compat barrier)
   - **Gap B (FFS items)**: items left as FFS in the Chairman's Notes. **The shortest path to a patent**
   - **Gap C (implementation-constraint gap)**: difference between the paper's ideal assumptions and 3GPP implementation constraints. **The strongest source of inventive step**. Describe in the form "the paper assumes X, but NR has constraint Y"
6. Annotate each gap against the IP axis (Axis 6):
   - novelty: is the difference from prior art clear?
   - inventive-step: does the approach to resolving the implementation constraint contain a non-obvious idea?
   - spec-mapping: which part of a future TS/TR could it correspond to?
7. Write **Next Steps**
8. Output the result to chat
9. If persisting, save to `documents/<yymmdd>_<slug>_gap.md`
10. **Always set links**: write the parent topic note as `up:` and related notes as `related:` wikilinks. Cited primary sources go into `references/` as Markdown and are pointed to from `references:` ([`framework/linking-policy.md`](../../../framework/linking-policy.md), [`references-policy.md`](../../../framework/references-policy.md))

**When no FFS items are found**: set Gap B to "該当なし（現時点で FFS 項目未確認）" and document the verification method (concrete meeting number, AI number) in Next Steps.

## Output

- **Format**: chat output (default). Save to a file if the user requests
- **Save location**: `documents/<yymmdd>_<slug>_gap.md` (flat)
- **frontmatter**: common schema + `gap-type: [A, B, C]` (applicable buckets)
- **status**: `draft`

## Skill-specific notes

- **Concentrate on Gap C** — time allocation guideline: Gap A (20%) / Gap B (30%) / Gap C (50%)
- **Always ask "what would happen if this paper's idea were dropped onto the OFDM frame structure?"**
- For Gap A, when the reason for non-adoption is unclear, do not guess — mark as `[要確認]`
- When multiple gaps interrelate, describe the relationship as well

## Related skills

- ← `/survey-topic` — basic information on the target topic is required
- → `/digest-paper` — detailed analysis of the papers grounding Gap A/C
- → `/connect-dots` — combinations of gaps from different topics
- ↔ `/demand-reverse` — which persona's pain point each gap solves