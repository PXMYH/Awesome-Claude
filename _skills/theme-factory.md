---
id: theme-factory
slug: theme-factory
name: Theme Factory Skill
description: '## Create your Own Theme'
prompt_preview: '---

  name: theme-factory

  description: Toolkit for styling artifacts with a theme. These artifacts can be
  slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with
  colors/fonts that you can apply to any artifact that has been creating, or can generate
  a new theme on-the-fly.

  license: Complete terms in LICENSE.txt

  ---



  # Theme Factory Skill


  This skill provides a curated collection of professional font and color themes themes,
  each with carefully selected color palettes a...'
full_prompt_length: 3124
tools_mentioned: []
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/theme-factory/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/theme-factory/SKILL.md
fetched_at: '2026-02-09T04:26:27.373060Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:15:12.570966Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is clear and well-structured with specific instructions
      for theme application, including a defined process and 10 pre-set themes. However,
      it lacks detail on how to actually implement the styling (e.g., specific tools
      or file formats), and edge cases like invalid theme selections or missing files
      aren't addressed. Best practices are partially followed with a structured workflow,
      but could be improved with more explicit constraints.
  usefulness:
    score: 4.5
    reasoning: This skill offers high practical value for creating visually consistent
      artifacts like slides or reports, saving time on design decisions. It covers
      the core task comprehensively with pre-set themes and custom theme generation,
      making it immediately actionable for users needing professional styling. The
      main limitation is dependency on external files (theme-showcase.pdf, themes/
      directory), which may not be available in all contexts.
  overall_rating: 4.25
  summary: A well-designed skill for theme application with clear structure and practical
    value, though implementation details and edge case handling could be more robust.
  tags_suggested:
  - styling
  - themes
  - design
  - presentation
  - customization
github_metrics:
  stars: 65988
  forks: 6576
  open_issues: 247
  last_commit: '2026-02-06'
  fetched_at: '2026-02-09T04:26:32.985453Z'
indexed_at: '2026-02-09T04:26:42.378191Z'
---
