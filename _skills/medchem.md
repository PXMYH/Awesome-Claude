---
id: medchem
slug: medchem
name: Medchem
description: Always cite the current version. The DOI and https://arxiv.org/abs/2609.00065
  resolve to the
prompt_preview: '---

  name: medchem

  description: Applies medicinal chemistry filters for compound triage, using drug-likeness
  rules (Lipinski, Veber, CNS), structural alert catalogs (PAINS, NIBR, ChEMBL), complexity
  metrics, and the medchem query language for library filtering.

  license: Apache-2.0 license

  allowed-tools: Read Write Edit Bash

  compatibility: Requires Python 3.11+ with medchem, datamol, and RDKit. Optional
  Lilly demerits require native tools built with medchem install-lilly, a C++ compiler,
  make, zli...'
full_prompt_length: 15698
tools_mentioned:
- Python
- python
- Ruby
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: skills/medchem/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/medchem/SKILL.md
fetched_at: '2026-10-25T07:15:53.888092+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T07:48:07.198799Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e2f6ea0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e2f6ea0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:04.772882Z'
indexed_at: '2026-10-25T12:12:04.772887Z'
---
