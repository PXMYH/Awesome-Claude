---
id: c-timer
slug: c-timer
name: Timer — Countdowns & Pomodoro
description: '- Always confirm the timer was set with the exact duration'
prompt_preview: '---

  name: c-timer

  description: Timers, alarms, and pomodoro — set countdowns with native notifications.

  tags: [timer, alarm, pomodoro, countdown, reminder]

  ---


  # Timer — Countdowns & Pomodoro


  Set timers and get notified via native macOS notifications. Uses `terminal-notifier`
  and background sleep.


  ## Commands


  ```bash

  # Simple timer (runs in background)

  (sleep 300 && terminal-notifier -title "Timer" -message "5 minutes is up!" -sound
  default) &


  # Timer with custom message

  (sleep 1800 && term...'
full_prompt_length: 1871
tools_mentioned: []
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-timer/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-timer/SKILL.md
fetched_at: '2026-05-03T05:31:20.915623+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-03T06:42:07.453305Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e340f54f0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e340f54f0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-03T08:17:30.743934Z'
indexed_at: '2026-05-03T08:17:30.743940Z'
---
