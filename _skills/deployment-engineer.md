---
id: deployment-engineer
slug: deployment-engineer
name: Deployment Engineer
description: Claude skill for Deployment Engineer
prompt_preview: '---

  name: deployment-engineer

  description: Expert deployment engineer specializing in CI/CD pipelines, release
  automation, and deployment strategies. Masters blue-green, canary, and rolling deployments
  with focus on zero-downtime releases and rapid rollback capabilities.

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: haiku

  ---


  You are a senior deployment engineer with expertise in designing and implementing
  sophisticated CI/CD pipelines, deployment automation, and release orchestration.
  Your...'
full_prompt_length: 6994
tools_mentioned:
- Azure
- kubernetes
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/deployment-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/deployment-engineer.md
fetched_at: '2026-02-06T04:14:28.520559Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:54:59.163865Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear sections and a comprehensive
      checklist, but it is incomplete and abruptly ends mid-sentence. It lacks specific
      instructions on how to execute the workflow phases and does not define clear
      boundaries for tool usage or response formats, which could lead to ambiguous
      behavior.
  usefulness:
    score: 4.0
    reasoning: The skill provides a valuable framework for deployment engineering
      with detailed checklists and strategy coverage, making it highly relevant for
      real-world CI/CD tasks. However, the incomplete nature limits immediate actionability,
      as users may not know how to proceed after the initial analysis phase.
  overall_rating: 3.75
  summary: A robust but unfinished prompt that outlines deployment engineering best
    practices effectively but requires completion to be fully operational.
  tags_suggested:
  - deployment
  - CI/CD
  - DevOps
  - automation
  - release-management
github_metrics:
  stars: 9630
  forks: 1048
  open_issues: 4
  last_commit: '2026-02-05'
  fetched_at: '2026-02-06T04:15:08.864089Z'
indexed_at: '2026-02-06T04:15:19.015979Z'
---
