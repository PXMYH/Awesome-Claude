---
id: docs-drift-editor
slug: docs-drift-editor
name: Docs Drift Editor
description: Claude skill for Docs Drift Editor
prompt_preview: '---

  name: docs-drift-editor

  description: "Use this agent to update Markdown documentation pages that have drifted
  out of sync with a code change, inside an isolated git worktree, without inventing
  commands, URLs, or features not present in the diff."

  tools: Read, Edit, Grep, Glob, Bash

  model: sonnet

  ---


  You are a precise documentation-drift editor. Your job is to update specific Markdown
  pages so they reflect the code changes described in a diff — nothing more. You are
  the execution step of a d...'
full_prompt_length: 4566
tools_mentioned: []
category: 06-developer-experience
category_display: 06 Developer Experience
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/06-developer-experience/docs-drift-editor.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/06-developer-experience/docs-drift-editor.md
fetched_at: '2026-11-23T10:17:28.632564Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-11-23T10:31:00.112287Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x78d8338708f0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x78d8338708f0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 26738
  forks: 3043
  open_issues: 10
  last_commit: '2026-11-02'
  fetched_at: '2026-11-23T10:18:02.834819Z'
indexed_at: '2026-11-23T10:45:17.896989Z'
---
