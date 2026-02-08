---
id: architecture-designer
slug: architecture-designer
name: Architecture Designer
description: Distributed systems, microservices, event-driven architecture, CQRS,
  DDD, CAP theorem, cloud platforms (AWS, GCP, Azure), containers, Kubernetes, message
  queues, caching, database design
prompt_preview: "---\nname: architecture-designer\ndescription: Use when designing\
  \ new system architecture, reviewing existing designs, or making architectural decisions.\
  \ Invoke for system design, architecture review, design patterns, ADRs, scalability\
  \ planning.\nlicense: MIT\nmetadata:\n  author: https://github.com/Jeffallan\n \
  \ version: \"1.0.0\"\n  domain: api-architecture\n  triggers: architecture, system\
  \ design, design pattern, microservices, scalability, ADR, technical design, infrastructure\n\
  \  role: expert\n  scope: d..."
full_prompt_length: 3119
tools_mentioned:
- GCP
- Kubernetes
- Azure
- AWS
category: community
category_display: Community
source_repo: jeffallan/claude-skills
source_path: skills/architecture-designer/SKILL.md
source_url: https://github.com/jeffallan/claude-skills/blob/main/skills/architecture-designer/SKILL.md
fetched_at: '2026-02-08T04:32:16.544740+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:57:12.812383Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear role definition,
      specific workflow, and comprehensive constraints. It follows prompt engineering
      best practices by defining triggers, scope, and output format upfront. The reference
      system is innovative but introduces potential dependency issues if external
      files aren't available.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate practical value for real-world architecture
      tasks with its structured workflow and ADR documentation focus. It covers the
      full lifecycle from requirements to review, making it highly actionable for
      developers and architects. The inclusion of trade-off analysis and stakeholder
      review ensures comprehensive architectural thinking.
  overall_rating: 4.75
  summary: An excellent, production-ready architecture skill that balances depth with
    practicality, though the external reference system could create implementation
    challenges.
  tags_suggested:
  - system-design
  - architecture
  - microservices
  - scalability
  - ADRs
  - distributed-systems
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.491770Z'
indexed_at: '2026-02-08T04:36:45.491775Z'
---
