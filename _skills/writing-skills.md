---
id: writing-skills
slug: writing-skills
name: Writing Skills
description: If you follow TDD for code, follow it for skills. It's the same discipline
  applied to documentation.
prompt_preview: "---\nname: writing-skills\ndescription: Use when creating new skills,\
  \ editing existing skills, or verifying skills work before deployment\n---\n\n#\
  \ Writing Skills\n\n## Overview\n\n**Writing skills IS Test-Driven Development applied\
  \ to process documentation.**\n\n**Personal skills live in agent-specific directories\
  \ (`~/.claude/skills` for Claude Code, `~/.codex/skills` for Codex)** \n\nYou write\
  \ test cases (pressure scenarios with subagents), watch them fail (baseline behavior),\
  \ write the skill (documentatio..."
full_prompt_length: 22377
tools_mentioned:
- go
- JavaScript
- Python
- React
- TypeScript
category: community
category_display: Community Skills
source_repo: obra/superpowers
source_path: skills/writing-skills/SKILL.md
source_url: https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md
fetched_at: '2026-02-05T04:14:38.085617Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:19:48.923043Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, mapping TDD
      concepts directly to skill creation with concrete examples. It provides specific
      constraints (e.g., frontmatter rules, directory structure) and handles edge
      cases by defining when NOT to create skills. The only minor weakness is the
      dependency on an external 'superpowers:test-driven-development' skill for the
      core RED-GREEN-REFACTOR cycle.
  usefulness:
    score: 5.0
    reasoning: 'This is highly practical for AI agent development, providing a systematic
      methodology for creating reusable skills. It directly addresses a real need:
      ensuring skills are validated through failure before documentation. The TDD
      analogy makes the process intuitive for developers, and the concrete examples
      (pressure scenarios, subagents) make it immediately actionable.'
  overall_rating: 4.75
  summary: An excellent, production-ready prompt that successfully adapts test-driven
    development to AI skill creation with clear methodology, practical constraints,
    and strong real-world applicability.
  tags_suggested:
  - tdd
  - skill-development
  - documentation
  - ai-agent
  - testing
github_metrics:
  stars: 44605
  forks: 3386
  open_issues: 131
  last_commit: '2026-01-30'
  fetched_at: '2026-02-05T04:14:40.551804Z'
indexed_at: '2026-02-05T04:14:41.453594Z'
---
