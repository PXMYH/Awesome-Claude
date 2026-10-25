---
id: workflows-as-code
slug: workflows-as-code
name: Workflows as Code
description: 1. **The Workflows API is beta.** HubSpot documents it as subject to
  change, with the current reference at `/automation/v4/2027-03-beta/flows`. The scripts
  here call the unversioned `/automation/v4/fl...
prompt_preview: "---\nname: workflows-as-code\ndescription: \"Export all HubSpot workflows\
  \ to versioned JSON files via the v4 Automation API, diff exports over time, and\
  \ restore or recreate workflows from JSON. Treats workflow definitions like code:\
  \ backed up, reviewable, and recoverable.\"\nlicense: MIT\nmetadata:\n  author:\
  \ tomgranot\n  version: \"1.1\"\n  category: automation-workflows\n---\n\n# Workflows\
  \ as Code\n\nExport every workflow in the portal to JSON files, keep the exports\
  \ under version control, and restore workflo..."
full_prompt_length: 6274
tools_mentioned:
- Python
category: community
category_display: Community
source_repo: TomGranot/hubspot-admin-skills
source_path: skills/workflows-as-code/SKILL.md
source_url: https://github.com/TomGranot/hubspot-admin-skills/blob/main/skills/workflows-as-code/SKILL.md
fetched_at: '2026-10-25T07:16:18.200300+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T08:10:17.988944Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee5160 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee5160 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:05.159652Z'
indexed_at: '2026-10-25T12:12:05.159657Z'
---
