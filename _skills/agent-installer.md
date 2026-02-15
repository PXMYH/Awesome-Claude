---
id: agent-installer
slug: agent-installer
name: Agent Installer
description: Claude skill for Agent Installer
prompt_preview: '---

  name: agent-installer

  description: "Use this agent when the user wants to discover, browse, or install
  Claude Code agents from the awesome-claude-code-subagents repository."

  tools: Bash, WebFetch, Read, Write, Glob

  model: haiku

  ---


  You are an agent installer that helps users browse and install Claude Code agents
  from the awesome-claude-code-subagents repository on GitHub.


  ## Your Capabilities


  You can:

  1. List all available agent categories

  2. List agents within a category

  3. Search for ag...'
full_prompt_length: 3555
tools_mentioned:
- python
- typescript
- PHP
- php
category: meta-orchestration
category_display: Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/agent-installer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/agent-installer.md
fetched_at: '2026-02-15T04:21:37.882464+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:09:47.144426Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly clear and specific, defining exact GitHub API
      endpoints, directory paths, and workflow steps. It includes practical examples
      and covers core operations like listing, searching, and installing agents. However,
      it lacks explicit handling for edge cases like network failures, invalid agent
      names, or permission issues during installation.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate practical value for developers wanting
      to extend Claude Code with community agents, covering the full lifecycle from
      discovery to installation. It addresses a real need for ecosystem expansion
      and follows actionable workflows that users can immediately apply to enhance
      their development environment.
  overall_rating: 4.75
  summary: A well-structured, highly practical prompt that effectively enables users
    to browse and install community Claude agents, with strong clarity and real-world
    utility for ecosystem management.
  tags_suggested:
  - meta-orchestration
  - agent-management
  - github-integration
  - community-tools
  - installation
github_metrics:
  stars: 10437
  forks: 1106
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-15T04:22:41.501003Z'
indexed_at: '2026-02-15T04:33:50.789873Z'
---
