---
id: semgrep-rule-variant-creator-semgrep-rule-variant-creator
slug: semgrep-rule-variant-creator-semgrep-rule-variant-creator
name: Semgrep Rule Variant Creator
description: '- For applicability analysis guidance, see [applicability-analysis.md]({baseDir}/references/applicability-analysis.md)'
prompt_preview: "---\nname: semgrep-rule-variant-creator\ndescription: Creates language\
  \ variants of existing Semgrep rules. Use when porting a Semgrep rule to specified\
  \ target languages. Takes an existing rule and target languages as input, produces\
  \ independent rule+test directories for each language.\nallowed-tools:\n  - Bash\n\
  \  - Read\n  - Write\n  - Edit\n  - Glob\n  - Grep\n  - WebFetch\n---\n\n# Semgrep\
  \ Rule Variant Creator\n\nPort existing Semgrep rules to new target languages with\
  \ proper applicability analysis and test-..."
full_prompt_length: 8029
tools_mentioned:
- go
- Go
- Java
- java
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md
fetched_at: '2026-02-08T04:32:46.279375+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:05:25.905987Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt demonstrates excellent structure with clear sections, specific
      input/output specifications, and a well-defined 4-phase workflow. It includes
      valuable guardrails like 'Rationalizations to Reject' and strictness requirements.
      The only minor weakness is the incomplete sentence in the Foundational Knowledge
      section, but overall it's highly clear and actionable.
  usefulness:
    score: 4.5
    reasoning: This skill addresses a real-world need for security teams managing
      polyglot codebases who need to maintain consistent rule coverage across languages.
      The test-first approach and applicability analysis ensure quality, while the
      structured workflow prevents common pitfalls in rule porting. It's practical
      for security engineers and DevSecOps professionals.
  overall_rating: 4.5
  summary: A well-structured, practical skill for porting Semgrep security rules across
    languages with strong quality controls and clear workflow guidance.
  tags_suggested:
  - security
  - semgrep
  - static-analysis
  - rule-porting
  - test-driven
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.813261Z'
indexed_at: '2026-02-08T04:36:45.813284Z'
---
