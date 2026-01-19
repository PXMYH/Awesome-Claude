---
id: plugin-development-plugin-authoring
slug: plugin-development-plugin-authoring
name: Plugin Authoring (Skill)
description: '- Prefer templates & scripts over freeform generation for deterministic
  tasks'
prompt_preview: '---

  name: plugin-authoring

  description: Use when creating, modifying, or debugging Claude Code plugins. Triggers
  on .claude-plugin/, plugin.json, marketplace.json, commands/, agents/, skills/,
  hooks/ directories. Provides schemas, templates, validation workflows, and troubleshooting.

  allowed-tools: Read, Grep, Glob

  ---


  # Plugin Authoring (Skill)


  You are the canonical guide for Claude Code plugin development. Prefer reading reference
  files and proposing vetted commands or diffs rather than writ...'
full_prompt_length: 6688
tools_mentioned:
- go
category: community
category_display: Community
source_repo: ivan-magda/claude-code-plugin-template
source_path: plugins/plugin-development/skills/plugin-authoring/SKILL.md
source_url: https://github.com/ivan-magda/claude-code-plugin-template/blob/main/plugins/plugin-development/skills/plugin-authoring/SKILL.md
fetched_at: '2026-01-19T00:20:03.216196+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:16:49.033939Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear triggers, flow
      of operation, and actionable checklists. It follows prompt engineering best
      practices by providing progressive disclosure through quick links and explicit
      guardrails. However, the prompt is cut off mid-sentence in the Playbooks section,
      which slightly reduces clarity for the intended scaffold workflow.
  usefulness:
    score: 5.0
    reasoning: This skill provides immense real-world value for plugin developers
      by offering immediate access to schemas, validation workflows, and common mistake
      prevention. It comprehensively covers the plugin development lifecycle from
      scaffolding to release, with specific, actionable commands like `/plugin-development:validate`.
      The red flags section is particularly practical, preventing silent failures
      that would otherwise be difficult to debug.
  overall_rating: 4.75
  summary: A highly effective skill prompt that excels at guiding plugin development
    with exceptional structure, actionable workflows, and practical guardrails, though
    it's slightly incomplete due to truncation.
  tags_suggested:
  - plugin-development
  - claude-code
  - validation
  - best-practices
  - developer-tools
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:36.649129Z'
indexed_at: '2026-01-19T01:30:36.649134Z'
---
