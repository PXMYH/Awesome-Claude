---
id: deploy-landed
slug: deploy-landed
name: deploy-landed — a deploy is done when the running thing is the thing you meant
description: A FAIL in any line means the deploy is not done, whatever the command
  printed.
prompt_preview: "---\nname: deploy-landed\ndescription: Prove a deploy landed — the\
  \ served revision is the commit you meant, its env is present, and the product does\
  \ its job — instead of trusting the deploy command's exit code. Also catches server\
  \ drift before a pull or deploy. Use after any deploy, rollout, restart or server-side\
  \ fix (\"задеплой\", \"выкати\", \"проверь на проде\", \"почему не обновилось\"\
  ). Loaded by devops, l3-support, infra-provisioner.\nwhen_to_use: |\n  Apply when:\n\
  \  - you ran, or are about to report,..."
full_prompt_length: 4324
tools_mentioned:
- docker
category: community
category_display: Community
source_repo: avelikiy/great_cto
source_path: skills/deploy-landed/SKILL.md
source_url: https://github.com/avelikiy/great_cto/blob/main/skills/deploy-landed/SKILL.md
fetched_at: '2026-10-25T07:16:55.800061+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T08:39:52.633044Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1d220 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1d220 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:05.683652Z'
indexed_at: '2026-10-25T12:12:05.683657Z'
---
