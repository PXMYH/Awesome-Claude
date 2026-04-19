---
id: import-art
slug: import-art
name: Import Art Skill
description: '**Why it matters:** Audio directory might not exist yet, especially
  for new albums.'
prompt_preview: "---\nname: import-art\ndescription: Places album art files in the\
  \ correct audio and content directory locations. Use when the user has generated\
  \ or downloaded album artwork that needs to be saved.\nargument-hint: <file-path>\
  \ <album-name>\nmodel: claude-haiku-4-5-20251001\nallowed-tools:\n  - Read\n  -\
  \ Bash\n  - Glob\n  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\
  \nImport album art to both the audio folder and album content folder.\n\n---\n\n\
  # Import Art Skill\n\nYou copy album art to both requi..."
full_prompt_length: 5541
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/import-art/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/import-art/SKILL.md
fetched_at: '2026-04-19T04:50:17.011661+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-19T05:42:25.041629Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0a3c20 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0a3c20 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-19T07:27:50.300844Z'
indexed_at: '2026-04-19T07:27:50.300849Z'
---
