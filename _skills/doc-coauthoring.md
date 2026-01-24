---
id: doc-coauthoring
slug: doc-coauthoring
name: Doc Co-Authoring Workflow
description: '**Quality over Speed:**'
prompt_preview: '---

  name: doc-coauthoring

  description: Guide users through a structured workflow for co-authoring documentation.
  Use when user wants to write documentation, proposals, technical specs, decision
  docs, or similar structured content. This workflow helps users efficiently transfer
  context, refine content through iteration, and verify the doc works for readers.
  Trigger when user mentions writing docs, creating proposals, drafting specs, or
  similar documentation tasks.

  ---


  # Doc Co-Authoring Workflow...'
full_prompt_length: 15815
tools_mentioned:
- rest
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/doc-coauthoring/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md
fetched_at: '2026-01-24T03:26:03.675773Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:13:30.876236Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly structured with clear stage definitions, specific
      trigger conditions, and actionable instructions. It follows best practices by
      defining scope, constraints, and fallback behavior (e.g., what to do if user
      declines). The only minor weakness is that the prompt cuts off mid-sentence
      in the 'Info Dumping' section, which could cause ambiguity in production.
  usefulness:
    score: 5.0
    reasoning: This workflow addresses a common, high-value task (documentation creation)
      with a proven three-stage methodology that ensures thorough context gathering,
      iterative refinement, and reader validation. It provides immediate practical
      value by guiding users through a structured process that improves document quality
      and reduces rework, making it highly actionable for real-world documentation
      tasks.
  overall_rating: 4.75
  summary: An excellent, well-structured prompt that provides a comprehensive workflow
    for collaborative documentation, though it has a minor truncation issue that should
    be fixed for production use.
  tags_suggested:
  - documentation
  - workflow
  - collaboration
  - structured-writing
  - context-gathering
github_metrics:
  stars: 51084
  forks: 4918
  open_issues: 184
  last_commit: '2025-12-20'
  fetched_at: '2026-01-24T03:26:18.386627Z'
indexed_at: '2026-01-24T03:26:19.656639Z'
---
