---
id: refactoring-specialist
slug: refactoring-specialist
name: Refactoring Specialist
description: Claude skill for Refactoring Specialist
prompt_preview: '---

  name: refactoring-specialist

  description: "Use when you need to transform poorly structured, complex, or duplicated
  code into clean, maintainable systems while preserving all existing behavior."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---

  You are a senior refactoring specialist with expertise in transforming complex,
  poorly structured code into clean, maintainable systems. Your focus spans code smell
  detection, refactoring pattern application, and safe transformation techniq...'
full_prompt_length: 6939
tools_mentioned: []
category: developer-experience
category_display: Developer Experience
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/06-developer-experience/refactoring-specialist.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/06-developer-experience/refactoring-specialist.md
fetched_at: '2026-02-15T04:21:33.897308+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:04:38.783261Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly structured with clear sections for code smells,
      refactoring patterns, and safety practices, providing excellent specificity.
      It follows prompt engineering best practices by defining a role, workflow, and
      checklist, though the workflow section is cut off mid-sentence, slightly reducing
      clarity.
  usefulness:
    score: 4.0
    reasoning: This skill offers high real-world value for developers tackling legacy
      code or complexity, with comprehensive coverage of refactoring techniques and
      safety measures. However, the abrupt end to the workflow section limits immediate
      actionability, as users may lack guidance on executing the final steps.
  overall_rating: 4.25
  summary: A robust, expert-level refactoring prompt with strong structure and practical
    depth, though incomplete workflow guidance slightly hampers usability.
  tags_suggested:
  - code-refactoring
  - developer-tools
  - code-quality
  - legacy-code
  - test-driven-development
github_metrics:
  stars: 10437
  forks: 1106
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-15T04:22:41.501003Z'
indexed_at: '2026-02-15T04:33:50.692238Z'
---
