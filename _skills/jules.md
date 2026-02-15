---
id: jules
slug: jules
name: Jules Task Delegation
description: '- **No CLI reply** → Use web UI for Jules questions'
prompt_preview: '---

  name: jules

  description: "Delegate coding tasks to Google Jules AI agent for asynchronous execution.
  Use when user says: ''have Jules fix'', ''delegate to Jules'', ''send to Jules'',
  ''ask Jules to'', ''check Jules sessions'', ''pull Jules results'', ''jules add
  tests'', ''jules add docs'', ''jules review pr''. Handles: bug fixes, documentation,
  features, tests, refactoring, code reviews. Works with GitHub repos, creates PRs."

  ---


  # Jules Task Delegation


  Delegate coding tasks to Google''s Jules AI agent on G...'
full_prompt_length: 5388
tools_mentioned:
- TypeScript
- React
- go
- Go
- java
- Python
- FastAPI
category: community
category_display: Community
source_repo: sanjay3290/ai-skills
source_path: skills/jules/SKILL.md
source_url: https://github.com/sanjay3290/ai-skills/blob/main/skills/jules/SKILL.md
fetched_at: '2026-02-15T04:22:20.370691+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:04:56.118731Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections for
      setup, commands, and templates. It provides specific CLI commands, handles edge
      cases like missing repos or authentication, and includes smart context injection
      for better results. The only minor weakness is the incomplete 'Poll Until Complete'
      section at the end, which cuts off mid-command.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate, practical value for developers using
      Google's Jules AI agent. It covers the full workflow from setup to task creation,
      monitoring, and integration with GitHub workflows. The inclusion of common task
      templates (tests, docs, lint fixes, PR reviews) and Git integration commands
      makes it highly actionable for real development scenarios.
  overall_rating: 4.75
  summary: An excellent, production-ready skill that comprehensively covers Jules
    AI agent delegation with clear setup instructions, practical command templates,
    and seamless GitHub integration, though it has a minor incomplete section at the
    end.
  tags_suggested:
  - automation
  - github
  - ai-assisted
  - code-review
  - testing
  - documentation
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:51.367468Z'
indexed_at: '2026-02-15T04:33:51.367474Z'
---
