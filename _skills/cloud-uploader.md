---
id: cloud-uploader
slug: cloud-uploader
name: Cloud Uploader Skill
description: '- v0.14.0 - Initial implementation'
prompt_preview: "---\nname: cloud-uploader\ndescription: Uploads promo videos and\
  \ content to Cloudflare R2 or AWS S3. Use when the user wants to host promo content\
  \ for social media or distribution.\nmodel: sonnet\neffort: low\nprerequisites:\n\
  \  - promo-director\nallowed-tools:\n  - Read\n  - Bash\n  - Glob\nrequirements:\n\
  \  python:\n    - boto3\n---\n\n# Cloud Uploader Skill\n\nUpload promo videos and\
  \ other album content to cloud storage (Cloudflare R2 or AWS S3).\n\n## Purpose\n\
  \nAfter generating promo videos with `/bitwize-music:pr..."
full_prompt_length: 8534
tools_mentioned:
- AWS
- PYTHON
- python
- aws
- Python
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/cloud-uploader/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/cloud-uploader/SKILL.md
fetched_at: '2026-06-07T06:24:15.800279+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T07:28:07.320357Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffcc08c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffcc08c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:52.624210Z'
indexed_at: '2026-06-07T10:04:52.624215Z'
---
