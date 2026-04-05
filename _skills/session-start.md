---
id: session-start
slug: session-start
name: Session Start Skill
description: 1. **Don't skip steps** — Each step matters for session integrity
prompt_preview: "---\nname: session-start\ndescription: Runs the session startup procedure\
  \ - verifies setup, loads config and state, checks skill models, and reports project\
  \ status. Use at the beginning of a fresh session.\nmodel: claude-sonnet-4-6\nallowed-tools:\n\
  \  - Read\n  - Bash\n  - Glob\n  - Grep\n  - WebSearch\n  - WebFetch\n  - bitwize-music-mcp\n\
  ---\n\n## Your Task\n\nRun the full session start procedure and report project status\
  \ to the user.\n\n---\n\n# Session Start Skill\n\nYou perform the 8-step session\
  \ startup procedur..."
full_prompt_length: 5284
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/session-start/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/session-start/SKILL.md
fetched_at: '2026-04-05T04:36:44.520525+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:54:31.216205Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac85615e0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac85615e0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.433327Z'
indexed_at: '2026-04-05T08:29:58.433332Z'
---
