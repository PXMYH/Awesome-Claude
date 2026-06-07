---
id: utility-pm-skill-auditor
slug: utility-pm-skill-auditor
name: PM Skill Auditor (Dispatch Skill)
description: '- Canonical sub-agent definition: [`agents/pm-skill-auditor.md`](../../agents/pm-skill-auditor.md)'
prompt_preview: '---

  name: utility-pm-skill-auditor

  description: Run a repo-wide cross-cutting governance audit via the pm-skill-auditor
  sub-agent. Dispatches natively on Claude Code with the pm-skills plugin (invokes
  @agent-pm-skills:pm-skill-auditor); on non-Claude clients (Codex CLI, Cursor, Windsurf,
  Copilot, Gemini CLI) reads agents/pm-skill-auditor.md and executes the system prompt
  inline. Returns a layered audit report (full findings + Status Summary prose + Status
  YAML envelope per master plan D26) with...'
full_prompt_length: 4896
tools_mentioned: []
category: community
category_display: Community
source_repo: product-on-purpose/pm-skills
source_path: skills/utility-pm-skill-auditor/SKILL.md
source_url: https://github.com/product-on-purpose/pm-skills/blob/main/skills/utility-pm-skill-auditor/SKILL.md
fetched_at: '2026-06-07T06:28:27.493850+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T09:42:49.495058Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc65f40 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc65f40 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:55.444388Z'
indexed_at: '2026-06-07T10:04:55.444394Z'
---
