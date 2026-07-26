---
id: private-github-search
slug: private-github-search
name: Private GitHub search
description: '- Only the default-branch tip is mirrored - for history or other branches,
  use `git log -S` in a full clone or GitHub web search.'
prompt_preview: '---

  name: private-github-search

  description: Full-text search across all of the user''s GitHub repos (including
  private ones) using a local mirror and ripgrep. Use for "where did I put X", "which
  repo has X", or any search spanning the user''s repos - gh search code / the REST
  API cannot reliably search private repos.

  ---


  # Private GitHub search


  GitHub''s modern code search (the one that indexes private repos) is web-only; `gh
  search code` uses the legacy engine and often returns nothing for priv...'
full_prompt_length: 1774
tools_mentioned:
- REST
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/private-github-search/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/private-github-search/SKILL.md
fetched_at: '2026-07-26T05:35:30.448261+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-26T09:22:25.562779Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1607eaef00 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1607eaef00 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-26T09:24:32.247290Z'
indexed_at: '2026-07-26T09:24:32.247296Z'
---
