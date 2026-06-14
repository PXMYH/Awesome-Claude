---
id: reddit-fetch
slug: reddit-fetch
name: Reddit Fetch
description: '- **Don''t fire parallel requests.** Make them sequentially with `sleep
  2` or `sleep 3` between each.'
prompt_preview: "---\nname: reddit-fetch\ndescription: Fetch content from Reddit using\
  \ the curl JSON API. Use when accessing Reddit URLs, researching topics on Reddit,\
  \ or when Reddit returns 403/blocked errors.\n---\n\n# Reddit Fetch\n\nReddit's\
  \ public JSON API works by appending `.json` to any Reddit URL.\n\n## Listing hot/new/top\
  \ posts\n\n```bash\ncurl -s -L -H \"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64;\
  \ x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\" \\\
  \n  \"https://old.reddit.com/r/SUBREDD..."
full_prompt_length: 2757
tools_mentioned: []
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/reddit-fetch/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/reddit-fetch/SKILL.md
fetched_at: '2026-06-14T06:42:35.396108+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-14T10:16:55.167976Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a083380 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f187a083380 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-14T10:18:27.866195Z'
indexed_at: '2026-06-14T10:18:27.866200Z'
---
