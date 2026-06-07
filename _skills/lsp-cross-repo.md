---
id: lsp-cross-repo
slug: lsp-cross-repo
name: lsp-cross-repo
description: start_lsp(root_dir="/repos/config-lib")
prompt_preview: '---

  name: lsp-cross-repo

  description: Cross-repository analysis — find all callers of a library symbol in
  one or more consumer repos. Use when refactoring a shared library and need to understand
  how consumers use it.

  argument-hint: "[symbol-name] in [library-file:line:col] used by [consumer-root
  ...]"

  user-invocable: true

  allowed-tools: mcp__lsp__start_lsp mcp__lsp__find_symbol mcp__lsp__get_cross_repo_references
  mcp__lsp__add_workspace_folder mcp__lsp__list_workspace_folders mcp__lsp__go_to_imp...'
full_prompt_length: 4392
tools_mentioned:
- go
category: community
category_display: Community
source_repo: blackwell-systems/agent-lsp
source_path: skills/lsp-cross-repo/SKILL.md
source_url: https://github.com/blackwell-systems/agent-lsp/blob/main/skills/lsp-cross-repo/SKILL.md
fetched_at: '2026-06-07T06:24:25.655521+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T07:34:45.673019Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44fffc0f80 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44fffc0f80 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:52.767297Z'
indexed_at: '2026-06-07T10:04:52.767320Z'
---
