---
id: health-check
slug: health-check
name: Health Check
description: 1. **Be concise** — this is a status report
prompt_preview: "---\nname: health-check\ndescription: Runs plugin health checks (venv\
  \ packages and skill registration). Use when the user asks to check plugin health,\
  \ verify setup, or troubleshoot missing skills.\nmodel: haiku\nallowed-tools:\n\
  \  - ToolSearch\n  - bitwize-music-mcp\n---\n\n# Health Check\n\n## Your Task\n\n\
  Run the `health_check` MCP tool and report results to the user.\n\n## Workflow\n\
  \n**IMPORTANT: Do NOT use Bash for any step. Use only the tools listed below.**\n\
  \n1. Use the `ToolSearch` tool with query `select:..."
full_prompt_length: 1613
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/health-check/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/health-check/SKILL.md
fetched_at: '2026-06-28T06:16:41.121414+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T07:22:50.541260Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a27d5a00 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a27d5a00 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:26.484376Z'
indexed_at: '2026-06-28T10:04:26.484382Z'
---
