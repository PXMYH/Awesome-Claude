---
id: ask-questions-if-underspecified-ask-questions-if-underspecified
slug: ask-questions-if-underspecified-ask-questions-if-underspecified
name: Ask Questions If Underspecified
description: '- Don''t ask questions you can answer with a quick, low-risk discovery
  read (e.g., configs, existing patterns, docs).'
prompt_preview: '---

  name: ask-questions-if-underspecified

  description: Clarify requirements before implementing. Use when serious doubts arise.

  ---


  # Ask Questions If Underspecified


  ## When to Use


  Use this skill when a request has multiple plausible interpretations or key details
  (objective, scope, constraints, environment, or safety) are unclear.


  ## When NOT to Use


  Do not use this skill when the request is already clear, or when a quick, low-risk
  discovery read can answer the missing details.


  ## Goal


  As...'
full_prompt_length: 3987
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/ask-questions-if-underspecified/skills/ask-questions-if-underspecified/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/ask-questions-if-underspecified/skills/ask-questions-if-underspecified/SKILL.md
fetched_at: '2026-02-08T04:32:38.666315+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:22:00.727244Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and specific, defining precise criteria
      for when to use the skill, a structured workflow, and concrete question templates.
      It handles edge cases by explicitly stating what to do if the user wants to
      proceed without answers and includes anti-patterns to guide behavior. It follows
      best practices by emphasizing scannability, offering defaults, and separating
      must-have from nice-to-have questions.
  usefulness:
    score: 5.0
    reasoning: This skill has high real-world value for preventing wasted effort in
      development by ensuring requirements are clarified upfront. It is comprehensive,
      covering key ambiguity dimensions like scope, constraints, and safety, and is
      immediately actionable with its structured workflow and templates. Users can
      directly apply this to reduce errors and improve efficiency in tasks like coding
      or system design.
  overall_rating: 4.75
  summary: A well-crafted, highly practical skill that effectively addresses underspecified
    requests with clear guidelines and actionable templates, making it a valuable
    tool for security and development workflows.
  tags_suggested:
  - clarification
  - requirements-gathering
  - security
  - development-workflow
  - risk-mitigation
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.731881Z'
indexed_at: '2026-02-08T04:36:45.731886Z'
---
