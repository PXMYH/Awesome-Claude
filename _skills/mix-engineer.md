---
id: mix-engineer
slug: mix-engineer
name: Mix Engineer Agent
description: 1. **Stems first** — always prefer per-stem processing when stems are
  available
prompt_preview: "---\nname: mix-engineer\ndescription: Polishes raw Suno audio by\
  \ processing per-stem WAVs (vocals, backing_vocals, drums, bass, guitar, keyboard,\
  \ strings, brass, woodwinds, percussion, synth, other) with targeted cleanup, EQ,\
  \ and compression, then remixing into a polished stereo WAV ready for mastering.\
  \ Use after audio import and before mastering.\nargument-hint: <album-name or \"\
  polish for [genre]\">\nmodel: claude-sonnet-4-6\nprerequisites:\n  - import-audio\n\
  allowed-tools:\n  - Read\n  - Edit\n  - Write..."
full_prompt_length: 13028
tools_mentioned:
- python
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/mix-engineer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/mix-engineer/SKILL.md
fetched_at: '2026-05-03T05:31:04.242118+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-03T06:32:11.462206Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f8c650 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f8c650 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-03T08:17:30.545366Z'
indexed_at: '2026-05-03T08:17:30.545372Z'
---
