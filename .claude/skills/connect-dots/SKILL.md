---
name: connect-dots
description: Discover synergy, conflict, and combinational value across topics, and generate a discussion memo. トピック間の相乗効果・矛盾・組合せ価値を発見し考察メモを生成。
user-invocable: true
---

# connect-dots

## Motivation

Some value remains invisible when topics are examined in isolation.
Crossing two topics surfaces **synergies that neither produces alone**, as well as
**conflicts that were being overlooked**.
Ideas that emerge from combinations often have higher patent novelty than improvements to a single technology.

## Usage

```
/connect-dots <topic-a> <topic-b>
/connect-dots <topic-a> <topic-b> --persona <persona-file>
```

## Inputs and prerequisites

- **Required input**: two topic names (notes must exist in `documents/`)
- **Optional**: a persona file (under `framework/personas/`)
- **Prerequisites**: both notes should have `axes` populated in frontmatter (empty is allowed but degrades precision)
- **Cannot proceed when**: notes for the specified topics do not exist in `documents/` → propose `/survey-topic` first

## Execution flow

1. Read `framework/templates/connect-dots.md` and confirm the analysis steps
2. Read both topic notes from `documents/`
3. **Compare common axes**: compare the `axes` of both frontmatters and identify values they share and values they differ on
4. **Generate synergy hypotheses**: starting from shared axes, describe value created by the combination as hypotheses
   - Form: 「A + B により [KPI] が [メカニズム] で改善される」
   - For each hypothesis, judge whether it is "additive" (sum of independent effects) or "multiplicative" (amplification through interaction)
   - Cite supporting evidence (papers, specs, use cases) when available; otherwise mark `[仮説]`
5. **Detect conflicts / trade-offs**: identify points where the assumptions or requirements of the two topics conflict
   - Form: 「A は [X] を前提とするが、B は [Y] を要求する」
   - Evaluate whether the conflict is resolvable or is an essential trade-off
6. **Persona-perspective evaluation** (when `--persona` is given):
   - Read the specified persona file
   - Evaluate whether the combination has value for the persona and is viable cost-wise
   - Consider reasons it might be opposed in standardization (refer to `framework/lenses/standardization-dynamics.md` as needed)
7. Write **Next Steps**
8. Save to `documents/<yymmdd>_<topicA>-x-<topicB>.md`
9. **Always set links**: list both topic notes under frontmatter `related:` as wikilinks, and embed `[[topic-a]]` and `[[topic-b]]` in the body. Set `up:` to the primary axis topic ([`framework/linking-policy.md`](../../../framework/linking-policy.md))

**When axes are thin**: infer axis values from the body of the notes and mark `[推定]`.

## Output

- **Format**: file save + chat summary
- **Save location**: `documents/<yymmdd>_<topicA>-x-<topicB>.md` (flat)
- **frontmatter**: common schema + the following extra fields:
  ```yaml
  connection:
    topic-a: "[[topicA のファイル名]]"
    topic-b: "[[topicB のファイル名]]"
    persona: "framework/personas/... の相対パス（使用時のみ）"
  ```
- **status**: `draft`

## Skill-specific notes

- **Actively look for "multiplicative" hypotheses** — instead of merely listing the merits of both, ask for emergent effects from the combination
- **Conflicts are not negative** — the resolution of a conflict is itself a seed of IP
- **Re-analyzing the same pair is allowed** — running again with a different persona, or at a different point in time, can be valuable. Distinguish via the date in the filename
- **Three or more topic connections**: limited to two. For 3+, run pairwise and integrate the results

## Related skills

- ← `/survey-topic` — basic information for each topic
- → `/analyze-gap` — turn synergy hypotheses into concrete gaps
- ↔ `/demand-reverse` — discover combination candidates from persona pain points