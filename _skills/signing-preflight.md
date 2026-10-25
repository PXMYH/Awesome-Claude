---
id: signing-preflight
slug: signing-preflight
name: signing-preflight — find the locked key before the first commit, not after the
  hundredth
description: '```bash'
prompt_preview: '---

  name: signing-preflight

  description: Before the first commit of a session, check that commit signing will
  work — the key is loaded and unlocked — and ask the operator to unlock it once,
  up front, instead of discovering it after a hundred unsigned commits. Never disables
  signing silently, never re-signs history without asking. Use at the start of implementation
  work in a repo that signs commits ("коммиты не подписаны", "ssh-keygen висит", "gpg
  failed to sign"). Loaded by senior-dev, devops.

  w...'
full_prompt_length: 3246
tools_mentioned: []
category: community
category_display: Community
source_repo: avelikiy/great_cto
source_path: skills/signing-preflight/SKILL.md
source_url: https://github.com/avelikiy/great_cto/blob/main/skills/signing-preflight/SKILL.md
fetched_at: '2026-10-25T07:16:57.741009+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T08:41:54.352542Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee4c80 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee4c80 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:05.719453Z'
indexed_at: '2026-10-25T12:12:05.719457Z'
---
