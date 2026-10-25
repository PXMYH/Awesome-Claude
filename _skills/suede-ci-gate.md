---
id: suede-ci-gate
slug: suede-ci-gate
name: Suede CI Gate
description: '- The gate is failing on real defects → **suede-code** to review and
  grade the change (`--findings-only` when the caller wants no letter grade)'
prompt_preview: '---

  name: suede-ci-gate

  description: "Suede AI CI and branch-protection wiring for any repo and any stack:
  path-aware jobs, a single aggregator required check that cannot deadlock, lockfile
  hygiene, runtime pinning from the repo, and the exact branch-protection settings.
  Use when asked to set up CI, protect main, make CI block a bad merge, fix a required
  check that hangs pending forever, or repair duplicate or misfiring pipelines. Detects
  the repo''s real apps, package managers, and runtime versi...'
full_prompt_length: 10031
tools_mentioned:
- Python
- python
- go
category: community
category_display: Community
source_repo: JasonColapietro/suede-creator-skills
source_path: skills/suede-ci-gate/SKILL.md
source_url: https://github.com/JasonColapietro/suede-creator-skills/blob/main/skills/suede-ci-gate/SKILL.md
fetched_at: '2026-10-25T07:15:33.760534+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T07:29:02.479571Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8debb860 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8debb860 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:04.453740Z'
indexed_at: '2026-10-25T12:12:04.453745Z'
---
