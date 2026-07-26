---
id: album-conceptualizer
slug: album-conceptualizer
name: Album Conceptualizer Agent
description: '**When in doubt, cut.** Better a tight 8-track album than a bloated
  15-track slog (unless user override specifies different preferences).'
prompt_preview: "---\nname: album-conceptualizer\ndescription: Designs album concepts,\
  \ tracklist architecture, and thematic planning through 7 structured phases. Use\
  \ when planning a new album or reworking an existing album concept.\nargument-hint:\
  \ <\"plan album about [topic]\" or album-path>\nmodel: opus\neffort: max\nprerequisites:\n\
  \  - new-album\nallowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n  - Glob\n\
  \  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\nWhen invoked\
  \ for new album:\n1. Ask clarifying quest..."
full_prompt_length: 14247
tools_mentioned:
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/album-conceptualizer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/album-conceptualizer/SKILL.md
fetched_at: '2026-07-26T05:31:38.411061+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-26T06:38:43.557137Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1607eaef60 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1607eaef60 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-26T09:24:28.652343Z'
indexed_at: '2026-07-26T09:24:28.652349Z'
---
