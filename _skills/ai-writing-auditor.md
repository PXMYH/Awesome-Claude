---
id: ai-writing-auditor
slug: ai-writing-auditor
name: Ai Writing Auditor
description: Claude skill for Ai Writing Auditor
prompt_preview: '---

  name: ai-writing-auditor

  description: "Use this agent when you need to audit content for AI writing patterns
  and rewrite text to remove them."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are an AI writing auditor that detects and removes machine-generated writing
  patterns ("AI-isms") from text content. Your goal is to make AI-assisted writing
  sound natural and human.


  When invoked:

  1. Read the provided content

  2. Audit it for AI writing patterns across 34 detection catego...'
full_prompt_length: 4232
tools_mentioned: []
category: quality-security
category_display: Quality & Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/ai-writing-auditor.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/ai-writing-auditor.md
fetched_at: '2026-05-29T06:12:09.836361Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-29T06:20:41.654429Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f829ac24920 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f829ac24920 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 20800
  forks: 2430
  open_issues: 4
  last_commit: '2026-05-27'
  fetched_at: '2026-05-29T06:12:34.340410Z'
indexed_at: '2026-05-29T06:37:40.676768Z'
---
