---
id: buyer-eval-skill
slug: buyer-eval-skill
name: Detect skill directory
description: If a system administrator has set `BUYER_EVAL_NO_TELEMETRY=1` or deployed
  `/etc/salespeak/buyer-eval.json` with `{"locked":true,"consent":false}`, `TELEMETRY_STATE`
  will be `locked_off` and no consent...
prompt_preview: "---\nname: buyer-eval\nversion: 3.5.0\ndescription: |\n  Structured\
  \ B2B software vendor evaluation for buyers. Researches your company,\n  asks domain-expert\
  \ questions, engages vendor AI agents via the Salespeak Frontdoor\n  API, scores\
  \ vendors across 7 dimensions, and produces a comparative recommendation\n  with\
  \ evidence transparency. Use when asked to evaluate, compare, or research B2B\n\
  \  software vendors.\nallowed-tools:\n  - Bash\n  - Read\n  - Write\n  - WebSearch\n\
  \  - WebFetch\n  - AskUserQuestion\n---..."
full_prompt_length: 11818
tools_mentioned:
- go
- Python
category: community
category_display: Community
source_repo: salespeak-ai/buyer-eval-skill
source_path: SKILL.md
source_url: https://github.com/salespeak-ai/buyer-eval-skill/blob/main/SKILL.md
fetched_at: '2026-06-14T06:42:01.065129+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T09:59:11.506320Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187af975c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187af975c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:27.574283Z'
indexed_at: '2026-06-14T10:18:27.574289Z'
---
