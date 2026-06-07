---
id: lsp-simulate
slug: lsp-simulate
name: lsp-simulate
description: See [references/patterns.md](references/patterns.md) for detailed field
prompt_preview: '---

  name: lsp-simulate

  description: Speculative code editing session — simulate changes in memory before
  touching disk. Use when planning edits that might break things, exploring refactors
  across multiple files, or verifying an edit is safe before applying.

  user-invocable: true

  allowed-tools: mcp__lsp__start_lsp mcp__lsp__create_simulation_session mcp__lsp__simulate_edit
  mcp__lsp__simulate_chain mcp__lsp__evaluate_session mcp__lsp__commit_session mcp__lsp__discard_session
  mcp__lsp__destroy_sessi...'
full_prompt_length: 7246
tools_mentioned:
- go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-simulate/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-simulate/SKILL.md
fetched_at: '2026-06-07T06:24:29.135467+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T07:37:11.683073Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc66000 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc66000 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:52.817592Z'
indexed_at: '2026-06-07T10:04:52.817597Z'
---
