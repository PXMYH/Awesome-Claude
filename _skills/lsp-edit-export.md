---
id: lsp-edit-export
slug: lsp-edit-export
name: lsp-edit-export
description: '`position_pattern` with `@@` is a agent-lsp extension. If your MCP client'
prompt_preview: '---

  name: lsp-edit-export

  description: Safe workflow for editing exported symbols or public APIs. Use when
  changing a function signature, modifying a public type, or altering any symbol used
  outside its own package — finds all callers first so nothing breaks silently.

  argument-hint: "[symbol-name]"

  user-invocable: true

  allowed-tools: mcp__lsp__go_to_symbol mcp__lsp__open_document mcp__lsp__find_references
  mcp__lsp__get_diagnostics mcp__lsp__run_build mcp__lsp__replace_symbol_body Edit
  Write

  lice...'
full_prompt_length: 7424
tools_mentioned:
- Java
- Python
- go
- Go
- TypeScript
- Rust
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-edit-export/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-edit-export/SKILL.md
fetched_at: '2026-06-28T06:16:47.661642+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T07:29:13.057056Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a2950b90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a2950b90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:26.625176Z'
indexed_at: '2026-06-28T10:04:26.625182Z'
---
