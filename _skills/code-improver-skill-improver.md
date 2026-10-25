---
id: code-improver-skill-improver
slug: code-improver-skill-improver
name: Skill Improver
description: '- **One-time review**: dispatch the `plugin-dev:skill-reviewer` agent
  directly'
prompt_preview: '---

  name: skill-improver

  description: "Runs an autonomous review-and-fix improvement loop over a Claude Code
  skill until a review comes back clean, with a cross-round findings ledger, escalation
  when fixes stop converging, and a mechanical scope guard. Reviews are performed
  by the plugin-dev skill-reviewer agent. Use to fix skill quality issues, iteratively
  refine a skill, or resume a loop after an escalation (''fix my skill'', ''improve
  this skill until it passes review'', ''skill improvement loop'')...'
full_prompt_length: 8248
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/code-improver/skills/skill-improver/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/code-improver/skills/skill-improver/SKILL.md
fetched_at: '2026-10-25T07:20:32.594278+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:40:22.848377Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1e570 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1e570 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:08.918412Z'
indexed_at: '2026-10-25T12:12:08.918416Z'
---
