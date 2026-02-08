---
id: food-database-query
slug: food-database-query
name: 食物数据库查询技能
description: '**技能版本**: v1.0'
prompt_preview: '# 食物数据库查询技能


  **技能名称**: Food Database Query

  **技能类型**: 数据查询与分析

  **创建日期**: 2026-01-06

  **版本**: v1.0


  ---


  ## 技能概述


  本技能提供全面的营养食物数据库查询功能,支持食物营养信息查询、比较、推荐和自动营养计算。


  **核心功能**:

  - ✅ 食物营养信息查询

  - ✅ 食物比较分析

  - ✅ 智能食物推荐

  - ✅ 自动营养计算

  - ✅ 分类浏览和搜索

  - ✅ 份量转换和估算


  ---


  ## 数据源


  ### 主数据库

  - **文件**: `data/food-database.json`

  - **内容**: 50种常见食物的详细营养数据

  - **结构**: 每种食物包含30+营养素指标


  ### 分类体系

  - **文件**: `data/food-categories.json`

  - **分类**: 10大类,30+子类

  - **支持**: 按分类浏览和筛选


  ---


  ## 功能模块


  ### 1. 食物查询 (Food Query)


  #### 1.1 精确查询


  **用途**: 根据食...'
full_prompt_length: 11557
tools_mentioned:
- python
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/food-database-query/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/food-database-query/SKILL.md
fetched_at: '2026-02-08T04:32:11.916541+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:54:17.944270Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is well-structured with clear sections for overview, data
      sources, and functional modules. It provides specific examples and code snippets
      for implementation. However, it lacks handling for edge cases like ambiguous
      food names, missing data, or invalid inputs, and the prompt ends abruptly without
      completing the health conditions section.
  usefulness:
    score: 3.5
    reasoning: The skill provides practical nutrition query functionality with real-world
      value for health and diet applications. The comprehensive coverage of food types,
      nutrients, and recommendation logic is actionable. However, the limited database
      size (50 foods) and lack of integration details (e.g., API endpoints, data format)
      reduce immediate practicality for production use.
  overall_rating: 3.75
  summary: A well-structured but incomplete prompt for a nutrition database skill
    with strong conceptual design but missing edge case handling and practical implementation
    details.
  tags_suggested:
  - nutrition
  - food-database
  - health
  - data-query
  - diet-planning
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.431129Z'
indexed_at: '2026-02-08T04:36:45.431135Z'
---
