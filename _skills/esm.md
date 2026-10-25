---
id: esm
slug: esm
name: 'ESM: protein generation, embeddings, and folding'
description: Always cite the current version. The DOI and https://arxiv.org/abs/2609.00065
  resolve to the
prompt_preview: '---

  name: esm

  description: Uses the Biohub esm Python SDK for ESM3 protein generation, ESMC embeddings,
  and ESMFold2 all-atom folding. Applies to local model inference and Biohub hosted
  clients, including former Forge workflows; distinguishes the separate legacy fair-esm
  distribution.

  license: MIT license

  compatibility: Requires Python 3.12+ and esm 3.4.1.post1. Local pretrained inference
  needs model weights and sufficient RAM or GPU memory; hosted inference needs network
  access and ESM_API_KEY....'
full_prompt_length: 10740
tools_mentioned:
- Python
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: skills/esm/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/esm/SKILL.md
fetched_at: '2026-10-25T07:15:48.607453+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T07:42:17.769079Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee4350 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee4350 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:04.671756Z'
indexed_at: '2026-10-25T12:12:04.671761Z'
---
