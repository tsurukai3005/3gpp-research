# Linking Policy

To make the relationships between documents legible in Obsidian's graph view,
**always link notes**. Hierarchy is also expressed via links.

This policy is a top-level rule for every skill and command, and is referenced from `framework/skill-contract.md`.

---

## 1. Basic rules

### 1.1 Every note has at least one link

- When creating or updating a note, **always set at least one inbound or outbound link**
- Fully orphaned notes (islands in the graph view) are forbidden
- If the link target does not yet exist, write the "next note to create" in frontmatter `next:`, and embed a placeholder wikilink `[[未作成のノート名]]` in the body (Obsidian renders unresolved links in red)

### 1.2 Use Obsidian wikilinks as the standard

- Internal links use `[[<filename without extension>]]` first
  - Example: `[[260421_TS38.211-Section4-BWPとCarrier-Aggregationの体系整理]]`
- For an alias, use `[[<filename>|表示テキスト]]`
  - Example: `[[260421_TS38.211-Section4-BWPとCarrier-Aggregationの体系整理|BWP/CA 体系整理]]`
- Reserve plain Markdown links `[text](path.md)` for situations where they must survive outside Obsidian (READMEs, PR descriptions, issues, external URLs)
- Section reference: `[[<filename>#<heading>]]`. Block reference: `[[<filename>^block-id]]`

### 1.3 Express hierarchy via link direction

Links are not just references — they encode parent / child / sibling / inbound relationships via frontmatter.

| frontmatter field | meaning | value form |
|:---|:---|:---|
| `up` | Parent note (this note's higher-level concept or MoC) | one wikilink (e.g. `"[[260421_NRフレーム構造の発表資料ドラフト]]"`) |
| `related` | Sibling / related notes (parallel relationships) | list of wikilinks |
| `children` | Child notes (notes that branch out from this note as parent) | list of wikilinks (optional — may be omitted if inbound links make it discoverable) |
| `next` | Notes that should be written next, after this one | list of wikilinks (may include unresolved placeholders) |

- `up` is **0 or 1 entry**. For topics with multiple parents, place the primary parent in `up` and secondary parents in `related`
- When a note acts as a Map of Content (MoC) or a higher-level survey, child notes refer back to it via `up`. The MoC itself may enumerate children via `children:`
- Using `up` in the graph view makes hierarchy visually apparent (Local Graph + tag/folder coloring is recommended)

---

## 2. Procedure when writing a note

1. **Before creating a new note**: grep `documents/` to find existing related notes
2. **While writing**: every time a related topic is mentioned, embed a wikilink `[[ファイル名]]` in the body
   - For "フレーム構造", link to a concrete note like `[[260420_NRフレーム構造とリソースブロックの進化まとめ|フレーム構造]]`
   - For primary sources (spec numbers, Tdoc numbers), link to a note inside `references/` ([references-policy.md](./references-policy.md))
3. **After creating**: fill in frontmatter `up` / `related`. At least one entry must be present
4. **Reverse links from existing notes**: when needed, add a `[[新規ノート]]` reference on the parent note as well (bidirectional linking is ideal)

---

## 3. Link hygiene

- When renaming a file, update wikilinks in both the body and the frontmatter. Do not rely solely on Obsidian's auto-rename — verify with grep
- When a broken link is found, treat it as a fix candidate for the relevant skill
- The `/review` and `/status` commands detect broken links and orphan notes (rolled out incrementally)

---

## 4. Apply this policy under `framework/` as well

This policy applies not only to research notes under `documents/`, but also to rule-definition
files under `framework/` (axes, lenses, personas, templates, and various policies).

- Each subfolder (`framework/axes/`, `lenses/`, `personas/`, `templates/`) has a README.md that serves as its MoC
- Files inside a subfolder reference the MoC via frontmatter `up: "[[../README|フォルダ名]]"`
- Related files within the same folder are connected via `related:` as siblings
- Cross-cutting relations (axis ↔ persona, axis ↔ template, lens ↔ persona) are also expressed via `related:`
- Exception: the `yymmdd_` prefix naming rule of `documents/` does not apply to `framework/` (use the meaningful filenames as-is)

## 5. Policy after the note count grows (deferred)

Once notes accumulate to the point where the graph view becomes hard to read:

- Introduce hub notes (MoC: Map of Content) and aggregate via `up` (already done under `framework/`)
- Add cross-cutting classification via tags (`tags:`)
- Decide whether to reintroduce folder structure (`documents/mimo/` etc.)

Until then, **express hierarchy through flat layout + links only**.