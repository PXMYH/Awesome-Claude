---
id: sleep-analyzer
slug: sleep-analyzer
name: 睡眠分析器技能
description: '**技能版本**: v1.0'
prompt_preview: '---

  name: sleep-analyzer

  description: 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。

  allowed-tools: Read, Grep, Glob, Write

  ---


  # 睡眠分析器技能


  分析睡眠数据，识别睡眠模式，评估睡眠质量，并提供个性化睡眠改善建议。


  ## 功能


  ### 1. 睡眠趋势分析


  分析睡眠时长、质量、效率的变化趋势，识别改善或需要关注的方面。


  **分析维度**：

  - 睡眠时长趋势（平均睡眠时长变化）

  - 睡眠效率趋势（睡眠效率百分比变化）

  - 入睡时间模式（上床时间、入睡时间、起床时间）

  - 作息规律性评分（sleep consistency score）

  - 周末vs工作日对比（social jetlag）


  **输出**：

  - 趋势方向（改善/稳定/下降）

  - 变化幅度和百分比

  - 趋势显著性评估

  - 最佳睡眠时间窗口识别

  - 改进建议


  ### 2. 睡眠质量评估


  综合评估睡眠质量，识别影响睡眠质量的关键因素。


  **评估内容**：

  - PSQI分数追踪和趋...'
full_prompt_length: 11385
tools_mentioned:
- python
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/sleep-analyzer/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/sleep-analyzer/SKILL.md
fetched_at: '2026-02-01T04:29:17.569046+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:56:09.981443Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, specific
      analysis dimensions, and detailed output formats. It follows prompt engineering
      best practices by defining trigger conditions, execution steps, and expected
      outputs. However, it lacks explicit handling of edge cases like missing data
      or invalid inputs, and the data source paths are hypothetical without validation
      logic.
  usefulness:
    score: 4.0
    reasoning: This skill provides high real-world value for health monitoring and
      sleep improvement, covering comprehensive analysis dimensions from trends to
      correlations. The actionable recommendations and structured reporting format
      make it immediately beneficial for users tracking sleep data. However, its practicality
      is limited by the assumption of specific data file structures that may not exist
      in real implementations.
  overall_rating: 4.25
  summary: A well-crafted, comprehensive sleep analysis skill with excellent structure
    and practical health insights, though it could benefit from more robust error
    handling and real data integration guidance.
  tags_suggested:
  - health
  - sleep-analysis
  - data-analysis
  - wellness
  - personalized-recommendations
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.673879Z'
indexed_at: '2026-02-01T04:32:50.673885Z'
---
