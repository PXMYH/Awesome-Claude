---
id: lyric-reviewer
slug: lyric-reviewer
name: Lyric Reviewer
description: '**Your deliverable**: Verification report with applied pronunciation
  fixes, remaining issues, and warnings.'
prompt_preview: "---\nname: lyric-reviewer\ndescription: Reviews lyrics against a\
  \ quality checklist before Suno generation. Use before generating tracks to catch\
  \ rhyme, prosody, pronunciation, and structural issues.\nargument-hint: <track-path\
  \ | album-path | --fix>\nmodel: opus\neffort: max\nprerequisites:\n  - lyric-writer\n\
  \  - pronunciation-specialist\nallowed-tools:\n  - Read\n  - Edit\n  - Glob\n  -\
  \ Grep\n  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\n\
  ### Instrumental Guard\n\nWhen reviewing a track, **firs..."
full_prompt_length: 11089
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/lyric-reviewer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/lyric-reviewer/SKILL.md
fetched_at: '2026-07-12T05:31:56.816565+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-12T06:42:31.316609Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0063fdc890 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0063fdc890 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-12T09:23:54.359776Z'
indexed_at: '2026-07-12T09:23:54.359782Z'
---
