---
name: survey-topic
description: Systematically survey a topic across the 6 analysis axes and write the result as a Markdown note under documents/. 指定トピックを6軸で体系調査し documents/ に記録。
user-invocable: true
---

# survey-topic

## Motivation

When first encountering a new technology topic, collecting fragmentary information does not surface the seeds of IP. Applying the six axes' questions systematically lets **the location of implementation-constraint gaps**
(= the source of inventive step) emerge from the very first survey pass.

## Usage

```
/survey-topic <トピック名>
```

## Inputs and prerequisites

- **Required input**: a topic name (e.g. `Cell-Free Massive MIMO`, `GRAND decoding`)
- **Prerequisites**: none (this skill is the entry point for new topics)
- **Cannot proceed when**: the topic name is too vague to convert into a search query → ask the user to make it concrete

## Execution flow

1. Read `framework/principles.md` and confirm the six principles
2. Read all six files under `framework/axes/` and absorb each axis' questions
3. Read `framework/templates/survey-topic.md` and confirm the seven survey items
4. Read `framework/sources.md` and confirm source priority
5. Read `framework/linking-policy.md` and `framework/references-policy.md` and confirm save rules
6. **Scan existing notes**: grep `documents/` for related existing topics first (to avoid creating an orphan note)
7. Collect information in this priority:
   - **3GPP portal**: presence of the relevant WI/SI, Tdoc list, Chairman's Notes
   - **arXiv / IEEE**: major papers (top-cited, last 2 years)
   - **NGMN / ITU-R**: positioning in requirements documents
   - **Vendor blogs**: technical writeups from Qualcomm / Ericsson / Nokia / Samsung
8. **Markdown-render primary sources**: papers, Tdocs, and specs that you cite must be converted to Markdown and saved under `references/` per `tools.md`. Use the paper title / contribution number / arXiv ID verbatim as the filename (`framework/references-policy.md`)
9. Organize per the seven template items:
   - Definition and background (Why) / technical core (What) / implementation constraints (How)
   - Diff vs. previous generation / major players / open issues / market and IP headroom
10. Record applicable axes in frontmatter `axes:`
11. Confirm that the **diff vs. previous generation (3G/4G/5G)** section is not empty
12. Write **Next Steps** (concrete actions including search queries, document numbers, URLs)
13. **Save the note as `documents/<yymmdd>_<slug>.md`** (`status: draft`; `yymmdd` is today's last-two-digits-of-year + month + day)
14. **Always set links**:
    - List cited references as wikilinks under frontmatter `references:`
    - List related existing notes under `up` (one nearest parent) and `related` (siblings)
    - In the body, mention related topics on first occurrence with wikilinks like `[[260420_NRフレーム構造とリソースブロックの進化まとめ|フレーム構造]]`
    - Add a reverse `[[新規ノート]]` link from the parent note (bidirectional linking)

**When information is insufficient**: mark missing items as `[要確認]` and record the investigation method in Next Steps. Do not leave a section blank.

## Output

- **Format**: file save + chat summary
- **Save location**: `documents/<yymmdd>_<slug>.md` (flat, no subfolders)
- **frontmatter**: follow the common schema in `framework/skill-contract.md` (fill in `up` / `related` / `references`)
- **status**: `draft`

## Skill-specific notes

- **Granularity**: 1 topic = 1 independent technical concept. "MIMO" is too broad; "Cell-Free Massive MIMO のパイロット汚染対策" is too narrow; "Cell-Free Massive MIMO" is about right
- **When 3GPP information is absent**: even purely academic topics may be surveyed. State "3GPP での議論状況: なし（学術段階）" explicitly
- **Do not use folders**: place every note directly under `documents/`. Defer category folders until they become necessary

## Related skills

- → `/analyze-gap` — extract concrete gaps from the survey
- → `/digest-paper` — deep-dive into important papers found during the survey
- → `/connect-dots` — explore synergies with other topics