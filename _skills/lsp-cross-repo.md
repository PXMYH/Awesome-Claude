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
fetched_at: '2026-06-14T06:39:18.019292+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T07:48:19.896728Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a4e55b0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a4e55b0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:25.443577Z'
indexed_at: '2026-06-14T10:18:25.443582Z'
---
