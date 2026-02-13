---
id: ml-engineer
slug: ml-engineer
name: Ml Engineer
description: Claude skill for Ml Engineer
prompt_preview: '---

  name: ml-engineer

  description: "Use this agent when building production ML systems requiring model
  training pipelines, model serving infrastructure, performance optimization, and
  automated retraining."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior ML engineer with expertise in the complete machine learning lifecycle.
  Your focus spans pipeline development, model training, validation, deployment, and
  monitoring with emphasis on building production-ready ML syst...'
full_prompt_length: 6463
tools_mentioned:
- gRPC
- REST
category: 05-data-ai
category_display: 05 Data Ai
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/05-data-ai/ml-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/ml-engineer.md
fetched_at: '2026-02-13T04:21:03.441234Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:01:31.864384Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt has a clear structure with defined sections and a comprehensive
      checklist, but it's incomplete - the 'Implementation Phase' section cuts off
      mid-sentence. While the technical content is specific and well-organized, the
      abrupt ending creates ambiguity about the full workflow. The communication protocol
      is well-defined but the incomplete implementation guidance limits clarity.
  usefulness:
    score: 4.0
    reasoning: The prompt provides substantial real-world value with detailed ML engineering
      checklists covering production deployment, monitoring, and optimization. It
      comprehensively addresses the ML lifecycle from data validation to production
      patterns. The actionable checklists and tooling ecosystem references would help
      users implement robust ML systems, though the incomplete workflow reduces practical
      utility.
  overall_rating: 3.75
  summary: A technically comprehensive ML engineering prompt with excellent production-focused
    checklists and tooling references, but significantly undermined by an incomplete
    implementation section that cuts off mid-sentence, reducing its practical usability.
  tags_suggested:
  - machine-learning
  - ml-engineering
  - production-deployment
  - mlops
  - model-monitoring
github_metrics:
  stars: 10303
  forks: 1096
  open_issues: 3
  last_commit: '2026-02-12'
  fetched_at: '2026-02-13T04:21:22.535205Z'
indexed_at: '2026-02-13T04:21:32.019819Z'
---
