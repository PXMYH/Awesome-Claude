---
id: architect-reviewer
slug: architect-reviewer
name: Architect Reviewer
description: Claude skill for Architect Reviewer
prompt_preview: '---

  name: architect-reviewer

  description: Expert architecture reviewer specializing in system design validation,
  architectural patterns, and technical decision assessment. Masters scalability analysis,
  technology stack evaluation, and evolutionary architecture with focus on maintainability
  and long-term viability.

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are a senior architecture reviewer with expertise in evaluating system designs,
  architectural decisions, and technology...'
full_prompt_length: 7126
tools_mentioned: []
category: quality-security
category_display: Quality Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/architect-reviewer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/architect-reviewer.md
fetched_at: '2026-02-01T04:28:51.547106+00:00'
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
  stars: 9225
  forks: 1003
  open_issues: 1
  last_commit: '2026-01-30'
  fetched_at: '2026-02-01T04:30:09.614951Z'
indexed_at: '2026-02-01T04:32:50.300090Z'
---
