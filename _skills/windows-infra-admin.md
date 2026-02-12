---
id: windows-infra-admin
slug: windows-infra-admin
name: Windows Infra Admin
description: Claude skill for Windows Infra Admin
prompt_preview: '---

  name: windows-infra-admin

  description: "Use when managing Windows Server infrastructure, Active Directory,
  DNS, DHCP, and Group Policy configurations, especially for enterprise-scale deployments
  requiring safe automation and compliance validation."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a Windows Server and Active Directory automation expert. You design safe,

  repeatable, documented workflows for enterprise infrastructure changes.


  ## Core Capabilities


  ### Acti...'
full_prompt_length: 1963
tools_mentioned: []
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/windows-infra-admin.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/windows-infra-admin.md
fetched_at: '2026-02-12T04:24:11.033156Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:56:57.439170Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly clear and specific, defining a precise scope (Active
      Directory, DNS, DHCP, GPO, server administration) and expected behaviors (safe,
      repeatable, documented workflows). It follows best practices by including structured
      sections (Core Capabilities, Checklists, Example Use Cases) and explicitly lists
      tools and integration points. However, it lacks explicit edge-case handling
      or fallback guidance for scenarios like permission failures or partial failures
      during automation.
  usefulness:
    score: 4.5
    reasoning: This skill offers high real-world value for IT administrators managing
      Windows infrastructure, providing actionable checklists and example use cases
      for common tasks like migrations and restructuring. It is comprehensive in covering
      key enterprise domains (AD, DNS, DHCP, GPO) and promotes safety through pre-change
      verification and rollback planning. Users can immediately benefit from the structured
      approach to automate and document infrastructure changes.
  overall_rating: 4.5
  summary: A well-structured, practical prompt that excels in clarity and real-world
    applicability for Windows infrastructure automation, though it could be strengthened
    with more explicit edge-case handling.
  tags_suggested:
  - windows
  - active-directory
  - powershell
  - infrastructure-automation
  - enterprise-it
github_metrics:
  stars: 10218
  forks: 1093
  open_issues: 4
  last_commit: '2026-02-10'
  fetched_at: '2026-02-12T04:24:36.992823Z'
indexed_at: '2026-02-12T04:24:46.587005Z'
---
