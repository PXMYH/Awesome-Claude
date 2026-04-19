---
id: family-health-analyzer
slug: family-health-analyzer
name: 家庭健康分析技能
description: '**技能版本**: v1.0'
prompt_preview: "---\nname: family-health-analyzer\ndescription: 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议\n\
  allowed-tools: Read, Write, Grep, Glob\n---\n\n# 家庭健康分析技能\n\n## 技能概述\n\n本技能提供家庭健康数据的深度分析,包括:\n\
  - 遗传风险评估\n- 家族疾病模式识别\n- 家庭共同问题分析\n- 个性化预防建议\n- 可视化报告生成\n\n## 触发条件\n\n当用户请求以下内容时,使用此技能:\n\
  - \"家庭健康报告\"\n- \"家族病史分析\"\n- \"遗传风险评估\"\n- \"家庭健康趋势\"\n- 执行 `/family report` 命令\n\
  - 执行 `/family risk` 命令\n\n## 分析步骤\n\n### 步骤1: 确定分析目标\n\n识别用户请求类型:\n- 家族病史分析\n- 遗传风险评估\n\
  - 家庭健康趋势\n- 家庭健康报告\n\n### 步骤2: 读取家庭数据\n\n**数据源:**\n1. 主数据文件: `data/family-health-tracker.json`\n\
  2. 集成模块数据:\n   - `dat..."
full_prompt_length: 1576
tools_mentioned:
- python
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/family-health-analyzer/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/family-health-analyzer/SKILL.md
fetched_at: '2026-04-19T04:50:42.642997+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-19T06:02:34.365530Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0c9280 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0c9280 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-19T07:27:50.745412Z'
indexed_at: '2026-04-19T07:27:50.745418Z'
---
