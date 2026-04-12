---
id: suno-engineer
slug: suno-engineer
name: Suno Engineer Agent
description: Simple prompts + good lyrics + section tags + user preferences + targeted
  exclusions = best results.
prompt_preview: "---\nname: suno-engineer\ndescription: Constructs technical Suno\
  \ V5 style prompts, selects genres, and optimizes generation settings. Use when\
  \ creating or refining Suno prompts for track generation.\nargument-hint: <track-file-path\
  \ or \"create prompt for [concept]\">\nmodel: claude-opus-4-6\nprerequisites:\n\
  \  - lyric-writer\nallowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n  -\
  \ Glob\n  - Bash\n  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\
  \nWhen invoked with a track file:\n1. Read the trac..."
full_prompt_length: 12122
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/suno-engineer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/suno-engineer/SKILL.md
fetched_at: '2026-04-12T04:47:35.337179+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-12T05:44:54.027680Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f3993443650 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f3993443650 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-12T07:23:20.314257Z'
indexed_at: '2026-04-12T07:23:20.314263Z'
---
