---
id: c-ai
slug: c-ai
name: AI / LLM Tools
description: '- Use `llm` for piping text through LLMs (summarize, translate, analyze)'
prompt_preview: '---

  name: c-ai

  description: Query LLMs from the CLI — pipe text for summarization, chat interactively,
  use local or cloud models with llm or aichat.

  tags: [ai, llm, summarize, chat]

  ---


  # AI / LLM Tools


  ## llm (Simon Willison)


  ```bash

  # Quick prompt

  llm "What is the capital of France?"


  # Pipe text for processing

  cat article.txt | llm "Summarize this in 3 bullet points"

  git diff | llm "Write a commit message for these changes"

  pbpaste | llm "Fix the grammar in this text"


  # Interactive chat

  l...'
full_prompt_length: 1581
tools_mentioned:
- Docker
- Rust
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-ai/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-ai/SKILL.md
fetched_at: '2026-05-03T05:31:13.701066+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-03T06:37:09.396532Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e34428560 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e34428560 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-03T08:17:30.646849Z'
indexed_at: '2026-05-03T08:17:30.646854Z'
---
