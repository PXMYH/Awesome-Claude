---
id: skin-health-analyzer
slug: skin-health-analyzer
name: 皮肤健康分析技能
description: '**版本**: v1.0.0'
prompt_preview: '---

  description: 分析皮肤健康数据、识别皮肤问题模式、评估皮肤健康状况、提供个性化皮肤健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。

  ---


  # 皮肤健康分析技能


  ## 技能概述


  本技能提供全面的皮肤健康数据分析功能，包括趋势识别、风险评估、问题诊断和个性化建议生成。特别强调痣的监测和皮肤癌预防。


  ## 医学免责声明


  ⚠️ **重要提示**：本技能提供的数据分析和建议仅供参考，不构成医学诊断或治疗建议。


  - 所有皮肤问题应由专业皮肤科医生诊断和治疗

  - 痣的异常变化必须立即就医检查

  - 皮肤癌需要专业诊断，不能仅依靠自我评估

  - 分析结果不能替代专业皮肤科检查

  - 紧急情况应立即就医

  - 请遵循皮肤科医生的专业建议


  ## 核心功能


  ### 1. 趋势分析


  #### 皮肤问题发展趋势

  - 识别痤疮、湿疹等问题的发生模式

  - 分析问题的季节性和周期性

  - 评估问题严重程度的变化

  - 预测未来发作风险


  **输出内容**：

  - 问题发生频率曲线

  - 严重程度变化趋势

  - 诱发因素分析

  - 预防建议


  #### 痣的变化监测

  - 新增痣的位置和数...'
full_prompt_length: 7221
tools_mentioned: []
category: community
category_display: Community
source_repo: huifer/Claude-Ally-Health
source_path: skills/skin-health-analyzer/SKILL.md
source_url: https://github.com/huifer/Claude-Ally-Health/blob/main/skills/skin-health-analyzer/SKILL.md
fetched_at: '2026-01-25T03:52:15.172362+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:55:59.726613Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, comprehensive
      medical disclaimers, and detailed functional specifications. It follows best
      practices by defining scope, constraints, and expected outputs for each module.
      However, it lacks explicit edge case handling (e.g., conflicting data, missing
      information) and fallback guidance for ambiguous inputs.
  usefulness:
    score: 4.0
    reasoning: The skill offers high real-world value for personal health monitoring
      and education, covering major skin conditions and their systemic connections
      comprehensively. It provides actionable outputs like risk assessments and personalized
      recommendations, though its effectiveness depends on user data quality and it
      cannot replace professional medical advice.
  overall_rating: 4.25
  summary: A robust, well-structured health analysis skill with strong educational
    value and practical outputs, though it requires careful handling of medical limitations
    and edge cases in real deployment.
  tags_suggested:
  - healthcare
  - medical_analysis
  - skin_care
  - preventive_health
  - personalized_recommendations
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:52.822331Z'
indexed_at: '2026-01-25T04:05:52.822336Z'
---
