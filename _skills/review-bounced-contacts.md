---
id: review-bounced-contacts
slug: review-bounced-contacts
name: Review Bounced Contacts
description: Run weekly, ideally Monday morning. Should take 5-15 minutes depending
  on volume. If volume exceeds 50 contacts per week, investigate the root cause (bad
  list source, form spam, etc.).
prompt_preview: "---\nname: review-bounced-contacts\ndescription: \"Weekly manual\
  \ review of contacts with 3+ bounce events. Decide whether to delete or attempt\
  \ recovery for each flagged contact. Prevents over-suppression while removing truly\
  \ bad data.\"\nlicense: MIT\nmetadata:\n  author: tomgranot\n  version: \"1.0\"\n\
  \  category: ongoing-maintenance\n---\n\n# Review Bounced Contacts\n\nA weekly manual\
  \ review process for contacts flagged with 3+ bounces. The bounce monitoring workflow\
  \ auto-suppresses these contacts, but a human..."
full_prompt_length: 3018
tools_mentioned:
- python
category: community
category_display: Community
source_repo: TomGranot/hubspot-admin-skills
source_path: skills/review-bounced-contacts/SKILL.md
source_url: https://github.com/TomGranot/hubspot-admin-skills/blob/main/skills/review-bounced-contacts/SKILL.md
fetched_at: '2026-04-12T04:46:44.419022+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-12T05:16:23.257819Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f3993613b90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f3993613b90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-12T07:23:19.672584Z'
indexed_at: '2026-04-12T07:23:19.672590Z'
---
