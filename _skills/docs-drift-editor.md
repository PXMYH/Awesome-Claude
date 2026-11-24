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
fetched_at: '2026-11-24T11:59:44.467217Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-11-24T12:13:12.218812Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x728f95bb58b0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x728f95bb58b0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 26752
  forks: 3045
  open_issues: 10
  last_commit: '2026-11-02'
  fetched_at: '2026-11-24T12:00:18.721507Z'
indexed_at: '2026-11-24T12:27:25.829382Z'
---
