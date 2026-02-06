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
full_prompt_length: 9966
tools_mentioned: []
category: community
category_display: Community Skills
source_repo: obra/superpowers
source_path: skills/subagent-driven-development/SKILL.md
source_url: https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
fetched_at: '2026-02-06T04:15:04.527677Z'
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
  stars: 45535
  forks: 3440
  open_issues: 101
  last_commit: '2026-02-06'
  fetched_at: '2026-02-06T04:15:10.256978Z'
indexed_at: '2026-02-06T04:15:19.434042Z'
---
