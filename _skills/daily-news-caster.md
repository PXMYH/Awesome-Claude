---
id: daily-news-caster
slug: daily-news-caster
name: Daily News Caster Skill
description: '- **Scripts executed**: `news-aggregator-skill/scripts/fetch_news.py`
  (fetches news from public sources) and `tts/scripts/tts.py` (generates speech audio).
  Both must be present locally before this ski...'
prompt_preview: "---\nname: daily-news-caster\ndescription: Fetches the latest news\
  \ using news-aggregator-skill, formats it into a podcast script in Markdown format,\
  \ and uses the tts skill to generate a podcast audio file. Use when the user asks\
  \ to get the latest news and read it out as a podcast.\npermissions:\n  - network\n\
  \  - filesystem\ndependencies:\n  skills:\n    - news-aggregator-skill\n    - tts\n\
  \  binaries:\n    - python3\n    - ffmpeg\n---\n\n# Daily News Caster Skill\n\n\
  This skill allows the agent to fetch real-time..."
full_prompt_length: 6534
tools_mentioned: []
category: community
category_display: Community
source_repo: NoizAI/skills
source_path: skills/daily-news-caster/SKILL.md
source_url: https://github.com/NoizAI/skills/blob/main/skills/daily-news-caster/SKILL.md
fetched_at: '2026-04-05T04:36:09.626995+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T05:11:07.949841Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8ed6210 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8ed6210 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:57.749669Z'
indexed_at: '2026-04-05T08:29:57.749675Z'
---
