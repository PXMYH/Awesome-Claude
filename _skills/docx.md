---
id: docx
slug: docx
name: DOCX creation, editing, and analysis
description: '- **pandoc**: `sudo apt-get install pandoc` (for text extraction)'
prompt_preview: '---

  name: docx

  description: "Comprehensive document creation, editing, and analysis with support
  for tracked changes, comments, formatting preservation, and text extraction. When
  Claude needs to work with professional documents (.docx files) for: (1) Creating
  new documents, (2) Modifying or editing content, (3) Working with tracked changes,
  (4) Adding comments, or any other document tasks"

  license: Proprietary. LICENSE.txt has complete terms

  ---


  # DOCX creation, editing, and analysis


  ## Overvi...'
full_prompt_length: 10150
tools_mentioned:
- Python
- TypeScript
- python
- JavaScript
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/docx/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md
fetched_at: '2026-02-02T04:24:27.083747Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:13:40.925713Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly structured with clear workflows and decision trees,
      making it easy to follow. It provides specific commands and file references,
      though it lacks explicit error handling guidance for edge cases like corrupted
      files or permission issues.
  usefulness:
    score: 4.5
    reasoning: This skill covers a comprehensive range of document operations from
      creation to analysis, addressing real-world professional needs. The workflows
      are practical and actionable, though the dependency on external files (docx-js.md,
      ooxml.md) creates a potential point of failure if those resources are unavailable.
  overall_rating: 4.5
  summary: A well-structured, practical skill for document manipulation that balances
    high-level workflows with technical implementation details, though it could benefit
    from more robust error handling and dependency management guidance.
  tags_suggested:
  - document-processing
  - office-documents
  - ooxml
  - workflow-automation
  - professional-tools
github_metrics:
  stars: 60457
  forks: 5911
  open_issues: 223
  last_commit: '2025-12-20'
  fetched_at: '2026-02-02T04:24:41.396011Z'
indexed_at: '2026-02-02T04:24:42.769226Z'
---
