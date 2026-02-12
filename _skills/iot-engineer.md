---
id: iot-engineer
slug: iot-engineer
name: Iot Engineer
description: Claude skill for Iot Engineer
prompt_preview: '---

  name: iot-engineer

  description: "Use when designing and deploying IoT solutions requiring expertise
  in device management, edge computing, cloud integration, and handling challenges
  like massive device scale, complex connectivity scenarios, or real-time data pipelines."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior IoT engineer with expertise in designing and implementing comprehensive
  IoT solutions. Your focus spans device connectivity, edge computing, cloud...'
full_prompt_length: 6363
tools_mentioned:
- AWS
- Azure
- WebSocket
category: 07-specialized-domains
category_display: 07 Specialized Domains
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/07-specialized-domains/iot-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/07-specialized-domains/iot-engineer.md
fetched_at: '2026-02-12T04:24:19.751106Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:06:12.837816Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear sections for IoT architecture,
      protocols, and workflows, but it's incomplete and contains errors. The 'Implementation
      Phase' section cuts off mid-sentence ('Managem'), and the checklist items have
      awkward phrasing ('achieved properly', 'verified completely') that reduces clarity.
      While the framework is logical, the abrupt ending and minor grammatical issues
      prevent it from being fully polished.
  usefulness:
    score: 4.0
    reasoning: Despite being incomplete, the prompt provides substantial practical
      value for IoT engineering tasks. It covers critical domains like device management,
      edge computing, security, and cloud platforms with specific technologies and
      considerations. The structured approach with checklists and architecture layers
      would help users systematically design IoT solutions, though the incomplete
      implementation section limits immediate actionability.
  overall_rating: 3.75
  summary: A comprehensive but incomplete IoT engineering prompt that provides strong
    architectural frameworks and domain coverage, though it needs completion and refinement
    to reach its full potential.
  tags_suggested:
  - IoT
  - Edge Computing
  - Cloud Architecture
  - Device Management
  - Security
github_metrics:
  stars: 10218
  forks: 1093
  open_issues: 4
  last_commit: '2026-02-10'
  fetched_at: '2026-02-12T04:24:36.992823Z'
indexed_at: '2026-02-12T04:24:46.758511Z'
---
