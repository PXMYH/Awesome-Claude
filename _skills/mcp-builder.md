---
id: mcp-builder
slug: mcp-builder
name: MCP Server Development Guide
description: '### Evaluation Guide (Load During Phase 4)'
prompt_preview: '---

  name: mcp-builder

  description: Guide for creating high-quality MCP (Model Context Protocol) servers
  that enable LLMs to interact with external services through well-designed tools.
  Use when building MCP servers to integrate external APIs or services, whether in
  Python (FastMCP) or Node/TypeScript (MCP SDK).

  license: Complete terms in LICENSE.txt

  ---


  # MCP Server Development Guide


  ## Overview


  Create MCP (Model Context Protocol) servers that enable LLMs to interact with external
  services th...'
full_prompt_length: 9059
tools_mentioned:
- typescript
- TypeScript
- Python
- python
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/mcp-builder/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/mcp-builder/SKILL.md
fetched_at: '2026-02-05T04:14:25.912367Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:14:15.429649Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly structured with clear phases and actionable steps,
      providing specific references to documentation and frameworks. It demonstrates
      strong specificity by recommending TypeScript as the primary language and streamable
      HTTP for transport, with clear rationale. However, it lacks explicit handling
      of edge cases like API rate limiting or authentication failures, and some instructions
      (e.g., 'Use WebFetch to load...') assume tool capabilities that may not be universally
      available.
  usefulness:
    score: 5.0
    reasoning: This guide offers exceptional real-world value by providing a comprehensive,
      step-by-step workflow for building MCP servers, covering research, planning,
      and implementation. It is highly actionable, with direct references to external
      resources and language-specific guides, enabling developers to immediately start
      building. The focus on practical considerations like tool discoverability and
      error messaging makes it directly applicable to real development tasks.
  overall_rating: 4.75
  summary: An excellent, well-structured guide that provides a robust framework for
    developing high-quality MCP servers, though it could benefit from more explicit
    edge-case handling and assumptions about tool availability.
  tags_suggested:
  - MCP
  - TypeScript
  - API Integration
  - Server Development
  - LLM Tools
github_metrics:
  stars: 63268
  forks: 6229
  open_issues: 236
  last_commit: '2026-02-04'
  fetched_at: '2026-02-05T04:14:39.842970Z'
indexed_at: '2026-02-05T04:14:41.366500Z'
---
