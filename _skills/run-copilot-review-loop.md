---
id: run-copilot-review-loop
slug: run-copilot-review-loop
name: Run the Copilot Review Loop
description: '- `create-pull-request` - opens and manages the PR this loop drives
  to a clean pass'
prompt_preview: "---\nname: run-copilot-review-loop\ndescription: >\n  Drive a GitHub\
  \ Copilot (or any bot reviewer) pull-request review to a\n  clean pass without babysitting\
  \ it: fix each finding in its own commit,\n  reply to the review thread with the\
  \ fix sha, resolve the thread,\n  re-request the bot, and poll for the async re-review.\
  \ Covers the\n  thread node-id (PRRT_...) vs comment databaseId distinction, the\n\
  \  resolveReviewThread GraphQL mutation, the\n  copilot-pull-request-reviewer[bot]\
  \ slug, and how to read th..."
full_prompt_length: 13294
tools_mentioned:
- GraphQL
- REST
- go
- graphql
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/run-copilot-review-loop/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/run-copilot-review-loop/SKILL.md
fetched_at: '2026-07-12T05:35:00.241613+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-12T08:41:32.321933Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0063e33320 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0063e33320 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-12T09:23:56.885122Z'
indexed_at: '2026-07-12T09:23:56.885128Z'
---
