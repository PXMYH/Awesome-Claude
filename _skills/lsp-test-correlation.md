---
id: lsp-test-correlation
slug: lsp-test-correlation
name: lsp-test-correlation
description: '# Report correlation, then run:'
prompt_preview: '---

  name: lsp-test-correlation

  description: Find and run the tests that cover a source file. Use after editing
  a file to discover exactly which test files and test functions need to run — without
  running the entire test suite.

  argument-hint: "[file-path] [optional: run=true]"

  user-invocable: true

  allowed-tools: mcp__lsp__get_tests_for_file mcp__lsp__find_symbol mcp__lsp__open_document
  mcp__lsp__run_tests

  license: MIT

  compatibility: Requires the agent-lsp MCP server (github.com/blackwell-systems/...'
full_prompt_length: 5627
tools_mentioned:
- go
- Go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-test-correlation/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-test-correlation/SKILL.md
fetched_at: '2026-06-28T06:16:49.877565+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T07:31:23.102466Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a262e540 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a262e540 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:26.673084Z'
indexed_at: '2026-06-28T10:04:26.673090Z'
---
