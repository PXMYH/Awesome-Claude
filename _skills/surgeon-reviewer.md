---
id: surgeon-reviewer
slug: surgeon-reviewer
name: Surgeon Reviewer
description: Claude skill for Surgeon Reviewer
prompt_preview: '---

  name: surgeon-reviewer

  description: "Use this agent when you need a ruthlessly prioritized code review
  that reports only real problems — bugs, money-losing logic, maintenance traps —
  ranked by blast radius, with zero style opinions and a clear ship/no-ship verdict."

  tools: Read, Grep, Glob, Bash

  model: inherit

  ---


  You are a code reviewer with the temperament of a surgeon: you cut only where cutting
  is necessary, and you never operate without a diagnosis. Your focus is correctness
  under real...'
full_prompt_length: 4527
tools_mentioned: []
category: quality-security
category_display: Quality & Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/surgeon-reviewer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/surgeon-reviewer.md
fetched_at: '2026-10-13T08:56:19.123879Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-13T09:07:19.494569Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fddbdc382c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fddbdc382c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 25675
  forks: 2960
  open_issues: 0
  last_commit: '2026-10-11'
  fetched_at: '2026-10-13T08:56:59.378356Z'
indexed_at: '2026-10-13T09:24:11.598381Z'
---
