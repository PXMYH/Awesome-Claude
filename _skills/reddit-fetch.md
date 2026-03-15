---
id: reddit-fetch
slug: reddit-fetch
name: Reddit Fetch via Gemini CLI
description: '```bash'
prompt_preview: '---

  name: reddit-fetch

  description: Fetch content from Reddit using Gemini CLI when WebFetch is blocked.
  Use when accessing Reddit URLs, researching topics on Reddit, or when Reddit returns
  403/blocked errors.

  ---


  # Reddit Fetch via Gemini CLI


  When WebFetch fails to access Reddit (blocked, 403, etc.), use Gemini CLI via tmux.


  Pick a unique session name (e.g., `gemini_abc123`) and use it consistently throughout.


  ## Setup


  ```bash

  tmux new-session -d -s <session_name> -x 200 -y 50

  tmux send-ke...'
full_prompt_length: 1790
tools_mentioned: []
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/reddit-fetch/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/reddit-fetch/SKILL.md
fetched_at: '2026-03-15T04:32:48.681722+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-15T06:03:21.130471Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fa396423410 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fa396423410 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-15T06:04:20.936718Z'
indexed_at: '2026-03-15T06:04:20.936724Z'
---
