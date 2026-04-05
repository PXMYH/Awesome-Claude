---
id: skill-model-updater
slug: skill-model-updater
name: Skill Model Updater
description: '- **Check before update** - Always know what will change'
prompt_preview: "---\nname: skill-model-updater\ndescription: Updates model references\
  \ across all skill files when new Claude models are released. Use when Anthropic\
  \ releases new Claude models to keep skills current.\nargument-hint: <\"check\"\
  \ | \"update\" | \"update --dry-run\">\nmodel: claude-haiku-4-5-20251001\nallowed-tools:\n\
  \  - Read\n  - Edit\n  - Glob\n  - Grep\n  - WebSearch\n  - WebFetch\n---\n\n##\
  \ Your Task\n\n**Command**: $ARGUMENTS\n\nBased on the command:\n1. **check** -\
  \ Discover current models, scan all skills, report stat..."
full_prompt_length: 7166
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/skill-model-updater/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/skill-model-updater/SKILL.md
fetched_at: '2026-04-05T04:36:44.983549+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:55:03.950859Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8eabb90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8eabb90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.444328Z'
indexed_at: '2026-04-05T08:29:58.444334Z'
---
