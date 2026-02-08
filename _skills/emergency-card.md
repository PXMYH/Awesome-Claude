---
id: emergency-card
slug: emergency-card
name: 紧急医疗信息卡生成器
description: 详细的输出格式说明请参考 [formats.md](formats.md)。
prompt_preview: '---

  name: emergency-card

  description: 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。

  ---


  # 紧急医疗信息卡生成器


  生成紧急情况下快速访问的医疗信息摘要，用于急救或就医。


  ## 核心功能


  ### 1. 紧急信息提取

  从用户的健康数据中提取最关键的信息：

  - **严重过敏**：优先提取4级（过敏性休克）和3级过敏

  - **当前用药**：活跃药物的名称、剂量、频率

  - **急症情况**：需要紧急处理的医疗状况

  - **植入物**：心脏起搏器、支架等（影响检查和治疗）

  - **紧急联系人**：快速联系的家属信息


  ### 2. 信息优先级排序

  按照医疗紧急程度对信息排序：

  1. **P0 - 危急信息**：过敏性休克、严重药物过敏、危及生命的疾病

  2. **P1 - 重要信息**：当前用药、慢性病、植入物

  3. **P2 - 一般信息**：血型、年龄、...'
full_prompt_length: 10841
tools_mentioned:
- javascript
- python
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/emergency-card/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/emergency-card/SKILL.md
fetched_at: '2026-02-08T04:32:11.480296+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:53:45.064552Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is highly structured and specific about data sources and
      extraction logic, but it contains significant inconsistencies. It mixes conceptual
      instructions with actual code snippets (JavaScript/Python) that appear to be
      for a different system, creating confusion about the intended execution environment.
      The prompt also abruptly cuts off mid-sentence in the diabetes section, indicating
      incomplete content.
  usefulness:
    score: 4.0
    reasoning: The concept is highly practical for emergency medical scenarios, addressing
      real needs for quick information access during travel or medical emergencies.
      The multi-format output (HTML, JSON, text, PDF) and prioritization of critical
      information (P0-P2) show thoughtful design for different user scenarios. However,
      the mixed code examples reduce immediate usability as they don't align with
      typical AI agent prompt formats.
  overall_rating: 3.75
  summary: A well-conceived emergency medical card generator with practical multi-format
    outputs, but the prompt quality is undermined by inconsistent code examples and
    incomplete sections that need clarification for actual implementation.
  tags_suggested:
  - medical
  - emergency
  - healthcare
  - information-management
  - multi-format
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.419756Z'
indexed_at: '2026-02-08T04:36:45.419765Z'
---
