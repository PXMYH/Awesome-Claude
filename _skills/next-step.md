---
id: next-step
slug: next-step
name: Next Step Advisor
description: 1. **One clear recommendation** — Don't list 5 options. Pick the best
  one.
prompt_preview: "---\nname: next-step\ndescription: Analyzes album state and recommends\
  \ the optimal next action. Use when the user asks \"what should I do next?\" or\
  \ \"what's left to do?\"\nargument-hint: [album-name]\nmodel: haiku\nprerequisites:\n\
  \  - resume\nallowed-tools:\n  - Read\n  - Glob\n  - Grep\n  - bitwize-music-mcp\n\
  ---\n\n## Your Task\n\n**Input**: $ARGUMENTS (optional album name)\n\nAnalyze current\
  \ project state and recommend the single best next action.\n\n---\n\n# Next Step\
  \ Advisor\n\nYou analyze the current state of albums..."
full_prompt_length: 6520
tools_mentioned:
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/next-step/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/next-step/SKILL.md
fetched_at: '2026-06-14T06:39:13.414147+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T07:43:52.071827Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a0c6bd0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a0c6bd0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:25.370863Z'
indexed_at: '2026-06-14T10:18:25.370868Z'
---
