---
id: configure
slug: configure
name: Plugin Configuration Skill
description: '- **Preserve exact casing** - If user says "bitwize", write "bitwize"
  not "Bitwize"'
prompt_preview: "---\nname: configure\ndescription: Sets up or edits the plugin configuration\
  \ file interactively. Use on first-time setup, when config is missing, or when the\
  \ user wants to change settings.\nargument-hint: [setup | edit | show | validate\
  \ | reset]\nmodel: claude-sonnet-4-6\nallowed-tools:\n  - Read\n  - Write\n  - Bash\n\
  \  - AskUserQuestion\n  - Glob\n---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\n\
  Route based on argument:\n- `setup` or no argument → Interactive first-time setup\n\
  - `edit` → Edit specific settings\n- `..."
full_prompt_length: 8853
tools_mentioned:
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/configure/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/configure/SKILL.md
fetched_at: '2026-04-05T04:36:40.443218+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:49:54.192556Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac86dbe00 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac86dbe00 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.338418Z'
indexed_at: '2026-04-05T08:29:58.338423Z'
---
