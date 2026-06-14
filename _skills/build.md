---
id: build
slug: build
name: build — implement spec
description: '- No sub-agents. No parallel workers. Main thread only.'
prompt_preview: "---\nname: build\ndescription: |\n  Plan-then-execute implementation\
  \ against SPEC.md. Native single-thread\n  loop, no sub-agents. On test or build\
  \ failure, auto-invokes the backprop\n  skill before retrying — a failed verification\
  \ always considers whether\n  a new §V invariant would prevent recurrence. Triggers\
  \ when the user asks\n  to build, implement, execute the spec, or tackle a specific\
  \ §T task\n  (`build §T.3`, `build --next`, `implement next task`, `run the build`).\n\
  \  Expects SPEC.md to exist; i..."
full_prompt_length: 2499
tools_mentioned: []
category: community
category_display: Community
source_repo: JuliusBrussee/blueprint
source_path: skills/build/SKILL.md
source_url: https://github.com/JuliusBrussee/blueprint/blob/main/skills/build/SKILL.md
fetched_at: '2026-06-14T06:38:07.403304+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T06:47:03.677111Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a0837d0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a0837d0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:24.436011Z'
indexed_at: '2026-06-14T10:18:24.436015Z'
---
