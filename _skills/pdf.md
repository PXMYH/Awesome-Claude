---
id: pdf
slug: pdf
name: PDF Processing Guide
description: '- For advanced pypdfium2 usage, see reference.md'
prompt_preview: '---

  name: pdf

  description: Comprehensive PDF manipulation toolkit for extracting text and tables,
  creating new PDFs, merging/splitting documents, and handling forms. When Claude
  needs to fill in a PDF form or programmatically process, generate, or analyze PDF
  documents at scale.

  license: Proprietary. LICENSE.txt has complete terms

  ---


  # PDF Processing Guide


  ## Overview


  This guide covers essential PDF processing operations using Python libraries and
  command-line tools. For advanced features, J...'
full_prompt_length: 7068
tools_mentioned:
- python
- JavaScript
- Python
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/pdf/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md
fetched_at: '2026-01-23T03:41:59.542341Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:14:25.481483Z'
  prompt_quality:
    score: 2.5
    reasoning: The prompt provides clear code examples for common PDF operations,
      but lacks critical context about required installations, environment setup,
      and error handling. The incomplete code snippet at the end demonstrates poor
      attention to detail, and there's no guidance on handling edge cases like corrupted
      files or permission issues.
  usefulness:
    score: 3.5
    reasoning: The skill covers practical PDF manipulation tasks including text extraction,
      table extraction, merging, splitting, and creation, which are valuable for real-world
      document processing workflows. However, the incomplete example and missing installation
      instructions reduce immediate usability, requiring users to research additional
      setup steps.
  overall_rating: 3.0
  summary: A moderately useful PDF processing guide with practical code examples,
    but significantly hampered by an incomplete code snippet and missing setup instructions
    that would hinder immediate implementation.
  tags_suggested:
  - pdf
  - document-processing
  - python
  - text-extraction
  - table-extraction
github_metrics:
  stars: 49819
  forks: 4771
  open_issues: 180
  last_commit: '2025-12-20'
  fetched_at: '2026-01-23T03:42:11.995098Z'
indexed_at: '2026-01-23T03:42:13.394693Z'
---
