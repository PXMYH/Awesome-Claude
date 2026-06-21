---
id: lsp-extract-function
slug: lsp-extract-function
name: 'lsp-extract-function: Extract Code Block into a Named Function'
description: '- **Go:** gopls may offer "Extract function" in code actions for selection
  ranges.'
prompt_preview: '---

  name: lsp-extract-function

  description: Extract a selected code block into a named function. Primary path uses
  the language server''s extract-function code action; falls back to manual extraction
  when no code action is available. Validates captured variables, scope shadowing,
  and compilation after extraction.

  argument-hint: "[file-path] [start-line] [end-line] [new-function-name]"

  user-invocable: true

  allowed-tools: mcp__lsp__list_symbols mcp__lsp__suggest_fixes mcp__lsp__execute_command
  mcp_...'
full_prompt_length: 7947
tools_mentioned:
- Go
- typescript
- TypeScript
- Python
- go
- JavaScript
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-extract-function/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-extract-function/SKILL.md
fetched_at: '2026-06-21T06:50:16.260683+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-21T08:01:06.531971Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9ac9b50 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9ac9b50 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-21T10:34:00.673326Z'
indexed_at: '2026-06-21T10:34:00.673333Z'
---
