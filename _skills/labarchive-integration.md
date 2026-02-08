---
id: labarchive-integration
slug: labarchive-integration
name: LabArchives Integration
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: labarchive-integration\ndescription: Electronic lab notebook\
  \ API integration. Access notebooks, manage entries/attachments, backup notebooks,\
  \ integrate with Protocols.io/Jupyter/REDCap, for programmatic ELN workflows.\n\
  license: Unknown\nmetadata:\n    skill-author: K-Dense Inc.\n---\n\n# LabArchives\
  \ Integration\n\n## Overview\n\nLabArchives is an electronic lab notebook platform\
  \ for research documentation and data management. Access notebooks, manage entries\
  \ and attachments, generate reports, and..."
full_prompt_length: 10260
tools_mentioned:
- go
- python
- Python
- REST
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/labarchive-integration/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/labarchive-integration/SKILL.md
fetched_at: '2026-02-08T04:31:26.632994+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:32:04.158997Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is well-structured with clear sections and practical examples,
      but it has some issues. It references external scripts and files (scripts/setup_config.py,
      references/authentication_guide.md) that don't exist in the prompt context,
      which could confuse users. The authentication section assumes specific Python
      libraries and API endpoints that may not be universally available.
  usefulness:
    score: 4.5
    reasoning: This is highly practical for researchers and lab managers needing to
      automate LabArchives workflows. It covers real-world use cases like backups,
      integration with other tools, and programmatic entry management. The inclusion
      of regional endpoints and specific API methods makes it immediately actionable
      for users with proper LabArchives Enterprise access.
  overall_rating: 4.25
  summary: A solid, practical skill prompt for LabArchives integration that provides
    concrete workflows and examples, though it suffers from minor issues with external
    dependencies and assumes specific technical environments.
  tags_suggested:
  - scientific
  - automation
  - elab
  - api-integration
  - research
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:44.522628Z'
indexed_at: '2026-02-08T04:36:44.522634Z'
---
