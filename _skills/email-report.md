---
id: email-report
slug: email-report
name: Email Report
description: '- **Open rate is noisy** since Apple MPP. Always report CTR and CTOR
  alongside. If open rate moves >5pp but CTOR doesn''t, it''s probably MPP population
  change, not real behavior.'
prompt_preview: "---\nname: email-report\ndescription: Auto-generate the weekly or\
  \ monthly email performance report in three formats — Slack update, CEO email, board-deck\
  \ section — from real ESP data\nversion: \"1.0.0\"\nauthor: Cogny AI\nrequires:\
  \ cogny-mcp\nplatforms: [klaviyo, mailchimp, rule, get-a-newsletter]\nuser-invocable:\
  \ true\nargument-hint: \"[weekly|monthly] [slack|ceo|deck|all]\"\nallowed-tools:\n\
  \  # Cogny Cloud (aggregated) namespace\n  - mcp__cogny__klaviyo__*\n  - mcp__cogny__mailchimp__*\n\
  \  - mcp__cogny__rule__*..."
full_prompt_length: 9196
tools_mentioned: []
category: community
category_display: Community
source_repo: cognyai/claude-code-marketing-skills
source_path: skills/email-report/SKILL.md
source_url: https://github.com/cognyai/claude-code-marketing-skills/blob/main/skills/email-report/SKILL.md
fetched_at: '2026-06-14T06:39:24.222445+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T07:53:12.631160Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a3a86e0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a3a86e0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:25.523054Z'
indexed_at: '2026-06-14T10:18:25.523059Z'
---
