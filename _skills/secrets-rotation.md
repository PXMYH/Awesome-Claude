---
id: secrets-rotation
slug: secrets-rotation
name: secrets-rotation — an exposed secret is spent
description: An open rotation task older than 48 hours goes to the top of the next
  session's report
prompt_preview: '---

  name: secrets-rotation

  description: What to do the moment a secret is exposed — pasted into chat, committed,
  logged, shown in a transcript or a screenshot. The secret is compromised; only revoking
  and rotating it helps. Turns it into one tracked task with an escalation, not a
  reminder repeated every session. Use when you see a key, token, password or private
  key anywhere it should not be ("ключ в чате", "токен в логах", "закоммитил .env").
  Loaded by security-officer, l3-support, devops.

  when...'
full_prompt_length: 3533
tools_mentioned: []
category: community
category_display: Community
source_repo: avelikiy/great_cto
source_path: skills/secrets-rotation/SKILL.md
source_url: https://github.com/avelikiy/great_cto/blob/main/skills/secrets-rotation/SKILL.md
fetched_at: '2026-10-25T07:16:57.612277+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T08:41:46.266966Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee68d0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee68d0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:05.717351Z'
indexed_at: '2026-10-25T12:12:05.717355Z'
---
