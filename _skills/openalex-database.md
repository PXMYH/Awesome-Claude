---
id: openalex-database
slug: openalex-database
name: OpenAlex Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: openalex-database

  description: Query and analyze scholarly literature using the OpenAlex database.
  This skill should be used when searching for academic papers, analyzing research
  trends, finding works by authors or institutions, tracking citations, discovering
  open access publications, or conducting bibliometric analysis across 240M+ scholarly
  works. Use for literature searches, research output analysis, citation analysis,
  and academic database queries.

  license: Unknown

  metadata:...'
full_prompt_length: 12871
tools_mentioned:
- go
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/openalex-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/openalex-database/SKILL.md
fetched_at: '2026-01-25T03:51:38.769504+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:35:48.971705Z'
  prompt_quality:
    score: 2.0
    reasoning: The prompt has significant quality issues. It contains a truncated
      code snippet at the end (incomplete function call for analyze_research_output),
      lacks proper error handling guidance, and provides incomplete installation instructions
      (missing uv installation command). The documentation structure is clear but
      the incomplete content undermines reliability.
  usefulness:
    score: 3.5
    reasoning: The skill demonstrates high practical value for academic research tasks
      with comprehensive coverage of common use cases including literature search,
      author/institution analysis, and bibliometrics. The two-step pattern for finding
      works by author/institution is particularly useful, though the incomplete code
      examples reduce immediate usability.
  overall_rating: 2.75
  summary: A well-structured academic research skill with strong practical applications,
    but significantly undermined by incomplete code examples and missing installation
    details that would hinder immediate implementation.
  tags_suggested:
  - academic-research
  - literature-search
  - bibliometrics
  - open-access
  - scholarly-databases
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:51.991297Z'
indexed_at: '2026-01-25T04:05:51.991303Z'
---
