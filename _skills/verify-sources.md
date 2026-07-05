---
id: verify-sources
slug: verify-sources
name: Source Verification Skill
description: '- **Never auto-verify** — this skill exists specifically for human review'
prompt_preview: "---\nname: verify-sources\ndescription: Captures human source verification\
  \ for tracks, timestamps it, and updates track files. Use when sources need human\
  \ review before generation.\nargument-hint: <album-name>\nmodel: sonnet\neffort:\
  \ low\nallowed-tools:\n  - Read\n  - Edit\n  - Glob\n  - Grep\n  - Bash\n  - bitwize-music-mcp\n\
  ---\n\n## Your Task\n\n**Input**: $ARGUMENTS (album name)\n\nGuide the user through\
  \ source verification for all tracks with pending sources in the specified album.\n\
  \n---\n\n# Source Verification..."
full_prompt_length: 5314
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/verify-sources/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/verify-sources/SKILL.md
fetched_at: '2026-07-05T06:03:44.621213+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-05T07:16:04.796285Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f63066e41d0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f63066e41d0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-05T09:51:15.705155Z'
indexed_at: '2026-07-05T09:51:15.705168Z'
---
