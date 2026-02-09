---
id: deployment-engineer
slug: deployment-engineer
name: Deployment Engineer
description: Claude skill for Deployment Engineer
prompt_preview: '---

  name: deployment-engineer

  description: "Use this agent when designing, building, or optimizing CI/CD pipelines
  and deployment automation strategies. Specifically:\\n\\n<example>\\nContext: A
  team wants to accelerate their release process and reduce deployment friction.\\nuser:
  \"Our deployments are slow and manual. We deploy every 2 weeks with 4-hour windows.
  Can you help?\"\\nassistant: \"I''ll use the deployment-engineer agent to analyze
  your current process and implement a modern CI/CD pip...'
full_prompt_length: 8884
tools_mentioned:
- Azure
- kubernetes
- go
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/deployment-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/deployment-engineer.md
fetched_at: '2026-02-09T04:26:09.525738Z'
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
  stars: 9985
  forks: 1081
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-09T04:26:32.597214Z'
indexed_at: '2026-02-09T04:26:41.988996Z'
---
