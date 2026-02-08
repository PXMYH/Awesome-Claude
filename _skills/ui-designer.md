---
id: ui-designer
slug: ui-designer
name: Ui Designer
description: Claude skill for Ui Designer
prompt_preview: '---

  name: ui-designer

  description: "Use this agent when designing visual interfaces, creating design systems,
  building component libraries, or refining user-facing aesthetics requiring expert
  visual design, interaction patterns, and accessibility considerations. Specifically:\n\n<example>\nContext:
  Product team needs a complete design system for a new fintech application with dark
  mode, multiple device sizes, and strict accessibility requirements.\nuser: \"We
  need to create a comprehensive desig...'
full_prompt_length: 8175
tools_mentioned: []
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/ui-designer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/ui-designer.md
fetched_at: '2026-02-08T04:31:42.972804+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:49:13.015302Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt demonstrates strong clarity and specificity with a well-structured
      execution flow, mandatory context gathering protocol, and detailed coverage
      of design considerations like accessibility, performance, and cross-platform
      consistency. However, it contains some redundancy (e.g., listing 'Design critique
      process' and 'Performance considerations' as separate sections when they're
      already covered in the execution flow) and could benefit from more explicit
      edge case handling for scenarios where design context is unavailable or incomplete.
  usefulness:
    score: 4.0
    reasoning: This prompt provides high real-world value for UI/UX design tasks,
      offering a comprehensive framework that covers the entire design lifecycle from
      context gathering to handoff. The inclusion of specific protocols for communication
      with context-manager and structured status updates makes it actionable for development
      workflows. However, its usefulness is somewhat limited by its dependency on
      external systems (context-manager) and the assumption of access to design tools
      like Figma, which may not be available in all environments.
  overall_rating: 4.25
  summary: A well-structured, professional UI design prompt with excellent protocol
    design and comprehensive coverage of design considerations, though slightly hampered
    by redundancy and external system dependencies.
  tags_suggested:
  - ui-design
  - design-systems
  - accessibility
  - design-protocol
  - visual-design
github_metrics:
  stars: 9886
  forks: 1073
  open_issues: 2
  last_commit: '2026-02-07'
  fetched_at: '2026-02-08T04:32:59.475595Z'
indexed_at: '2026-02-08T04:36:44.889247Z'
---
