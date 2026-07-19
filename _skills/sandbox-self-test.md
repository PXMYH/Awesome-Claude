---
id: sandbox-self-test
slug: sandbox-self-test
name: Sandbox Self-Test
description: It runs preflight → seed → suite → teardown on **manual dispatch only**
  and uploads the report as an artifact. It never runs on push or PR — the sandbox
  is yours, so the trigger is too. (It ships outs...
prompt_preview: "---\nname: sandbox-self-test\ndescription: \"Verify the entire toolkit\
  \ against a disposable HubSpot developer test account or sandbox that you bring:\
  \ seed synthetic fixtures, run every scripted skill's read path, exercise end-to-end\
  \ and API round-trip cases, produce a graded report, and tear everything down. Hard-refuses\
  \ to run against production.\"\nlicense: MIT\nmetadata:\n  author: tomgranot\n \
  \ version: \"1.0\"\n  category: audit-planning\n---\n\n# Sandbox Self-Test\n\n##\
  \ Purpose\n\nEvery skill in this repo mu..."
full_prompt_length: 9057
tools_mentioned:
- Python
- GO
category: community
category_display: Community
source_repo: TomGranot/hubspot-admin-skills
source_path: skills/sandbox-self-test/SKILL.md
source_url: https://github.com/TomGranot/hubspot-admin-skills/blob/main/skills/sandbox-self-test/SKILL.md
fetched_at: '2026-07-19T05:20:10.633268+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T05:56:08.539523Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101899a0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101899a0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:17.433850Z'
indexed_at: '2026-07-19T09:13:17.433860Z'
---
