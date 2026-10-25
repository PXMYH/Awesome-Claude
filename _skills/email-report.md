---
id: email-report
slug: email-report
name: Email Report
description: Use `create_ticket` when the workspace has it (Cloud) and `create_finding`
  otherwise (Solo).
prompt_preview: '---

  name: email-report

  description: Auto-generate the weekly or monthly email performance report in three
  formats — Slack update, CEO email, board-deck section — from real ESP data

  version: "1.1.2"

  author: Cogny AI

  requires: cogny-mcp

  platforms: [klaviyo, mailchimp, rule, get-a-newsletter, brevo, mailerlite, drip,
  salesforce-marketing-cloud, symplify, braze, shopify, woocommerce, abicart, litium,
  stripe, google-analytics-4, plausible]

  user-invocable: true

  argument-hint: "[weekly|monthly] [slack|...'
full_prompt_length: 24696
tools_mentioned:
- rest
category: community
category_display: Community
source_repo: cognyai/claude-code-marketing-skills
source_path: skills/email-report/SKILL.md
source_url: https://github.com/cognyai/claude-code-marketing-skills/blob/main/skills/email-report/SKILL.md
fetched_at: '2026-10-25T07:17:14.644427+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T08:56:07.498242Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8deb9a30 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8deb9a30 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:05.975595Z'
indexed_at: '2026-10-25T12:12:05.975601Z'
---
