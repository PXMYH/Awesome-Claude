---
id: linear
slug: linear
name: Linear
description: '- Linear MCP: https://linear.app/docs/mcp.md'
prompt_preview: "---\nname: Linear\ndescription: Managing Linear issues, projects,\
  \ and teams. Use when working with Linear tasks, creating issues, updating status,\
  \ querying projects, or managing team workflows.\nallowed-tools:\n  - mcp__linear\n\
  \  - WebFetch(domain:linear.app)\n  - Bash\n---\n\n# Linear\n\nTools and workflows\
  \ for managing issues, projects, and teams in Linear.\n\n---\n\n## ⚠️ Tool Availability\
  \ (READ FIRST)\n\n**This skill supports multiple tool backends. Use whichever is\
  \ available:**\n\n1. **MCP Tools (mcp__linear)..."
full_prompt_length: 44805
tools_mentioned:
- GraphQL
- Node.js
- Go
- JavaScript
- graphql
- typescript
- TypeScript
- javascript
category: community
category_display: Community
source_repo: wrsmith108/linear-claude-skill
source_path: skills/linear/SKILL.md
source_url: https://github.com/wrsmith108/linear-claude-skill/blob/main/skills/linear/SKILL.md
fetched_at: '2026-01-19T00:20:25.192580+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:29:09.240896Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured with explicit
      tool availability guidance, security warnings, and fallback procedures. It handles
      the edge case of missing MCP tools by providing CLI alternatives and includes
      comprehensive setup instructions. The security section is particularly strong
      with clear safe/unsafe command examples and Varlock integration guidance.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate practical value for Linear workflow management
      with comprehensive coverage of common operations like issue creation, status
      updates, and project management. The inclusion of helper scripts for complex
      operations (sub-issues, initiatives) and detailed setup instructions makes it
      immediately actionable for real development workflows.
  overall_rating: 4.75
  summary: An excellent, production-ready skill prompt with outstanding security practices,
    clear fallback procedures for tool availability, and comprehensive coverage of
    Linear operations that would be immediately useful for development teams.
  tags_suggested:
  - project-management
  - issue-tracking
  - linear
  - team-workflow
  - security
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:36.869113Z'
indexed_at: '2026-01-19T01:30:36.869122Z'
---
