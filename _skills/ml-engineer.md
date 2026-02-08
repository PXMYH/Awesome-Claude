---
id: ml-engineer
slug: ml-engineer
name: Ml Engineer
description: Claude skill for Ml Engineer
prompt_preview: '---

  name: ml-engineer

  description: "Use this agent when building production ML systems requiring model
  training pipelines, model serving infrastructure, performance optimization, and
  automated retraining. Specifically:\\n\\n<example>\\nContext: A team needs to implement
  a complete ML system that trains a recommendation model, serves predictions at scale,
  and monitors for performance degradation.\\nuser: \"We need to build an ML pipeline
  that trains a collaborative filtering model on 100M user ev...'
full_prompt_length: 9498
tools_mentioned:
- gRPC
- REST
category: data-ai
category_display: Data Ai
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/05-data-ai/ml-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/ml-engineer.md
fetched_at: '2026-02-08T04:31:53.517071+00:00'
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
  stars: 9886
  forks: 1073
  open_issues: 2
  last_commit: '2026-02-07'
  fetched_at: '2026-02-08T04:32:59.475595Z'
indexed_at: '2026-02-08T04:36:45.128821Z'
---
