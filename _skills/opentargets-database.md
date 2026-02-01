---
id: opentargets-database
slug: opentargets-database
name: Open Targets Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: opentargets-database\ndescription: Query Open Targets\
  \ Platform for target-disease associations, drug target discovery, tractability/safety\
  \ data, genetics/omics evidence, known drugs, for therapeutic target identification.\n\
  license: Unknown\nmetadata:\n    skill-author: K-Dense Inc.\n---\n\n# Open Targets\
  \ Database\n\n## Overview\n\nThe Open Targets Platform is a comprehensive resource\
  \ for systematic identification and prioritization of potential therapeutic drug\
  \ targets. It integrates publicly ava..."
full_prompt_length: 14890
tools_mentioned:
- go
- python
- GraphQL
- graphql
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/opentargets-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/opentargets-database/SKILL.md
fetched_at: '2026-02-01T04:28:28.734338+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:35:58.714748Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides clear structure and good overview of the Open Targets
      Platform, with specific use cases and workflow examples. However, it is incomplete
      (cut off at 'Query Disease I'), lacks edge case handling, and has incomplete
      code examples that reference non-existent helper functions without implementation
      details.
  usefulness:
    score: 4.0
    reasoning: The skill addresses high-value scientific use cases like target discovery
      and drug repurposing with practical workflow guidance. It provides concrete
      examples and explains key data types, making it immediately actionable for researchers
      in biotech/pharma despite the incomplete prompt.
  overall_rating: 3.75
  summary: A scientifically valuable but technically incomplete prompt that provides
    excellent domain context and use cases but lacks full implementation details and
    edge case handling.
  tags_suggested:
  - scientific
  - biotech
  - drug-discovery
  - genomics
  - api-integration
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:49.887432Z'
indexed_at: '2026-02-01T04:32:49.887438Z'
---
