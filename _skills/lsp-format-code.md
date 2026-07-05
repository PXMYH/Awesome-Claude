---
id: lsp-format-code
slug: lsp-format-code
name: lsp-format-code
description: The language server delegates to the language's standard formatter —
  results
prompt_preview: '---

  name: lsp-format-code

  description: Format a file or selection using the language server''s formatter.
  Use before committing to apply consistent style, or after generating code to clean
  up indentation and spacing. Supports full-file and range-based formatting.

  argument-hint: "[file-path] [optional: start_line-end_line]"

  user-invocable: true

  allowed-tools: mcp__lsp__open_document mcp__lsp__format_document mcp__lsp__format_range
  mcp__lsp__apply_edit mcp__lsp__get_diagnostics mcp__lsp__get_server...'
full_prompt_length: 5090
tools_mentioned:
- Go
- TypeScript
- go
- rust
- typescript
- Python
- JavaScript
- Rust
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-format-code/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-format-code/SKILL.md
fetched_at: '2026-07-05T06:03:46.755984+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-05T07:17:42.938379Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f63066e40b0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f63066e40b0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-05T09:51:15.739283Z'
indexed_at: '2026-07-05T09:51:15.739290Z'
---
