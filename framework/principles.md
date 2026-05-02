# Invariant Principles

Principles Claude must always follow when surveying, analyzing, and recording.

## 1. Always record the primary source

Cite URL, document number, and access date. Do not stop at secondary sources.
For 3GPP, state the TS/TR number with version, and the Tdoc number explicitly.

## 2. Always contrast "academic ideal assumptions" with "3GPP implementation constraints"

Academic papers usually assume idealized channel conditions. The inventive step
typically lies in the constraints that arise when implementing on a real radio system:

- Ideal channel → real synchronization offsets, delay spread, Doppler
- Continuous-valued parameters → quantization to a few bits in DCI
- Perfect-information assumptions → limited feedback bandwidth
- Infinite compute → chip area and power constraints

## 3. Compare with successes and failures of past generations

When examining a new technology, always ask "what was the limitation in the previous generation?"
Given 5G's struggles (immature B2B, deteriorating ROI), repeatedly ask what 6G needs.

## 4. Separate descriptions into three layers

- **Why**: motivation and background — why it was needed
- **What**: the minimal core idea of the method
- **How**: implementation constraints, parameters, trade-offs

## 5. Mark unknowns and low-confidence statements

Mark ambiguous guesses as `[要確認]`.
Record the confidence level in the `confidence` frontmatter field.

## 6. Always leave Next Steps

After any survey or analysis, record concrete next actions for "where to investigate next".
Write them so future-you can act immediately — search queries, document numbers, URLs.

```markdown
## Next Steps
- [ ] arXiv で "RIS channel estimation complexity" を検索
- [ ] RAN1 #123 の AI_7.2.3 の Chairman's Notes を確認
```