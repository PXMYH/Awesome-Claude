---
id: citation-management
slug: citation-management
name: Citation Management
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: citation-management\ndescription: Comprehensive citation\
  \ management for academic research. Search Google Scholar and PubMed for papers,\
  \ extract accurate metadata, validate citations, and generate properly formatted\
  \ BibTeX entries. This skill should be used when you need to find papers, verify\
  \ citation information, convert DOIs to BibTeX, or ensure reference accuracy in\
  \ scientific writing.\nallowed-tools: [Read, Write, Edit, Bash]\nlicense: MIT License\n\
  metadata:\n    skill-author: K-Dense I..."
full_prompt_length: 33416
tools_mentioned:
- go
- python
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/citation-management/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/citation-management/SKILL.md
fetched_at: '2026-02-01T04:28:17.628036+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:23:48.539672Z'
  prompt_quality:
    score: 4.0
    reasoning: 'The prompt provides clear, structured instructions with specific workflow
      phases and command examples. However, it contains a significant flaw: it references
      external scripts and files (e.g., ''python scripts/search_google_scholar.py'',
      ''references/google_scholar_search.md'') that likely don''t exist in a standard
      environment, creating a dependency on unavailable resources. The core workflow
      is well-defined but incomplete, cutting off mid-sentence in the advanced search
      strategies section.'
  usefulness:
    score: 3.5
    reasoning: The skill addresses a genuine need in academic research for systematic
      citation management, covering key tasks like searching, validation, and BibTeX
      generation. However, its practicality is severely limited by the dependency
      on non-existent scripts and the incomplete workflow documentation, which would
      prevent immediate implementation without significant modification or additional
      development.
  overall_rating: 3.75
  summary: A well-structured but flawed prompt that outlines a valuable scientific
    citation management workflow but is undermined by incomplete content and references
    to unavailable external resources, requiring substantial revision for practical
    use.
  tags_suggested:
  - academic-research
  - citation-management
  - bibliography
  - scientific-writing
  - incomplete
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:49.680563Z'
indexed_at: '2026-02-01T04:32:49.680568Z'
---
