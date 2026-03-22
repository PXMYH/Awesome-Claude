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
fetched_at: '2026-03-22T04:19:48.835544+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-22T05:12:27.387041Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc3f5676000 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc3f5676000 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-22T06:44:15.684539Z'
indexed_at: '2026-03-22T06:44:15.684545Z'
---
