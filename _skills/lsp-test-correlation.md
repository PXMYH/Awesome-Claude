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
- Go
- go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-test-correlation/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-test-correlation/SKILL.md
fetched_at: '2026-07-19T05:20:56.748191+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T06:37:34.332955Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2108e3290 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2108e3290 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:18.370340Z'
indexed_at: '2026-07-19T09:13:18.370345Z'
---
