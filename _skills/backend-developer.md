---
id: backend-developer
slug: backend-developer
name: Backend Developer
description: Claude skill for Backend Developer
prompt_preview: '---

  name: backend-developer

  description: "Use this agent when building server-side APIs, microservices, and
  backend systems that require robust architecture, scalability planning, and production-ready
  implementation."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior backend developer specializing in server-side applications with
  deep expertise in Node.js 18+, Python 3.11+, and Go 1.21+. Your primary focus is
  building scalable, secure, and performant backend systems....'
full_prompt_length: 6682
tools_mentioned:
- Docker
- Python
- Node.js
- Redis
- Go
- PostgreSQL
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/backend-developer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/backend-developer.md
fetched_at: '2026-02-16T04:24:54.990646Z'
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
  stars: 10503
  forks: 1111
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-16T04:25:43.240264Z'
indexed_at: '2026-02-16T04:26:01.449411Z'
---
