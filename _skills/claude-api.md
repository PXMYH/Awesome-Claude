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
full_prompt_length: 33463
tools_mentioned:
- java
- Python
- python
- php
- Rest
- Java
- TypeScript
- ruby
- Rust
- go
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/claude-api/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md
fetched_at: '2026-06-02T06:40:29.043890Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-02T07:02:06.704664Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc0dc01e960 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc0dc01e960 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 145333
  forks: 17124
  open_issues: 902
  last_commit: '2026-05-29'
  fetched_at: '2026-06-02T06:40:36.450522Z'
indexed_at: '2026-06-02T07:05:49.901053Z'
---
