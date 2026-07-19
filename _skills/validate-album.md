---
id: validate-album
slug: validate-album
name: Album Validator Agent
description: 1. **Use MCP tools first** - `get_config()`, `find_album()`, `validate_album_structure()`
  before manual checks
prompt_preview: "---\nname: validate-album\ndescription: Validates album directory\
  \ structure, file locations, and content integrity. Use before release or whenever\
  \ the user wants to check an album's structural health.\nargument-hint: <album-name>\n\
  model: haiku\ncontext: fork\nallowed-tools:\n  - Read\n  - Bash\n  - Glob\n  - Grep\n\
  \  - bitwize-music-mcp\n---\n\n# Album Validator Agent\n\n## Your Task\n\n**Input**:\
  \ $ARGUMENTS (album name, e.g., `sample-album`)\n\nValidate that an album has all\
  \ required files in the correct locations,..."
full_prompt_length: 7841
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/validate-album/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/validate-album/SKILL.md
fetched_at: '2026-07-19T05:20:53.138683+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T06:34:19.380837Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff21018ba70 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff21018ba70 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:18.297520Z'
indexed_at: '2026-07-19T09:13:18.297525Z'
---
