---
id: get-available-resources
slug: get-available-resources
name: Get Available Resources
description: '**Inaccurate memory readings:**'
prompt_preview: '---

  name: get-available-resources

  description: This skill should be used at the start of any computationally intensive
  scientific task to detect and report available system resources (CPU cores, GPUs,
  memory, disk space). It creates a JSON file with resource information and strategic
  recommendations that inform computational approach decisions such as whether to
  use parallel processing (joblib, multiprocessing), out-of-core computing (Dask,
  Zarr), GPU acceleration (PyTorch, JAX), or memory-effic...'
full_prompt_length: 9844
tools_mentioned:
- python
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: skills/get-available-resources/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/get-available-resources/SKILL.md
fetched_at: '2026-05-31T06:15:06.817407+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-31T06:25:47.337391Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f5621711e50 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f5621711e50 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-31T09:00:14.272868Z'
indexed_at: '2026-05-31T09:00:14.272874Z'
---
