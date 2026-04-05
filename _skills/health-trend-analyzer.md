---
id: health-trend-analyzer
slug: health-trend-analyzer
name: 健康趋势分析器
description: '- 支持添加新的数据维度'
prompt_preview: '---

  name: health-trend-analyzer

  description: 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重/BMI、症状、药物依从性、化验结果、情绪睡眠），相关性分析，变化检测，以及交互式HTML可视化报告（ECharts图表）。

  allowed-tools: Read, Grep, Glob, Write

  ---


  # 健康趋势分析器


  分析一段时间内健康数据的趋势和模式，识别变化、相关性，并提供数据驱动的健康洞察。


  ## 核心功能


  ### 1. 多维度趋势分析

  - **体重/BMI 趋势**：追踪体重和BMI随时间的变化，评估健康趋势

  - **症状模式**：识别反复出现的症状、频率变化、潜在诱因

  - **药物依从性**：分析用药规律，识别漏服模式和改善空间

  - **化验结果趋势**：追踪生化指标变化（胆固醇、血糖、血压等）

  - **情绪与睡眠**：关联情绪状...'
full_prompt_length: 7109
tools_mentioned:
- javascript
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/health-trend-analyzer/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/health-trend-analyzer/SKILL.md
fetched_at: '2026-04-05T04:37:07.244983+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T06:11:22.753849Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8c1f680 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8c1f680 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:29:58.780711Z'
indexed_at: '2026-04-05T08:29:58.780717Z'
---
