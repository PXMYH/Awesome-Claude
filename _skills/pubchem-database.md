---
id: pubchem-database
slug: pubchem-database
name: PubChem Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: pubchem-database\ndescription: Query PubChem via PUG-REST\
  \ API/PubChemPy (110M+ compounds). Search by name/CID/SMILES, retrieve properties,\
  \ similarity/substructure searches, bioactivity, for cheminformatics.\nlicense:\
  \ Unknown\nmetadata:\n    skill-author: K-Dense Inc.\n---\n\n# PubChem Database\n\
  \n## Overview\n\nPubChem is the world's largest freely available chemical database\
  \ with 110M+ compounds and 270M+ bioactivities. Query chemical structures by name,\
  \ CID, or SMILES, retrieve molecular proper..."
full_prompt_length: 17132
tools_mentioned:
- Python
- python
- go
- rest
- REST
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/pubchem-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/pubchem-database/SKILL.md
fetched_at: '2026-01-19T00:19:19.943662+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:38:05.601573Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides clear code examples and covers core capabilities
      well, but lacks critical edge case handling (e.g., API rate limits, network
      errors, compound not found scenarios). It also has an incomplete section (Similarity
      Search cuts off mid-sentence) and doesn't specify constraints like API usage
      limits or error handling best practices.
  usefulness:
    score: 4.5
    reasoning: The skill offers high real-world value for cheminformatics, drug discovery,
      and chemical research tasks with comprehensive coverage of PubChem's capabilities.
      The practical code examples enable immediate implementation for property retrieval,
      similarity searches, and batch processing, making it highly actionable for scientific
      workflows.
  overall_rating: 4.0
  summary: A highly useful cheminformatics skill with strong practical value, but
    needs improved completeness and edge case handling to reach full potential.
  tags_suggested:
  - cheminformatics
  - drug discovery
  - chemical database
  - pubchem
  - scientific computing
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.905539Z'
indexed_at: '2026-01-19T01:30:35.905544Z'
---
