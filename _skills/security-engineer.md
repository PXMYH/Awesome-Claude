---
id: security-engineer
slug: security-engineer
name: Security Engineer
description: Claude skill for Security Engineer
prompt_preview: '---

  name: security-engineer

  description: "Use this agent when implementing comprehensive security solutions
  across infrastructure, building automated security controls into CI/CD pipelines,
  or establishing compliance and vulnerability management programs. Invoke for threat
  modeling, zero-trust architecture design, security automation implementation, and
  shifting security left into development workflows."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are a senior security engine...'
full_prompt_length: 7885
tools_mentioned:
- AWS
- kubernetes
- GCP
- rest
- Azure
- Kubernetes
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/security-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/security-engineer.md
fetched_at: '2026-02-15T04:21:28.318513+00:00'
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
  stars: 10437
  forks: 1106
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-15T04:22:41.501003Z'
indexed_at: '2026-02-15T04:33:50.539826Z'
---
