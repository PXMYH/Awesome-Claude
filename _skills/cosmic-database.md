---
id: cosmic-database
slug: cosmic-database
name: COSMIC Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: cosmic-database\ndescription: Access COSMIC cancer mutation\
  \ database. Query somatic mutations, Cancer Gene Census, mutational signatures,\
  \ gene fusions, for cancer research and precision oncology. Requires authentication.\n\
  license: Unknown\nmetadata:\n    skill-author: K-Dense Inc.\n---\n\n# COSMIC Database\n\
  \n## Overview\n\nCOSMIC (Catalogue of Somatic Mutations in Cancer) is the world's\
  \ largest and most comprehensive database for exploring somatic mutations in human\
  \ cancer. Access COSMIC's exten..."
full_prompt_length: 10851
tools_mentioned:
- Python
- python
- go
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/cosmic-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/cosmic-database/SKILL.md
fetched_at: '2026-01-19T00:19:07.275986+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:25:18.199348Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides clear structure and specific examples for downloading
      COSMIC data, but it's incomplete and contains errors. The 'Mutational Signatures'
      section cuts off mid-sentence, and there's no actual implementation code or
      function definitions provided—only usage examples referencing non-existent scripts.
      The authentication requirements are clearly stated, but the prompt lacks error
      handling guidance and fails to address rate limits or API limitations.
  usefulness:
    score: 3.0
    reasoning: The skill addresses a real need in cancer research for accessing COSMIC
      data programmatically, which has practical value for bioinformatics workflows.
      However, its usefulness is severely limited by the incomplete content and lack
      of actual implementation code. Users would need to create the download scripts
      and handle authentication themselves, reducing immediate actionability despite
      the clear use cases outlined.
  overall_rating: 3.25
  summary: This is a partially developed skill prompt that identifies an important
    scientific use case but lacks complete implementation details and contains incomplete
    sections, making it more of a conceptual outline than a functional skill.
  tags_suggested:
  - cancer-research
  - bioinformatics
  - genomics
  - data-access
  - incomplete
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.628914Z'
indexed_at: '2026-01-19T01:30:35.628919Z'
---
