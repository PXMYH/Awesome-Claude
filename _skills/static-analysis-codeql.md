---
id: static-analysis-codeql
slug: static-analysis-codeql
name: CodeQL Analysis
description: '- [ ] Output directory resolved (user-specified or auto-incremented
  default)'
prompt_preview: "---\nname: codeql\ndescription: >-\n  Scans a codebase for security\
  \ vulnerabilities using CodeQL's interprocedural data flow and\n  taint tracking\
  \ analysis. Triggers on \"run codeql\", \"codeql scan\", \"codeql analysis\", \"\
  build\n  codeql database\", or \"find vulnerabilities with codeql\". Supports \"\
  run all\" (security-and-quality\n  + security-experimental suites) and \"important\
  \ only\" (high-precision security findings) scan\n  modes. Also handles creating\
  \ data extension models and processing CodeQL SARIF outp..."
full_prompt_length: 15475
tools_mentioned:
- go
- Django
- JavaScript
- TypeScript
- Ruby
- Python
- Go
- python
- Java
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/static-analysis/skills/codeql/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/codeql/SKILL.md
fetched_at: '2026-06-07T06:29:07.249192+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T09:57:41.717756Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffb0fda0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffb0fda0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:55.756801Z'
indexed_at: '2026-06-07T10:04:55.756807Z'
---
