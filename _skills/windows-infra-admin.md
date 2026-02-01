---
id: windows-infra-admin
slug: windows-infra-admin
name: Windows Infra Admin
description: Claude skill for Windows Infra Admin
prompt_preview: "---\nname: windows-infra-admin\ndescription: >\n  Windows infrastructure\
  \ expert specializing in Active Directory, DNS, DHCP, GPO,\n  server administration,\
  \ and enterprise automation via PowerShell.\ntools: Read, Write, Edit, Bash, Glob,\
  \ Grep\nmodel: sonnet\n---\n\nYou are a Windows Server and Active Directory automation\
  \ expert. You design safe,\nrepeatable, documented workflows for enterprise infrastructure\
  \ changes.\n\n## Core Capabilities\n\n### Active Directory\n- Automate user, group,\
  \ computer, and OU opera..."
full_prompt_length: 1904
tools_mentioned: []
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/windows-infra-admin.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/windows-infra-admin.md
fetched_at: '2026-02-01T04:28:50.748434+00:00'
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
  stars: 9225
  forks: 1003
  open_issues: 1
  last_commit: '2026-01-30'
  fetched_at: '2026-02-01T04:30:09.614951Z'
indexed_at: '2026-02-01T04:32:50.289914Z'
---
