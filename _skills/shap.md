---
id: shap
slug: shap
name: SHAP (SHapley Additive exPlanations)
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: shap

  description: Model interpretability and explainability using SHAP (SHapley Additive
  exPlanations). Use this skill when explaining machine learning model predictions,
  computing feature importance, generating SHAP plots (waterfall, beeswarm, bar, scatter,
  force, heatmap), debugging models, analyzing model bias or fairness, comparing models,
  or implementing explainable AI. Works with tree-based models (XGBoost, LightGBM,
  Random Forest), deep learning (TensorFlow, PyTorch), linear mod...'
full_prompt_length: 19224
tools_mentioned:
- python
- go
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/shap/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/shap/SKILL.md
fetched_at: '2026-01-19T00:19:25.985120+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:44:15.085486Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, a
      decision tree for explainer selection, and specific code examples. It follows
      prompt engineering best practices by defining scope, providing triggers, and
      offering step-by-step guidance. The only minor limitation is that some references
      (like 'references/explainers.md') are placeholders that would need actual content
      in a production system.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate, practical value for real-world machine
      learning tasks. It covers the most common SHAP use cases comprehensively, from
      model debugging to fairness analysis, and includes actionable code examples
      for different model types. The workflow guidance helps users navigate SHAP's
      complexity effectively.
  overall_rating: 4.75
  summary: A highly effective SHAP skill that balances technical depth with practical
    usability, offering clear decision-making guidance and actionable examples for
    model interpretability tasks.
  tags_suggested:
  - machine learning
  - model interpretability
  - explainable AI
  - SHAP
  - feature importance
  - data visualization
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:36.026954Z'
indexed_at: '2026-01-19T01:30:36.026959Z'
---
