---
id: pronunciation-specialist
slug: pronunciation-specialist
name: Pronunciation Specialist
description: 1. **Load both guides at start** - Base guide + override guide (if exists)
prompt_preview: "---\nname: pronunciation-specialist\ndescription: Scans lyrics for\
  \ pronunciation risks and prevents Suno mispronunciations. Use when writing lyrics\
  \ with proper nouns, technical terms, homographs, or non-English words.\nargument-hint:\
  \ <track-file-path or paste lyrics to scan>\nmodel: sonnet\neffort: medium\nprerequisites:\n\
  \  - lyric-writer\nallowed-tools:\n  - Read\n  - Edit\n  - Write\n  - Grep\n  -\
  \ Glob\n  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Input**: $ARGUMENTS\n\n\
  ### Instrumental Guard\n\nWhen invoked with..."
full_prompt_length: 9029
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/pronunciation-specialist/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/pronunciation-specialist/SKILL.md
fetched_at: '2026-08-02T05:26:58.417546+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-08-02T06:41:03.302660Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0acaefe90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0acaefe90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-08-02T09:26:14.188942Z'
indexed_at: '2026-08-02T09:26:14.188951Z'
---
