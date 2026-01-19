---
id: pdb-database
slug: pdb-database
name: PDB Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: pdb-database\ndescription: Access RCSB PDB for 3D protein/nucleic\
  \ acid structures. Search by text/sequence/structure, download coordinates (PDB/mmCIF),\
  \ retrieve metadata, for structural biology and drug discovery.\nlicense: Unknown\n\
  metadata:\n    skill-author: K-Dense Inc.\n---\n\n# PDB Database\n\n## Overview\n\
  \nRCSB PDB is the worldwide repository for 3D structural data of biological macromolecules.\
  \ Search for structures, retrieve coordinates and metadata, perform sequence and\
  \ structure simila..."
full_prompt_length: 10047
tools_mentioned:
- Python
- GraphQL
- python
- go
- graphql
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/pdb-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/pdb-database/SKILL.md
fetched_at: '2026-01-19T00:19:18.523178+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:36:42.541388Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt demonstrates excellent clarity and specificity with well-structured
      sections, clear code examples, and specific use cases. It follows prompt engineering
      best practices by providing context, examples, and clear boundaries. However,
      it's incomplete (cuts off mid-sentence in the downloading section) and lacks
      explicit error handling guidance or edge case coverage.
  usefulness:
    score: 5.0
    reasoning: This skill provides exceptional real-world value for structural biology,
      drug discovery, and computational biology workflows. It covers comprehensive
      capabilities including search, retrieval, and download operations with practical
      code examples. The actionability is high as users can immediately implement
      the provided examples for real PDB data access.
  overall_rating: 4.75
  summary: A highly practical and well-structured scientific skill for accessing RCSB
    PDB data, though incomplete in its current form, offering comprehensive coverage
    of structural biology data operations with clear, actionable examples.
  tags_suggested:
  - structural-biology
  - protein-structures
  - drug-discovery
  - bioinformatics
  - data-retrieval
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.876411Z'
indexed_at: '2026-01-19T01:30:35.876416Z'
---
