---
id: album-conceptualizer
slug: album-conceptualizer
name: Album Conceptualizer Agent
description: '**When in doubt, cut.** Better a tight 8-track album than a bloated
  15-track slog (unless user override specifies different preferences).'
prompt_preview: "---\nname: album-conceptualizer\ndescription: Designs album concepts,\
  \ tracklist architecture, and thematic planning through 7 structured phases. Use\
  \ when planning a new album or reworking an existing album concept.\nargument-hint:\
  \ <\"plan album about [topic]\" or album-path>\nmodel: claude-opus-4-6\nprerequisites:\n\
  \  - new-album\nallowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n  - Glob\n\
  \  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\nWhen invoked\
  \ for new album:\n1. Ask clarifying questi..."
full_prompt_length: 13019
tools_mentioned:
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/album-conceptualizer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/album-conceptualizer/SKILL.md
fetched_at: '2026-05-03T05:31:00.813191+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-03T06:29:51.014769Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f2c650 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f2c650 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-03T08:17:30.497566Z'
indexed_at: '2026-05-03T08:17:30.497572Z'
---
