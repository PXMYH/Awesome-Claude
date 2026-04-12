---
id: setup
slug: setup
name: Setup Assistant
description: '- **Be specific** - show exact commands for their environment'
prompt_preview: "---\nname: setup\ndescription: Detects your Python environment and\
  \ guides you through installing plugin dependencies. Use on first-time setup or\
  \ when MCP server fails to start.\nargument-hint: <blank for full check | \"mcp\"\
  \ | \"mastering\" | \"document-hunter\">\nmodel: claude-haiku-4-5-20251001\nallowed-tools:\n\
  \  - Bash\n---\n\nBase directory for this skill: ${CLAUDE_PLUGIN_BASE_DIR}\n\n##\
  \ Your Task\n\nGuide the user through installing bitwize-music plugin dependencies\
  \ based on their Python environment and reque..."
full_prompt_length: 5765
tools_mentioned:
- Python
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/setup/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/setup/SKILL.md
fetched_at: '2026-04-12T04:47:34.739473+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-12T05:44:29.789989Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f39934405f0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f39934405f0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-12T07:23:20.305330Z'
indexed_at: '2026-04-12T07:23:20.305336Z'
---
