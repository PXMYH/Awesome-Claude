---
id: explicit-checker
slug: explicit-checker
name: Explicit Content Checker
description: '- Case-insensitive matching (Fuck = fuck = FUCK)'
prompt_preview: "---\nname: explicit-checker\ndescription: Scans lyrics for explicit\
  \ content and verifies that explicit flags match actual content. Use before Suno\
  \ generation or release to ensure accurate content ratings.\nargument-hint: <album-path\
  \ or track-path>\nmodel: claude-sonnet-4-6\nallowed-tools:\n  - Read\n  - Glob\n\
  \  - Grep\n  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Path to scan**: $ARGUMENTS\n\
  \n1. Scan all lyrics for explicit words\n2. Report findings with word counts per\
  \ track\n3. Flag mismatches (explicit cont..."
full_prompt_length: 5157
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/explicit-checker/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/explicit-checker/SKILL.md
fetched_at: '2026-04-26T04:58:51.429800+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-26T05:56:38.771588Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe11ac32c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe11ac32c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-26T07:41:25.554783Z'
indexed_at: '2026-04-26T07:41:25.554788Z'
---
