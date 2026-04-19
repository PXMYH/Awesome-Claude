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
  \ <folder-path or \"master for [platform]\">\nmodel: claude-sonnet-4-6\nprerequisites:\n\
  \  - import-audio\nallowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n  -\
  \ Glob\n  - Bash\n  - bitwize-music-mcp\nrequirements:\n  python:\n    - matchering\n\
  \    - pyloudnorm\n    - scipy\n    - numpy..."
full_prompt_length: 11547
tools_mentioned:
- Python
- python
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/mastering-engineer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/mastering-engineer/SKILL.md
fetched_at: '2026-04-19T04:50:17.904884+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-19T05:43:13.776550Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0ff080 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0ff080 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-19T07:27:50.318952Z'
indexed_at: '2026-04-19T07:27:50.318958Z'
---
