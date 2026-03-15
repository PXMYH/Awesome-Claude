---
id: c-files
slug: c-files
name: Cloud Files (rclone)
description: '- `rclone sync` deletes files on destination — use `rclone copy` if
  unsure'
prompt_preview: '---

  name: c-files

  description: Sync files to Google Drive, S3, Dropbox, OneDrive, and 70+ cloud providers
  using rclone.

  tags: [files, cloud, sync, backup, storage]

  ---


  # Cloud Files (rclone)


  ```bash

  # List configured remotes

  rclone listremotes


  # List files in a remote

  rclone ls remote:path

  rclone lsd remote:path    # directories only


  # Copy files to/from cloud

  rclone copy local/path remote:path

  rclone copy remote:path local/path


  # Sync (make remote match local — deletes extra files on remot...'
full_prompt_length: 1267
tools_mentioned:
- Azure
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-files/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-files/SKILL.md
fetched_at: '2026-03-15T04:31:46.300418+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-15T05:20:21.479322Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fa3969f8800 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fa3969f8800 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-15T06:04:20.028189Z'
indexed_at: '2026-03-15T06:04:20.028195Z'
---
