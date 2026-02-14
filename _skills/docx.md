---
id: docx
slug: docx
name: DOCX creation, editing, and analysis
description: '- **pandoc**: Text extraction'
prompt_preview: '---

  name: docx

  description: "Use this skill whenever the user wants to create, read, edit, or manipulate
  Word documents (.docx files). Triggers include: any mention of \"Word doc\", \"word
  document\", \".docx\", or requests to produce professional documents with formatting
  like tables of contents, headings, page numbers, or letterheads. Also use when extracting
  or reorganizing content from .docx files, inserting or replacing images in documents,
  performing find-and-replace in Word files, working...'
full_prompt_length: 17113
tools_mentioned:
- Python
- JavaScript
- javascript
- python
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/docx/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md
fetched_at: '2026-02-14T04:10:10.958358Z'
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
  stars: 69457
  forks: 7009
  open_issues: 271
  last_commit: '2026-02-06'
  fetched_at: '2026-02-14T04:10:24.914857Z'
indexed_at: '2026-02-14T04:10:35.186668Z'
---
