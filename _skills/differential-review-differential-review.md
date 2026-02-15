---
id: differential-review-differential-review
slug: differential-review-differential-review
name: Differential Security Review
description: '**For experienced users:** Use this page''s Quick Reference and Decision
  Tree to navigate directly to needed content.'
prompt_preview: "---\nname: differential-review\ndescription: >\n  Performs security-focused\
  \ differential review of code changes (PRs, commits, diffs).\n  Adapts analysis\
  \ depth to codebase size, uses git history for context, calculates\n  blast radius,\
  \ checks test coverage, and generates comprehensive markdown reports.\n  Automatically\
  \ detects and prevents security regressions.\nallowed-tools:\n  - Read\n  - Write\n\
  \  - Grep\n  - Glob\n  - Bash\n---\n\n# Differential Security Review\n\nSecurity-focused\
  \ code review for PRs, commit..."
full_prompt_length: 6504
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/differential-review/skills/differential-review/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/differential-review/skills/differential-review/SKILL.md
fetched_at: '2026-02-15T04:22:27.158485+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:22:42.420371Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt demonstrates excellent structure with clear sections, rationalizations,
      and decision trees. It follows strong prompt engineering practices with explicit
      workflows and quality checklists. However, it references external documentation
      files (methodology.md, adversarial.md, etc.) that aren't provided, creating
      ambiguity about execution paths.
  usefulness:
    score: 4.0
    reasoning: The skill addresses a critical real-world need for systematic security
      reviews of code changes with adaptive strategies based on codebase size. The
      risk-first approach and comprehensive reporting framework provide practical
      value. However, the dependency on missing external documentation limits immediate
      usability, and the workflow assumes specific tool capabilities that may not
      be universally available.
  overall_rating: 4.25
  summary: A well-structured security review prompt with strong methodology and risk-focused
    principles, but hampered by missing referenced documentation and unclear tool
    integration requirements.
  tags_suggested:
  - security
  - code-review
  - risk-assessment
  - differential-analysis
  - reporting
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:51.443648Z'
indexed_at: '2026-02-15T04:33:51.443654Z'
---
