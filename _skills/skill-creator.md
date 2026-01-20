---
id: skill-creator
slug: skill-creator
name: Skill Creator
description: 1. Use the skill on real tasks
prompt_preview: '---

  name: skill-creator

  description: Guide for creating effective skills. This skill should be used when
  users want to create a new skill (or update an existing skill) that extends Claude''s
  capabilities with specialized knowledge, workflows, or tool integrations.

  license: Complete terms in LICENSE.txt

  ---


  # Skill Creator


  This skill provides guidance for creating effective skills.


  ## About Skills


  Skills are modular, self-contained packages that extend Claude''s capabilities by
  providing

  specia...'
full_prompt_length: 17701
tools_mentioned:
- aws
- gcp
- Python
- Azure
- AWS
- GCP
- azure
- React
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/skill-creator/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
fetched_at: '2026-01-20T03:43:13.337657Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:14:50.112847Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, with a logical
      flow from core principles to practical anatomy. It provides specific guidance
      on context window management and appropriate degrees of freedom, though it's
      incomplete (cuts off mid-sentence in the references section). The YAML frontmatter
      requirements are clearly defined.
  usefulness:
    score: 4.0
    reasoning: This skill provides high practical value for users creating custom
      skills, offering concrete frameworks for decision-making and structure. It's
      actionable and addresses real development challenges like token efficiency and
      context management. However, its incomplete state limits immediate utility,
      and it assumes familiarity with the skill ecosystem.
  overall_rating: 4.25
  summary: A well-crafted, principled guide for skill creation that balances conciseness
    with practical guidance, though its incomplete presentation prevents full evaluation
    of its comprehensive value.
  tags_suggested:
  - skill-creation
  - prompt-engineering
  - documentation
  - best-practices
github_metrics:
  stars: 45847
  forks: 4315
  open_issues: 169
  last_commit: '2025-12-20'
  fetched_at: '2026-01-20T03:43:25.558111Z'
indexed_at: '2026-01-20T03:43:26.916174Z'
---
