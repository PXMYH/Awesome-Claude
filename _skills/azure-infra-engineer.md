---
id: azure-infra-engineer
slug: azure-infra-engineer
name: Azure Infra Engineer
description: Claude skill for Azure Infra Engineer
prompt_preview: '---

  name: azure-infra-engineer

  description: "Use when designing, deploying, or managing Azure infrastructure with
  focus on network architecture, Entra ID integration, PowerShell automation, and
  Bicep IaC. Specifically:\\n\\n<example>\\nContext: Building a multi-region Azure
  infrastructure with hybrid identity and secure networking for an enterprise migration\\nuser:
  \"We''re migrating on-premises workloads to Azure. Need multi-region infrastructure
  with VNets, NSGs, Azure Firewall, Entra ID sync...'
full_prompt_length: 5598
tools_mentioned:
- Azure
- azure
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/azure-infra-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/azure-infra-engineer.md
fetched_at: '2026-02-09T04:26:09.060130Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:54:27.310367Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly structured and clear, with a well-defined scope
      and specific capabilities. It follows best practices by including a description,
      tools, core capabilities, and integration notes. However, it lacks explicit
      edge-case handling or fallback guidance for ambiguous user requests, which prevents
      a perfect score.
  usefulness:
    score: 5.0
    reasoning: This skill has high real-world value for Azure infrastructure tasks,
      covering essential areas like IaC, automation, and security. It is comprehensive
      for its domain and actionable, enabling users to immediately leverage it for
      deployment, automation, and optimization tasks in Azure environments.
  overall_rating: 4.75
  summary: A well-crafted, practical skill for Azure infrastructure engineering with
    strong clarity and high utility, though it could benefit from more explicit edge-case
    guidance.
  tags_suggested:
  - Azure
  - Infrastructure
  - Automation
  - PowerShell
  - Bicep
  - DevOps
github_metrics:
  stars: 9985
  forks: 1081
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-09T04:26:32.597214Z'
indexed_at: '2026-02-09T04:26:41.978048Z'
---
