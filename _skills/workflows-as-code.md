---
id: workflows-as-code
slug: workflows-as-code
name: Workflows as Code
description: 1. **Updating in place requires the current `revisionId`.** `PUT /automation/v4/{flowId}`
  must include the flow's latest `revisionId` and `type` — a stale revision is rejected.
  The restore script side...
prompt_preview: "---\nname: workflows-as-code\ndescription: \"Export all HubSpot workflows\
  \ to versioned JSON files via the v4 Automation API, diff exports over time, and\
  \ restore or recreate workflows from JSON. Treats workflow definitions like code:\
  \ backed up, reviewable, and recoverable.\"\nlicense: MIT\nmetadata:\n  author:\
  \ tomgranot\n  version: \"1.1\"\n  category: automation-workflows\n---\n\n# Workflows\
  \ as Code\n\nExport every workflow in the portal to JSON files, keep the exports\
  \ under version control, and restore workflo..."
full_prompt_length: 5399
tools_mentioned:
- Python
category: community
category_display: Community
source_repo: TomGranot/hubspot-admin-skills
source_path: skills/workflows-as-code/SKILL.md
source_url: https://github.com/TomGranot/hubspot-admin-skills/blob/main/skills/workflows-as-code/SKILL.md
fetched_at: '2026-07-19T05:20:11.496747+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T05:57:07.321202Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2107fa180 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2107fa180 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:17.455481Z'
indexed_at: '2026-07-19T09:13:17.455487Z'
---
