---
id: plagiarism-checker
slug: plagiarism-checker
name: Plagiarism Checker
description: '```'
prompt_preview: "---\nname: plagiarism-checker\ndescription: Scans lyrics for phrases\
  \ that may match existing songs using web search and LLM knowledge. Use before release\
  \ to check for unintentional borrowing.\nargument-hint: <album-name> [track-slug]\n\
  model: claude-sonnet-4-6\nallowed-tools:\n  - Read\n  - Glob\n  - Grep\n  - WebSearch\n\
  \  - WebFetch\n  - bitwize-music-mcp\n---\n\n## Your Task\n\n**Target**: $ARGUMENTS\n\
  \n1. Get lyrics for the specified track(s)\n2. Extract distinctive phrases using\
  \ MCP tool\n3. Web search top phras..."
full_prompt_length: 5676
tools_mentioned: []
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/plagiarism-checker/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/plagiarism-checker/SKILL.md
fetched_at: '2026-04-26T04:58:53.408382+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-26T05:58:24.003746Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe11ac32c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe11ac32c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-26T07:41:25.592886Z'
indexed_at: '2026-04-26T07:41:25.592892Z'
---
