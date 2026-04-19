---
id: circuit-breaker-pattern
slug: circuit-breaker-pattern
name: Circuit Breaker Pattern
description: Claude skill for Circuit Breaker Pattern
prompt_preview: "---\r\nname: circuit-breaker-pattern\r\ndescription: >\r\n  Implement\
  \ circuit breaker logic for agentic tool calls — tracking tool health,\r\n  transitioning\
  \ between closed/open/half-open states, reducing task scope when\r\n  tools fail,\
  \ routing to alternatives via capability maps, and enforcing failure\r\n  budgets\
  \ to prevent error accumulation. Separates orchestration (deciding what\r\n  to\
  \ attempt) from execution (calling tools), following the expeditor pattern.\r\n\
  \  Use when building agents that depend on m..."
full_prompt_length: 24323
tools_mentioned: []
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/circuit-breaker-pattern/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/circuit-breaker-pattern/SKILL.md
fetched_at: '2026-04-19T04:51:21.009967+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-19T06:26:09.859886Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7cf2bb90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7cf2bb90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-19T07:27:51.258904Z'
indexed_at: '2026-04-19T07:27:51.258909Z'
---
