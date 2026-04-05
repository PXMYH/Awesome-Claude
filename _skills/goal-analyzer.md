---
id: goal-analyzer
slug: goal-analyzer
name: 健康目标分析器技能
description: '**使用此技能时,始终优先考虑用户的健康和安全!**'
prompt_preview: "---\nname: goal-analyzer\ndescription: 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。\n\
  allowed-tools: Read, Grep, Glob, Write\n---\n\n# 健康目标分析器技能\n\n分析健康目标数据,识别目标模式和进度,评估目标达成情况,并提供个性化目标管理建议。\n\
  \n## 功能\n\n### 1. SMART目标验证\n\n验证设定的新目标是否符合SMART原则。\n\n**验证维度**:\n- **S**pecific(具体性)\n\
  \  - 目标是否明确具体\n  - 是否有清晰的定义\n  - 是否避免模糊表述\n\n- **M**easurable(可衡量性)\n  - 是否有可量化的指标\n\
  \  - 是否有明确的衡量标准\n  - 是否可以追踪进度\n\n- **A**chievable(可实现性)\n  - 目标是否现实可行\n  - 是否考虑了当前状况\n\
  \  - 是否在合理时间范围内\n  - 减重目标:建议每周0.5-1公斤\n  - 运动目标:建议每周3-5次,每次30-60分钟\n\n- **R*..."
full_prompt_length: 8104
tools_mentioned:
- javascript
- python
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/goal-analyzer/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/goal-analyzer/SKILL.md
fetched_at: '2026-04-05T04:37:07.135469+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T06:11:14.650210Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8560170 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8560170 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.777785Z'
indexed_at: '2026-04-05T08:29:58.777790Z'
---
