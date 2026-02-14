---
id: compliance-auditor
slug: compliance-auditor
name: Compliance Auditor
description: Claude skill for Compliance Auditor
prompt_preview: '---

  name: compliance-auditor

  description: "Use this agent when you need to achieve regulatory compliance, implement
  compliance controls, or prepare for audits across frameworks like GDPR, HIPAA, PCI
  DSS, SOC 2, and ISO standards."

  tools: Read, Grep, Glob

  model: opus

  ---


  You are a senior compliance auditor with deep expertise in regulatory compliance,
  data privacy laws, and security standards. Your focus spans GDPR, CCPA, HIPAA, PCI
  DSS, SOC 2, and ISO frameworks with emphasis on automated compl...'
full_prompt_length: 6865
tools_mentioned: []
category: quality-security
category_display: Quality & Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/compliance-auditor.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/compliance-auditor.md
fetched_at: '2026-02-14T04:09:46.816717Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:58:08.546696Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear categories and comprehensive
      checklists, but it's incomplete—the Development Workflow section cuts off mid-sentence
      during 'Test im' and lacks a conclusion. While the compliance frameworks and
      validation criteria are specific, the actual execution instructions are truncated,
      reducing clarity for the agent's operational steps.
  usefulness:
    score: 4.0
    reasoning: The prompt provides high practical value for compliance auditing with
      detailed regulatory frameworks, validation checklists, and structured protocols.
      However, the incomplete workflow limits immediate actionability, as users cannot
      fully implement the described process without inferring missing steps.
  overall_rating: 3.75
  summary: A strong compliance auditing prompt with excellent framework coverage and
    structured protocols, but severely hampered by an incomplete Development Workflow
    section that cuts off mid-sentence, reducing its operational clarity and immediate
    usability.
  tags_suggested:
  - compliance
  - auditing
  - regulatory
  - security
  - gdpr
  - hipaa
github_metrics:
  stars: 10374
  forks: 1101
  open_issues: 4
  last_commit: '2026-02-12'
  fetched_at: '2026-02-14T04:10:24.197233Z'
indexed_at: '2026-02-14T04:10:34.894991Z'
---
