---
id: sre-engineer
slug: sre-engineer
name: Sre Engineer
description: Claude skill for Sre Engineer
prompt_preview: '---

  name: sre-engineer

  description: "Use this agent when you need to establish or improve system reliability
  through SLO definition, error budget management, and automation. Invoke when implementing
  SLI/SLO frameworks, reducing operational toil, designing fault-tolerant systems,
  conducting chaos engineering, or optimizing incident response processes."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior Site Reliability Engineer with expertise in building and maintainin...'
full_prompt_length: 6943
tools_mentioned:
- Go
- Python
- kubernetes
- Kubernetes
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/sre-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/sre-engineer.md
fetched_at: '2026-02-11T04:28:53.192597Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:56:37.285476Z'
  prompt_quality:
    score: 2.5
    reasoning: The prompt is highly structured with clear categories and checklists,
      but it is incomplete and cuts off mid-sentence in the Development Workflow section.
      This lack of completion creates ambiguity about the full instructions and expected
      behavior, violating best practices for prompt completeness.
  usefulness:
    score: 3.5
    reasoning: The prompt provides a comprehensive framework for SRE tasks with detailed
      checklists and protocols, offering real-world value for reliability engineering.
      However, the incomplete workflow limits immediate actionability, as users may
      not know how to proceed after the initial analysis phase.
  overall_rating: 3.0
  summary: A well-structured but incomplete SRE prompt that offers strong conceptual
    coverage but lacks full execution guidance, reducing its practical utility.
  tags_suggested:
  - site-reliability-engineering
  - infrastructure
  - slo-management
  - automation
  - chaos-engineering
github_metrics:
  stars: 10153
  forks: 1087
  open_issues: 3
  last_commit: '2026-02-10'
  fetched_at: '2026-02-11T04:29:28.992841Z'
indexed_at: '2026-02-11T04:29:38.961001Z'
---
