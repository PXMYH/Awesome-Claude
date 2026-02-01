---
id: google-calendar
slug: google-calendar
name: Google Calendar
description: Tokens are automatically refreshed when expired using Google's cloud
  function.
prompt_preview: "---\nname: google-calendar\ndescription: |\n  Interact with Google\
  \ Calendar - list calendars, view events, create/update/delete events, and find\
  \ free time.\n  Use when user asks to: check calendar, schedule a meeting, create\
  \ an event, find available time, list upcoming events,\n  delete or update a calendar\
  \ event, or respond to meeting invitations. Lightweight alternative to full\n  Google\
  \ Workspace MCP server with standalone OAuth authentication.\n---\n\n# Google Calendar\n\
  \nLightweight Google Calendar in..."
full_prompt_length: 4575
tools_mentioned:
- python
category: community
category_display: Community
source_repo: sanjay3290/ai-skills
source_path: skills/google-calendar/SKILL.md
source_url: https://github.com/sanjay3290/ai-skills/blob/main/skills/google-calendar/SKILL.md
fetched_at: '2026-02-01T04:29:43.729926+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:03:51.507770Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, with a logical
      flow from setup to specific commands. It provides concrete examples for each
      operation, making it highly actionable. However, it lacks explicit guidance
      on handling common edge cases like timezone mismatches, API rate limits, or
      error handling for invalid inputs.
  usefulness:
    score: 4.0
    reasoning: This skill offers high real-world value for users needing to interact
      with Google Calendar programmatically, covering a comprehensive range of operations
      from listing to scheduling. The standalone OAuth approach is practical for lightweight
      use, but the requirement for a Google Workspace account limits its applicability
      for personal users.
  overall_rating: 4.25
  summary: A well-crafted, practical prompt that provides clear, actionable instructions
    for Google Calendar integration, though it could benefit from more robust error-handling
    guidance and broader account compatibility.
  tags_suggested:
  - productivity
  - automation
  - calendar
  - OAuth
  - API integration
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.872602Z'
indexed_at: '2026-02-01T04:32:50.872608Z'
---
