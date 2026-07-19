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
  polish for [genre]\">\nmodel: sonnet\neffort: low\nprerequisites:\n  - import-audio\n\
  allowed-tools:\n  - Read\n  - Edit\n  - Write..."
full_prompt_length: 13359
tools_mentioned:
- rest
- python
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/mix-engineer/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/mix-engineer/SKILL.md
fetched_at: '2026-07-19T05:20:49.454156+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T06:30:13.591556Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff210470800 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff210470800 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:18.205456Z'
indexed_at: '2026-07-19T09:13:18.205461Z'
---
