---
id: kegg-database
slug: kegg-database
name: KEGG Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: kegg-database\ndescription: Direct REST API access to\
  \ KEGG (academic use only). Pathway analysis, gene-pathway mapping, metabolic pathways,\
  \ drug interactions, ID conversion. For Python workflows with multiple databases,\
  \ prefer bioservices. Use this for direct HTTP/REST work or KEGG-specific control.\n\
  license: Non-academic use of KEGG requires a commercial license\nmetadata:\n   \
  \ skill-author: K-Dense Inc.\n---\n\n# KEGG Database\n\n## Overview\n\nKEGG (Kyoto\
  \ Encyclopedia of Genes and Genomes) is..."
full_prompt_length: 12579
tools_mentioned:
- python
- go
- REST
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/kegg-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/kegg-database/SKILL.md
fetched_at: '2026-02-15T04:21:10.594480+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:31:53.994473Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, with excellent
      organization using markdown headers and code examples. It provides specific
      function names, usage patterns, and common parameters. However, it has a minor
      formatting issue at the end (incomplete sentence about output formats) and lacks
      explicit edge case handling (e.g., API rate limits, error handling, or what
      happens when queries return no results).
  usefulness:
    score: 4.0
    reasoning: This skill provides high practical value for bioinformatics workflows,
      offering direct access to KEGG's comprehensive database for pathway analysis,
      gene mapping, and drug interactions. The inclusion of Python helper functions
      and reference documentation makes it immediately actionable for academic researchers.
      However, the utility is limited by the academic-only license restriction and
      the incomplete documentation at the end.
  overall_rating: 4.25
  summary: A well-structured and practical KEGG database skill with clear instructions
    and useful examples, though it has minor documentation gaps and license limitations
    that reduce its broader applicability.
  tags_suggested:
  - bioinformatics
  - pathway-analysis
  - KEGG
  - REST-API
  - academic-research
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:50.034523Z'
indexed_at: '2026-02-15T04:33:50.034529Z'
---
