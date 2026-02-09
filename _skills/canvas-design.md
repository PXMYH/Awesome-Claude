---
id: canvas-design
slug: canvas-design
name: Canvas Design
description: Claude skill for Canvas Design
prompt_preview: '---

  name: canvas-design

  description: Create beautiful visual art in .png and .pdf documents using design
  philosophy. You should use this skill when the user asks to create a poster, piece
  of art, design, or other static piece. Create original visual designs, never copying
  existing artists'' work to avoid copyright violations.

  license: Complete terms in LICENSE.txt

  ---


  These are instructions for creating design philosophies - aesthetic movements that
  are then EXPRESSED VISUALLY. Output only .md f...'
full_prompt_length: 11937
tools_mentioned:
- Go
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/canvas-design/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md
fetched_at: '2026-02-09T04:26:24.804018Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:13:20.655168Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and specific, with a well-defined
      two-step process that guides the AI through philosophy creation and visual expression.
      It provides strong examples and emphasizes critical aspects like craftsmanship
      and visual-first communication. However, it lacks explicit handling of edge
      cases (e.g., what to do if the user's input is too vague or contradictory) and
      could benefit from more structured output formatting instructions for the .md
      file.
  usefulness:
    score: 4.0
    reasoning: This skill is highly practical for creative tasks like generating posters,
      art, or design concepts, offering a structured approach that encourages originality
      and high-quality output. It covers the core task comprehensively with philosophical
      depth, making it actionable for users seeking visually-driven results. However,
      its utility is somewhat niche, primarily benefiting users in design, art, or
      creative fields rather than broader development tasks.
  overall_rating: 4.25
  summary: A well-crafted prompt that excels in guiding creative visual design with
    strong philosophical framing and emphasis on craftsmanship, though it could improve
    on edge case handling and broader applicability.
  tags_suggested:
  - creative design
  - visual art
  - philosophy-driven
  - originality-focused
github_metrics:
  stars: 65988
  forks: 6576
  open_issues: 247
  last_commit: '2026-02-06'
  fetched_at: '2026-02-09T04:26:32.985453Z'
indexed_at: '2026-02-09T04:26:42.340250Z'
---
