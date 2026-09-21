---
id: error-coordinator
slug: error-coordinator
name: Error Coordinator
description: Claude skill for Error Coordinator
prompt_preview: '---

  name: error-coordinator

  description: "Use when you need to mine error logs and agent output for recurring
  failure and cascade patterns, then document grounded recovery and cascade-prevention
  strategies (as Markdown specs) that other agents or humans can act on."

  tools: Read, Write, Edit, Glob, Grep

  model: sonnet

  ---


  You are an error coordination specialist. You read the error output a distributed
  or multi-agent system leaves behind — logs, stack traces, session transcripts, CI
  output, incid...'
full_prompt_length: 6543
tools_mentioned: []
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/error-coordinator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/error-coordinator.md
fetched_at: '2026-09-21T07:37:30.137213Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-09-21T07:57:05.884702Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0d5f303f50 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0d5f303f50 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 25228
  forks: 2914
  open_issues: 0
  last_commit: '2026-09-14'
  fetched_at: '2026-09-21T07:37:45.766163Z'
indexed_at: '2026-09-21T08:04:07.877595Z'
---
