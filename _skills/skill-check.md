---
id: skill-check
slug: skill-check
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
full_prompt_length: 30071
tools_mentioned:
- Python
- Azure
- REST
- Go
category: community
category_display: Community
source_repo: olgasafonova/SkillCheck-Free
source_path: skills/skill-check/SKILL.md
source_url: https://github.com/olgasafonova/SkillCheck-Free/blob/main/skills/skill-check/SKILL.md
fetched_at: '2026-05-17T05:48:13.811138+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-17T07:16:25.999976Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f48a8a64f80 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f48a8a64f80 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-17T08:28:04.949519Z'
indexed_at: '2026-05-17T08:28:04.949525Z'
---
