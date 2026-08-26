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
full_prompt_length: 75045
tools_mentioned:
- Python
- Ruby
- go
- GCP
- Rust
- php
- Java
- AWS
- aws
- REST
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/claude-api/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md
fetched_at: '2026-08-26T03:02:13.498951Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-08-26T03:24:54.096226Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fe2179ac860 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fe2179ac860 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 171607
  forks: 20386
  open_issues: 1172
  last_commit: '2026-08-21'
  fetched_at: '2026-08-26T03:02:27.198890Z'
indexed_at: '2026-08-26T03:28:49.159336Z'
---
