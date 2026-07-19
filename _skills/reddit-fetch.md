---
id: reddit-fetch
slug: reddit-fetch
name: Reddit Fetch
description: '- **Don''t fire parallel requests** - run them sequentially with `sleep
  2`/`sleep 3` (or brief pauses between navigations). Fetch one listing, parse it,
  then fetch threads one at a time.'
prompt_preview: '---

  name: reddit-fetch

  description: Fetch content from Reddit via its JSON API using a browser session
  (DuckDuckGo-hop unlock). Use when accessing Reddit URLs, researching topics on Reddit,
  or when Reddit returns 403/blocked errors.

  ---


  # Reddit Fetch


  Reddit''s public JSON API works by appending `.json` to any Reddit URL — but Reddit
  now hard-blocks automated access. **curl 403s essentially every time (host AND container,
  regardless of User-Agent), and even a cold Playwright navigation to `redd...'
full_prompt_length: 5476
tools_mentioned:
- rest
- go
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/reddit-fetch/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/reddit-fetch/SKILL.md
fetched_at: '2026-07-19T05:24:41.327461+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T09:11:30.770419Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2104c5430 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2104c5430 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:21.891770Z'
indexed_at: '2026-07-19T09:13:21.891776Z'
---
