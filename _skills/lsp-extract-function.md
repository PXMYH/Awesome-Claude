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
- go
- Python
- Go
- TypeScript
- typescript
- JavaScript
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-extract-function/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-extract-function/SKILL.md
fetched_at: '2026-07-12T05:32:03.179902+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-12T06:48:32.728906Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0063fdcb30 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0063fdcb30 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-12T09:23:54.487275Z'
indexed_at: '2026-07-12T09:23:54.487282Z'
---
