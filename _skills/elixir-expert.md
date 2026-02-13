---
id: elixir-expert
slug: elixir-expert
name: Elixir Expert
description: Claude skill for Elixir Expert
prompt_preview: '---

  name: elixir-expert

  description: "Use this agent when you need to build fault-tolerant, concurrent systems
  leveraging OTP patterns, GenServer architectures, and Phoenix framework for real-time
  applications."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior Elixir developer with deep expertise in Elixir 1.15+ and the OTP
  ecosystem, specializing in building fault-tolerant, concurrent, and distributed
  systems. Your focus spans Phoenix web applications, real-time fe...'
full_prompt_length: 8134
tools_mentioned:
- kubernetes
- websocket
- Docker
- Kubernetes
- rust
- JavaScript
category: language-specialists
category_display: Language Specialists
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/02-language-specialists/elixir-expert.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/02-language-specialists/elixir-expert.md
fetched_at: '2026-02-13T04:20:54.085341Z'
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
  stars: 10303
  forks: 1096
  open_issues: 3
  last_commit: '2026-02-12'
  fetched_at: '2026-02-13T04:21:22.535205Z'
indexed_at: '2026-02-13T04:21:31.809940Z'
---
