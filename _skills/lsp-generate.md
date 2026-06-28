---
id: lsp-generate
slug: lsp-generate
name: lsp-generate
description: '- Do NOT batch `execute_command` calls — run one generator at a time'
prompt_preview: '---

  name: lsp-generate

  description: Trigger language server code generation — implement interface stubs,
  generate test skeletons, add missing methods, generate mock types. Uses suggest_fixes
  to surface generator options and execute_command to run them.

  argument-hint: "[file-path:line:col] [generation-intent]"

  user-invocable: true

  allowed-tools: mcp__lsp__suggest_fixes mcp__lsp__execute_command mcp__lsp__apply_edit
  mcp__lsp__format_document mcp__lsp__get_diagnostics mcp__lsp__open_document mcp__l...'
full_prompt_length: 5774
tools_mentioned:
- Python
- typescript
- go
- Go
- rust
- TypeScript
- Rust
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-generate/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-generate/SKILL.md
fetched_at: '2026-06-28T06:16:48.600683+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T07:30:02.205976Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a2c240e0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a2c240e0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:26.643226Z'
indexed_at: '2026-06-28T10:04:26.643232Z'
---
