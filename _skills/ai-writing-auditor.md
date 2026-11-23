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

  model: inherit

  ---


  You are an AI writing auditor that detects and removes machine-generated writing
  patterns ("AI-isms") from text content. Your goal is to make AI-assisted writing
  sound natural and human.


  When invoked:

  1. Read the provided content

  2. Audit it for AI writing patterns across 34 detection cat...'
full_prompt_length: 4235
tools_mentioned: []
category: quality-security
category_display: Quality & Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/ai-writing-auditor.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/ai-writing-auditor.md
fetched_at: '2026-11-23T10:17:20.199731Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-11-23T10:26:30.907576Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x78d8336bffe0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x78d8336bffe0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 26738
  forks: 3043
  open_issues: 10
  last_commit: '2026-11-02'
  fetched_at: '2026-11-23T10:18:02.834819Z'
indexed_at: '2026-11-23T10:45:17.822476Z'
---
