---
id: debug-buttercup-debug-buttercup
slug: debug-buttercup-debug-buttercup
name: Debug Buttercup
description: This collects pod status, events, resource usage, Redis health, and queue
  depths in one pass.
prompt_preview: "---\nname: debug-buttercup\ndescription: >\n  Debugs the Buttercup\
  \ CRS (Cyber Reasoning System) running on Kubernetes.\n  Use when diagnosing pod\
  \ crashes, restart loops, Redis failures, resource pressure,\n  disk saturation,\
  \ DinD issues, or any service misbehavior in the crs namespace.\n  Covers triage,\
  \ log analysis, queue inspection, and common failure patterns\n  for: redis, fuzzer-bot,\
  \ coverage-bot, seed-gen, patcher, build-bot, scheduler,\n  task-server, task-downloader,\
  \ program-model, litellm, dind..."
full_prompt_length: 9921
tools_mentioned:
- docker
- kubernetes
- redis
- Redis
- Docker
- Kubernetes
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/debug-buttercup/skills/debug-buttercup/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/debug-buttercup/skills/debug-buttercup/SKILL.md
fetched_at: '2026-03-01T04:22:36.373704+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-01T05:31:15.385514Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6f7b55d490 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6f7b55d490 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-01T05:39:09.645258Z'
indexed_at: '2026-03-01T05:39:09.645263Z'
---
