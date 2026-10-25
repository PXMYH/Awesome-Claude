---
id: grounded-explanations
slug: grounded-explanations
name: Grounded scientific explanations
description: This is a renderer for **trusted tool output**, not an authenticity or
  scientific
prompt_preview: '# Grounded scientific explanations


  Author: Hesham Salama <hesham.salama@rub.de>.


  The optional deterministic renderer covers `crystal_mapper`, `h_refinement`,

  `cfl_checker`, and `md_analysis_planner`. It separates decisions, quantities,

  units and limits without using a language model''s prose.


  Capture a tool''s JSON directly, verify that its recorded inputs match the user''s

  request, then pass that JSON on stdin to:


  ```sh

  python -m materials_simulation_skills.scientific_explanations --tool h_ref...'
full_prompt_length: 1627
tools_mentioned:
- python
category: community
category_display: Community
source_repo: HeshamFS/materials-simulation-skills
source_path: skills/GROUNDED_EXPLANATIONS.md
source_url: https://github.com/HeshamFS/materials-simulation-skills/blob/main/skills/GROUNDED_EXPLANATIONS.md
fetched_at: '2026-10-25T07:15:29.282767+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T07:25:47.829359Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8deb8b30 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8deb8b30 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:04.394440Z'
indexed_at: '2026-10-25T12:12:04.394444Z'
---
