---
id: test-x402-payment-client
slug: test-x402-payment-client
name: Test an x402 Payment Client
description: '- `test-a2a-interop` — protocol-conformance testing for A2A agents;
  same'
prompt_preview: "---\nname: test-x402-payment-client\ndescription: >\n  Test an x402\
  \ payment client end to end against a live endpoint: drive the\n  full 402 -> PAYMENT-REQUIRED\
  \ -> sign -> PAYMENT-SIGNATURE -> verify/settle\n  loop, confirm settlement on chain,\
  \ and check any signed offers or receipts\n  for conformance. Use when validating\
  \ a new x402 client or SDK before\n  shipping, debugging a payment that never completes\
  \ despite a well-formed\n  402, running x402 conformance in CI against a testnet\
  \ facilitator, or..."
full_prompt_length: 21704
tools_mentioned:
- rest
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/test-x402-payment-client/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/test-x402-payment-client/SKILL.md
fetched_at: '2026-10-25T07:19:54.369260+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:13:12.009866Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1d7f0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1d7f0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:08.424427Z'
indexed_at: '2026-10-25T12:12:08.424431Z'
---
