---
id: testing-handbook-skills-constant-time-testing
slug: testing-handbook-skills-constant-time-testing
name: Constant-Time Testing
description: '- [Trail of Bits: Constant-Time Programming](https://www.youtube.com/watch?v=vW6wqTzfz5g)
  - Overview of constant-time programming principles and tools'
prompt_preview: "---\nname: constant-time-testing\ntype: domain\ndescription: >\n\
  \  Constant-time testing detects timing side channels in cryptographic code.\n \
  \ Use when auditing crypto implementations for timing vulnerabilities.\n---\n\n\
  # Constant-Time Testing\n\nTiming attacks exploit variations in execution time to\
  \ extract secret information from cryptographic implementations. Unlike cryptanalysis\
  \ that targets theoretical weaknesses, timing attacks leverage implementation flaws\
  \ - and they can affect any cryptographic co..."
full_prompt_length: 20621
tools_mentioned:
- aws
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/testing-handbook-skills/skills/constant-time-testing/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/testing-handbook-skills/skills/constant-time-testing/SKILL.md
fetched_at: '2026-01-25T03:52:43.271034+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:26:13.008019Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, definitions,
      and examples. It provides comprehensive background information and specific
      violation patterns. However, it lacks explicit instructions on what the AI should
      actually do with this knowledge - there's no clear task definition or expected
      output format.
  usefulness:
    score: 4.0
    reasoning: The content is highly valuable for security auditing and cryptography
      development, covering real-world attack vectors with academic references. It
      provides actionable patterns to identify. However, without clear task instructions,
      users may struggle to apply this knowledge practically in an automated workflow.
  overall_rating: 4.25
  summary: Excellent educational content on timing side-channel attacks, but needs
    clearer task definition to transform from reference material into an actionable
    skill.
  tags_suggested:
  - cryptography
  - security-audit
  - timing-attacks
  - side-channels
  - vulnerability-detection
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:53.157020Z'
indexed_at: '2026-01-25T04:05:53.157025Z'
---
