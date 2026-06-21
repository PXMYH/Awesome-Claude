---
id: trailmark-audit-augmentation
slug: trailmark-audit-augmentation
name: Audit Augmentation
description: '- **[references/formats.md](references/formats.md)** — SARIF 2.1.0 and'
prompt_preview: "---\nname: audit-augmentation\ndescription: >\n  Augments Trailmark\
  \ code graphs with external audit findings from SARIF static\n  analysis results\
  \ and weAudit annotation files. Maps findings to graph nodes by\n  file and line\
  \ overlap, creates severity-based subgraphs, and enables\n  cross-referencing findings\
  \ with pre-analysis data (blast radius, taint, etc.).\n  Use when projecting SARIF\
  \ results onto a code graph, overlaying weAudit\n  annotations, cross-referencing\
  \ Semgrep or CodeQL findings with call..."
full_prompt_length: 6821
tools_mentioned:
- rust
- python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/trailmark/skills/audit-augmentation/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/trailmark/skills/audit-augmentation/SKILL.md
fetched_at: '2026-06-21T06:53:14.562447+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-21T10:29:13.827775Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9c94b30 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9c94b30 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-21T10:34:03.792126Z'
indexed_at: '2026-06-21T10:34:03.792131Z'
---
