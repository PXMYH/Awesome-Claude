---
id: brand-guidelines
slug: brand-guidelines
name: Anthropic Brand Styling
description: '- Uses RGB color values for precise brand matching'
prompt_preview: '---

  name: brand-guidelines

  description: Applies Anthropic''s official brand colors and typography to any sort
  of artifact that may benefit from having Anthropic''s look-and-feel. Use it when
  brand colors or style guidelines, visual formatting, or company design standards
  apply.

  license: Complete terms in LICENSE.txt

  ---


  # Anthropic Brand Styling


  ## Overview


  To access Anthropic''s official brand identity and style resources, use this skill.


  **Keywords**: branding, corporate identity, visual iden...'
full_prompt_length: 2235
tools_mentioned:
- python
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/brand-guidelines/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md
fetched_at: '2026-01-22T03:46:50.017014Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:13:10.359464Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured with explicit
      color codes, font specifications, and fallback guidance. It defines scope (brand
      styling for artifacts), constraints (font availability), and provides technical
      implementation details. The only minor limitation is that it assumes specific
      tools (python-pptx) without broader applicability guidance.
  usefulness:
    score: 4.0
    reasoning: This skill provides high practical value for creating on-brand documents
      and presentations, especially for internal Anthropic work. It's immediately
      actionable with specific color codes and font names, though its utility is limited
      to environments where python-pptx is available and brand compliance is required.
      The comprehensive guidelines make it valuable for maintaining visual consistency.
  overall_rating: 4.25
  summary: A well-crafted, technically detailed prompt that effectively translates
    Anthropic's brand guidelines into actionable styling instructions, though its
    scope is somewhat constrained by specific tool dependencies.
  tags_suggested:
  - branding
  - visual-design
  - document-styling
  - corporate-identity
  - python-pptx
github_metrics:
  stars: 48287
  forks: 4573
  open_issues: 175
  last_commit: '2025-12-20'
  fetched_at: '2026-01-22T03:47:00.855764Z'
indexed_at: '2026-01-22T03:47:02.058995Z'
---
