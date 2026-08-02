---
id: ru-check
slug: ru-check
name: Russian Text Quality Check
description: 'Return:'
prompt_preview: "---\nname: ru-check\ndescription: >\n  Full Russian text quality\
  \ check against the whole corpus. Triggers: вычитай, вычитай через\n  ru-text, прогони\
  \ ru-text, проверь текст по ru-text, ru-check, полная вычитка. Use when the\n  user\
  \ asks to proofread Russian text, or when a project gate names ru-text. Returns\
  \ findings\n  with the rule behind each and a proposed replacement; never edits\
  \ a file. Self-initiated\n  runs start with a fast triage and escalate on evidence;\
  \ an explicit request always runs the..."
full_prompt_length: 8599
tools_mentioned:
- rest
category: community
category_display: Community
source_repo: talkstream/ru-text
source_path: skills/ru-check/SKILL.md
source_url: https://github.com/talkstream/ru-text/blob/main/skills/ru-check/SKILL.md
fetched_at: '2026-08-02T05:31:03.970180+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-08-02T09:09:42.060626Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0acaed7c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0acaed7c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-08-02T09:26:16.980256Z'
indexed_at: '2026-08-02T09:26:16.980262Z'
---
