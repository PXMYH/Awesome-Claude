---
id: validate-album
slug: validate-album
name: Album Validator Agent
description: 1. **Use MCP tools first** - `get_config()`, `find_album()`, `validate_album_structure()`
  before manual checks
prompt_preview: "---\nname: validate-album\ndescription: Validates album directory\
  \ structure, file locations, and content integrity. Use before release or whenever\
  \ the user wants to check an album's structural health.\nargument-hint: <album-name>\n\
  model: claude-haiku-4-5-20251001\ncontext: fork\nallowed-tools:\n  - Read\n  - Bash\n\
  \  - Glob\n  - Grep\n  - bitwize-music-mcp\n---\n\n# Album Validator Agent\n\n##\
  \ Your Task\n\n**Input**: $ARGUMENTS (album name, e.g., `sample-album`)\n\nValidate\
  \ that an album has all required files in th..."
full_prompt_length: 7861
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/validate-album/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/validate-album/SKILL.md
fetched_at: '2026-04-05T04:36:45.471719+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:55:36.346816Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8844590 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8844590 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.455414Z'
indexed_at: '2026-04-05T08:29:58.455419Z'
---
