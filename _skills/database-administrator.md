---
id: database-administrator
slug: database-administrator
name: Database Administrator
description: Claude skill for Database Administrator
prompt_preview: '---

  name: database-administrator

  description: Expert database administrator specializing in high-availability systems,
  performance optimization, and disaster recovery. Masters PostgreSQL, MySQL, MongoDB,
  and Redis with focus on reliability, scalability, and operational excellence.

  tools: Read, Write, Edit, Bash, Glob, Grep

  ---


  You are a senior database administrator with mastery across major database systems
  (PostgreSQL, MySQL, MongoDB, Redis), specializing in high-availability architectures,
  p...'
full_prompt_length: 7364
tools_mentioned:
- Redis
- MySQL
- PostgreSQL
- rest
- MongoDB
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/database-administrator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/database-administrator.md
fetched_at: '2026-01-24T03:25:36.167960Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:54:49.645780Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear sections and a comprehensive
      checklist, but it is incomplete and cuts off mid-sentence in the Development
      Workflow section. While the defined scope and technical depth are strong, the
      abrupt ending creates ambiguity about the expected execution flow and limits
      the prompt's completeness.
  usefulness:
    score: 4.0
    reasoning: The prompt outlines a robust framework for database administration
      with specific, actionable checklists and technical areas (e.g., HA patterns,
      backup strategies). It would be highly valuable for guiding systematic database
      management tasks, though the incomplete workflow section reduces immediate practicality
      for end-to-end execution.
  overall_rating: 3.75
  summary: A technically strong and detailed prompt for database administration that
    is hampered by an incomplete workflow section, limiting its full operational utility.
  tags_suggested:
  - database
  - infrastructure
  - postgresql
  - mysql
  - high-availability
  - performance-optimization
github_metrics:
  stars: 8621
  forks: 947
  open_issues: 4
  last_commit: '2026-01-14'
  fetched_at: '2026-01-24T03:26:17.832148Z'
indexed_at: '2026-01-24T03:26:19.317099Z'
---
