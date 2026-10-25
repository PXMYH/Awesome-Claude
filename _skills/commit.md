---
id: commit
slug: commit
name: Git Commit
description: Stage and create the commit in a single message. Do not do anything else.
prompt_preview: "---\nname: commit\ndescription: Create a single well-crafted git\
  \ commit from current changes. Analyzes diff, follows repo's commit style, and writes\
  \ a concise \"why not what\" message.\nuser_invocable: true\nallowed-tools:\n  -\
  \ Bash(git add:*)\n  - Bash(git status:*)\n  - Bash(git commit:*)\n---\n\n# Git\
  \ Commit\n\n## Context\n\nGather this context before committing:\n- Current git\
  \ status: `git status`\n- Current git diff (staged and unstaged): `git diff HEAD`\n\
  - Current branch: `git branch --show-current`\n- Recent..."
full_prompt_length: 2002
tools_mentioned: []
category: community
category_display: Community
source_repo: sneg55/agent-starter
source_path: skills/commit/SKILL.md
source_url: https://github.com/sneg55/agent-starter/blob/main/skills/commit/SKILL.md
fetched_at: '2026-10-25T07:20:19.038516+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:33:27.757012Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e057da0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e057da0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:08.793942Z'
indexed_at: '2026-10-25T12:12:08.793946Z'
---
