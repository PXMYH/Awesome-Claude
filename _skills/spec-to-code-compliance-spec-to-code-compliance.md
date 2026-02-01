---
id: spec-to-code-compliance-spec-to-code-compliance
slug: spec-to-code-compliance-spec-to-code-compliance
name: Spec-to-Code Compliance Checker Skill
description: '# END OF SKILL'
prompt_preview: '---

  name: spec-to-code-compliance

  description: Verifies code implements exactly what documentation specifies for blockchain
  audits. Use when comparing code against whitepapers, finding gaps between specs
  and implementation, or performing compliance checks for protocol implementations.

  ---


  ## When to Use


  Use this skill when you need to:

  - Verify code implements exactly what documentation specifies

  - Audit smart contracts against whitepapers or design documents

  - Find gaps between intended behav...'
full_prompt_length: 10252
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md
fetched_at: '2026-02-01T04:29:56.701732+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:24:18.783591Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and specific, with well-defined phases,
      rules, and rationalizations that prevent common AI hallucinations. It provides
      concrete triggers and edge case handling through its 'When NOT to Use' section
      and rationalizations table. The structured approach with Phase 0 and Phase 1
      demonstrates strong prompt engineering practices.
  usefulness:
    score: 4.0
    reasoning: This skill addresses a critical real-world need in blockchain security
      audits, where spec-to-code alignment is fundamental for compliance and vulnerability
      detection. The comprehensive framework covering documentation discovery, normalization,
      and evidence-based verification provides actionable value for auditors and developers.
      However, its utility is somewhat limited to blockchain contexts with formal
      specifications, reducing broader applicability.
  overall_rating: 4.25
  summary: A well-structured, high-quality prompt that provides a rigorous framework
    for spec-to-code compliance checking, particularly valuable for blockchain audits,
    though somewhat specialized in its domain focus.
  tags_suggested:
  - blockchain
  - security-audit
  - compliance-checking
  - specification-verification
  - smart-contracts
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.984437Z'
indexed_at: '2026-02-01T04:32:50.984443Z'
---
