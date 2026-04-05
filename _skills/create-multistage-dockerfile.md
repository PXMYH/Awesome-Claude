---
id: create-multistage-dockerfile
slug: create-multistage-dockerfile
name: Create Multi-Stage Dockerfile
description: Claude skill for Create Multi-Stage Dockerfile
prompt_preview: "---\r\nname: create-multistage-dockerfile\r\ndescription: >\r\n \
  \ Create multi-stage Dockerfiles that separate build and runtime environments\r\n\
  \  for minimal production images. Covers builder/runtime stage separation,\r\n \
  \ artifact copying, scratch/distroless/alpine targets, and size comparison.\r\n\
  \  Use when production images are too large, when build tools are included in\r\n\
  \  the final image, when you need separate dev and prod images from one\r\n  Dockerfile,\
  \ or when deploying to constrained environments li..."
full_prompt_length: 7339
tools_mentioned:
- go
- docker
- python
- Node.js
- Go
- Rust
- Docker
- rust
- Python
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/create-multistage-dockerfile/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/create-multistage-dockerfile/SKILL.md
fetched_at: '2026-04-05T04:37:43.717003+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T06:47:41.077995Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8563500 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8563500 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:59.338527Z'
indexed_at: '2026-04-05T08:29:59.338532Z'
---
