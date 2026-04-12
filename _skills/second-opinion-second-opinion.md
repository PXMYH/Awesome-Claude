---
id: second-opinion-second-opinion
slug: second-opinion-second-opinion
name: Second Opinion
description: '**Large diff warning:**'
prompt_preview: "---\nname: second-opinion\ndescription: \"Runs external LLM code\
  \ reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs,\
  \ or specific commits. Use when the user asks for a second opinion, external review,\
  \ codex review, gemini review, or mentions /second-opinion.\"\nallowed-tools:\n\
  \  - Bash\n  - Read\n  - Glob\n  - Grep\n  - AskUserQuestion\n---\n\n# Second Opinion\n\
  \nShell out to external LLM CLIs for an independent code review powered by\na separate\
  \ model. Supports OpenAI Codex CLI and..."
full_prompt_length: 9917
tools_mentioned:
- go
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/second-opinion/skills/second-opinion/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/second-opinion/skills/second-opinion/SKILL.md
fetched_at: '2026-04-12T04:50:31.784343+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-12T07:15:27.631764Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f39934d5640 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f39934d5640 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-12T07:23:22.321049Z'
indexed_at: '2026-04-12T07:23:22.321055Z'
---
