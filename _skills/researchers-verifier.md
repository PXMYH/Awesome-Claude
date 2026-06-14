---
id: researchers-verifier
slug: researchers-verifier
name: Research Verifier
description: '**Your deliverable**: Verification report with clear status (ready/needs
  fixes), categorized issues, and actionable recommendations.'
prompt_preview: "---\nname: researchers-verifier\ndescription: Performs quality control,\
  \ citation validation, and fact-checking before human review. Use after research\
  \ is complete to verify all sources and claims before production.\nargument-hint:\
  \ <\"research [topic]\" or track-path to verify>\nmodel: opus\neffort: high\nuser-invocable:\
  \ false\ncontext: fork\nallowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n\
  \  - Glob\n  - WebFetch\n  - WebSearch\n---\n\n## Your Task\n\n**Research topic**:\
  \ $ARGUMENTS\n\nWhen invoked:\n1. Verify all..."
full_prompt_length: 5914
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/researchers-verifier/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/researchers-verifier/SKILL.md
fetched_at: '2026-06-14T06:39:15.818346+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T07:46:34.604587Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a0c7b90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a0c7b90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:25.415034Z'
indexed_at: '2026-06-14T10:18:25.415039Z'
---
