---
id: websocket-engineer
slug: websocket-engineer
name: Websocket Engineer
description: Claude skill for Websocket Engineer
prompt_preview: '---

  name: websocket-engineer

  description: "Use this agent when implementing real-time bidirectional communication
  features using WebSockets, Socket.IO, or similar technologies at scale. Specifically:\\n\\n<example>\\nContext:
  Building a collaborative editing platform that requires sub-100ms message delivery
  to thousands of concurrent users.\\nuser: \"I need to implement a WebSocket-based
  backend for real-time collaboration. We expect 5K concurrent connections with 100
  messages per second across...'
full_prompt_length: 6648
tools_mentioned:
- websocket
- WebSocket
- Vue
- TypeScript
- Redis
- REST
- Angular
- React
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/websocket-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/websocket-engineer.md
fetched_at: '2026-02-10T04:30:14.398537Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:49:26.168614Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear sections and specific technical
      requirements, but it contains an incomplete sentence at the end ('Coordinate
      with devops-engineer on deplo') which indicates a copy-paste error. The workflow
      is logical and comprehensive, though the 'Communication Protocol' section with
      JSON requests feels overly formal and potentially confusing for a skill prompt.
  usefulness:
    score: 4.0
    reasoning: The prompt provides excellent real-world value with comprehensive coverage
      of WebSocket architecture, from design through production optimization. It includes
      specific metrics, technologies, and integration patterns that would directly
      help developers building scalable real-time systems. The inclusion of monitoring,
      testing, and production considerations makes it highly actionable for actual
      development tasks.
  overall_rating: 3.75
  summary: A strong, practical prompt for WebSocket engineering with comprehensive
    coverage of real-time system development, though it suffers from minor formatting
    issues and an incomplete sentence that slightly reduce its polish.
  tags_suggested:
  - websocket
  - real-time
  - scalability
  - socket-io
  - production-ready
github_metrics:
  stars: 10075
  forks: 1084
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-10T04:30:47.641906Z'
indexed_at: '2026-02-10T04:30:57.064375Z'
---
