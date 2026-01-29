---
id: xlsx
slug: xlsx
name: Requirements for Outputs
description: '**For Excel files themselves**:'
prompt_preview: '---

  name: xlsx

  description: "Comprehensive spreadsheet creation, editing, and analysis with support
  for formulas, formatting, data analysis, and visualization. When Claude needs to
  work with spreadsheets (.xlsx, .xlsm, .csv, .tsv, etc) for: (1) Creating new spreadsheets
  with formulas and formatting, (2) Reading or analyzing data, (3) Modify existing
  spreadsheets while preserving formulas, (4) Data analysis and visualization in spreadsheets,
  or (5) Recalculating formulas"

  license: Proprietary. LI...'
full_prompt_length: 10628
tools_mentioned:
- Python
- python
category: official
category_display: Official Anthropic Skills
source_repo: anthropics/skills
source_path: skills/xlsx/SKILL.md
source_url: https://github.com/anthropics/skills/blob/main/skills/xlsx/SKILL.md
fetched_at: '2026-01-29T04:07:13.128736Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:15:44.771179Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly specific and clear, with well-defined standards
      for financial modeling (color coding, formatting, formula construction). It
      provides concrete examples and actionable rules. However, the prompt appears
      incomplete as it cuts off mid-sentence in the pandas code example, which reduces
      clarity for the intended workflow.
  usefulness:
    score: 4.0
    reasoning: The requirements are extremely practical for financial modeling and
      spreadsheet tasks, covering real-world needs like error prevention, documentation
      standards, and industry conventions. The LibreOffice requirement is a practical
      constraint for formula recalculation. The incomplete pandas section limits immediate
      actionability for data analysis workflows.
  overall_rating: 4.25
  summary: A strong, detailed prompt for financial spreadsheet standards that provides
    clear, industry-relevant guidelines, but is incomplete and cuts off during the
    technical implementation section.
  tags_suggested:
  - financial_modeling
  - spreadsheet
  - excel
  - data_analysis
  - formula_validation
github_metrics:
  stars: 57260
  forks: 5595
  open_issues: 207
  last_commit: '2025-12-20'
  fetched_at: '2026-01-29T04:07:19.542479Z'
indexed_at: '2026-01-29T04:07:20.789256Z'
---
