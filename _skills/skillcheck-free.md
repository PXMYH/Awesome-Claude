---
id: skillcheck-free
slug: skillcheck-free
name: SkillCheck (Free)
description: Skills can also be distributed via the `/v1/skills` API endpoint. See
  [agentskills.io](https://agentskills.io) for the specification.
prompt_preview: "---\nname: skill-check\ndescription: Validate Claude Code skills\
  \ against Anthropic guidelines. Use when user says \"check skill\", \"skillcheck\"\
  , \"validate SKILL.md\", or asks to find issues in skill definitions. Covers structural\
  \ and semantic validation. Do NOT use for anti-slop detection, security scanning,\
  \ token analysis, or enterprise checks; use skill-check-pro for those.\nlicense:\
  \ MIT\nallowed-tools: Read Glob\ncategory: development\ncompatibility: claude-code\n\
  metadata:\n  version: 3.15.0\n  author: o..."
full_prompt_length: 24129
tools_mentioned:
- Go
- Python
- Azure
category: community
category_display: Community
source_repo: olgasafonova/SkillCheck-Free
source_path: SKILL.md
source_url: https://github.com/olgasafonova/SkillCheck-Free/blob/main/SKILL.md
fetched_at: '2026-04-05T04:37:31.323698+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T06:30:00.882964Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac87070b0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac87070b0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:59.096600Z'
indexed_at: '2026-04-05T08:29:59.096605Z'
---
