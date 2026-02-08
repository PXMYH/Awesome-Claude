---
id: security-reviewer
slug: security-reviewer
name: Security Reviewer
description: OWASP Top 10, CWE, Semgrep, Bandit, ESLint Security, gosec, npm audit,
  gitleaks, trufflehog, CVSS scoring, nmap, Burp Suite, sqlmap, Trivy, Checkov, HashiCorp
  Vault, AWS Security Hub, CIS benchmarks, ...
prompt_preview: "---\nname: security-reviewer\ndescription: Use when conducting security\
  \ audits, reviewing code for vulnerabilities, or analyzing infrastructure security.\
  \ Invoke for SAST scans, penetration testing, DevSecOps practices, cloud security\
  \ reviews.\nlicense: MIT\nallowed-tools: Read, Grep, Glob, Bash\nmetadata:\n  author:\
  \ https://github.com/Jeffallan\n  version: \"1.0.0\"\n  domain: security\n  triggers:\
  \ security review, vulnerability scan, SAST, security audit, penetration test, code\
  \ audit, security analysis, i..."
full_prompt_length: 3683
tools_mentioned:
- kubernetes
- AWS
category: community
category_display: Community
source_repo: jeffallan/claude-skills
source_path: skills/security-reviewer/SKILL.md
source_url: https://github.com/jeffallan/claude-skills/blob/main/skills/security-reviewer/SKILL.md
fetched_at: '2026-02-08T04:32:23.936584+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:01:15.346389Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt demonstrates strong clarity and specificity with well-defined
      role, workflow, and constraints. It follows excellent prompt engineering practices
      by including triggers, allowed tools, and output format. However, it lacks explicit
      edge case handling for scenarios like missing authorization or unavailable tools,
      and the reference file paths may not be accessible in all environments.
  usefulness:
    score: 4.0
    reasoning: The skill provides high real-world value for security professionals
      with comprehensive coverage of security review tasks and actionable remediation
      guidance. It covers multiple security domains (code, infrastructure, cloud)
      and includes practical tools and methodologies. The main limitation is dependency
      on external reference files that may not exist, reducing immediate usability
      without proper setup.
  overall_rating: 4.25
  summary: A well-structured security review skill with strong prompt engineering
    that provides comprehensive security analysis capabilities, though it requires
    proper reference file setup for full functionality.
  tags_suggested:
  - security
  - code-review
  - vulnerability-assessment
  - devsecops
  - penetration-testing
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.561974Z'
indexed_at: '2026-02-08T04:36:45.561979Z'
---
