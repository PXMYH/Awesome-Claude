---
id: cloud-uploader
slug: cloud-uploader
name: Cloud Uploader Skill
description: '- v0.14.0 - Initial implementation'
prompt_preview: "---\nname: cloud-uploader\ndescription: Uploads promo videos and\
  \ content to Cloudflare R2 or AWS S3. Use when the user wants to host promo content\
  \ for social media or distribution.\nmodel: claude-sonnet-4-6\nprerequisites:\n\
  \  - promo-director\nallowed-tools:\n  - Read\n  - Bash\n  - Glob\nrequirements:\n\
  \  python:\n    - boto3\n---\n\n# Cloud Uploader Skill\n\nUpload promo videos and\
  \ other album content to cloud storage (Cloudflare R2 or AWS S3).\n\n## Purpose\n\
  \nAfter generating promo videos with `/bitwize-music:pro..."
full_prompt_length: 8533
tools_mentioned:
- Python
- PYTHON
- aws
- python
- AWS
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/cloud-uploader/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/cloud-uploader/SKILL.md
fetched_at: '2026-05-03T05:31:01.617101+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-03T06:30:23.980854Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f2f500 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f2f500 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-03T08:17:30.508703Z'
indexed_at: '2026-05-03T08:17:30.508709Z'
---
