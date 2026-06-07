---
id: import-audio
slug: import-audio
name: Import Audio Skill
description: Use `resolve_path` with the appropriate `path_type` ("content", "audio",
  "documents") to get the right path.
prompt_preview: "---\nname: import-audio\ndescription: Moves audio files to the correct\
  \ album location with proper path structure. Use when the user has downloaded WAV\
  \ files from Suno or other sources that need to be organized.\nargument-hint: <file-path>\
  \ <album-name> [track-slug]\nmodel: haiku\nallowed-tools:\n  - Read\n  - Bash\n\
  \  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\nImport an\
  \ audio file (WAV, MP3, etc.) to the correct album location based on config.\n\n\
  ---\n\n# Import Audio Skill\n\nYou move audio..."
full_prompt_length: 6010
tools_mentioned:
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/import-audio/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/import-audio/SKILL.md
fetched_at: '2026-06-07T06:24:17.318774+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T07:29:11.981640Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f4500678e90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f4500678e90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:52.647569Z'
indexed_at: '2026-06-07T10:04:52.647575Z'
---
