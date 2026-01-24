---
id: internal-comms
slug: internal-comms
name: Internal Comms
description: Claude skill for Internal Comms
prompt_preview: '---

  name: internal-comms

  description: A set of resources to help me write all kinds of internal communications,
  using the formats that my company likes to use. Claude should use this skill whenever
  asked to write some sort of internal communications (status reports, leadership
  updates, 3P updates, company newsletters, FAQs, incident reports, project updates,
  etc.).

  license: Complete terms in LICENSE.txt

  ---


  ## When to use this skill

  To write internal communications, use this skill for:

  - 3P upd...'
full_prompt_length: 1511
tools_mentioned: []
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/internal-comms/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/internal-comms/SKILL.md
fetched_at: '2026-01-24T03:26:05.399899Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:14:02.805765Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly clear and specific, defining exact use cases and
      a structured workflow with explicit file references. It follows best practices
      by providing a clear trigger condition and a fallback for edge cases (asking
      for clarification). The only minor weakness is that it assumes the existence
      of specific external files, which could be a point of failure if those files
      are missing or inaccessible.
  usefulness:
    score: 4.5
    reasoning: This skill offers high real-world value by standardizing internal communications,
      which is a common and time-consuming business task. It is comprehensive for
      the listed communication types and immediately actionable for users who need
      to generate professional, consistent documents quickly. The utility is slightly
      capped by its dependency on pre-existing template files.
  overall_rating: 4.5
  summary: A well-structured and highly practical skill that effectively automates
    the creation of standardized internal communications, though its functionality
    relies on the availability of specific external guideline files.
  tags_suggested:
  - business communication
  - documentation
  - workflow automation
  - content generation
github_metrics:
  stars: 51084
  forks: 4918
  open_issues: 184
  last_commit: '2025-12-20'
  fetched_at: '2026-01-24T03:26:18.386627Z'
indexed_at: '2026-01-24T03:26:19.667356Z'
---
