---
id: outline
slug: outline
name: Outline Wiki Skill
description: 1. Run `auth-info` to verify connection
prompt_preview: "---\nname: outline\ndescription: \"Search, read, and manage Outline\
  \ wiki documents. Use when: (1) searching wiki for documentation, (2) reading wiki\
  \ pages or articles, (3) listing wiki collections or documents, (4) creating or\
  \ updating wiki content, (5) exporting documents as markdown. Works with any Outline\
  \ wiki instance (self-hosted or cloud).\"\nlicense: Apache-2.0\nmetadata:\n  author:\
  \ sanjay3290\n  version: \"1.0\"\n---\n\n# Outline Wiki Skill\n\nSearch, read, create,\
  \ and manage documents in any Outline w..."
full_prompt_length: 4347
tools_mentioned:
- Go
- Python
category: community
category_display: Community
source_repo: sanjay3290/ai-skills
source_path: skills/outline/SKILL.md
source_url: https://github.com/sanjay3290/ai-skills/blob/main/skills/outline/SKILL.md
fetched_at: '2026-02-22T04:16:44.159860+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:05:06.043231Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured with comprehensive
      documentation covering setup, usage, and troubleshooting. It follows best practices
      by providing specific examples for each command and including environment variable
      configuration. However, it lacks explicit edge case handling for common scenarios
      like network failures, rate limiting, or malformed API responses.
  usefulness:
    score: 4.0
    reasoning: This skill provides high practical value for developers and teams using
      Outline wiki, covering essential operations like search, CRUD, and export. The
      comprehensive command reference and troubleshooting guide make it immediately
      actionable for real-world documentation management tasks. The main limitation
      is that it requires a specific Python script implementation that isn't provided
      in the prompt itself.
  overall_rating: 4.25
  summary: A well-documented, practical skill for managing Outline wiki documents
    with clear instructions and comprehensive coverage of common operations, though
    it assumes implementation of the underlying Python script.
  tags_suggested:
  - documentation
  - wiki
  - outline
  - knowledge-management
  - cli-tool
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-22T05:20:56.865098Z'
indexed_at: '2026-02-22T05:20:56.865104Z'
---
