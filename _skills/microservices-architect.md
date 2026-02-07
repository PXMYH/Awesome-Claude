---
id: microservices-architect
slug: microservices-architect
name: Microservices Architect
description: Claude skill for Microservices Architect
prompt_preview: '---

  name: microservices-architect

  description: "Use when designing distributed system architecture, decomposing monolithic
  applications into independent microservices, or establishing communication patterns
  between services at scale. Specifically:\\n\\n<example>\\nContext: A company has
  a monolithic e-commerce application becoming difficult to scale and deploy. Different
  teams need to own separate business domains independently.\\nuser: \"Help us decompose
  our monolith into microservices. We hav...'
full_prompt_length: 10179
tools_mentioned:
- Kubernetes
- REST
- graphql
- gRPC
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/microservices-architect.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/microservices-architect.md
fetched_at: '2026-02-07T04:07:30.208141Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:48:52.479592Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly structured with clear sections for principles,
      patterns, and protocols, following good prompt engineering practices. However,
      it is incomplete (cut off mid-sentence in the 'Service Implementation' section),
      which introduces ambiguity about the full scope of expected behavior. The specific
      checklists and frameworks provide strong guidance for the agent's thought process.
  usefulness:
    score: 4.0
    reasoning: The prompt provides immense real-world value by offering a comprehensive
      framework for microservices design, covering resilience, data management, and
      observability. It is actionable for complex distributed system tasks, though
      the incomplete nature limits immediate usability without assuming the missing
      content. The inclusion of specific tools and communication protocols enhances
      practicality.
  overall_rating: 4.25
  summary: A robust and well-structured prompt for a microservices architect agent,
    offering detailed checklists and principles, but its utility is slightly hampered
    by being truncated mid-content.
  tags_suggested:
  - distributed-systems
  - kubernetes
  - cloud-native
  - microservices
  - system-design
github_metrics:
  stars: 9780
  forks: 1066
  open_issues: 2
  last_commit: '2026-02-06'
  fetched_at: '2026-02-07T04:08:16.529193Z'
indexed_at: '2026-02-07T04:08:26.518453Z'
---
