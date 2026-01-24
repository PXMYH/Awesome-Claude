---
id: subagent-driven-development
slug: subagent-driven-development
name: Subagent-Driven Development
description: '**Alternative workflow:**'
prompt_preview: "---\nname: subagent-driven-development\ndescription: Use when executing\
  \ implementation plans with independent tasks in the current session\n---\n\n# Subagent-Driven\
  \ Development\n\nExecute plan by dispatching fresh subagent per task, with two-stage\
  \ review after each: spec compliance review first, then code quality review.\n\n\
  **Core principle:** Fresh subagent per task + two-stage review (spec then quality)\
  \ = high quality, fast iteration\n\n## When to Use\n\n```dot\ndigraph when_to_use\
  \ {\n    \"Have implementatio..."
full_prompt_length: 9799
tools_mentioned: []
category: community
category_display: Community Skills
source_repo: obra/superpowers
source_path: skills/subagent-driven-development/SKILL.md
source_url: https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
fetched_at: '2026-01-24T03:26:13.571707Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:18:28.258356Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is highly structured with clear diagrams and a well-defined
      two-stage review process. However, it references external files (./implementer-prompt.md,
      etc.) without providing their content, creating ambiguity. The core principle
      is clearly stated, but the incomplete diagram and missing sub-prompt details
      reduce clarity.
  usefulness:
    score: 4.5
    reasoning: This is a practical, high-value pattern for complex development tasks,
      promoting quality and speed through parallel subagent workflows. The two-stage
      review (spec then code quality) addresses common development pitfalls. It would
      be immediately actionable for users with implementation plans, though it requires
      the referenced sub-prompt files to be fully functional.
  overall_rating: 4.25
  summary: A well-structured, high-quality prompt for parallel task execution with
    built-in quality gates, but its practicality depends on the completeness of the
    referenced sub-prompt files.
  tags_suggested:
  - development
  - parallel-execution
  - code-review
  - subagent
  - quality-assurance
github_metrics:
  stars: 34663
  forks: 2627
  open_issues: 82
  last_commit: '2026-01-23'
  fetched_at: '2026-01-24T03:26:18.884211Z'
indexed_at: '2026-01-24T03:26:19.725939Z'
---
