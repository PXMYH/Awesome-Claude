---
id: executing-plans
slug: executing-plans
name: Executing Plans
description: '## Remember'
prompt_preview: '---

  name: executing-plans

  description: Use when you have a written implementation plan to execute in a separate
  session with review checkpoints

  ---


  # Executing Plans


  ## Overview


  Load plan, review critically, execute tasks in batches, report for review between
  batches.


  **Core principle:** Batch execution with checkpoints for architect review.


  **Announce at start:** "I''m using the executing-plans skill to implement this plan."


  ## The Process


  ### Step 1: Load and Review Plan

  1. Read plan fil...'
full_prompt_length: 2171
tools_mentioned: []
category: community
category_display: Community Skills
source_repo: obra/superpowers
source_path: skills/executing-plans/SKILL.md
source_url: https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md
fetched_at: '2026-01-30T04:09:11.452547Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:17:31.876506Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, using a step-by-step
      process with explicit checkpoints and stop conditions. It follows best practices
      by defining a core principle, announcing usage, and providing fallback guidance
      for blockers. The only minor limitation is the reliance on external skills (like
      'finishing-a-development-branch') which are not defined within this prompt,
      potentially creating ambiguity if those skills are unavailable.
  usefulness:
    score: 4.5
    reasoning: This skill provides high real-world value for structured development
      tasks, especially for complex implementations requiring iterative review. It
      promotes safe execution by enforcing batch processing and mandatory verification,
      reducing the risk of uncontrolled changes. The actionability is strong for users
      with existing plans, though its utility depends on the availability of the referenced
      sub-skills.
  overall_rating: 4.5
  summary: A robust, well-structured prompt that excels at enforcing disciplined,
    batched execution of plans with critical review checkpoints, making it highly
    valuable for complex development workflows.
  tags_suggested:
  - development
  - planning
  - batch-execution
  - review-checkpoints
  - structured-workflow
github_metrics:
  stars: 40005
  forks: 3045
  open_issues: 111
  last_commit: '2026-01-23'
  fetched_at: '2026-01-30T04:09:17.723457Z'
indexed_at: '2026-01-30T04:09:18.556448Z'
---
