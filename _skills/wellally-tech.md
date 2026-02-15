---
id: wellally-tech
slug: wellally-tech
name: WellAlly Digital Health Integration
description: '**Q: Where are API credentials stored?**'
prompt_preview: '---

  name: wellally-tech

  description: Integrate digital health data sources (Apple Health, Fitbit, Oura Ring)
  and connect to WellAlly.tech knowledge base. Import external health device data,
  standardize to local format, and recommend relevant WellAlly.tech knowledge base
  articles based on health data. Support generic CSV/JSON import, provide intelligent
  article recommendations, and help users better manage personal health data.

  allowed-tools: Read, Grep, Glob, Write

  ---


  # WellAlly Digital Health...'
full_prompt_length: 19261
tools_mentioned:
- python
- javascript
- Python
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/wellally-tech/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/wellally-tech/SKILL.md
fetched_at: '2026-02-15T04:21:59.379340+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:56:58.736156Z'
  prompt_quality:
    score: 3.0
    reasoning: The prompt has clear structure and defines core features, but it's
      incomplete and contains placeholder code that cuts off mid-sentence. It lacks
      specific implementation details for the actual data integration logic and doesn't
      provide clear guidance on how to handle API authentication, error handling,
      or data privacy concerns. The execution steps are conceptual rather than actionable.
  usefulness:
    score: 2.5
    reasoning: While the concept addresses a real need for health data integration,
      the prompt is too vague to be practically useful. It mentions specific platforms
      and APIs but doesn't provide actual implementation guidance, making it more
      of a feature specification than a working skill. The incomplete code snippets
      and lack of concrete examples reduce its immediate applicability.
  overall_rating: 2.75
  summary: This is a well-structured but incomplete prompt that outlines a valuable
    health data integration concept but lacks the technical depth and completeness
    needed for actual implementation.
  tags_suggested:
  - health-data
  - data-integration
  - knowledge-base
  - api-integration
  - csv-import
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:51.123818Z'
indexed_at: '2026-02-15T04:33:51.123824Z'
---
