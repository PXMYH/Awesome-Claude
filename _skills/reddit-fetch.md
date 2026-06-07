---
id: reddit-fetch
slug: reddit-fetch
name: Reddit Fetch
description: '- **Don''t fire parallel requests.** Make them sequentially with `sleep
  2` or `sleep 3` between each.'
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
full_prompt_length: 4826
tools_mentioned: []
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/reddit-fetch/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/reddit-fetch/SKILL.md
fetched_at: '2026-06-07T06:29:21.240585+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T10:03:21.544925Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffb0f050 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffb0f050 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:55.878890Z'
indexed_at: '2026-06-07T10:04:55.878899Z'
---
