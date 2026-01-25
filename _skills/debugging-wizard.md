---
id: debugging-wizard
slug: debugging-wizard
name: Debugging Wizard
description: '- **Test Master** - Writing regression tests'
prompt_preview: "---\nname: debugging-wizard\ndescription: Use when investigating\
  \ errors, analyzing stack traces, or finding root causes of unexpected behavior.\
  \ Invoke for error investigation, troubleshooting, log analysis, root cause analysis.\n\
  triggers:\n  - debug\n  - error\n  - bug\n  - exception\n  - traceback\n  - stack\
  \ trace\n  - troubleshoot\n  - not working\n  - crash\n  - fix issue\nrole: specialist\n\
  scope: analysis\noutput-format: analysis\n---\n\n# Debugging Wizard\n\nExpert debugger\
  \ applying systematic methodology to is..."
full_prompt_length: 3128
tools_mentioned: []
category: community
category_display: Community
source_repo: jeffallan/claude-skills
source_path: skills/debugging-wizard/SKILL.md
source_url: https://github.com/jeffallan/claude-skills/blob/main/skills/debugging-wizard/SKILL.md
fetched_at: '2026-01-25T03:52:19.318278+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:57:46.315668Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear role definition,
      specific workflow steps, and explicit constraints. It follows best practices
      by defining triggers, scope, and output format upfront. The only minor weakness
      is the reference system which relies on external files that may not exist in
      all contexts.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate practical value for developers debugging
      real issues. The systematic workflow (reproduce, isolate, hypothesize, test,
      fix, prevent) mirrors professional debugging practices. The output templates
      ensure actionable results, and the constraints prevent common debugging pitfalls.
  overall_rating: 4.75
  summary: An excellent debugging prompt that balances comprehensive methodology with
    practical constraints, making it highly effective for real-world troubleshooting
    scenarios.
  tags_suggested:
  - debugging
  - troubleshooting
  - root-cause-analysis
  - systematic-methodology
  - developer-tools
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:52.858742Z'
indexed_at: '2026-01-25T04:05:52.858748Z'
---
