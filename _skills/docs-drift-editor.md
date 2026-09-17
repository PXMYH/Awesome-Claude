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
fetched_at: '2026-09-17T07:09:35.493386Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-09-17T07:22:32.709483Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff30ca10bc0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff30ca10bc0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 25138
  forks: 2903
  open_issues: 0
  last_commit: '2026-09-14'
  fetched_at: '2026-09-17T07:09:58.701307Z'
indexed_at: '2026-09-17T07:36:10.965953Z'
---
