---
id: reddit-fetch
slug: reddit-fetch
name: Reddit Fetch
description: '- **Fast path, often fails:** plain curl JSON (host or safeclaw container)
  with a browser `User-Agent` is faster when it works, but usually 403s now (changing
  the UA doesn''t help). Worth one quick try...'
prompt_preview: '---

  name: reddit-fetch

  description: Fetch content from Reddit using the curl JSON API. Use when accessing
  Reddit URLs, researching topics on Reddit, or when Reddit returns 403/blocked errors.

  ---


  # Reddit Fetch


  Reddit''s public JSON API works by appending `.json` to any Reddit URL. All `curl`
  examples below need a browser `User-Agent` header - export it once and reuse it:


  ```bash

  UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/120.0.0.0 Safari/537.36...'
full_prompt_length: 5291
tools_mentioned:
- go
- rest
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/reddit-fetch/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/reddit-fetch/SKILL.md
fetched_at: '2026-06-28T06:19:56.024286+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T10:02:38.591496Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a26d2180 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a26d2180 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:29.978872Z'
indexed_at: '2026-06-28T10:04:29.978896Z'
---
