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
fetched_at: '2026-09-02T06:48:36.351483Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-09-02T07:08:05.363190Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1a897ad670 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1a897ad670 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 24795
  forks: 2871
  open_issues: 10
  last_commit: '2026-09-01'
  fetched_at: '2026-09-02T06:48:57.673475Z'
indexed_at: '2026-09-02T07:14:51.668202Z'
---
