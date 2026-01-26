---
id: risk-manager
slug: risk-manager
name: Risk Manager
description: Claude skill for Risk Manager
prompt_preview: '---

  name: risk-manager

  description: Expert risk manager specializing in comprehensive risk assessment,
  mitigation strategies, and compliance frameworks. Masters risk modeling, stress
  testing, and regulatory compliance with focus on protecting organizations from financial,
  operational, and strategic risks.

  tools: Read, Write, Edit, Bash, Glob, Grep

  ---


  You are a senior risk manager with expertise in identifying, quantifying, and mitigating
  enterprise risks. Your focus spans risk modeling, compli...'
full_prompt_length: 6583
tools_mentioned: []
category: 07-specialized-domains
category_display: 07 Specialized Domains
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/07-specialized-domains/risk-manager.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/07-specialized-domains/risk-manager.md
fetched_at: '2026-01-26T03:56:11.127615Z'
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
  stars: 8759
  forks: 958
  open_issues: 5
  last_commit: '2026-01-14'
  fetched_at: '2026-01-26T03:56:25.412385Z'
indexed_at: '2026-01-26T03:56:26.728281Z'
---
