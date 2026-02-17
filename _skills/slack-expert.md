---
id: slack-expert
slug: slack-expert
name: Slack Expert
description: Claude skill for Slack Expert
prompt_preview: '---

  name: slack-expert

  description: "Use this agent when developing Slack applications, implementing Slack
  API integrations, or reviewing Slack bot code for security and best practices."

  tools: Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch

  model: sonnet

  ---

  You are an elite Slack Platform Expert and Developer Advocate with deep expertise
  in the Slack API ecosystem. You have extensive hands-on experience with @slack/bolt,
  the Slack Web API, Events API, and the latest platform features....'
full_prompt_length: 6608
tools_mentioned:
- typescript
- TypeScript
category: 06-developer-experience
category_display: 06 Developer Experience
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/06-developer-experience/slack-expert.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/06-developer-experience/slack-expert.md
fetched_at: '2026-02-17T04:20:04.003611Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:04:52.774239Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is highly specific and well-structured with clear expertise
      areas and checklists. However, it's incomplete - the Development Workflow section
      cuts off mid-sentence during the Analysis Phase, which creates ambiguity about
      the full process. The core instructions are clear but the abrupt ending undermines
      completeness.
  usefulness:
    score: 4.5
    reasoning: This is extremely practical for Slack development with comprehensive
      coverage of modern APIs, security practices, and architecture patterns. The
      checklists and specific technical guidance provide immediate value for developers
      building Slack apps. The only limitation is the incomplete workflow section.
  overall_rating: 4.25
  summary: A highly valuable Slack development skill with excellent technical depth
    and practical guidance, though the prompt is incomplete and cuts off during the
    workflow description.
  tags_suggested:
  - slack
  - slack-api
  - slack-bolt
  - block-kit
  - developer-tools
  - api-integration
github_metrics:
  stars: 10561
  forks: 1120
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-17T04:20:20.236835Z'
indexed_at: '2026-02-17T04:20:37.978570Z'
---
