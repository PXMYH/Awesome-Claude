---
id: charles-proxy-extract-skill
slug: charles-proxy-extract-skill
name: Charles Proxy Session Extractor
description: '**Python not found:**'
prompt_preview: '---

  name: charles-proxy-extract

  description: Extracts HTTP/HTTPS request and response data from Charles Proxy session
  files (.chlsj format), including URLs, methods, status codes, headers, request bodies,
  and response bodies. Use when analyzing captured network traffic from Charles Proxy
  debug sessions, inspecting API calls, debugging HTTP requests, or examining proxy
  logs.

  allowed-tools: Bash

  ---


  # Charles Proxy Session Extractor


  Parses and extracts structured data from Charles Proxy session...'
full_prompt_length: 5987
tools_mentioned:
- python
- Python
category: community
category_display: Community
source_repo: wannabehero/charles-proxy-extract-skill
source_path: SKILL.md
source_url: https://github.com/wannabehero/charles-proxy-extract-skill/blob/main/SKILL.md
fetched_at: '2026-02-08T04:32:52.743830+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:05:35.914323Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and specific, providing precise command
      syntax, parameter definitions, and practical examples. It follows strong prompt
      engineering practices by defining prerequisites, execution patterns, and edge
      cases like case-sensitive matching. The only minor weakness is the incomplete
      output format section at the end, which slightly impacts completeness.
  usefulness:
    score: 5.0
    reasoning: This skill addresses a real and common development task—analyzing Charles
      Proxy session files—which is highly valuable for API debugging and network traffic
      inspection. It provides comprehensive coverage of extraction needs with filtering,
      summarization, and export capabilities. The actionability is excellent, as users
      can immediately apply the skill with clear examples and parameter guidance.
  overall_rating: 4.75
  summary: A well-crafted, highly practical skill that excels in clarity and real-world
    utility for developers working with Charles Proxy sessions, though it has a minor
    formatting issue at the end.
  tags_suggested:
  - network-debugging
  - api-analysis
  - proxy-tools
  - data-extraction
  - http-traffic
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.898525Z'
indexed_at: '2026-02-08T04:36:45.898530Z'
---
