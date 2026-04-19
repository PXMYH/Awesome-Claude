---
id: choose-loop-wakeup-interval
slug: choose-loop-wakeup-interval
name: Choose Loop Wakeup Interval
description: '<!-- Keep under 500 lines. Current: ~200 lines. -->'
prompt_preview: "---\nname: choose-loop-wakeup-interval\ndescription: >\n  Select\
  \ a `delaySeconds` value when scheduling a loop wakeup via the\n  `ScheduleWakeup`\
  \ tool or the `/loop` slash command. Covers the three-tier\n  cache-aware decision\
  \ (cache-warm under 5 minutes, cache-miss 5 minutes to\n  1 hour, idle default 20\
  \ to 30 minutes), the 300-second anti-pattern, the\n  [60, 3600] runtime clamp,\
  \ the minute-boundary rounding quirk, and writing\n  a telemetry-worthy `reason`\
  \ field. Use when designing an autonomous loop..."
full_prompt_length: 10932
tools_mentioned:
- go
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/choose-loop-wakeup-interval/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/choose-loop-wakeup-interval/SKILL.md
fetched_at: '2026-04-19T04:51:20.702038+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-19T06:25:52.611865Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0ca990 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0ca990 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-19T07:27:51.253053Z'
indexed_at: '2026-04-19T07:27:51.253059Z'
---
