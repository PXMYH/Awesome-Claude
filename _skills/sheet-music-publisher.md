---
id: sheet-music-publisher
slug: sheet-music-publisher
name: Sheet Music Publisher Agent
description: 'User should end with:'
prompt_preview: "---\nname: sheet-music-publisher\ndescription: Converts mastered\
  \ audio to sheet music and creates printable songbooks. Use after mastering when\
  \ the user wants sheet music or a songbook for their album.\nargument-hint: <album-name\
  \ or /path/to/track.wav>\nmodel: claude-sonnet-4-6\nallowed-tools:\n  - Read\n \
  \ - Edit\n  - Write\n  - Grep\n  - Glob\n  - Bash\n  - bitwize-music-mcp\nrequirements:\n\
  \  external:\n    - name: AnthemScore\n      purpose: Audio to sheet music transcription\n\
  \      url: https://www.lunaverus...."
full_prompt_length: 7335
tools_mentioned:
- python
- Python
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/sheet-music-publisher/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/sheet-music-publisher/SKILL.md
fetched_at: '2026-05-03T05:31:09.291956+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-03T06:35:38.680924Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f8d280 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7e33f8d280 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-03T08:17:30.615721Z'
indexed_at: '2026-05-03T08:17:30.615727Z'
---
