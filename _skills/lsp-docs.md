---
id: lsp-docs
slug: lsp-docs
name: lsp-docs
description: Tier 3 — skipped (Tier 2 succeeded)
prompt_preview: '---

  name: lsp-docs

  description: Three-tier documentation lookup for any symbol — hover → offline toolchain
  doc → source definition. Use when hover text is absent, insufficient, or the symbol
  is in an unindexed dependency.

  argument-hint: "[symbol-name]"

  user-invocable: true

  allowed-tools: mcp__lsp__inspect_symbol mcp__lsp__get_symbol_documentation mcp__lsp__go_to_definition
  mcp__lsp__get_symbol_source

  license: MIT

  compatibility: Requires the agent-lsp MCP server (github.com/blackwell-systems/agen...'
full_prompt_length: 4794
tools_mentioned:
- Go
- Rust
- go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-docs/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-docs/SKILL.md
fetched_at: '2026-07-19T05:20:54.615340+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T06:35:16.077436Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c06e0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c06e0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:18.318796Z'
indexed_at: '2026-07-19T09:13:18.318801Z'
---
