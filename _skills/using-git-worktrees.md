---
id: using-git-worktrees
slug: using-git-worktrees
name: Using Git Worktrees
description: '**Pairs with:**'
prompt_preview: '---

  name: using-git-worktrees

  description: Use when starting feature work that needs isolation from current workspace
  or before executing implementation plans - creates isolated git worktrees with smart
  directory selection and safety verification

  ---


  # Using Git Worktrees


  ## Overview


  Git worktrees create isolated workspaces sharing the same repository, allowing work
  on multiple branches simultaneously without switching.


  **Core principle:** Systematic directory selection + safety verification...'
full_prompt_length: 5633
tools_mentioned:
- go
- Node.js
- Go
- Rust
- Python
category: community
category_display: Community
source_repo: obra/superpowers
source_path: skills/using-git-worktrees/SKILL.md
source_url: https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md
fetched_at: '2026-02-01T04:29:36.010321+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:19:04.521597Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly structured with clear, step-by-step instructions
      and a logical priority order for directory selection. It includes specific safety
      verification commands and handles key edge cases like existing directories and
      .gitignore compliance. However, it has minor formatting issues (e.g., incomplete
      'Common Mistakes' section) and could benefit from more explicit error handling
      for missing dependencies or non-standard project structures.
  usefulness:
    score: 4.5
    reasoning: This skill provides significant real-world value by automating the
      setup of isolated Git worktrees, which is a common need for parallel development.
      It comprehensively covers directory selection, safety checks, and project initialization,
      making it immediately actionable for developers working on multiple features
      simultaneously. The inclusion of baseline testing and reporting ensures reliability
      and user awareness.
  overall_rating: 4.5
  summary: A well-designed, practical skill that effectively automates Git worktree
    creation with strong safety and usability considerations, though it has minor
    gaps in error handling and documentation completeness.
  tags_suggested:
  - git
  - worktrees
  - development
  - automation
  - safety
github_metrics:
  stars: 41145
  forks: 3129
  open_issues: 111
  last_commit: '2026-01-30'
  fetched_at: '2026-02-01T04:30:11.029444Z'
indexed_at: '2026-02-01T04:32:50.810928Z'
---
