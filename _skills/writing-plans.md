---
id: writing-plans
slug: writing-plans
name: Writing Plans
description: '**If Parallel Session chosen:**'
prompt_preview: '---

  name: writing-plans

  description: Use when you have a spec or requirements for a multi-step task, before
  touching code

  ---


  # Writing Plans


  ## Overview


  Write comprehensive implementation plans assuming the engineer has zero context
  for our codebase and questionable taste. Document everything they need to know:
  which files to touch for each task, code, testing, docs they might need to check,
  how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent
  commits.


  Ass...'
full_prompt_length: 3264
tools_mentioned:
- python
- pytest
category: community
category_display: Community Skills
source_repo: obra/superpowers
source_path: skills/writing-plans/SKILL.md
source_url: https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
fetched_at: '2026-01-30T04:09:15.549304Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:19:38.556178Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and specific, defining exact file
      paths, code snippets, and commands. It follows strong prompt engineering practices
      by setting explicit constraints (zero context, questionable taste) and providing
      a rigid structure. The only minor deduction is for the slightly ambiguous 'questionable
      taste' assumption, which could be interpreted differently.
  usefulness:
    score: 5.0
    reasoning: This skill provides immense real-world value for complex development
      tasks by enforcing TDD, DRY, and YAGNI principles. It comprehensively covers
      implementation from test to commit, making it highly actionable for engineers.
      The execution handoff options add practical flexibility for different workflow
      preferences.
  overall_rating: 4.75
  summary: An outstanding prompt that creates a rigorous, executable implementation
    plan with exceptional clarity and practical utility for software development.
  tags_suggested:
  - planning
  - tdd
  - implementation
  - documentation
  - code-generation
github_metrics:
  stars: 40005
  forks: 3045
  open_issues: 111
  last_commit: '2026-01-23'
  fetched_at: '2026-01-30T04:09:17.723457Z'
indexed_at: '2026-01-30T04:09:18.592969Z'
---
