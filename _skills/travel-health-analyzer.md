---
id: travel-health-analyzer
slug: travel-health-analyzer
name: 旅行健康分析技能
description: '**版本**: v1.0.0'
prompt_preview: '---

  name: travel-health-analyzer

  description: 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。

  allowed-tools: Read, Write, Grep, Glob

  ---


  # 旅行健康分析技能


  ## 🚨 重要医学免责声明


  **本技能提供的所有健康建议和信息仅供参考,不能替代专业医疗建议。**


  - ⚠️ **所有建议必须由专业医生审核**

  - ⚠️ **疫苗接种和用药方案必须由医生制定**

  - ⚠️ **不提供具体的医疗处方或诊断**

  - ⚠️ **健康风险数据来源于WHO/CDC,可能存在滞后性**

  - ⚠️ **紧急情况下请立即就医**


  ---


  ## 技能功能


  ### 1. 旅行健康规划分析


  分析用户的旅行计划,提供全面的健康准备建议。


  **输入**: 旅行目的地、日期、旅行目的

  **输出**:

  - 目的地健康风险评估

  - 必要和推荐的疫苗接种清单

  - 旅行药箱建议清单

  - 预防措施建议

  - 旅行前准备时间表


  **分析要点...'
full_prompt_length: 5038
tools_mentioned: []
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/travel-health-analyzer/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/travel-health-analyzer/SKILL.md
fetched_at: '2026-04-05T04:37:08.360710+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T06:12:44.995483Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8878e00 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8878e00 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.809658Z'
indexed_at: '2026-04-05T08:29:58.809664Z'
---
