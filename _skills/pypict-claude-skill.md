---
id: pypict-claude-skill
slug: pypict-claude-skill
name: PICT Test Designer
description: '**Output:** 12-15 test cases covering all valid payment/shipping/user
  combinations with expected costs and outcomes.'
prompt_preview: '---

  name: pict-test-designer

  description: Design comprehensive test cases using PICT (Pairwise Independent Combinatorial
  Testing) for any piece of requirements or code. Analyzes inputs, generates PICT
  models with parameters, values, and constraints for valid scenarios using pairwise
  testing. Outputs the PICT model, markdown table of test cases, and expected results.

  ---


  # PICT Test Designer


  This skill enables systematic test case design using PICT (Pairwise Independent
  Combinatorial Testing)....'
full_prompt_length: 10928
tools_mentioned:
- PostgreSQL
- SQLite
- python
- MySQL
- Python
category: community
category_display: Community
source_repo: omkamal/pypict-claude-skill
source_path: SKILL.md
source_url: https://github.com/omkamal/pypict-claude-skill/blob/main/SKILL.md
fetched_at: '2026-02-01T04:29:39.821210+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:20:55.020062Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear workflow steps,
      specific examples, and comprehensive references. It follows best practices by
      defining when to use the skill, providing a step-by-step process, and including
      code examples. The only minor issue is the incomplete bash command at the end,
      which slightly impacts clarity.
  usefulness:
    score: 5.0
    reasoning: This skill addresses a real and valuable testing need—systematic test
      case design using pairwise combinatorial testing. It provides practical value
      by automating the complex process of generating comprehensive test cases with
      minimal redundancy. The inclusion of PICT model generation, markdown tables,
      and expected results makes it immediately actionable for developers and QA engineers.
  overall_rating: 4.75
  summary: An excellent, production-ready skill that provides significant value for
    systematic test design using PICT combinatorial testing, with clear workflow,
    practical examples, and comprehensive coverage of the testing methodology.
  tags_suggested:
  - testing
  - combinatorial-testing
  - pict
  - test-design
  - quality-assurance
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.843204Z'
indexed_at: '2026-02-01T04:32:50.843209Z'
---
