---
id: technical-writer
slug: technical-writer
name: Technical Writer
description: Claude skill for Technical Writer
prompt_preview: '---

  name: technical-writer

  description: "Use this agent when you need to create, improve, or maintain technical
  documentation including API references, user guides, SDK documentation, and getting-started
  guides. Specifically:\\n\\n<example>\\nContext: A development team has completed
  a new REST API but lacks documentation. The API includes 12 endpoints with varying
  authentication methods and rate limits.\\nuser: \"We need comprehensive documentation
  for our new payment API. It has 12 endpoints a...'
full_prompt_length: 8809
tools_mentioned:
- REST
- Python
category: 08-business-product
category_display: 08 Business Product
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/08-business-product/technical-writer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/08-business-product/technical-writer.md
fetched_at: '2026-02-07T04:07:56.193492Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:09:16.290417Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides a clear role definition and comprehensive checklist
      of technical writing standards, but it's incomplete and contains a truncated
      development workflow section. The communication protocol is well-structured
      with JSON formatting, but the abrupt ending limits its practical usability.
      While the content covers many technical writing aspects, the incomplete structure
      reduces clarity for actual implementation.
  usefulness:
    score: 3.0
    reasoning: The prompt outlines valuable technical writing frameworks and documentation
      types that would be useful for creating comprehensive documentation. However,
      the incomplete development workflow and lack of concrete execution steps limit
      immediate actionability. The extensive checklists and standards are theoretically
      valuable but need completion to be practically useful for real-world documentation
      tasks.
  overall_rating: 3.25
  summary: A well-structured but incomplete technical writing prompt that establishes
    strong foundations but requires completion of the development workflow section
    to be fully functional.
  tags_suggested:
  - technical-writing
  - documentation
  - api-docs
  - user-guides
  - content-creation
github_metrics:
  stars: 9780
  forks: 1066
  open_issues: 2
  last_commit: '2026-02-06'
  fetched_at: '2026-02-07T04:08:16.529193Z'
indexed_at: '2026-02-07T04:08:26.914490Z'
---
