---
id: ru-score
slug: ru-score
name: Russian Text Quality Score
description: If a dimension has no issues, write «Замечаний нет» in the remarks column.
prompt_preview: "---\nname: ru-score\ndescription: >\n  Score Russian text 0.0–10.0\
  \ across five dimensions: typography, clean language, grammar,\n  structure, precision\
  \ for the reader. Triggers: оцени текст, ru-score, оценка качества\n  текста, насколько\
  \ хорош текст, балл за текст. Use when the user wants a number rather than\n  a\
  \ list of findings. Never edits a file.\nallowed-tools: Read, Grep, Glob\ndisallowed-tools:\
  \ Write, Edit, NotebookEdit, Bash, PowerShell, Monitor\ncontext: fork\nuser-invocable:\
  \ true\n---\n\n# Russian..."
full_prompt_length: 4886
tools_mentioned: []
category: community
category_display: Community
source_repo: talkstream/ru-text
source_path: skills/ru-score/SKILL.md
source_url: https://github.com/talkstream/ru-text/blob/main/skills/ru-score/SKILL.md
fetched_at: '2026-08-02T05:31:04.130115+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-08-02T09:09:50.427607Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0acaed550 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0acaed550 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-08-02T09:26:16.982750Z'
indexed_at: '2026-08-02T09:26:16.982755Z'
---
