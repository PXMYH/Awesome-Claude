---
id: tutorial
slug: tutorial
name: Interactive Tutorial Agent
description: '- **Preserve exact casing** - If user says "bitwize", use "bitwize"
  not "Bitwize"'
prompt_preview: "---\nname: tutorial\ndescription: Provides interactive guided album\
  \ creation for new users. Use when the user is new to the plugin or asks for a walkthrough\
  \ of the album creation process.\nargument-hint: <new-album | resume | help>\nmodel:\
  \ claude-sonnet-4-6\nallowed-tools:\n  - Read\n  - Write\n  - Edit\n  - Glob\n \
  \ - Grep\n  - Bash\n  - AskUserQuestion\n  - bitwize-music-mcp\n---\n\n## Your Task\n\
  \n**Input**: $ARGUMENTS\n\nRoute based on argument:\n- `new-album` or no argument\
  \ → Start guided album creation\n- `resum..."
full_prompt_length: 9355
tools_mentioned:
- go
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/tutorial/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/tutorial/SKILL.md
fetched_at: '2026-04-05T04:36:45.350460+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:55:28.247986Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8909520 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8909520 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.452600Z'
indexed_at: '2026-04-05T08:29:58.452610Z'
---
