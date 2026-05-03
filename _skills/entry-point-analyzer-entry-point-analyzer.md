---
id: entry-point-analyzer-entry-point-analyzer
slug: entry-point-analyzer-entry-point-analyzer
name: Entry Point Analyzer
description: 'If a file cannot be parsed:'
prompt_preview: '---

  name: entry-point-analyzer

  description: Analyzes smart contract codebases to identify state-changing entry
  points for security auditing. Detects externally callable functions that modify
  state, categorizes them by access level (public, admin, role-restricted, contract-only),
  and generates structured audit reports. Excludes view/pure/read-only functions.
  Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm)
  or when asked to find entry points, audit flows, exter...'
full_prompt_length: 9575
tools_mentioned:
- Rust
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md
fetched_at: '2026-05-03T05:34:03.116371+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-03T08:08:07.483145Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33e605c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33e605c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-03T08:17:32.511443Z'
indexed_at: '2026-05-03T08:17:32.511449Z'
---
