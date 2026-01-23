---
id: api-documenter
slug: api-documenter
name: Api Documenter
description: Claude skill for Api Documenter
prompt_preview: '---

  name: api-documenter

  description: Expert API documenter specializing in creating comprehensive, developer-friendly
  API documentation. Masters OpenAPI/Swagger specifications, interactive documentation
  portals, and documentation automation with focus on clarity, completeness, and exceptional
  developer experience.

  tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch

  ---


  You are a senior API documenter with expertise in creating world-class API documentation.
  Your focus spans OpenAPI speci...'
full_prompt_length: 6417
tools_mentioned:
- WebSocket
- REST
- GraphQL
- gRPC
category: 07-specialized-domains
category_display: 07 Specialized Domains
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/07-specialized-domains/api-documenter.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/07-specialized-domains/api-documenter.md
fetched_at: '2026-01-23T03:41:44.040604Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:05:17.381302Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear sections and comprehensive
      checklists, but it's incomplete - the 'Implementation Phase' section cuts off
      mid-sentence ('Add int'). While the documentation categories and features are
      thoroughly enumerated, the actual execution instructions are fragmented and
      lack a complete workflow. The communication protocol is defined but not fully
      integrated into the action steps.
  usefulness:
    score: 4.0
    reasoning: The prompt provides exceptional value for API documentation tasks with
      extensive coverage of OpenAPI specs, interactive features, authentication methods,
      and integration guides. The comprehensive checklists and structured approach
      would significantly help developers create professional API documentation. However,
      the incomplete workflow reduces immediate actionability for users expecting
      a complete end-to-end process.
  overall_rating: 3.75
  summary: A highly detailed and well-organized API documentation prompt with excellent
    coverage of documentation types and best practices, but critically incomplete
    - it cuts off mid-sentence in the implementation workflow, preventing full execution
    of the documented process.
  tags_suggested:
  - api-documentation
  - openapi
  - developer-tools
  - documentation-automation
  - technical-writing
github_metrics:
  stars: 8539
  forks: 938
  open_issues: 4
  last_commit: '2026-01-14'
  fetched_at: '2026-01-23T03:42:11.391211Z'
indexed_at: '2026-01-23T03:42:13.221818Z'
---
