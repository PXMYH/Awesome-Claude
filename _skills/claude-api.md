---
id: claude-api
slug: claude-api
name: Building LLM-Powered Applications with Claude
description: '- Don''t truncate inputs when passing files or content to the API. If
  the content is too long to fit in the context window, notify the user and discuss
  options (chunking, summarization, etc.) rather th...'
prompt_preview: '---

  name: claude-api

  description: "Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built
  with this skill should include prompt caching. Also handles migrating existing Claude
  API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).
  TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude
  API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature
  (caching, thinking, compaction, tool use, batch, fi...'
full_prompt_length: 32719
tools_mentioned:
- php
- python
- typescript
- go
- Python
- Java
- TypeScript
- rest
- Go
- Ruby
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/claude-api/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md
fetched_at: '2026-05-05T05:13:52.160421Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-05T05:34:07.177474Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f28f60cfa40 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f28f60cfa40 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 128154
  forks: 15076
  open_issues: 805
  last_commit: '2026-05-03'
  fetched_at: '2026-05-05T05:14:04.940394Z'
indexed_at: '2026-05-05T05:37:47.162816Z'
---
