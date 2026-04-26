---
id: skillcheck-free
slug: skillcheck-free
name: SkillCheck (Free)
description: Skills can also be distributed via the `/v1/skills` API endpoint. See
  [agentskills.io](https://agentskills.io) for the specification.
prompt_preview: '---

  name: skill-check

  description: Validate Claude Code skills against Anthropic guidelines. Use when
  user says "check skill", "skillcheck", "validate SKILL.md", or asks to find issues
  in skill definitions. Covers structural and semantic validation. Do NOT use for
  anti-slop detection, security scanning, token analysis, enterprise checks, or Eval
  Kit generation; use skill-check-pro for those. Do NOT use for LinkedIn skill engagement;
  use skillcheck-engage for that.

  license: MIT

  allowed-tools: Rea...'
full_prompt_length: 25354
tools_mentioned:
- Azure
- Python
- Go
category: community
category_display: Community
source_repo: olgasafonova/SkillCheck-Free
source_path: SKILL.md
source_url: https://github.com/olgasafonova/SkillCheck-Free/blob/main/SKILL.md
fetched_at: '2026-04-26T04:59:47.510932+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-26T06:32:30.766480Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe11221f40 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe11221f40 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-26T07:41:26.344791Z'
indexed_at: '2026-04-26T07:41:26.344797Z'
---
