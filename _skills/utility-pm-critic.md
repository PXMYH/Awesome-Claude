---
id: utility-pm-critic
slug: utility-pm-critic
name: PM Critic (Dispatch Skill)
description: '- Canonical sub-agent definition: [`agents/pm-critic.md`](../../agents/pm-critic.md)'
prompt_preview: '---

  name: utility-pm-critic

  description: Run adversarial review on a PM artifact via the pm-critic sub-agent.
  Dispatches natively on Claude Code with the pm-skills plugin (invokes @agent-pm-skills:pm-critic);
  on non-Claude clients (Codex CLI, Cursor, Windsurf, Copilot, Gemini CLI) reads agents/pm-critic.md
  and executes the system prompt inline. Returns findings graded P0/P1/P2/P3 with
  concrete fix suggestions per finding, plus a layered Status Summary section and
  machine-readable Status YAML blo...'
full_prompt_length: 6337
tools_mentioned: []
category: community
category_display: Community
source_repo: product-on-purpose/pm-skills
source_path: skills/utility-pm-critic/SKILL.md
source_url: https://github.com/product-on-purpose/pm-skills/blob/main/skills/utility-pm-critic/SKILL.md
fetched_at: '2026-05-31T06:17:26.387974+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-31T08:43:07.954218Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f56212251c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f56212251c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-31T09:00:17.313047Z'
indexed_at: '2026-05-31T09:00:17.313052Z'
---
