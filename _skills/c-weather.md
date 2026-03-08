---
id: c-weather
slug: c-weather
name: Weather — Forecasts & Conditions
description: '- Default to the user''s location (check memory/SOUL.md for city)'
prompt_preview: '---

  name: c-weather

  description: Weather forecasts and conditions — current, hourly, multi-day. No API
  key needed.

  tags: [weather, forecast, temperature, assistant]

  ---


  # Weather — Forecasts & Conditions


  Get weather information using `curl` and wttr.in. No API key required, no tool to
  install.


  ## Commands


  ```bash

  # Current weather (auto-detects location)

  curl -s "wttr.in?format=3"


  # Detailed current conditions

  curl -s "wttr.in?format=%l:+%c+%t+%h+%w+%p"


  # Full forecast (today + 2 days)

  cur...'
full_prompt_length: 1406
tools_mentioned: []
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-weather/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-weather/SKILL.md
fetched_at: '2026-03-08T04:09:56.983599+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-08T05:02:12.522000Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f787fa41a60 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f787fa41a60 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-08T05:42:14.598174Z'
indexed_at: '2026-03-08T05:42:14.598179Z'
---
