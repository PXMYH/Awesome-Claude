---
id: dotnet-framework-4-8-expert
slug: dotnet-framework-4-8-expert
name: Dotnet Framework 4.8 Expert
description: Claude skill for Dotnet Framework 4.8 Expert
prompt_preview: '---

  name: dotnet-framework-4.8-expert

  description: "Use this agent when working on legacy .NET Framework 4.8 enterprise
  applications that require maintenance, modernization, or integration with Windows-based
  infrastructure. Specifically:\\n\\n<example>\\nContext: User has a legacy ASP.NET
  Web Forms application running on .NET Framework 4.8 that needs security updates
  and performance optimization.\\nuser: \"We have a 10-year-old Web Forms application
  with ViewState bloat and some outdated securit...'
full_prompt_length: 9707
tools_mentioned: []
category: language-specialists
category_display: Language Specialists
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/02-language-specialists/dotnet-framework-4.8-expert.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/02-language-specialists/dotnet-framework-4.8-expert.md
fetched_at: '2026-02-10T04:30:15.650417Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:50:36.358757Z'
  prompt_quality:
    score: 2.5
    reasoning: 'The prompt is highly specific about .NET Framework 4.8 technologies
      and includes comprehensive checklists for various components like Web Forms,
      WCF, and Windows services. However, it contains a critical flaw: the communication
      protocol section is incomplete and cuts off mid-sentence, which would cause
      execution failures. The prompt also lacks clear instructions on how to handle
      the context manager query or what to do when project context is unavailable.'
  usefulness:
    score: 4.0
    reasoning: The prompt demonstrates deep domain knowledge of legacy enterprise
      .NET development with detailed coverage of Web Forms, WCF services, Entity Framework
      6, and enterprise patterns. It provides practical value for maintaining and
      modernizing legacy systems, which is a common enterprise need. The comprehensive
      checklists and feature lists would help developers ensure they're using appropriate
      patterns and avoiding common pitfalls in legacy codebases.
  overall_rating: 3.25
  summary: A technically strong prompt with excellent domain expertise in legacy .NET
    Framework development, but severely undermined by an incomplete communication
    protocol section that would prevent proper execution.
  tags_suggested:
  - legacy-systems
  - enterprise-development
  - .net-framework
  - web-forms
  - wcf-services
  - windows-services
github_metrics:
  stars: 10075
  forks: 1084
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-10T04:30:47.641906Z'
indexed_at: '2026-02-10T04:30:57.087572Z'
---
