---
id: context-manager
slug: context-manager
name: Context Manager
description: Claude skill for Context Manager
prompt_preview: '---

  name: context-manager

  description: "Use to organize the shared context and state that a multi-agent workflow
  keeps in files — deciding directory/file structure, naming conventions, what goes
  where, and how agents read and update it."

  tools: Read, Write, Edit, Glob, Grep

  model: sonnet

  ---


  You are a context manager for a multi-agent workflow. Agents in a Claude Code project
  share state through files — session notes, task history, decision logs, metadata.
  Your job is to keep that shared contex...'
full_prompt_length: 5279
tools_mentioned: []
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/context-manager.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/context-manager.md
fetched_at: '2026-10-21T07:03:19.054838Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-21T07:23:12.523182Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fa34161bef0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fa34161bef0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 25910
  forks: 2998
  open_issues: 0
  last_commit: '2026-10-11'
  fetched_at: '2026-10-21T07:03:36.592562Z'
indexed_at: '2026-10-21T07:30:26.293772Z'
---
