---
id: hn-summarize
slug: hn-summarize
name: HN Summarize
description: 'For each story give: title, points, comment count, source, a few sentences
  on what the article says, then **comment themes** - group the discussion into 3-6
  recurring threads (agreement, rebuttals, ta...'
prompt_preview: '---

  name: hn-summarize

  description: Fetch and summarize Hacker News / hckrnews.com top stories, articles,
  and their comment threads. Use when asked to summarize HN front-page stories, a
  specific HN story plus its discussion, or "the top N from hckrnews".

  ---


  # HN Summarize


  `hckrnews.com` is a JavaScript-rendered front end - curling it returns an empty
  shell, so **do not scrape it**. Instead use the official Hacker News APIs (Firebase
  + Algolia), which give the same stories with points, comment...'
full_prompt_length: 3767
tools_mentioned:
- JavaScript
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/hn-summarize/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/hn-summarize/SKILL.md
fetched_at: '2026-07-19T05:24:41.094876+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T09:11:14.450411Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff21018a6f0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff21018a6f0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:21.885609Z'
indexed_at: '2026-07-19T09:13:21.885614Z'
---
