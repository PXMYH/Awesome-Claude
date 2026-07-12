---
id: lsp-safe-edit
slug: lsp-safe-edit
name: lsp-safe-edit
description: Report the combined diagnostic diff across all files in the final summary.
prompt_preview: '---

  name: lsp-safe-edit

  description: Wrap any code edit with before/after diagnostic comparison. Speculatively
  previews the change first (preview_edit), then applies to disk only if the error
  delta is acceptable. If post-edit errors appear, surfaces code actions for quick
  fixes. Handles single and multi-file edits.

  user-invocable: true

  allowed-tools: mcp__lsp__start_lsp mcp__lsp__open_document mcp__lsp__get_diagnostics
  mcp__lsp__preview_edit mcp__lsp__simulate_chain mcp__lsp__suggest_fixes mcp__...'
full_prompt_length: 9866
tools_mentioned:
- go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-safe-edit/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-safe-edit/SKILL.md
fetched_at: '2026-07-12T05:32:04.630367+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-12T06:50:02.447611Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0064548e00 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0064548e00 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-12T09:23:54.519227Z'
indexed_at: '2026-07-12T09:23:54.519232Z'
---
