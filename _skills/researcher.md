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
  \ sonnet\neffort: high\nprerequisites:\n  - album-conceptualizer\nallowed-tools:\n\
  \  - Read\n  - Edit\n  - Write\n  - Grep\n  - Glob\n  - WebFetch\n  - WebSearch\n\
  \  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $A..."
full_prompt_length: 10981
tools_mentioned:
- Go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/researcher/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/researcher/SKILL.md
fetched_at: '2026-06-28T06:16:43.761120+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T07:25:42.046120Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a262daf0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a262daf0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:26.546864Z'
indexed_at: '2026-06-28T10:04:26.546870Z'
---
