---
id: autoskill
slug: autoskill
name: autoskill
description: The autoskill's embedding index covers all 135 sibling skills. Workflows
  that look like scientific writing will match `scientific-writing` / `literature-review`
  / `citation-management`; figure work wi...
prompt_preview: '---

  name: autoskill

  description: Observe the user''s screen via screenpipe, detect repeated research
  workflows, match them against existing scientific-agent-skills, and draft new skills
  (or composition recipes that chain existing ones) for the patterns not yet covered.
  Use when the user asks to analyze their recent work and propose skills based on
  what they actually do. Requires the screenpipe daemon (https://github.com/screenpipe/screenpipe)
  running locally on port 3030 — the skill has no other...'
full_prompt_length: 12125
tools_mentioned:
- Python
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: skills/autoskill/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/autoskill/SKILL.md
fetched_at: '2026-06-21T06:49:11.678573+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-21T06:59:45.654820Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9c97500 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9c97500 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-21T10:33:59.372609Z'
indexed_at: '2026-06-21T10:33:59.372615Z'
---
