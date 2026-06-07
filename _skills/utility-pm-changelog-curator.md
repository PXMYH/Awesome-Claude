---
id: utility-pm-changelog-curator
slug: utility-pm-changelog-curator
name: PM Changelog Curator (Dispatch Skill)
description: '- Canonical sub-agent definition: [`agents/pm-changelog-curator.md`](../../agents/pm-changelog-curator.md)'
prompt_preview: '---

  name: utility-pm-changelog-curator

  description: Draft CHANGELOG entries from git log via the pm-changelog-curator sub-agent.
  Dispatches natively on Claude Code with the pm-skills plugin (invokes @agent-pm-skills:pm-changelog-curator);
  on non-Claude clients (Codex CLI, Cursor, Windsurf, Copilot, Gemini CLI) reads agents/pm-changelog-curator.md
  and executes the system prompt inline. Applies CLAUDE.md hygiene rules (no internal-notes
  references, no em-dashes, no Claude attribution trailers, pub...'
full_prompt_length: 4641
tools_mentioned: []
category: community
category_display: Community
source_repo: product-on-purpose/pm-skills
source_path: skills/utility-pm-changelog-curator/SKILL.md
source_url: https://github.com/product-on-purpose/pm-skills/blob/main/skills/utility-pm-changelog-curator/SKILL.md
fetched_at: '2026-06-07T06:28:26.938807+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T09:42:24.846720Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc66e40 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc66e40 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:55.435898Z'
indexed_at: '2026-06-07T10:04:55.435903Z'
---
