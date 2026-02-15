---
id: google-drive
slug: google-drive
name: Google Drive
description: Automatically refreshes expired tokens using Google's cloud function.
prompt_preview: "---\nname: google-drive\ndescription: |\n  Interact with Google Drive\
  \ - search files, find folders, list contents, download files, upload files,\n \
  \ create folders, move, copy, rename, and trash files. Use when user asks to: search\
  \ Google Drive,\n  find a file/folder, list Drive contents, download or upload files,\
  \ create folders, move files,\n  or organize Drive content. Lightweight integration\
  \ with standalone OAuth authentication supporting\n  full read/write access.\n---\n\
  \n# Google Drive\n\nLightweight Go..."
full_prompt_length: 3926
tools_mentioned:
- python
category: community
category_display: Community
source_repo: sanjay3290/ai-skills
source_path: skills/google-drive/SKILL.md
source_url: https://github.com/sanjay3290/ai-skills/blob/main/skills/google-drive/SKILL.md
fetched_at: '2026-02-15T04:22:19.906092+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:04:26.426522Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, with a concise
      description, explicit setup instructions, and detailed command examples. It
      defines scope and constraints effectively, noting limitations like unsupported
      personal Gmail accounts and Google Workspace file download restrictions. Best
      practices are followed with a logical flow from setup to usage, though it could
      briefly mention error handling or troubleshooting for authentication failures.
  usefulness:
    score: 4.5
    reasoning: This skill provides high real-world value for developers needing lightweight
      Google Drive access without a full MCP server, covering common tasks like search,
      listing, and downloading. It is comprehensive for its niche, with actionable
      commands that users can implement immediately. However, usefulness is slightly
      limited by the lack of integration examples or error scenarios, which could
      enhance practicality in complex workflows.
  overall_rating: 4.5
  summary: A robust, well-crafted prompt that offers a practical Google Drive integration
    with clear instructions and useful features, though it could benefit from more
    edge-case guidance for broader applicability.
  tags_suggested:
  - google-drive
  - oauth
  - file-management
  - automation
  - productivity
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:51.352512Z'
indexed_at: '2026-02-15T04:33:51.352517Z'
---
