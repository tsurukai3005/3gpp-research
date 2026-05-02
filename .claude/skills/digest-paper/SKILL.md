---
name: digest-paper
description: Read a paper and save a structured memo under documents/ that emphasizes the gap to 3GPP implementation constraints. 論文を読み 3GPP 実装制約との差分を強調した構造化メモを documents/ に保存。
user-invocable: true
---

# digest-paper

## Motivation

Reading a paper alone does not surface the seeds of IP.
Only by making the **assumptions the paper implicitly relies on** explicit and **comparing them with 3GPP implementation constraints**
does "where an inventive solution is needed" emerge (Principle 2).
This skill connects paper reading directly to discovering patent opportunities.

## Usage

```
/digest-paper <論文の URL or タイトル>
```

## Inputs and prerequisites

- **Required input**: a way to access the paper (URL, PDF path, or arXiv ID)
- **Prerequisites**: none (executable on a paper alone)
- **Cannot proceed when**: the paper content cannot be accessed → ask the user to provide a summary

## Execution flow

1. Acquire the paper content (URL / PDF / user-supplied)
2. Read `framework/templates/paper-digest.md` and `framework/references-policy.md`; confirm the extraction items and save rules
3. **Markdown-render the paper body and save under `references/`**:
   - PDF: use `tools.md` §2 `pdftotext -layout`
   - docx: use `tools.md` §1 `pandoc -t gfm --wrap=none`
   - Use the **paper title / contribution number / arXiv ID verbatim** as the filename (e.g. `references/arXiv-2508.08225.md`, `references/R1-2503456.md`)
   - frontmatter follows the schema in `framework/references-policy.md` §3
4. Extract metadata:
   - authors / year / venue (conference or journal) / DOI or arXiv ID
5. Summarize the contribution in 3-5 bullets
6. **List assumptions explicitly** (preparation for the most important step):
   - channel model / SNR range / antenna configuration / CSI assumption / computational complexity / simulation environment
   - For implicit assumptions the paper does not state, mark them as `[暗黙の仮定]`
7. **Build the assumption vs. 3GPP-implementation-constraint gap table** (the most important step):

   | 論文の前提 | 3GPP の現実 | ギャップ |
   |:---|:---|:---|
   | 完全 CSI | 限られた PUCCH リソース | CSI 量子化誤差への耐性が未検証 |

8. **Save the digest note as `documents/<yymmdd>_<first-author>_<slug>.md`**
9. **Always set links** (`framework/linking-policy.md`):
   - List the `[[references/arXiv-XXXX]]` you created above as at least one entry under frontmatter `references:`
   - List related existing topic notes under `up` (nearest parent) and `related`
   - Embed `[[既存ノート]]` wikilinks in the body
   - Add a reverse link by appending the new note to the related `documents/` notes' `related:`
10. Write **Next Steps**

**Survey papers**: consolidate into a single digest file but separate the gap table per individual technique. For especially important techniques, propose individual `/digest-paper` runs in Next Steps.

## Output

- **Format**: two files (the original-text Markdown under references + the digest under documents) + a chat summary
- **Save location**:
  - Original Markdown: `references/<論文番号 or arXiv-ID or 著者-年-タイトル>.md`
  - Digest: `documents/<yymmdd>_<first-author>_<slug>.md`
- **frontmatter** (digest): common schema + the following extra fields:
  ```yaml
  paper:
    authors: []
    year: YYYY
    venue: "会議名 or ジャーナル名"
    doi: "DOI or arXiv ID"
  ```
- **status**: `draft`

## Skill-specific notes

- **An empty gap table is not allowed** — even for 3GPP-conformant simulation environments, examine "computational complexity", "backward compatibility", "signaling overhead", etc.
- **Do not accept the paper's claims uncritically** — when simulation conditions are limited, state so explicitly
- **Papers with multiple independent proposals**: evaluate the gap for each proposal individually

## Related skills

- → `/analyze-gap` — integrate the paper's gap into a topic-wide gap analysis
- → `/connect-dots` — combine the paper's idea with other topics
- → `/survey-topic` — when the paper opens a new topic