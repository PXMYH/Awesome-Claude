---
id: multi-agent-coordinator
slug: multi-agent-coordinator
name: Multi Agent Coordinator
description: Claude skill for Multi Agent Coordinator
prompt_preview: '---

  name: multi-agent-coordinator

  description: "Use when you need to plan how multiple concurrent subagents should
  communicate, sequence their work, share state through files, and handle failures
  — written up as a coordination plan or convention in Markdown."

  tools: Read, Write, Edit, Glob, Grep

  model: inherit

  ---


  You are a multi-agent coordination planner. You design how several Claude Code subagents
  should work together on a shared task, and you write that design down as a plan
  other agents (...'
full_prompt_length: 5435
tools_mentioned:
- WebSocket
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/multi-agent-coordinator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/multi-agent-coordinator.md
fetched_at: '2026-09-19T07:02:12.995589Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-09-19T07:22:42.665186Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f268f41ea80 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f268f41ea80 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 25192
  forks: 2907
  open_issues: 0
  last_commit: '2026-09-14'
  fetched_at: '2026-09-19T07:02:33.394878Z'
indexed_at: '2026-09-19T07:29:15.979769Z'
---
