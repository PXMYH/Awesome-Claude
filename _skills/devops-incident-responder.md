---
id: devops-incident-responder
slug: devops-incident-responder
name: Devops Incident Responder
description: Claude skill for Devops Incident Responder
prompt_preview: '---

  name: devops-incident-responder

  description: "Use when actively responding to production incidents, diagnosing critical
  service failures, or conducting incident postmortems to implement permanent fixes
  and preventative measures."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior DevOps incident responder with expertise in managing critical production
  incidents, performing rapid diagnostics, and implementing permanent fixes. Your
  focus spans incident detection, re...'
full_prompt_length: 6801
tools_mentioned: []
category: infrastructure
category_display: Infrastructure
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/03-infrastructure/devops-incident-responder.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/devops-incident-responder.md
fetched_at: '2026-02-17T04:19:55.638237Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:55:23.023436Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear sections and specific metrics,
      but it's incomplete and ends abruptly during the 'Preparedness Analysis' section.
      While the content is specific and follows good prompt engineering practices
      with structured checklists and protocols, the incomplete nature reduces clarity
      and leaves critical gaps in the workflow.
  usefulness:
    score: 4.0
    reasoning: The prompt provides comprehensive real-world value with detailed incident
      response frameworks, measurable targets (MTTD/MTTA/MTTR), and systematic approaches
      to DevOps incidents. It covers detection, diagnosis, response coordination,
      and postmortem processes that would immediately benefit teams handling production
      incidents.
  overall_rating: 3.75
  summary: A valuable but incomplete DevOps incident response prompt that provides
    excellent frameworks and metrics but needs completion to be fully functional.
  tags_suggested:
  - incident-response
  - devops
  - production-support
  - observability
  - root-cause-analysis
github_metrics:
  stars: 10561
  forks: 1120
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-17T04:20:20.236835Z'
indexed_at: '2026-02-17T04:20:37.806970Z'
---
