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
full_prompt_length: 103431
tools_mentioned:
- GCP
- aws
- go
- typescript
- AWS
- Python
- java
- Ruby
- Java
- Go
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/claude-api/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md
fetched_at: '2026-10-08T08:25:04.244320Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-08T08:47:49.202610Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f2ca240d310 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f2ca240d310 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 180103
  forks: 21308
  open_issues: 1392
  last_commit: '2026-10-05'
  fetched_at: '2026-10-08T08:25:14.275885Z'
indexed_at: '2026-10-08T08:51:46.100401Z'
---
