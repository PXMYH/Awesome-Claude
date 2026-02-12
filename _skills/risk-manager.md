---
id: risk-manager
slug: risk-manager
name: Risk Manager
description: Claude skill for Risk Manager
prompt_preview: '---

  name: risk-manager

  description: "Use this agent when you need to identify, quantify, and mitigate enterprise-level
  risks across financial, operational, regulatory, and strategic domains. Invoke this
  agent when you need to assess risk exposure, design control frameworks, validate
  risk models, or ensure regulatory compliance."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are a senior risk manager with expertise in identifying, quantifying, and mitigating
  enterprise risks. Yo...'
full_prompt_length: 6619
tools_mentioned: []
category: 07-specialized-domains
category_display: 07 Specialized Domains
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/07-specialized-domains/risk-manager.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/07-specialized-domains/risk-manager.md
fetched_at: '2026-02-12T04:24:20.737170Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:07:18.615083Z'
  prompt_quality:
    score: 2.5
    reasoning: The prompt provides a comprehensive taxonomy of risk management concepts
      and frameworks, but suffers from significant structural issues. The implementation
      phase is incomplete (cut off mid-sentence at 'Monitoring se'), and the communication
      protocol lacks practical implementation details. While the risk categories and
      checklists are well-organized, the prompt lacks clear action instructions for
      the agent to follow when invoked.
  usefulness:
    score: 3.0
    reasoning: The prompt contains valuable domain knowledge with extensive risk management
      frameworks, methodologies, and categories that could be useful for risk assessment
      tasks. However, its practical utility is severely limited by the incomplete
      implementation workflow and unclear execution instructions. The extensive lists
      of risk types and frameworks provide good reference material but don't translate
      into actionable guidance for the agent.
  overall_rating: 2.75
  summary: This prompt demonstrates strong domain knowledge organization but is fundamentally
    incomplete and structurally flawed, with a truncated implementation phase and
    insufficient operational guidance for the agent to function effectively.
  tags_suggested:
  - risk-management
  - compliance
  - enterprise-risk
  - incomplete-prompt
  - domain-expert
github_metrics:
  stars: 10218
  forks: 1093
  open_issues: 4
  last_commit: '2026-02-10'
  fetched_at: '2026-02-12T04:24:36.992823Z'
indexed_at: '2026-02-12T04:24:46.777154Z'
---
