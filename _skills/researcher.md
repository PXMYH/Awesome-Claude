---
id: researcher
slug: researcher
name: Investigative Research Agent
description: 1. **Load override first** - Call `load_override("research-preferences.md")`
  at invocation
prompt_preview: "---\nname: researcher\ndescription: Conducts investigative-grade\
  \ research with primary source analysis, cross-verification, and trial-level depth.\
  \ Use when an album needs factual research, source material, or verification of\
  \ claims.\nargument-hint: <\"research [topic]\" or track-path to verify>\nmodel:\
  \ claude-sonnet-4-6\nprerequisites:\n  - album-conceptualizer\nallowed-tools:\n\
  \  - Read\n  - Edit\n  - Write\n  - Grep\n  - Glob\n  - WebFetch\n  - WebSearch\n\
  \  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $ARG..."
full_prompt_length: 10979
tools_mentioned:
- Go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/researcher/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/researcher/SKILL.md
fetched_at: '2026-04-05T04:36:43.024565+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:52:53.785935Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac86da450 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac86da450 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.399762Z'
indexed_at: '2026-04-05T08:29:58.399767Z'
---
