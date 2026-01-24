---
id: pptx
slug: pptx
name: PPTX creation, editing, and analysis
description: '- **markitdown**: `pip install "markitdown[pptx]"` (for text extraction
  from presentations)'
prompt_preview: '---

  name: pptx

  description: "Presentation creation, editing, and analysis. When Claude needs to
  work with presentations (.pptx files) for: (1) Creating new presentations, (2) Modifying
  or editing content, (3) Working with layouts, (4) Adding comments or speaker notes,
  or any other presentation tasks"

  license: Proprietary. LICENSE.txt has complete terms

  ---


  # PPTX creation, editing, and analysis


  ## Overview


  A user may ask you to create, edit, or analyze the contents of a .pptx file. A .pptx
  fi...'
full_prompt_length: 25533
tools_mentioned:
- react
- JavaScript
- python
- rust
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/pptx/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md
fetched_at: '2026-01-24T03:26:06.792177Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:14:39.890747Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is well-structured with clear sections for different use
      cases (reading/analysis vs. creation) and provides specific technical instructions.
      However, it appears truncated at the end (cut off mid-sentence in the color
      palette section), which reduces clarity and completeness. The instructions for
      XML access and tool usage are specific and actionable.
  usefulness:
    score: 4.0
    reasoning: The skill provides practical workflows for common PowerPoint tasks
      like text extraction, XML analysis, and HTML-to-PPTX conversion. The inclusion
      of specific file paths and command examples makes it immediately actionable
      for developers. However, the truncated content and lack of complete guidance
      on the HTML-to-PPTX workflow limits its full practical value.
  overall_rating: 4.25
  summary: A technically sound prompt with clear workflows for PowerPoint manipulation,
    but the truncated content and incomplete sections prevent it from reaching its
    full potential as a comprehensive skill.
  tags_suggested:
  - pptx
  - powerpoint
  - xml
  - presentation
  - document-processing
github_metrics:
  stars: 51084
  forks: 4918
  open_issues: 184
  last_commit: '2025-12-20'
  fetched_at: '2026-01-24T03:26:18.386627Z'
indexed_at: '2026-01-24T03:26:19.678459Z'
---
