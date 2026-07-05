---
id: lsp-onboard
slug: lsp-onboard
name: lsp-onboard
description: '- Cap exploration at 10 packages and 5 hotspot files to keep the'
prompt_preview: '---

  name: lsp-onboard

  description: First-session project onboarding. Explores the project structure, detects
  build system, test runner, entry points, and key architecture patterns. Produces
  a structured project profile the agent can reference throughout the session.

  argument-hint: "[workspace-root-path]"

  user-invocable: true

  allowed-tools: mcp__lsp__start_lsp mcp__lsp__detect_lsp_servers mcp__lsp__list_symbols
  mcp__lsp__find_symbol mcp__lsp__blast_radius mcp__lsp__run_build mcp__lsp__run_tests
  m...'
full_prompt_length: 4823
tools_mentioned:
- Go
- TypeScript
- go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-onboard/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-onboard/SKILL.md
fetched_at: '2026-07-05T06:03:47.565722+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-05T07:18:31.789273Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6306c6cf20 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6306c6cf20 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-05T09:51:15.756825Z'
indexed_at: '2026-07-05T09:51:15.756831Z'
---
