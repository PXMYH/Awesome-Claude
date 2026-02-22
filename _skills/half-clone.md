---
id: half-clone
slug: half-clone
name: Half Clone
description: Claude skill for Half Clone
prompt_preview: '---

  name: half-clone

  description: Clone the later half of the current conversation, discarding earlier
  context to reduce token usage while preserving recent work.

  ---


  Clone the later half of the current conversation, discarding earlier context to
  reduce token usage while preserving recent work.


  Steps:

  1. Get the current session ID and project path: `tail -1 ~/.claude/history.jsonl
  | jq -r ''[.sessionId, .project] | @tsv''`

  2. Find half-clone-conversation.sh with bash: `find ~/.claude -name "half...'
full_prompt_length: 1313
tools_mentioned: []
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/half-clone/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/half-clone/SKILL.md
fetched_at: '2026-02-22T04:17:09.118270+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-02-22T05:19:48.982592Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc9323b3d10 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc9323b3d10 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-22T05:20:57.024459Z'
indexed_at: '2026-02-22T05:20:57.024465Z'
---
