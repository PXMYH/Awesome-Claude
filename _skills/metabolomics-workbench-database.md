---
id: metabolomics-workbench-database
slug: metabolomics-workbench-database
name: Metabolomics Workbench Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: metabolomics-workbench-database\ndescription: Access NIH\
  \ Metabolomics Workbench via REST API (4,200+ studies). Query metabolites, RefMet\
  \ nomenclature, MS/NMR data, m/z searches, study metadata, for metabolomics and\
  \ biomarker discovery.\nlicense: Unknown\nmetadata:\n    skill-author: K-Dense Inc.\n\
  ---\n\n# Metabolomics Workbench Database\n\n## Overview\n\nThe Metabolomics Workbench\
  \ is a comprehensive NIH Common Fund-sponsored platform hosted at UCSD that serves\
  \ as the primary repository for metabo..."
full_prompt_length: 11129
tools_mentioned:
- python
- go
- REST
- rest
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/metabolomics-workbench-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/metabolomics-workbench-database/SKILL.md
fetched_at: '2026-02-15T04:21:12.167245+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:34:16.804411Z'
  prompt_quality:
    score: 4.0
    reasoning: 'The prompt is well-structured with clear sections and practical examples,
      but it has a significant flaw: the final code snippet is incomplete (ends with
      ''response'' without a complete statement). The examples are specific and demonstrate
      real API usage, though there''s no guidance on error handling or rate limiting.
      The structure follows good prompt engineering practices with clear ''When to
      Use'' and ''Core Capabilities'' sections.'
  usefulness:
    score: 4.5
    reasoning: This skill provides high practical value for metabolomics researchers,
      offering direct access to a major NIH repository with over 4,200 studies. The
      examples cover essential use cases like compound querying, study access, and
      nomenclature standardization. The skill is immediately actionable for anyone
      working with metabolomics data, though it could benefit from more context about
      API authentication or data format details.
  overall_rating: 4.25
  summary: A well-designed scientific skill with strong practical value for metabolomics
    research, though slightly marred by an incomplete code example; the clear structure
    and comprehensive coverage of NIH Metabolomics Workbench capabilities make it
    highly useful for researchers.
  tags_suggested:
  - metabolomics
  - bioinformatics
  - NIH
  - data-repository
  - REST-API
  - scientific-research
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:50.083015Z'
indexed_at: '2026-02-15T04:33:50.083020Z'
---
