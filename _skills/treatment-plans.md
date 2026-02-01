---
id: treatment-plans
slug: treatment-plans
name: Treatment Plan Writing
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: treatment-plans

  description: Generate concise (3-4 page), focused medical treatment plans in LaTeX/PDF
  format for all clinical specialties. Supports general medical treatment, rehabilitation
  therapy, mental health care, chronic disease management, perioperative care, and
  pain management. Includes SMART goal frameworks, evidence-based interventions with
  minimal text citations, regulatory compliance (HIPAA), and professional formatting.
  Prioritizes brevity and clinical actionability.

  all...'
full_prompt_length: 53429
tools_mentioned:
- go
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/treatment-plans/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/treatment-plans/SKILL.md
fetched_at: '2026-02-01T04:28:38.549708+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:45:59.424032Z'
  prompt_quality:
    score: 4.5
    reasoning: 'The prompt is highly structured with clear sections, specific constraints
      (3-4 pages), and defined scope across medical specialties. It follows best practices
      by including a mandatory visual enhancement requirement and providing explicit
      tool usage guidance. However, it has a critical flaw: the ''scientific-schematics''
      skill and related bash commands are referenced but not defined in the allowed-tools
      list, creating ambiguity about actual execution capabilities.'
  usefulness:
    score: 4.0
    reasoning: The skill addresses a genuine need for standardized, compliant medical
      documentation with practical templates and frameworks. It provides actionable
      guidance for multiple clinical scenarios and emphasizes evidence-based, patient-centered
      care. The mandatory visual component, while potentially burdensome, could enhance
      communication in complex treatment plans, though the unclear tool integration
      limits immediate usability.
  overall_rating: 4.25
  summary: A well-structured prompt with strong clinical focus and clear constraints,
    but undermined by inconsistent tool definitions that may hinder practical implementation.
  tags_suggested:
  - medical-documentation
  - latex
  - clinical-workflows
  - evidence-based-medicine
  - regulatory-compliance
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.098278Z'
indexed_at: '2026-02-01T04:32:50.098284Z'
---
