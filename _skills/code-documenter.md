---
id: code-documenter
slug: code-documenter
name: Code Documenter
description: '**Spec Miner** - Informs from code analysis | **Fullstack Guardian**
  - Documents during implementation | **Code Reviewer** - Checks documentation quality'
prompt_preview: "---\nname: code-documenter\ndescription: Use when adding docstrings,\
  \ creating API documentation, or building documentation sites. Invoke for OpenAPI/Swagger\
  \ specs, JSDoc, doc portals, tutorials, user guides.\ntriggers:\n  - documentation\n\
  \  - docstrings\n  - OpenAPI\n  - Swagger\n  - JSDoc\n  - comments\n  - API docs\n\
  \  - tutorials\n  - user guides\n  - doc site\nrole: specialist\nscope: implementation\n\
  output-format: code\n---\n\n# Code Documenter\n\nDocumentation specialist for inline\
  \ documentation, API specs, doc..."
full_prompt_length: 3768
tools_mentioned:
- FastAPI
- Django
- python
- typescript
- gRPC
- django
- Node.js
- WebSocket
- TypeScript
- fastapi
category: community
category_display: Community
source_repo: jeffallan/claude-skills
source_path: skills/code-documenter/SKILL.md
source_url: https://github.com/jeffallan/claude-skills/blob/main/skills/code-documenter/SKILL.md
fetched_at: '2026-02-01T04:29:21.947522+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:57:35.702926Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear role definition,
      specific triggers, and a comprehensive workflow. It follows prompt engineering
      best practices by including constraints, output formats, and knowledge references.
      The only minor weakness is the reference guide section which references external
      files that may not exist in the actual system context.
  usefulness:
    score: 4.5
    reasoning: This skill addresses a critical and common development task with high
      real-world value. It covers a comprehensive range of documentation scenarios
      from inline docstrings to full documentation sites. The actionability is strong
      with clear triggers and workflow, though the effectiveness depends on the availability
      of the referenced documentation files.
  overall_rating: 4.5
  summary: A well-crafted, comprehensive documentation skill that provides clear guidance
    for various documentation tasks with strong practical value for developers.
  tags_suggested:
  - documentation
  - api-docs
  - docstrings
  - technical-writing
  - developer-tools
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.700683Z'
indexed_at: '2026-02-01T04:32:50.700689Z'
---
