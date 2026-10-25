---
id: hypogenic
slug: hypogenic
name: HypoGeniC
description: Always cite the current version. The DOI and https://arxiv.org/abs/2609.00065
  resolve to the
prompt_preview: '---

  name: hypogenic

  description: Plans and audits use of ChicagoHAI HypoGeniC/HypoRefine for LLM-assisted
  hypothesis generation from labeled text datasets. Use for the `hypogenic` package,
  its task configs, hypothesis banks, or HypoBench datasets—not for manual hypothesis
  formulation or scientific validation.

  license: MIT

  compatibility: Requires Python 3.10+ and uv for the pinned upstream package. Bundled
  local audit tools use only the Python standard library for JSON; YAML input requires
  exactl...'
full_prompt_length: 14322
tools_mentioned:
- Python
- Redis
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: skills/hypogenic/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/hypogenic/SKILL.md
fetched_at: '2026-10-25T07:15:51.457371+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T07:45:24.588889Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e67f710 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e67f710 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:04.725633Z'
indexed_at: '2026-10-25T12:12:04.725638Z'
---
