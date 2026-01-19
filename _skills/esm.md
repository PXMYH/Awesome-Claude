---
id: esm
slug: esm
name: 'ESM: Evolutionary Scale Modeling'
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: esm

  description: Comprehensive toolkit for protein language models including ESM3 (generative
  multimodal protein design across sequence, structure, and function) and ESM C (efficient
  protein embeddings and representations). Use this skill when working with protein
  sequences, structures, or function prediction; designing novel proteins; generating
  protein embeddings; performing inverse folding; or conducting protein engineering
  tasks. Supports both local model usage and cloud-based Forg...'
full_prompt_length: 11381
tools_mentioned:
- AWS
- python
- go
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/esm/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/esm/SKILL.md
fetched_at: '2026-01-19T00:19:10.327238+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:27:47.393404Z'
  prompt_quality:
    score: 2.5
    reasoning: The prompt has significant structural issues that undermine its quality.
      It contains incomplete code snippets (ESM C section cuts off mid-sentence),
      lacks clear instructions for the AI agent on how to interpret and execute these
      commands, and provides no guidance on error handling, model requirements, or
      API authentication. The prompt is more of a documentation snippet than an actionable
      agent instruction.
  usefulness:
    score: 3.0
    reasoning: The prompt covers valuable protein modeling capabilities including
      sequence generation, structure prediction, and embeddings, which are highly
      relevant for bioinformatics and protein engineering. However, its practical
      utility is severely limited by the incomplete code examples and lack of operational
      guidance, making it difficult for users to implement without additional research.
  overall_rating: 2.75
  summary: This prompt serves as a useful reference for ESM model capabilities but
    fails as an actionable agent instruction due to incomplete code examples, missing
    operational details, and unclear execution instructions.
  tags_suggested:
  - protein modeling
  - bioinformatics
  - ESM3
  - ESM C
  - generative AI
  - scientific computing
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.673908Z'
indexed_at: '2026-01-19T01:30:35.673913Z'
---
