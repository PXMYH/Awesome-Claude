---
id: llms-txt-checker
slug: llms-txt-checker
name: LLMs.txt Checker Skill
description: '- **Mintlify** auto-generates both `llms.txt` and `llms-full.txt` for
  all projects, and adds HTTP headers (`Link: </llms.txt>; rel="llms-txt"`) for discovery'
prompt_preview: "---\nname: llms-txt-checker\ndescription: >\n  Audits any domain's\
  \ AI-readiness by using curl to directly probe robots.txt, llms.txt, and\n  llms-full.txt,\
  \ then scores each file against a structured checklist and delivers a formatted\n\
  \  report with pass/warn/fail findings and actionable fixes.\n  Use this skill whenever\
  \ a user provides a domain or URL and wants to know if llms.txt or llms-full.txt\
  \ is\n  available, discoverable, or properly structured. Trigger on phrases like\
  \ \"check llms.txt for\",\n  \"do..."
full_prompt_length: 9549
tools_mentioned: []
category: community
category_display: Community
source_repo: Infrasity-Labs/dev-gtm-claude-skills
source_path: skills/llms-txt-checker/SKILL.md
source_url: https://github.com/Infrasity-Labs/dev-gtm-claude-skills/blob/main/skills/llms-txt-checker/SKILL.md
fetched_at: '2026-06-14T06:38:06.066066+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T06:46:23.159209Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a5761e0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a5761e0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:24.424611Z'
indexed_at: '2026-06-14T10:18:24.424616Z'
---
