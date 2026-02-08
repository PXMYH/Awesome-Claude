---
id: secure-code-guardian
slug: secure-code-guardian
name: Secure Code Guardian
description: OWASP Top 10, bcrypt/argon2, JWT, OAuth 2.0, OIDC, CSP, CORS, rate limiting,
  input validation, output encoding, encryption (AES, RSA), TLS, security headers
prompt_preview: "---\nname: secure-code-guardian\ndescription: Use when implementing\
  \ authentication/authorization, securing user input, or preventing OWASP Top 10\
  \ vulnerabilities. Invoke for authentication, authorization, input validation, encryption,\
  \ OWASP Top 10 prevention.\nlicense: MIT\nmetadata:\n  author: https://github.com/Jeffallan\n\
  \  version: \"1.0.0\"\n  domain: security\n  triggers: security, authentication,\
  \ authorization, encryption, OWASP, vulnerability, secure coding, password, JWT,\
  \ OAuth\n  role: specialist..."
full_prompt_length: 2977
tools_mentioned: []
category: community
category_display: Community
source_repo: jeffallan/claude-skills
source_path: skills/secure-code-guardian/SKILL.md
source_url: https://github.com/jeffallan/claude-skills/blob/main/skills/secure-code-guardian/SKILL.md
fetched_at: '2026-02-08T04:32:23.794592+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:00:49.992153Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear role definition,
      specific constraints, and actionable workflows. It follows best practices by
      defining triggers, scope, and output format upfront. The only minor limitation
      is the reference guide references external files that may not exist in all contexts,
      which could cause confusion if those resources aren't available.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate practical value for developers implementing
      security features, with comprehensive coverage of authentication, input validation,
      and OWASP prevention. The concrete constraints (e.g., 'hash passwords with bcrypt/argon2')
      and output templates make it highly actionable for real-world development tasks.
      It addresses critical security concerns that developers frequently encounter.
  overall_rating: 4.75
  summary: An excellent security-focused prompt that balances comprehensive guidance
    with practical constraints, making it highly valuable for secure code development.
  tags_suggested:
  - security
  - owasp
  - authentication
  - secure-coding
  - vulnerability-prevention
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.558214Z'
indexed_at: '2026-02-08T04:36:45.558219Z'
---
