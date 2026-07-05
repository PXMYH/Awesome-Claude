---
id: winback-engine
slug: winback-engine
name: Winback Engine
description: '- **Never suppress before a winback attempt.** Give Tier D subscribers
  one last chance to re-engage.'
prompt_preview: "---\nname: winback-engine\ndescription: Find dormant subscribers,\
  \ segment by historical value, draft personalized winback emails per tier, and identify\
  \ suppression candidates\nversion: \"1.0.0\"\nauthor: Cogny AI\nrequires: cogny-mcp\n\
  platforms: [klaviyo, mailchimp, rule, get-a-newsletter]\nuser-invocable: true\n\
  argument-hint: \"[aggressive|standard|conservative]\"\nallowed-tools:\n  # Cogny\
  \ Cloud (aggregated) namespace\n  - mcp__cogny__klaviyo__*\n  - mcp__cogny__mailchimp__*\n\
  \  - mcp__cogny__rule__*\n  - mcp__c..."
full_prompt_length: 9405
tools_mentioned: []
category: community
category_display: Community
source_repo: cognyai/claude-code-marketing-skills
source_path: skills/winback-engine/SKILL.md
source_url: https://github.com/cognyai/claude-code-marketing-skills/blob/main/skills/winback-engine/SKILL.md
fetched_at: '2026-07-05T06:03:56.288548+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-05T07:26:42.727750Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6306738200 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6306738200 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-05T09:51:15.929803Z'
indexed_at: '2026-07-05T09:51:15.929810Z'
---
