---
id: new-album
slug: new-album
name: New Album Skill
description: '```bash'
prompt_preview: "---\nname: new-album\ndescription: Creates a new album with the correct\
  \ directory structure and templates. Use IMMEDIATELY when the user says 'make a\
  \ new album' or similar, before any discussion.\nargument-hint: <album-name> <genre>\n\
  model: haiku\nallowed-tools:\n  - Read\n  - Bash\n  - Write\n  - bitwize-music-mcp\n\
  ---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\nCreate a new album directory structure\
  \ with all required files and templates.\n\n---\n\n# New Album Skill\n\nYou create\
  \ the complete album directory structu..."
full_prompt_length: 6008
tools_mentioned:
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/new-album/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/new-album/SKILL.md
fetched_at: '2026-06-07T06:24:18.644763+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T07:30:08.874059Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffcc2c90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffcc2c90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:52.668382Z'
indexed_at: '2026-06-07T10:04:52.668388Z'
---
