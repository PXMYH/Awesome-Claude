---
id: lsp-explore
slug: lsp-explore
name: lsp-explore
description: '### Summary'
prompt_preview: '---

  name: lsp-explore

  description: "Tell me about this symbol": hover + implementations + call hierarchy
  + references in one pass — for navigating unfamiliar code.

  argument-hint: "[symbol-name]"

  user-invocable: true

  allowed-tools: mcp__lsp__start_lsp mcp__lsp__go_to_symbol mcp__lsp__inspect_symbol
  mcp__lsp__go_to_implementation mcp__lsp__find_callers mcp__lsp__find_references
  mcp__lsp__open_document mcp__lsp__get_server_capabilities

  license: MIT

  compatibility: Requires the agent-lsp MCP server (...'
full_prompt_length: 6308
tools_mentioned:
- go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-explore/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-explore/SKILL.md
fetched_at: '2026-07-19T05:20:54.967348+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T06:35:40.362221Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c3f20 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c3f20 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:18.327857Z'
indexed_at: '2026-07-19T09:13:18.327862Z'
---
