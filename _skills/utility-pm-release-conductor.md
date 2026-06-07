---
id: utility-pm-release-conductor
slug: utility-pm-release-conductor
name: PM Release Conductor (Dispatch Skill)
description: '- Canonical sub-agent definition: [`agents/pm-release-conductor.md`](../../agents/pm-release-conductor.md)'
prompt_preview: '---

  name: utility-pm-release-conductor

  description: Walk the guided release runbook (6 gates G0/G1/G2/G2.5/G3/G4) via the
  pm-release-conductor sub-agent. Dispatches natively on Claude Code with the pm-skills
  plugin (invokes @agent-pm-skills:pm-release-conductor with native chain composition
  to pm-skill-auditor at G0 and pm-changelog-curator at G2); on non-Claude clients
  (Codex CLI, Cursor, Windsurf, Copilot, Gemini CLI) reads agents/pm-release-conductor.md
  and inlines auditor + curator behaviors...'
full_prompt_length: 6843
tools_mentioned: []
category: community
category_display: Community
source_repo: product-on-purpose/pm-skills
source_path: skills/utility-pm-release-conductor/SKILL.md
source_url: https://github.com/product-on-purpose/pm-skills/blob/main/skills/utility-pm-release-conductor/SKILL.md
fetched_at: '2026-06-07T06:28:27.307112+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T09:42:41.407054Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc8bf80 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc8bf80 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:55.441557Z'
indexed_at: '2026-06-07T10:04:55.441563Z'
---
