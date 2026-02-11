---
id: architect-reviewer
slug: architect-reviewer
name: Architect Reviewer
description: Claude skill for Architect Reviewer
prompt_preview: '---

  name: architect-reviewer

  description: "Use this agent when you need to evaluate system design decisions,
  architectural patterns, and technology choices at the macro level."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are a senior architecture reviewer with expertise in evaluating system designs,
  architectural decisions, and technology choices. Your focus spans design patterns,
  scalability assessment, integration strategies, and technical debt analysis with
  emphasis on bui...'
full_prompt_length: 6987
tools_mentioned: []
category: quality-security
category_display: Quality & Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/architect-reviewer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/architect-reviewer.md
fetched_at: '2026-02-11T04:28:54.796243Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:57:32.068257Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is highly structured with clear categories and checklists,
      providing excellent specificity for architecture review tasks. However, it's
      incomplete (cuts off mid-sentence in the Development Workflow section) and lacks
      explicit instructions for tool usage, edge case handling, and fallback behaviors.
      The communication protocol is defined but not fully integrated into the workflow.
  usefulness:
    score: 4.0
    reasoning: The prompt provides comprehensive architecture review frameworks covering
      scalability, security, performance, and technical debt assessment, making it
      highly valuable for real-world system design validation. The structured checklists
      and categories enable systematic evaluation, though the incomplete workflow
      section limits immediate actionability for users.
  overall_rating: 3.75
  summary: A well-structured but incomplete architecture review prompt with strong
    conceptual frameworks and comprehensive checklists, though it needs completion
    and better integration of tool usage instructions to reach full practicality.
  tags_suggested:
  - architecture-review
  - system-design
  - quality-assurance
  - technical-debt
  - scalability-analysis
github_metrics:
  stars: 10153
  forks: 1087
  open_issues: 3
  last_commit: '2026-02-10'
  fetched_at: '2026-02-11T04:29:28.992841Z'
indexed_at: '2026-02-11T04:29:38.980047Z'
---
