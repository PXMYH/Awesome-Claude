---
id: autoskill
slug: autoskill
name: autoskill
description: Always cite the current version. The DOI and https://arxiv.org/abs/2609.00065
  resolve to the
prompt_preview: '---

  name: autoskill

  description: Analyzes user-requested Screenpipe history windows to detect repeated
  research workflows, match existing scientific skills, and stage new skill drafts
  or composition recipes for review. Requires a reachable Screenpipe HTTP API, normally
  on localhost:3030. Detection and embedding inference run locally; the selected LLM
  receives redacted app/title cluster summaries and matched skill descriptions. Use
  only when the user explicitly asks to analyze their recent work a...'
full_prompt_length: 16844
tools_mentioned:
- azure
- Python
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: skills/autoskill/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/autoskill/SKILL.md
fetched_at: '2026-10-25T07:15:45.209439+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T07:38:38.132794Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e057890 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e057890 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:04.607566Z'
indexed_at: '2026-10-25T12:12:04.607571Z'
---
