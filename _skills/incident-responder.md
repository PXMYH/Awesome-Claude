---
id: incident-responder
slug: incident-responder
name: Incident Responder
description: Claude skill for Incident Responder
prompt_preview: '---

  name: incident-responder

  description: Expert incident responder specializing in security and operational
  incident management. Masters evidence collection, forensic analysis, and coordinated
  response with focus on minimizing impact and preventing future incidents.

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior incident responder with expertise in managing both security breaches
  and operational incidents. Your focus spans rapid response, evidence preservation,
  i...'
full_prompt_length: 7101
tools_mentioned: []
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/incident-responder.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/incident-responder.md
fetched_at: '2026-02-03T04:14:27.996647Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:55:33.398305Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, comprehensive
      checklists, and detailed procedures. It follows best practices by defining specific
      tools, workflows, and communication protocols. However, it has some ambiguity
      in the 'When invoked' section where it references querying a 'context manager'
      without defining how this interaction occurs, which could create confusion about
      execution flow.
  usefulness:
    score: 4.0
    reasoning: The prompt provides substantial real-world value with detailed incident
      response frameworks covering security breaches, service outages, and operational
      incidents. It includes actionable checklists, classification systems, and procedures
      that would benefit actual incident management. The main limitation is that it's
      more of a reference guide than a focused operational skill, potentially overwhelming
      users with comprehensive but broad guidance.
  overall_rating: 4.25
  summary: A comprehensive and well-structured incident response prompt with excellent
    procedural detail and best practices, though slightly hampered by ambiguous context
    manager references and broad scope that may reduce immediate actionability.
  tags_suggested:
  - incident-response
  - security
  - operations
  - forensics
  - compliance
github_metrics:
  stars: 9412
  forks: 1016
  open_issues: 2
  last_commit: '2026-01-30'
  fetched_at: '2026-02-03T04:14:50.582017Z'
indexed_at: '2026-02-03T04:14:51.589155Z'
---
