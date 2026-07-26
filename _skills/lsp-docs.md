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
- go
- Rust
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-docs/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-docs/SKILL.md
fetched_at: '2026-07-26T05:31:46.831032+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-26T06:46:12.401516Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1607eae450 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1607eae450 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-26T09:24:28.815186Z'
indexed_at: '2026-07-26T09:24:28.815192Z'
---
