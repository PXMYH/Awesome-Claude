---
id: elixir-expert
slug: elixir-expert
name: Elixir Expert
description: Claude skill for Elixir Expert
prompt_preview: '---

  name: elixir-expert

  description: "Use this agent when you need to build fault-tolerant, concurrent systems
  leveraging OTP patterns, GenServer architectures, and Phoenix framework for real-time
  applications. Specifically:\\n\\n<example>\\nContext: Building a real-time chat
  application with WebSocket support, process supervision, and multi-node clustering.\\nuser:
  \"I need to create a Phoenix LiveView chat app with custom GenServer state management,
  WebSocket channels, and the ability to clust...'
full_prompt_length: 10901
tools_mentioned:
- kubernetes
- websocket
- JavaScript
- Docker
- WebSocket
- rust
- Kubernetes
category: language-specialists
category_display: Language Specialists
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/02-language-specialists/elixir-expert.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/02-language-specialists/elixir-expert.md
fetched_at: '2026-02-09T04:26:05.954817Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:50:46.714018Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is highly structured and comprehensive, covering Elixir
      development from fundamentals to advanced topics. However, it lacks clear action
      instructions for the agent to follow when invoked, and the checklist format
      is more of a knowledge dump than actionable guidance. The prompt ends abruptly
      with 'Code quality with ' which suggests incomplete content.
  usefulness:
    score: 4.5
    reasoning: The prompt demonstrates deep Elixir expertise across all major areas
      (OTP, Phoenix, LiveView, Ecto, testing, performance) making it extremely valuable
      for real-world Elixir development tasks. It provides comprehensive coverage
      of best practices, patterns, and tools that would help developers build robust,
      concurrent systems. The structured knowledge base format allows for consistent,
      high-quality responses across various Elixir development scenarios.
  overall_rating: 4.25
  summary: A comprehensive Elixir knowledge base that demonstrates expert-level understanding
    of the BEAM ecosystem, though it would benefit from clearer action instructions
    and completion of the truncated content.
  tags_suggested:
  - elixir
  - otp
  - phoenix
  - concurrency
  - fault-tolerance
github_metrics:
  stars: 9985
  forks: 1081
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-09T04:26:32.597214Z'
indexed_at: '2026-02-09T04:26:41.901643Z'
---
