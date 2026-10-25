---
id: claude-real-video
slug: claude-real-video
name: claude-real-video — let Claude actually watch a video
description: '- `--speakers`: label every transcript line with the speaker ([SPEAKER_00]
  ...) — use for interviews, podcasts, meetings. Needs `pip install "claude-real-video[speakers]"`
  (45 MB local model, download...'
prompt_preview: '---

  name: claude-real-video

  description: Watch a video for the user. Use when the user shares a video URL (YouTube
  etc.) or local video file and wants it summarized, analyzed, or discussed — Claude
  can''t ingest video directly, so this skill extracts scene-aware keyframes + transcript
  first, then reads those.

  ---


  # claude-real-video — let Claude actually watch a video


  ## When to use


  The user gives you a video (URL or file path) and asks what''s in it, to summarize
  it, to analyze its structure,...'
full_prompt_length: 2556
tools_mentioned:
- Python
category: community
category_display: Community
source_repo: HUANGCHIHHUNGLeo/claude-real-video
source_path: skills/claude-real-video/SKILL.md
source_url: https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/skills/claude-real-video/SKILL.md
fetched_at: '2026-10-25T07:15:28.505815+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T07:25:39.726816Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8deb9340 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8deb9340 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:04.392178Z'
indexed_at: '2026-10-25T12:12:04.392183Z'
---
