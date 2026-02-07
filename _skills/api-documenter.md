---
id: api-documenter
slug: api-documenter
name: Api Documenter
description: Claude skill for Api Documenter
prompt_preview: '---

  name: api-documenter

  description: "Use this agent when creating or improving API documentation, writing
  OpenAPI specifications, building interactive documentation portals, or generating
  code examples for APIs. Specifically:\\n\\n<example>\\nContext: A REST API has been
  built with multiple endpoints but lacks formal documentation or OpenAPI specifications.\\nuser:
  \"Our API has 40+ endpoints, but we only have scattered documentation. Can you create
  comprehensive OpenAPI specs and generate int...'
full_prompt_length: 8686
tools_mentioned:
- WebSocket
- GraphQL
- gRPC
- REST
category: 07-specialized-domains
category_display: 07 Specialized Domains
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/07-specialized-domains/api-documenter.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/07-specialized-domains/api-documenter.md
fetched_at: '2026-02-07T04:07:51.256474Z'
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
  stars: 9780
  forks: 1066
  open_issues: 2
  last_commit: '2026-02-06'
  fetched_at: '2026-02-07T04:08:16.529193Z'
indexed_at: '2026-02-07T04:08:26.841147Z'
---
