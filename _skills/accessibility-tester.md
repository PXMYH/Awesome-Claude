---
id: accessibility-tester
slug: accessibility-tester
name: Accessibility Tester
description: Claude skill for Accessibility Tester
prompt_preview: '---

  name: accessibility-tester

  description: "Use this agent when you need comprehensive accessibility testing,
  WCAG compliance verification, or assessment of assistive technology support."

  tools: Read, Grep, Glob, Bash

  model: haiku

  ---


  You are a senior accessibility tester with deep expertise in WCAG 2.1/3.0 standards,
  assistive technologies, and inclusive design principles. Your focus spans visual,
  auditory, motor, and cognitive accessibility with emphasis on creating universally
  accessible di...'
full_prompt_length: 7056
tools_mentioned: []
category: quality-security
category_display: Quality Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/accessibility-tester.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/accessibility-tester.md
fetched_at: '2026-02-15T04:21:29.061460+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:57:10.292975Z'
  prompt_quality:
    score: 4.0
    reasoning: 'The prompt is highly specific and well-structured with comprehensive
      checklists covering WCAG standards, screen readers, keyboard navigation, and
      various accessibility domains. However, it''s incomplete - the development workflow
      section cuts off mid-sentence (''Evaluation methodology: - Ru''), and the communication
      protocol mentions a context manager that isn''t defined or integrated into the
      actual execution flow.'
  usefulness:
    score: 4.5
    reasoning: This provides exceptional real-world value for accessibility testing
      with detailed, actionable checklists covering all major WCAG success criteria
      and assistive technologies. The structured approach with specific testing methodologies
      (automated scanning, manual verification, user testing) makes it immediately
      practical for developers and QA teams working on inclusive design compliance.
  overall_rating: 4.25
  summary: A comprehensive and highly practical accessibility testing prompt with
    excellent domain coverage, though it suffers from incomplete sections that limit
    its immediate usability without additional context or completion.
  tags_suggested:
  - accessibility
  - wcag-compliance
  - inclusive-design
  - quality-assurance
  - assistive-technology
github_metrics:
  stars: 10437
  forks: 1106
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-15T04:22:41.501003Z'
indexed_at: '2026-02-15T04:33:50.557934Z'
---
