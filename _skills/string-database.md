---
id: string-database
slug: string-database
name: STRING Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: string-database\ndescription: Query STRING API for protein-protein\
  \ interactions (59M proteins, 20B interactions). Network analysis, GO/KEGG enrichment,\
  \ interaction discovery, 5000+ species, for systems biology.\nlicense: Unknown\n\
  metadata:\n    skill-author: K-Dense Inc.\n---\n\n# STRING Database\n\n## Overview\n\
  \nSTRING is a comprehensive database of known and predicted protein-protein interactions\
  \ covering 59M proteins and 20B+ interactions across 5000+ organisms. Query interaction\
  \ networks, pe..."
full_prompt_length: 19042
tools_mentioned:
- python
- GO
- REST
- Python
- go
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/string-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/string-database/SKILL.md
fetched_at: '2026-02-08T04:31:38.773785+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:45:07.150294Z'
  prompt_quality:
    score: 2.5
    reasoning: The prompt has significant quality issues. It provides incomplete documentation
      with a truncated code example for network visualization and references non-existent
      files (scripts/string_api.py, references/string_reference.md) that would not
      be available to the AI. The structure is clear but lacks practical implementation
      details and has broken references.
  usefulness:
    score: 3.0
    reasoning: The skill concept is highly useful for bioinformatics and systems biology
      research, covering essential STRING API operations like ID mapping, network
      retrieval, and enrichment analysis. However, the incomplete documentation and
      missing implementation details reduce immediate practicality for users who would
      need to develop the actual API integration themselves.
  overall_rating: 2.75
  summary: This is a well-conceived but poorly executed skill prompt that outlines
    valuable bioinformatics functionality but fails to provide complete, implementable
    code or references, making it more of a specification than a usable skill.
  tags_suggested:
  - bioinformatics
  - protein-interactions
  - systems-biology
  - api-client
  - incomplete
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:44.810776Z'
indexed_at: '2026-02-08T04:36:44.810781Z'
---
