---
id: memex-verify
slug: memex-verify
name: Verify the Memex Repo Before Committing
description: '- `memex` — the umbrella skill for agent-native shared memory; this
  gate'
prompt_preview: "---\nname: memex-verify\ndescription: >\n  Run the local pre-commit\
  \ gate for the memex repo before staging a commit:\n  format check, clippy with\
  \ warnings denied, and the workspace unit-test\n  suite, mirroring memex's own CI.\
  \ Use right before `commit-changes` on a\n  memex working tree, after editing any\
  \ Rust crate under `crates/`, or when\n  reproducing a red CI run locally. Optionally\
  \ runs the Postgres-gated\n  integration suite when the `memex-pg` container is\
  \ up and `.env` is sourced.\n  This is a v..."
full_prompt_length: 8581
tools_mentioned:
- rust
- docker
- Rust
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/memex-verify/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/memex-verify/SKILL.md
fetched_at: '2026-06-28T06:18:47.370104+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T09:10:52.216687Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a2803980 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a2803980 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:28.873562Z'
indexed_at: '2026-06-28T10:04:28.873567Z'
---
