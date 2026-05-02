---
up: "[[README|templates]]"
related:
  - "[[paper-digest]]"
  - "[[../skill-contract]]"
  - "[[../references-policy]]"
---

# Template: Claim-Evidence Block

A reusable structure for recording each claim from a paper or primary source as five fields.
Used by `/digest-paper` and any skill that extracts claims from external sources.

> Parent: [[README|templates (MoC)]] | Related: [[paper-digest]] / [[../skill-contract]] / [[../references-policy]]

## Why five fields

A bare summary ("the paper proposes X") loses two things that matter for SEP-oriented research:

1. **The boundary between author claim and your interpretation** — without it, you re-read the note three months later and cannot tell which was which.
2. **The conditions under which the claim holds** — without explicit `Limitation`, the gap to 3GPP implementation constraints (Principle 2) cannot be reasoned about.

Splitting each claim into the five fields below forces both to surface.

## The five fields

| Field | Source | Purpose |
|:---|:---|:---|
| **Claim** | Author's words (paraphrased) | What the author asserts they achieved or established |
| **Evidence** | Author's words | The concrete support — dataset, metric, experimental condition, analytical result |
| **Method** | Author's words | The minimum description of the technique / mechanism that backs the claim |
| **Limitation** | Author's words | The range outside which the claim does not hold, or the assumption whose collapse breaks it |
| **Project relevance** | **Your interpretation** | Why this matters in the 3GPP / 6G context of this repository |

**Strict separation rule**: `Claim` / `Evidence` / `Method` / `Limitation` are the author's words.
`Project relevance` is your interpretation. Never blend the two in a single field.

## Mandatory rule: no orphan claims

A claim with an empty `Evidence` field **must not** be saved into `documents/`.
If the paper does not back the claim with concrete evidence, mark it `[要確認: Evidence なし]` and either:

- Re-read the paper to locate the missing evidence, or
- Drop the claim from the digest

Do not paper over a missing `Evidence` with a vague paraphrase of the abstract.

## Output shape

Each claim renders as:

```markdown
## Key Claims

### Claim N: <一行で主張>
- **Claim**: <著者が「達成した／確立した」と述べていること（paraphrase）>
- **Evidence**: <データセット、メトリクス、実験条件、解析結果を具体的に>
- **Method**: <主張を支える手法・メカニズムの最小記述>
- **Limitation**: <主張が成立しない範囲・前提が崩れる条件>
- **Project relevance**: <本プロジェクト（3GPP / 6G）の文脈での意味。**自己解釈としてマーク**>
```

`Limitation` and `Project relevance` may be one line each — verbosity is not the point, separation is.

## Promotion hint

If the same `Claim` shows up across multiple papers (e.g. "near-field MIMO requires polynomial-complexity beamforming"),
that claim is a candidate for promotion into a topic note under `documents/` rather than staying inside an individual paper digest.
