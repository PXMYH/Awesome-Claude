---
id: mastering-engineer
slug: mastering-engineer
name: Mastering Engineer Agent
description: '**Your deliverable**: Mastered WAV files at consistent loudness, optimized
  for streaming (with user preferences applied) → release-director handles release
  workflow.'
prompt_preview: "---\nname: mastering-engineer\ndescription: Guides audio mastering\
  \ for streaming platforms including loudness optimization and tonal balance. Use\
  \ when the user has approved tracks and wants to master audio files.\nargument-hint:\
  \ <folder-path or \"master for [platform]\">\nmodel: sonnet\neffort: low\nprerequisites:\n\
  \  - import-audio\nallowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n  -\
  \ Glob\n  - Bash\n  - bitwize-music-mcp\nrequirements:\n  python:\n    - matchering\n\
  \    - pyloudnorm\n    - scipy\n    - numpy..."
full_prompt_length: 14891
tools_mentioned:
- Python
- python
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/mastering-engineer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/mastering-engineer/SKILL.md
fetched_at: '2026-06-21T06:50:10.836758+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-21T07:55:22.075207Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9c94a40 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9c94a40 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-21T10:34:00.550109Z'
indexed_at: '2026-06-21T10:34:00.550119Z'
---
