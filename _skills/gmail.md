---
id: gmail
slug: gmail
name: Gmail
description: Tokens automatically refresh when expired using Google's cloud function.
prompt_preview: "---\nname: gmail\ndescription: |\n  Interact with Gmail - search\
  \ emails, read messages, send emails, create drafts, and manage labels.\n  Use when\
  \ user asks to: search email, read email, send email, create email draft, mark as\
  \ read,\n  archive email, star email, or manage Gmail labels. Lightweight alternative\
  \ to full Google\n  Workspace MCP server with standalone OAuth authentication.\n\
  ---\n\n# Gmail\n\nLightweight Gmail integration with standalone OAuth authentication.\
  \ No MCP server required.\n\n> **⚠️ Requ..."
full_prompt_length: 4680
tools_mentioned:
- python
category: community
category_display: Community
source_repo: sanjay3290/ai-skills
source_path: skills/gmail/SKILL.md
source_url: https://github.com/sanjay3290/ai-skills/blob/main/skills/gmail/SKILL.md
fetched_at: '2026-02-08T04:32:35.997888+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:03:30.617145Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured with comprehensive
      command examples covering all major Gmail operations. It follows best practices
      by including setup instructions, query syntax reference, and clear categorization
      of commands. The only minor limitation is that it assumes the underlying scripts
      exist and work as described, which is typical for skill prompts but could be
      more explicit about error handling.
  usefulness:
    score: 4.5
    reasoning: This skill provides high real-world value for email automation tasks
      like searching, reading, sending, and managing labels without requiring a full
      Google Workspace MCP server. It covers a comprehensive range of Gmail operations
      that developers commonly need, making it immediately actionable for workflow
      automation. The standalone OAuth authentication approach is practical for lightweight
      integrations.
  overall_rating: 4.5
  summary: A well-crafted, practical Gmail integration skill that balances comprehensive
    functionality with lightweight implementation, making it highly useful for developers
    needing email automation without complex infrastructure requirements.
  tags_suggested:
  - email
  - automation
  - productivity
  - google-workspace
  - oauth
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.688582Z'
indexed_at: '2026-02-08T04:36:45.688587Z'
---
