---
id: blueprint-generate
slug: blueprint-generate
name: Blueprint Generate
description: Claude skill for Blueprint Generate
prompt_preview: '---

  name: blueprint-generate

  description: End the Q&A phase and generate the plan. Use after the blueprint skill
  has gathered enough context.

  ---


  ## Blueprint — Generate plan


  Generate an implementation plan from the Q&A session.


  ### Step 1: Resolve template


  Recall the template name from the blueprint Q&A conversation. Read [references/templates.json](references/templates.json)
  and find the matching template.


  ### Step 2: Generate slug


  Create a concise 2-5 word kebab-case slug (max 50 chars)...'
full_prompt_length: 1322
tools_mentioned: []
category: community
category_display: Community
source_repo: imbue-ai/blueprint
source_path: skills/blueprint-generate/SKILL.md
source_url: https://github.com/imbue-ai/blueprint/blob/main/skills/blueprint-generate/SKILL.md
fetched_at: '2026-06-21T06:51:18.432572+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-21T08:58:02.690351Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9b02540 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9b02540 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-21T10:34:01.866079Z'
indexed_at: '2026-06-21T10:34:01.866085Z'
---
