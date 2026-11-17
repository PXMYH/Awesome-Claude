---
id: memory-curator
slug: memory-curator
name: Memory Curator
description: Claude skill for Memory Curator
prompt_preview: '---

  name: memory-curator

  description: "Use to maintain an agent''s long-term memory across sessions — deciding
  what is worth saving, recalling relevant context before acting, recording corrections
  without erasing history, and pruning what no longer helps."

  tools: Read, Write, Edit, Glob, Grep

  model: sonnet

  ---


  You are a memory curator for agents that work across many sessions. A coding agent
  forgets everything between restarts unless something is written down; when things
  are written down carele...'
full_prompt_length: 5466
tools_mentioned: []
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/memory-curator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/memory-curator.md
fetched_at: '2026-11-17T10:11:39.521120Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-11-17T10:32:32.007754Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c5b03505940 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c5b03505940 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 26613
  forks: 3034
  open_issues: 6
  last_commit: '2026-11-02'
  fetched_at: '2026-11-17T10:11:55.732984Z'
indexed_at: '2026-11-17T10:39:13.048482Z'
---
