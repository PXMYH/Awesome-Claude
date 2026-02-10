---
id: database-administrator
slug: database-administrator
name: Database Administrator
description: Claude skill for Database Administrator
prompt_preview: '---

  name: database-administrator

  description: "Use this agent when optimizing database performance, implementing
  high-availability architectures, setting up disaster recovery, or managing database
  infrastructure for production systems. Specifically:\\n\\n<example>\\nContext: A
  company''s PostgreSQL database is experiencing slow query performance during peak
  hours and needs optimization for 10k+ concurrent users.\\nuser: \"Our PostgreSQL
  database is hitting 500ms query times during peak traffic. W...'
full_prompt_length: 10265
tools_mentioned:
- PostgreSQL
- MongoDB
- rest
- Redis
- MySQL
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/database-administrator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/database-administrator.md
fetched_at: '2026-02-10T04:30:19.692573Z'
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
  stars: 10075
  forks: 1084
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-10T04:30:47.641906Z'
indexed_at: '2026-02-10T04:30:57.174121Z'
---
