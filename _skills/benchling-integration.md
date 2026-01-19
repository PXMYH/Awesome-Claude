---
id: benchling-integration
slug: benchling-integration
name: Benchling Integration
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: benchling-integration\ndescription: Benchling R&D platform\
  \ integration. Access registry (DNA, proteins), inventory, ELN entries, workflows\
  \ via API, build Benchling Apps, query Data Warehouse, for lab data management automation.\n\
  license: Unknown\ncompatibility: Requires a Benchling account and API key\nmetadata:\n\
  \    skill-author: K-Dense Inc.\n---\n\n# Benchling Integration\n\n## Overview\n\
  \nBenchling is a cloud platform for life sciences R&D. Access registry entities\
  \ (DNA, proteins), inventory,..."
full_prompt_length: 13880
tools_mentioned:
- Python
- python
- go
- AWS
- REST
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/benchling-integration/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/benchling-integration/SKILL.md
fetched_at: '2026-01-19T00:19:04.426722+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:22:00.883223Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt demonstrates excellent clarity and specificity, providing
      concrete code examples for authentication, entity creation, and updates. It
      includes important constraints like 'never both' for registry registration and
      notes on partial updates. However, it lacks handling of edge cases such as API
      rate limits, error handling, or validation failures, which are common in real-world
      API integrations.
  usefulness:
    score: 4.0
    reasoning: The skill provides high practical value for Benchling users, covering
      core operations like authentication, registry management, and entity updates
      with actionable code snippets. It addresses real-world needs for lab automation
      and data management. However, it's incomplete without examples for inventory
      operations, ELN entries, workflows, or data warehouse queries mentioned in the
      description, limiting its immediate applicability for those specific use cases.
  overall_rating: 4.25
  summary: A well-structured and practical prompt for Benchling integration that excels
    in clarity and core functionality but could be enhanced with more comprehensive
    coverage of all mentioned capabilities and edge case handling.
  tags_suggested:
  - scientific
  - API integration
  - life sciences
  - lab automation
  - Benchling
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.568444Z'
indexed_at: '2026-01-19T01:30:35.568449Z'
---
