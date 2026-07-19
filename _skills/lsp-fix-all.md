---
id: lsp-fix-all
slug: lsp-fix-all
name: lsp-fix-all
description: 'Auto-init note: agent-lsp supports workspace auto-inference from file
  paths.'
prompt_preview: '---

  name: lsp-fix-all

  description: Apply available quick-fix code actions for all current diagnostics
  in a file, one at a time with re-collection between each fix. Use to bulk-resolve
  errors and warnings the language server can fix automatically.

  argument-hint: "[file-path]"

  user-invocable: true

  allowed-tools: mcp__lsp__get_diagnostics mcp__lsp__suggest_fixes mcp__lsp__apply_edit
  mcp__lsp__open_document mcp__lsp__format_document

  license: MIT

  compatibility: Requires the agent-lsp MCP server (gith...'
full_prompt_length: 6402
tools_mentioned:
- go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-fix-all/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-fix-all/SKILL.md
fetched_at: '2026-07-19T05:20:55.261602+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T06:35:56.569972Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101f23c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101f23c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:18.333993Z'
indexed_at: '2026-07-19T09:13:18.333998Z'
---
