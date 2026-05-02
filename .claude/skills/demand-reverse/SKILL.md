---
name: demand-reverse
description: Reverse-lookup candidate technical topics that solve a persona's pain point. ペルソナの課題（ペインポイント）から解決候補となる技術トピックを逆引き。
user-invocable: true
---

# demand-reverse

## Motivation

Starting from a technology surfaces "what it can do" but tends to drop "who needs it".
Reverse-looking up from persona pain points asks
**not whether the technology is optimal, but whether it would actually be adopted**.
For standardization adoption, demand-side urgency matters as much as technical superiority.

## Usage

```
/demand-reverse <persona-file> <pain-point>
```

Examples:
```
/demand-reverse personas/regions/southeast-asia.md カバレッジコスト
/demand-reverse personas/industries/mno-operator.md エネルギー消費
/demand-reverse personas/stakeholders/operator-cxo.md 5G投資回収
```

## Inputs and prerequisites

- **Required input**: a persona file path + a pain point (free text)
- **Prerequisites**: the specified persona file exists under `framework/personas/`
- **Recommended**: multiple topic notes exist under `documents/` (population of candidates)
- **Cannot proceed when**: the specified persona file does not exist → list the available personas

## Execution flow

1. Read `framework/templates/demand-reverse.md` and confirm the analysis steps
2. Read the specified persona file (under `framework/personas/`)
3. From the persona, extract:
   - List of pain points
   - Value axes the persona prioritizes (mapping to `axes.value`)
   - Areas of technical interest
   - Constraints (cost, infrastructure, policy)
4. Scan all topics under `documents/` and check each topic's `axes.value` and `axes.market`
5. Score fit against the pain point with the four criteria below:

   | 基準 | 問い |
   |:---|:---|
   | 直接的関連性 | そのペインポイントを直接解決するか？ |
   | 成熟度 | 3GPP での議論段階は？（学術段階 / SI / WI / TS 化済み） |
   | 実装実現性 | ペルソナの制約（コスト、インフラ）で実現可能か？ |
   | 代替手段の有無 | 既存の代替技術と比較して優位な点は？ |

6. Rank highest-fit first and output (top 5 or so)
7. **Investigation proposals**: for each candidate, propose concrete next sources to consult
   - Actions that include search queries, Tdoc numbers, document names
8. **Identify uncovered areas**: surface technologies that have no notes under `documents/` yet but are likely relevant
   - When found, propose running `/survey-topic`
9. If saving, save to `documents/<yymmdd>_demand-reverse_<persona-slug>.md` (flat)
10. **Always set links**: list the top-fit candidate notes in `related:` as wikilinks, and embed `[[トピック名]]` at first mention in the body ([`framework/linking-policy.md`](../../../framework/linking-policy.md))

**When the persona is thin**: when the persona file is insufficient, supplement from general knowledge but mark `[ペルソナ情報不足: 一般的知識から推定]`.

## Output

- **Format**: chat output (default). File save if the user requests it
- **Save location**: `documents/YYYY-MM-DD_demand-reverse_<persona-slug>.md`
- **frontmatter**: common schema + the following extra fields:
  ```yaml
  demand-reverse:
    persona: "相対パス"
    pain-point: "ペインポイントの要約"
  ```
- **status**: `draft`

## Skill-specific notes

- **"Technically optimal" and "realistic for this persona" differ** — always factor in cost constraints, infrastructure, and policy environment
- **Check whether 5G already attempted a similar approach and failed**
- **The ranking is not absolute** — when criteria trade off, state so
- **Discovery of uncovered areas matters** — surfacing technologies missing from `documents/` is an important by-product of this skill

## Related skills

- → `/survey-topic` — investigate technologies discovered as uncovered areas
- → `/analyze-gap` — gap analysis of candidate technologies
- → `/connect-dots` — synergies among candidate technologies
- ↔ `/success-pattern` — historical validation of a candidate technology's adoption potential