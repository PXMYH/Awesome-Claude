---
id: lyric-refiner
slug: lyric-refiner
name: Lyric Refiner Agent
description: 1. **Load override first** — Call `load_override("lyric-writing-guide.md")`
  at invocation
prompt_preview: "---\nname: lyric-refiner\ndescription: Autonomous multi-pass lyric\
  \ refinement for tightening, cohesion, and album unity. Use after lyrics are written\
  \ to polish a track or entire album through iterative passes.\nargument-hint: <album-name\
  \ | track-path> [--passes N]\nmodel: opus\neffort: max\nprerequisites:\n  - lyric-writer\n\
  allowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n  - Glob\n  - bitwize-music-mcp\n\
  ---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\n### Parse Arguments\n\n1. **Identify\
  \ target scope**:\n   - I..."
full_prompt_length: 15002
tools_mentioned:
- go
- rest
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/lyric-refiner/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/lyric-refiner/SKILL.md
fetched_at: '2026-06-28T06:16:41.815944+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T07:23:31.571408Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a27d60c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a27d60c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:26.499067Z'
indexed_at: '2026-06-28T10:04:26.499073Z'
---
