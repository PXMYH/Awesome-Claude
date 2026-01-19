---
id: clinical-decision-support
slug: clinical-decision-support
name: Clinical Decision Support Documents
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: clinical-decision-support

  description: Generate professional clinical decision support (CDS) documents for
  pharmaceutical and clinical research settings, including patient cohort analyses
  (biomarker-stratified with outcomes) and treatment recommendation reports (evidence-based
  guidelines with decision algorithms). Supports GRADE evidence grading, statistical
  analysis (hazard ratios, survival curves, waterfall plots), biomarker integration,
  and regulatory compliance. Outputs publication...'
full_prompt_length: 27313
tools_mentioned:
- python
- go
- GCP
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/clinical-decision-support/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/clinical-decision-support/SKILL.md
fetched_at: '2026-01-19T00:19:06.162238+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:24:01.806862Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly specific and well-structured, clearly defining
      document types, capabilities, and clinical features. It includes excellent constraints
      (e.g., distinguishing from bedside treatment plans) and references complementary
      skills. However, it's truncated at the end, which slightly impacts completeness,
      and could benefit from more explicit output formatting instructions for LaTeX/PDF
      generation.
  usefulness:
    score: 4.0
    reasoning: This skill has high real-world value for pharmaceutical and clinical
      research professionals, covering critical tasks like cohort analysis and guideline
      development with regulatory compliance. It's comprehensive for its niche but
      may be overly specialized for general users, and the truncated description limits
      immediate actionability for some use cases.
  overall_rating: 4.25
  summary: A well-crafted, specialized prompt for clinical research documentation
    with strong specificity and practical value, though its truncated content and
    narrow focus slightly reduce its overall effectiveness.
  tags_suggested:
  - clinical-research
  - pharmaceutical
  - evidence-synthesis
  - latex
  - regulatory-compliance
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.606667Z'
indexed_at: '2026-01-19T01:30:35.606672Z'
---
