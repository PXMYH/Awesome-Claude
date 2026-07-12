---
id: observability-baseline
slug: observability-baseline
name: observability-baseline
description: A scaffolded app where the first prod error is captured, every request
  is traceable
prompt_preview: "---\nname: observability-baseline\ndescription: Scaffold-time observability\
  \ so a shipped product is not blind in prod from day one — error capture (Sentry),\
  \ request-id structured logging, and /healthz + /readyz endpoints. stack-baseline\
  \ pins Sentry but nothing wires it; this is the wiring. Loaded by app-scaffolder\
  \ (bake into the scaffold), infra-provisioner (prod env + probes), and consumed\
  \ by l3-support (traces) and devops (deploy gate).\nwhen_to_use: |\n  Apply when:\n\
  \  - app-scaffolder is generati..."
full_prompt_length: 3085
tools_mentioned:
- go
category: community
category_display: Community
source_repo: avelikiy/great_cto
source_path: skills/observability-baseline/SKILL.md
source_url: https://github.com/avelikiy/great_cto/blob/main/skills/observability-baseline/SKILL.md
fetched_at: '2026-07-12T05:31:49.158683+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-12T06:37:03.225607Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f00642af4d0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f00642af4d0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-12T09:23:54.244799Z'
indexed_at: '2026-07-12T09:23:54.244806Z'
---
