---
id: verify-sources
slug: verify-sources
name: Source Verification Skill
description: '- **Never auto-verify** — this skill exists specifically for human review'
prompt_preview: "---\nname: verify-sources\ndescription: Captures human source verification\
  \ for tracks, timestamps it, and updates track files. Use when sources need human\
  \ review before generation.\nargument-hint: <album-name>\nmodel: claude-sonnet-4-6\n\
  allowed-tools:\n  - Read\n  - Edit\n  - Glob\n  - Grep\n  - Bash\n  - bitwize-music-mcp\n\
  ---\n\n## Your Task\n\n**Input**: $ARGUMENTS (album name)\n\nGuide the user through\
  \ source verification for all tracks with pending sources in the specified album.\n\
  \n---\n\n# Source Verification..."
full_prompt_length: 5313
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/verify-sources/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/verify-sources/SKILL.md
fetched_at: '2026-04-26T04:58:57.774576+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-26T06:02:12.944958Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe112219d0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe112219d0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-26T07:41:25.675554Z'
indexed_at: '2026-04-26T07:41:25.675560Z'
---
