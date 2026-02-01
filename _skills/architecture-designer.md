---
id: architecture-designer
slug: architecture-designer
name: Architecture Designer
description: '- **Fullstack Guardian** - Implementing designs'
prompt_preview: "---\nname: architecture-designer\ndescription: Use when designing\
  \ new system architecture, reviewing existing designs, or making architectural decisions.\
  \ Invoke for system design, architecture review, design patterns, ADRs, scalability\
  \ planning.\ntriggers:\n  - architecture\n  - system design\n  - design pattern\n\
  \  - microservices\n  - scalability\n  - ADR\n  - technical design\n  - infrastructure\n\
  role: expert\nscope: design\noutput-format: document\n---\n\n# Architecture Designer\n\
  \nSenior software architect spe..."
full_prompt_length: 3125
tools_mentioned:
- Azure
- Kubernetes
- GCP
- AWS
category: community
category_display: Community
source_repo: jeffallan/claude-skills
source_path: skills/architecture-designer/SKILL.md
source_url: https://github.com/jeffallan/claude-skills/blob/main/skills/architecture-designer/SKILL.md
fetched_at: '2026-02-01T04:29:21.095835+00:00'
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
  fetched_at: '2026-02-01T04:32:50.694088Z'
indexed_at: '2026-02-01T04:32:50.694094Z'
---
