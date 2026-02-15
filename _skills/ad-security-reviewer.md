---
id: ad-security-reviewer
slug: ad-security-reviewer
name: Ad Security Reviewer
description: Claude skill for Ad Security Reviewer
prompt_preview: '---

  name: ad-security-reviewer

  description: "Use this agent when you need to audit Active Directory security posture,
  evaluate privilege escalation risks, review identity delegation patterns, or assess
  authentication protocol hardening."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are an AD security posture analyst who evaluates identity attack paths,

  privilege escalation vectors, and domain hardening gaps. You provide safe and

  actionable recommendations based on best practic...'
full_prompt_length: 2354
tools_mentioned: []
category: quality-security
category_display: Quality Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/ad-security-reviewer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/ad-security-reviewer.md
fetched_at: '2026-02-15T04:21:29.193809+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:57:20.965321Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections for
      capabilities, checklists, and integration. It uses specific Active Directory
      terminology and defines a comprehensive scope. However, it lacks explicit handling
      of edge cases like multi-forest environments or hybrid cloud scenarios, and
      doesn't provide fallback guidance for when certain tools or data sources might
      be unavailable.
  usefulness:
    score: 5.0
    reasoning: This prompt delivers high real-world value by addressing critical AD
      security concerns with actionable checklists and deliverables. It comprehensively
      covers identity attack paths, privilege escalation, and domain hardening with
      specific technical areas like LDAP signing, GPO security, and attack surface
      reduction. The integration section with other agents shows practical workflow
      planning for enterprise security operations.
  overall_rating: 4.75
  summary: This is a highly effective security specialist prompt with excellent structure,
    comprehensive coverage of AD security domains, and practical deliverables that
    would immediately benefit security professionals conducting enterprise AD assessments.
  tags_suggested:
  - Active Directory
  - Security Hardening
  - Identity Management
  - Enterprise Security
  - Privilege Escalation
github_metrics:
  stars: 10437
  forks: 1106
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-15T04:22:41.501003Z'
indexed_at: '2026-02-15T04:33:50.561779Z'
---
