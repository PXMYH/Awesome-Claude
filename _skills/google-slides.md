---
id: google-slides
slug: google-slides
name: Google Slides
description: Automatically refreshes expired tokens using Google's cloud function.
prompt_preview: "---\nname: google-slides\ndescription: |\n  Read content from Google\
  \ Slides presentations - get text, find presentations, and retrieve metadata.\n\
  \  Use when user asks to: read a presentation, find slides, get presentation content,\
  \ search for a slideshow,\n  or check presentation details. Lightweight alternative\
  \ to full Google Workspace MCP server with standalone\n  OAuth authentication. Read-only\
  \ operations only.\n---\n\n# Google Slides\n\nLightweight Google Slides integration\
  \ with standalone OAuth authent..."
full_prompt_length: 2575
tools_mentioned:
- python
category: community
category_display: Community
source_repo: sanjay3290/ai-skills
source_path: skills/google-slides/SKILL.md
source_url: https://github.com/sanjay3290/ai-skills/blob/main/skills/google-slides/SKILL.md
fetched_at: '2026-02-08T04:32:36.884692+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:04:46.430021Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, with excellent
      specificity on commands, output formats, and authentication requirements. It
      follows best practices by explicitly stating constraints (read-only, Google
      Workspace only) and providing practical examples. The only minor limitation
      is that it doesn't address potential error scenarios or troubleshooting steps
      in detail.
  usefulness:
    score: 4.5
    reasoning: This skill provides high real-world value for users needing to extract
      content from Google Slides presentations programmatically, especially for data
      analysis or documentation tasks. It's comprehensive for its stated purpose (read-only
      operations) and immediately actionable with clear command examples. The standalone
      OAuth approach makes it more accessible than full Google Workspace MCP servers
      for users who only need Slides functionality.
  overall_rating: 4.5
  summary: A well-crafted, practical skill that effectively addresses a common business
    need with clear instructions and robust authentication handling.
  tags_suggested:
  - google-slides
  - presentation
  - data-extraction
  - oauth
  - read-only
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.710925Z'
indexed_at: '2026-02-08T04:36:45.710930Z'
---
