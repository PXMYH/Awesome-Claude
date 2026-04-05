---
id: trailmark-trailmark-structural
slug: trailmark-trailmark-structural
name: Trailmark Structural Analysis
description: Some passes may produce no data for some codebases (this is
prompt_preview: "---\nname: trailmark-structural\ndescription: \"Runs full trailmark\
  \ structural analysis with all pre-analysis passes (blast radius, taint propagation,\
  \ privilege boundaries, complexity hotspots). Use when vivisect needs detailed structural\
  \ data for a target. Triggers: structural analysis, blast radius, taint analysis,\
  \ complexity hotspots.\"\nallowed-tools:\n  - Bash\n  - Read\n  - Grep\n  - Glob\n\
  ---\n\n# Trailmark Structural Analysis\n\nRuns `trailmark analyze` with all four\
  \ pre-analysis passes.\n\n## When to U..."
full_prompt_length: 3904
tools_mentioned:
- go
- typescript
- php
- java
- javascript
- ruby
- rust
- Python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/trailmark/skills/trailmark-structural/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/trailmark/skills/trailmark-structural/SKILL.md
fetched_at: '2026-04-05T04:38:37.547384+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T08:20:17.081489Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8562c00 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8562c00 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:30:00.420682Z'
indexed_at: '2026-04-05T08:30:00.420688Z'
---
