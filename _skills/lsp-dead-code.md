---
id: lsp-dead-code
slug: lsp-dead-code
name: lsp-dead-code
description: Do NOT auto-delete symbols without user confirmation. Present the dead
  code
prompt_preview: '---

  name: lsp-dead-code

  description: Enumerate exported symbols in a file and surface those with zero references
  across the workspace. Use when auditing for dead code, cleaning up APIs, or checking
  which exports are safe to remove.

  argument-hint: "[file-path]"

  user-invocable: true

  allowed-tools: mcp__lsp__list_symbols mcp__lsp__find_references mcp__lsp__open_document
  mcp__lsp__safe_delete_symbol

  license: MIT

  compatibility: Requires the agent-lsp MCP server (github.com/blackwell-systems/agent-lsp...'
full_prompt_length: 9455
tools_mentioned:
- Java
- Go
- TypeScript
- go
- Python
- Rust
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-dead-code/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-dead-code/SKILL.md
fetched_at: '2026-07-05T06:03:45.857922+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-05T07:16:45.647878Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f63066e5f40 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f63066e5f40 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-05T09:51:15.719333Z'
indexed_at: '2026-07-05T09:51:15.719339Z'
---
