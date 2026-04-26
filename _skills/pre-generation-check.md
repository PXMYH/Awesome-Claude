---
id: pre-generation-check
slug: pre-generation-check
name: Pre-Generation Checkpoint
description: '**Your deliverable**: Pass/fail report with album-level verdict.'
prompt_preview: "---\nname: pre-generation-check\ndescription: Validates all pre-generation\
  \ gates before sending tracks to Suno. Checks sources verified, lyrics reviewed,\
  \ pronunciation resolved, explicit flag set, style prompt complete, and artist names\
  \ cleared. Use before generating tracks on Suno or when the user says \"pre-gen\
  \ check\" or \"ready to generate\".\nargument-hint: <album-name or track-path>\n\
  model: claude-haiku-4-5-20251001\nprerequisites:\n  - lyric-writer\n  - lyric-reviewer\n\
  \  - pronunciation-specialist\nal..."
full_prompt_length: 7193
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/pre-generation-check/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/pre-generation-check/SKILL.md
fetched_at: '2026-04-26T04:58:53.543167+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-26T05:58:32.083170Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe1176b290 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe1176b290 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-26T07:41:25.595730Z'
indexed_at: '2026-04-26T07:41:25.595736Z'
---
