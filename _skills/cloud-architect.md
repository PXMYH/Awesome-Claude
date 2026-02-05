---
id: cloud-architect
slug: cloud-architect
name: Cloud Architect
description: Claude skill for Cloud Architect
prompt_preview: '---

  name: cloud-architect

  description: Expert cloud architect specializing in multi-cloud strategies, scalable
  architectures, and cost-effective solutions. Masters AWS, Azure, and GCP with focus
  on security, performance, and compliance while designing resilient cloud-native
  systems.

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are a senior cloud architect with expertise in designing and implementing scalable,
  secure, and cost-effective cloud solutions across AWS, Azure, and Go...'
full_prompt_length: 7041
tools_mentioned:
- GCP
- Azure
- AWS
- kubernetes
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/cloud-architect.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/cloud-architect.md
fetched_at: '2026-02-05T04:13:58.108866Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:54:38.452622Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is well-structured with clear sections and comprehensive
      checklists covering major cloud architecture domains. However, it lacks specific
      instructions for handling edge cases, such as conflicting requirements or resource
      constraints, and the workflow is incomplete (Discovery Analysis is the only
      phase described).
  usefulness:
    score: 4.5
    reasoning: The prompt provides high practical value with extensive checklists
      and frameworks (Well-Architected, 6Rs, etc.) that guide real-world cloud design
      decisions. It covers multi-cloud strategies, cost optimization, and security
      comprehensively, making it immediately actionable for architects.
  overall_rating: 4.25
  summary: A robust, comprehensive cloud architect prompt with excellent practical
    frameworks, though incomplete in workflow execution and edge case handling.
  tags_suggested:
  - cloud-architecture
  - multi-cloud
  - infrastructure
  - aws
  - azure
  - gcp
  - well-architected
github_metrics:
  stars: 9546
  forks: 1034
  open_issues: 2
  last_commit: '2026-01-30'
  fetched_at: '2026-02-05T04:14:39.064845Z'
indexed_at: '2026-02-05T04:14:40.993491Z'
---
