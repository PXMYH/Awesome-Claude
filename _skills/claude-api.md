---
id: claude-api
slug: claude-api
name: Building LLM-Powered Applications with Claude
description: '- Don''t truncate inputs when passing files or content to the API. If
  the content is too long to fit in the context window, notify the user and discuss
  options (chunking, summarization, etc.) rather th...'
prompt_preview: "---\nname: claude-api\ndescription: |-\n  Reference for the Claude\
  \ API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents,\
  \ caching, token counting, model migration.\n  TRIGGER — read BEFORE opening the\
  \ target file; don't skip because it \"looks like a one-liner\" — whenever: the\
  \ prompt names Claude/Anthropic in any form (Claude, Anthropic, Fable, Opus, Sonnet,\
  \ Haiku, `anthropic`, `@anthropic-ai`, `claude-*`, `us.anthropic.*`, `[1m]`); the\
  \ user asks about an LLM (pricing/mod..."
full_prompt_length: 105119
tools_mentioned:
- rest
- go
- ruby
- php
- Rust
- Go
- typescript
- java
- Ruby
- REST
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/claude-api/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md
fetched_at: '2026-11-23T10:17:48.802196Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-11-23T10:41:20.284972Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x78d8336bfd10 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x78d8336bfd10 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 199205
  forks: 23317
  open_issues: 1573
  last_commit: '2026-11-16'
  fetched_at: '2026-11-23T10:18:04.251923Z'
indexed_at: '2026-11-23T10:45:18.085733Z'
---
