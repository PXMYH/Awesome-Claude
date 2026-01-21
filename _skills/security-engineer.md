---
id: security-engineer
slug: security-engineer
name: Security Engineer
description: Claude skill for Security Engineer
prompt_preview: '---

  name: security-engineer

  description: Expert infrastructure security engineer specializing in DevSecOps,
  cloud security, and compliance frameworks. Masters security automation, vulnerability
  management, and zero-trust architecture with emphasis on shift-left security practices.

  tools: Read, Write, Edit, Bash, Glob, Grep

  ---


  You are a senior security engineer with deep expertise in infrastructure security,
  DevSecOps practices, and cloud security architecture. Your focus spans vulnerability
  ma...'
full_prompt_length: 7747
tools_mentioned:
- AWS
- GCP
- kubernetes
- rest
- Azure
- Kubernetes
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/security-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/security-engineer.md
fetched_at: '2026-01-21T03:42:50.744766Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:56:27.257363Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections for
      different security domains and a comprehensive checklist. It follows excellent
      prompt engineering practices with defined roles, context queries, and structured
      protocols. However, the security context query JSON is incomplete (missing closing
      braces and proper structure), which creates ambiguity in execution.
  usefulness:
    score: 4.0
    reasoning: The prompt provides comprehensive coverage of modern security engineering
      practices across DevSecOps, cloud, containers, and compliance, making it highly
      valuable for real infrastructure security tasks. The detailed checklists and
      domain-specific guidance offer actionable frameworks for security assessments
      and implementations. However, the incomplete context query limits immediate
      practicality without additional clarification on how to properly request infrastructure
      context.
  overall_rating: 4.25
  summary: A comprehensive and well-structured security engineering prompt with excellent
    domain coverage, though slightly hampered by an incomplete context query that
    needs correction for full practicality.
  tags_suggested:
  - security
  - devsecops
  - cloud-security
  - compliance
  - infrastructure
github_metrics:
  stars: 8385
  forks: 925
  open_issues: 3
  last_commit: '2026-01-14'
  fetched_at: '2026-01-21T03:43:25.803986Z'
indexed_at: '2026-01-21T03:43:27.490965Z'
---
