---
id: brenda-database
slug: brenda-database
name: BRENDA Database
description: '- BRENDA Home: https://www.brenda-enzymes.org/'
prompt_preview: "---\nname: brenda-database\ndescription: Access BRENDA enzyme database\
  \ via SOAP API. Retrieve kinetic parameters (Km, kcat), reaction equations, organism\
  \ data, and substrate-specific enzyme information for biochemical research and metabolic\
  \ pathway analysis.\nlicense: Unknown\nmetadata:\n    skill-author: K-Dense Inc.\n\
  ---\n\n# BRENDA Database\n\n## Overview\n\nBRENDA (BRaunschweig ENzyme DAtabase)\
  \ is the world's most comprehensive enzyme information system, containing detailed\
  \ enzyme data from scientific l..."
full_prompt_length: 22981
tools_mentioned:
- go
- Python
- php
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/brenda-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/brenda-database/SKILL.md
fetched_at: '2026-01-25T03:51:30.417282+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:23:05.369145Z'
  prompt_quality:
    score: 1.0
    reasoning: The prompt is critically flawed and incomplete, ending abruptly mid-sentence
      in the 'Searc' section. It contains placeholder code snippets referencing non-existent
      modules (brenda_client, scripts.brenda_queries) without any actual implementation
      or API connection details. The documentation is generic and lacks specific instructions
      for the agent on how to execute queries or handle the SOAP API.
  usefulness:
    score: 1.0
    reasoning: The skill is non-functional as presented, providing only conceptual
      examples without executable code or integration logic. It fails to address authentication,
      error handling, or data parsing requirements necessary for real-world biochemical
      research tasks. A user cannot immediately benefit from this prompt without significant
      additional development work.
  overall_rating: 1.0
  summary: This is a severely incomplete and non-functional prompt that appears to
    be a draft or template rather than a usable skill, requiring complete reconstruction
    to be practical.
  tags_suggested:
  - incomplete
  - placeholder
  - needs-revision
  - non-functional
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:51.747906Z'
indexed_at: '2026-01-25T04:05:51.747912Z'
---
