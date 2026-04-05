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
- Rust
- Docker
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-ai/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-ai/SKILL.md
fetched_at: '2026-04-05T04:36:48.052891+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:56:24.920509Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8a25430 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8a25430 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.472509Z'
indexed_at: '2026-04-05T08:29:58.472515Z'
---
