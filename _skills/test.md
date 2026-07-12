---
id: test
slug: test
name: Plugin Test Suite
description: '- Use Grep with `output_mode: content` and `-n` for line numbers'
prompt_preview: "---\nname: test\ndescription: Runs automated tests to validate plugin\
  \ integrity across 14 categories. Use before creating PRs, after making changes\
  \ to skills or templates, or to verify plugin health.\nargument-hint: \"[all | config\
  \ | skills | templates | workflow | suno | research | mastering | sheet-music |\
  \ release | consistency | terminology | behavior | quality | quick]\"\nmodel: haiku\n\
  context: fork\nallowed-tools:\n  - Read\n  - Grep\n  - Glob\n  - Bash\n---\n\n##\
  \ Your Task\n\n**Input**: $ARGUMENTS\n\nRun aut..."
full_prompt_length: 5646
tools_mentioned:
- Python
category: community
category_display: Community
source_repo: bitwize-music-studio/claude-ai-music-skills
source_path: skills/test/SKILL.md
source_url: https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/skills/test/SKILL.md
fetched_at: '2026-07-12T05:32:00.869529+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-12T06:46:43.850620Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f00649c67e0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f00649c67e0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-12T09:23:54.449495Z'
indexed_at: '2026-07-12T09:23:54.449501Z'
---
