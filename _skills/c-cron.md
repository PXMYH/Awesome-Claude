---
id: c-cron
slug: c-cron
name: Scheduling & Cron
description: '- Prefer lunchy-go for macOS services (launchd plists)'
prompt_preview: '---

  name: c-cron

  description: Manage cron jobs and macOS launchctl services — schedule recurring
  tasks, start/stop services using lunchy-go.

  tags: [cron, scheduling, launchctl, automation]

  ---


  # Scheduling & Cron


  ## lunchy-go (launchctl wrapper)


  Friendly wrapper around macOS `launchctl`:


  ```bash

  # List all services (pattern match)

  lunchy-go ls

  lunchy-go ls redis


  # Start a service

  lunchy-go start com.example.service

  lunchy-go start redis    # pattern match


  # Stop a service

  lunchy-go stop re...'
full_prompt_length: 1214
tools_mentioned:
- go
- redis
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-cron/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-cron/SKILL.md
fetched_at: '2026-05-03T05:31:15.672671+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-03T06:38:24.852143Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f2f590 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f2f590 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-03T08:17:30.671260Z'
indexed_at: '2026-05-03T08:17:30.671266Z'
---
