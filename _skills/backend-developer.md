---
id: backend-developer
slug: backend-developer
name: Backend Developer
description: Claude skill for Backend Developer
prompt_preview: '---

  name: backend-developer

  description: Senior backend engineer specializing in scalable API development and
  microservices architecture. Builds robust server-side solutions with focus on performance,
  security, and maintainability.

  tools: Read, Write, Edit, Bash, Glob, Grep

  ---


  You are a senior backend developer specializing in server-side applications with
  deep expertise in Node.js 18+, Python 3.11+, and Go 1.21+. Your primary focus is
  building scalable, secure, and performant backend systems....'
full_prompt_length: 6682
tools_mentioned:
- PostgreSQL
- Node.js
- Python
- Redis
- Docker
- Go
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/backend-developer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/backend-developer.md
fetched_at: '2026-01-29T04:06:42.720471Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:47:38.208757Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is highly specific and structured with clear sections for
      different backend development aspects, following good prompt engineering practices.
      However, it is incomplete—the Development Workflow section cuts off mid-sentence
      ('Security b'), and the Communication Protocol section lacks a clear mechanism
      for the agent to actually execute the context query or receive the response.
  usefulness:
    score: 4.0
    reasoning: The prompt provides comprehensive, real-world backend development guidelines
      covering API design, database architecture, security, performance, and microservices
      patterns, making it highly practical for senior-level tasks. The detailed checklists
      and standards offer immediate actionable value for developers building scalable
      systems, though the incomplete workflow reduces immediate usability.
  overall_rating: 3.75
  summary: A well-structured and detailed backend development prompt with strong practical
    value, but it is critically incomplete, lacking a defined execution flow and a
    complete workflow section.
  tags_suggested:
  - backend-development
  - api-design
  - microservices
  - security
  - performance-optimization
github_metrics:
  stars: 9014
  forks: 974
  open_issues: 6
  last_commit: '2026-01-26'
  fetched_at: '2026-01-29T04:07:19.023018Z'
indexed_at: '2026-01-29T04:07:20.262687Z'
---
