---
id: reddit-fetch
slug: reddit-fetch
name: Reddit Fetch
description: If the JSON API returns empty responses or HTTP 429, you may be rate-limited.
  Wait a moment and retry, or try with a different User-Agent string.
prompt_preview: '---

  name: reddit-fetch

  description: Fetch content from Reddit using Gemini CLI or curl JSON API fallback.
  Use when accessing Reddit URLs, researching topics on Reddit, or when Reddit returns
  403/blocked errors.

  ---


  # Reddit Fetch


  ## Method 1: Gemini CLI (Try First)


  Use Gemini CLI via tmux. It can browse, summarize, and answer complex questions
  about Reddit content.


  Pick a unique session name (e.g., `gemini_abc123`) and use it consistently throughout.


  ### Setup


  ```bash

  tmux new-session -d -...'
full_prompt_length: 3796
tools_mentioned: []
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/reddit-fetch/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/reddit-fetch/SKILL.md
fetched_at: '2026-03-22T04:22:35.243534+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-22T06:43:08.292444Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc3f5621190 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc3f5621190 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-22T06:44:17.295843Z'
indexed_at: '2026-03-22T06:44:17.295848Z'
---
