---
id: audit-api-usage
slug: audit-api-usage
name: Audit API Usage Before the 2027 Version Cutoff
description: 1. **Private app logs are the ground truth.** Code greps miss dynamically-built
  URLs; the per-app request logs in Settings show what is actually being called.
prompt_preview: "---\nname: audit-api-usage\ndescription: \"Inventory the integrations,\
  \ private apps, and internal tooling that call HubSpot APIs, and flag anything on\
  \ legacy v1-v4 endpoints ahead of HubSpot's March 30, 2027 end of support. Produces\
  \ a migration checklist to date-based API versions.\"\nlicense: MIT\nmetadata:\n\
  \  author: tomgranot\n  version: \"1.1\"\n  category: audit-planning\n---\n\n# Audit\
  \ API Usage Before the 2027 Version Cutoff\n\nIn March 2026 HubSpot replaced semantic\
  \ API versioning (v1-v4) with date-base..."
full_prompt_length: 5344
tools_mentioned:
- python
category: community
category_display: Community
source_repo: TomGranot/hubspot-admin-skills
source_path: skills/audit-api-usage/SKILL.md
source_url: https://github.com/TomGranot/hubspot-admin-skills/blob/main/skills/audit-api-usage/SKILL.md
fetched_at: '2026-07-19T05:20:07.277632+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T05:52:20.612550Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff210548260 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff210548260 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:17.346795Z'
indexed_at: '2026-07-19T09:13:17.346800Z'
---
