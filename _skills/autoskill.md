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
full_prompt_length: 11404
tools_mentioned:
- python
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/autoskill/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/autoskill/SKILL.md
fetched_at: '2026-05-10T05:35:20.032301+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-10T05:41:34.128371Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f8543df3050 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f8543df3050 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-10T08:19:27.165855Z'
indexed_at: '2026-05-10T08:19:27.165860Z'
---
