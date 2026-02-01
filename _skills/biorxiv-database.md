---
id: biorxiv-database
slug: biorxiv-database
name: bioRxiv Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: biorxiv-database\ndescription: Efficient database search\
  \ tool for bioRxiv preprint server. Use this skill when searching for life sciences\
  \ preprints by keywords, authors, date ranges, or categories, retrieving paper metadata,\
  \ downloading PDFs, or conducting literature reviews.\nlicense: Unknown\nmetadata:\n\
  \    skill-author: K-Dense Inc.\n---\n\n# bioRxiv Database\n\n## Overview\n\nThis\
  \ skill provides efficient Python-based tools for searching and retrieving preprints\
  \ from the bioRxiv database. It..."
full_prompt_length: 13370
tools_mentioned:
- go
- python
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/biorxiv-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/biorxiv-database/SKILL.md
fetched_at: '2026-02-01T04:28:16.600669+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:22:39.182027Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt provides clear, structured instructions with specific examples
      and well-defined search capabilities. However, it's incomplete (cut off mid-category
      list) and lacks error handling guidance, rate limiting information, or fallback
      strategies for API failures. The examples are practical but don't cover edge
      cases like empty results or invalid DOIs.
  usefulness:
    score: 4.5
    reasoning: This is highly practical for life sciences researchers needing to systematically
      search bioRxiv preprints. It covers essential use cases like keyword searches,
      author tracking, and literature reviews with actionable Python commands. The
      batch processing example for PDF downloads adds significant value for systematic
      reviews, though it assumes the underlying script exists.
  overall_rating: 4.25
  summary: A well-structured scientific search tool with clear examples and practical
    applications, though incomplete and missing error handling guidance.
  tags_suggested:
  - scientific
  - literature-review
  - preprints
  - bioinformatics
  - research-tools
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:49.660531Z'
indexed_at: '2026-02-01T04:32:49.660537Z'
---
