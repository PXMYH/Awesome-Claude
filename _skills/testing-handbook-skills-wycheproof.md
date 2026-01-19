---
id: testing-handbook-skills-wycheproof
slug: testing-handbook-skills-wycheproof
name: Wycheproof
description: The investment in writing a reusable testing harness pays dividends through
  continuous validation as new test vectors are added to the Wycheproof repository.
prompt_preview: "---\nname: wycheproof\ntype: domain\ndescription: >\n  Wycheproof\
  \ provides test vectors for validating cryptographic implementations.\n  Use when\
  \ testing crypto code for known attacks and edge cases.\n---\n\n# Wycheproof\n\n\
  Wycheproof is an extensive collection of test vectors designed to verify the correctness\
  \ of cryptographic implementations and test against known attacks. Originally developed\
  \ by Google, it is now a community-managed project where contributors can add test\
  \ vectors for specific cryptogra..."
full_prompt_length: 19328
tools_mentioned:
- Python
- python
- JavaScript
- java
- javascript
- Java
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/testing-handbook-skills/skills/wycheproof/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/testing-handbook-skills/skills/wycheproof/SKILL.md
fetched_at: '2026-01-19T00:20:23.877940+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:28:14.479281Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, tables,
      and a logical flow from background to practical application. It follows best
      practices by defining scope, providing context, and offering specific guidance
      on when to use the tool versus alternatives. The only minor limitation is that
      it doesn't explicitly define the expected output format or response structure
      for the agent.
  usefulness:
    score: 5.0
    reasoning: This prompt provides immediate, actionable value for developers working
      with cryptographic implementations by offering concrete test scenarios, workflow
      guidance, and algorithm-specific recommendations. It covers real-world use cases
      like CI/CD integration and third-party code auditing, making it highly practical
      for security engineering tasks. The quick reference table and repository structure
      details enable users to quickly implement testing without extensive research.
  overall_rating: 4.75
  summary: This is a high-quality, comprehensive prompt that effectively transforms
    Wycheproof from a complex security tool into an accessible, actionable resource
    for developers, with excellent structure and practical guidance.
  tags_suggested:
  - cryptography
  - security testing
  - test vectors
  - cryptographic validation
  - security auditing
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:36.861542Z'
indexed_at: '2026-01-19T01:30:36.861548Z'
---
