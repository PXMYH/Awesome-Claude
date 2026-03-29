---
id: c-clipboard
slug: c-clipboard
name: Clipboard — Copy & Paste
description: '- When the user says "copy this" or "put this in my clipboard", use
  `pbcopy`'
prompt_preview: '---

  name: c-clipboard

  description: System clipboard — copy, paste, transform content between clipboard
  and files.

  tags: [clipboard, copy, paste, pbcopy, pbpaste]

  ---


  # Clipboard — Copy & Paste


  Read from and write to the system clipboard. Built into macOS, no install needed.


  ## Commands


  ```bash

  # Read clipboard contents

  pbpaste


  # Copy text to clipboard

  echo "hello world" | pbcopy


  # Copy file contents to clipboard

  pbcopy < /path/to/file.txt


  # Save clipboard to file

  pbpaste > /path/to/output...'
full_prompt_length: 1414
tools_mentioned: []
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-clipboard/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-clipboard/SKILL.md
fetched_at: '2026-03-29T04:38:04.362091+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-29T05:30:36.318243Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f9d9730ad80 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f9d9730ad80 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-29T07:03:20.290696Z'
indexed_at: '2026-03-29T07:03:20.290701Z'
---
