---
id: platform-engineer
slug: platform-engineer
name: Platform Engineer
description: Claude skill for Platform Engineer
prompt_preview: '---

  name: platform-engineer

  description: "Use when building or improving internal developer platforms (IDPs),
  designing self-service infrastructure, or optimizing developer workflows to reduce
  friction and accelerate delivery. The platform-engineer agent specializes in designing
  platform architecture, implementing golden paths, and maximizing developer self-service
  capabilities."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are a senior platform engineer with deep expertise in...'
full_prompt_length: 7552
tools_mentioned:
- kubernetes
- GraphQL
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/platform-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/platform-engineer.md
fetched_at: '2026-02-12T04:24:10.160051Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:56:12.668664Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear sections and specific technical
      domains, but it's incomplete - it cuts off mid-sentence in the 'Developer Needs
      Analysis' section. The checklist and architecture sections provide good specificity,
      but the lack of completion and missing edge case handling reduces the overall
      quality.
  usefulness:
    score: 4.0
    reasoning: The prompt provides comprehensive coverage of platform engineering
      concepts including GitOps, golden paths, service catalogs, and developer experience
      optimization. It offers practical frameworks and metrics that would be valuable
      for real platform engineering tasks, though the incomplete nature limits immediate
      actionability.
  overall_rating: 3.75
  summary: A comprehensive but incomplete platform engineering prompt that covers
    key concepts well but needs completion to be fully functional.
  tags_suggested:
  - platform-engineering
  - devops
  - gitops
  - developer-experience
  - infrastructure
github_metrics:
  stars: 10218
  forks: 1093
  open_issues: 4
  last_commit: '2026-02-10'
  fetched_at: '2026-02-12T04:24:36.992823Z'
indexed_at: '2026-02-12T04:24:46.569103Z'
---
