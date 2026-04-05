---
id: lyric-writer
slug: lyric-writer
name: Lyric Writer Agent
description: '**Your deliverable**: Polished lyrics with proper prosody, clear pronunciation,
  factual accuracy (if documentary), and completed Suno style prompt (via auto-invoked
  suno-engineer).'
prompt_preview: "---\nname: lyric-writer\ndescription: Writes or reviews lyrics with\
  \ professional prosody, rhyme craft, and quality checks. Use when writing new lyrics,\
  \ revising existing lyrics, or when the user says 'let's work on a track.'\nargument-hint:\
  \ <track-file-path or \"write lyrics for [concept]\">\nmodel: claude-opus-4-6\n\
  allowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n  - Glob\n  - bitwize-music-mcp\n\
  ---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\n### Instrumental Guard\n\nWhen invoked\
  \ with a track file path, **f..."
full_prompt_length: 23268
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/lyric-writer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/lyric-writer/SKILL.md
fetched_at: '2026-04-05T04:36:41.534225+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:51:07.026173Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac86d9490 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac86d9490 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.363465Z'
indexed_at: '2026-04-05T08:29:58.363470Z'
---
