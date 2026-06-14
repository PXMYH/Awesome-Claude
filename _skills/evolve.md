---
id: evolve
slug: evolve
name: /harness:evolve
description: 'Plus: LangSmith URL, `git log --oneline` summary, suggest `/harness:deploy`.'
prompt_preview: '---

  name: harness:evolve

  description: "Use when the user wants to run the optimization loop, improve agent
  performance, evolve the agent, or iterate on quality. Requires .evolver.json to
  exist (run harness:setup first)."

  argument-hint: "[--iterations N]"

  allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Agent, AskUserQuestion]

  ---


  # /harness:evolve


  Run the propose-evaluate-iterate loop. LangSmith is the evaluation backend, git
  worktrees provide isolation.


  ## Setup


  `.evolver.json` must exi...'
full_prompt_length: 14113
tools_mentioned:
- python
- Python
category: community
category_display: Community
source_repo: raphaelchristi/harness-evolver
source_path: skills/evolve/SKILL.md
source_url: https://github.com/raphaelchristi/harness-evolver/blob/main/skills/evolve/SKILL.md
fetched_at: '2026-06-14T06:41:58.629446+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T09:58:30.870862Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1879f5a060 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1879f5a060 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:27.563214Z'
indexed_at: '2026-06-14T10:18:27.563223Z'
---
