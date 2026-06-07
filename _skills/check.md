---
id: check
slug: check
name: check — drift report
description: '- Zero writes. No SPEC.md edits. No code edits.'
prompt_preview: "---\nname: check\ndescription: |\n  Read-only drift detector. Diffs\
  \ SPEC.md against current code and reports\n  violations grouped by severity. Writes\
  \ nothing — suggests remedies via\n  the spec or build skills but never invokes\
  \ them. Triggers when the user\n  asks to check drift, audit the spec, verify invariants,\
  \ or ask whether\n  code still matches the spec. Phrasings: \"check drift\", \"\
  audit the spec\",\n  \"does the code still match §V\", \"check invariants\", \"\
  spec vs code\".\n---\n\n# check — drift report..."
full_prompt_length: 2467
tools_mentioned:
- go
category: community
category_display: Community
source_repo: JuliusBrussee/blueprint
source_path: skills/check/SKILL.md
source_url: https://github.com/JuliusBrussee/blueprint/blob/main/skills/check/SKILL.md
fetched_at: '2026-06-07T06:22:41.501149+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T06:34:10.028335Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc67c20 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc67c20 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:51.457063Z'
indexed_at: '2026-06-07T10:04:51.457068Z'
---
