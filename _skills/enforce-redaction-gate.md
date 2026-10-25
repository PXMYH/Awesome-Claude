---
id: enforce-redaction-gate
slug: enforce-redaction-gate
name: Enforce Redaction Gate
description: '- `redact-for-public-disclosure` — the methodology umbrella; this skill
  is the executable gate its Steps 3 and 7 describe, specialized and made structure-aware'
prompt_preview: "---\nname: enforce-redaction-gate\ndescription: >\n  Statically enforce\
  \ a privacy/redaction boundary on an artifact tree before\n  publication, the way\
  \ an AST checker enforces a code contract. Builds a\n  two-tier gate — a shape-based\
  \ deny-list (regex over identifier shapes) plus a\n  structure-aware tier that parses\
  \ JSON/HTML/SVG/Markdown/code and asserts\n  sensitive content cannot appear in\
  \ meaningful positions — with a strict\n  exit-code contract, label-only output\
  \ that never echoes the patterns..."
full_prompt_length: 21317
tools_mentioned: []
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/enforce-redaction-gate/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/enforce-redaction-gate/SKILL.md
fetched_at: '2026-10-25T07:19:27.516846+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T10:44:40.338616Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee78c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee78c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:07.890692Z'
indexed_at: '2026-10-25T12:12:07.890696Z'
---
