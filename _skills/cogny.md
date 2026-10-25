---
id: cogny
slug: cogny
name: Cogny Marketing Agent v1.1.2
description: '- `write_context_node` with path like `insights/seo/top-keywords` or
  `insights/linkedin/audience-profile`'
prompt_preview: "---\nname: cogny\ndescription: Run Cogny marketing analysis tasks\
  \ — fetch scheduled tasks, analyze ad accounts via MCP, report findings\nversion:\
  \ \"1.1.2\"\nrequires: cogny-mcp\nuser-invocable: true\nargument-hint: \"[status|run|loop|update]\"\
  \nallowed-tools:\n  # Core (both tiers)\n  - mcp__cogny__cogny_status\n  - mcp__cogny__list_integrations\n\
  \  - mcp__cogny__refresh_mcp_discovery\n  # Solo: task queue, heartbeat, findings\n\
  \  - mcp__cogny__get_queue_status\n  - mcp__cogny__get_next_task\n  - mcp__cogny__complet..."
full_prompt_length: 29431
tools_mentioned:
- go
category: community
category_display: Community
source_repo: cognyai/claude-code-marketing-skills
source_path: skills/cogny/SKILL.md
source_url: https://github.com/cognyai/claude-code-marketing-skills/blob/main/skills/cogny/SKILL.md
fetched_at: '2026-10-25T07:17:12.994120+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T08:54:29.849791Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1f7d0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1f7d0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:05.946466Z'
indexed_at: '2026-10-25T12:12:05.946485Z'
---
