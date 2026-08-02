---
id: timesfm-forecasting
slug: timesfm-forecasting
name: TimesFM Forecasting
description: '- **Paper**: [A Decoder-Only Foundation Model for Time-Series Forecasting](https://arxiv.org/abs/2310.10688)
  (ICML 2024)'
prompt_preview: "---\nname: timesfm-forecasting\ndescription: Zero-shot time series\
  \ forecasting with Google's TimesFM foundation model. Use for any univariate time\
  \ series (sales, sensors, energy, vitals, weather) without training a custom model.\
  \ Supports CSV/DataFrame/array inputs with point forecasts and prediction intervals.\
  \ Includes a preflight system checker script to verify RAM/GPU before first use.\n\
  allowed-tools: Read Write Edit Bash\nlicense: Apache-2.0 license\nmetadata:\n  version:\
  \ \"1.2\"\n  skill-author: Clay..."
full_prompt_length: 15420
tools_mentioned:
- Python
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: skills/timesfm-forecasting/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/timesfm-forecasting/SKILL.md
fetched_at: '2026-08-02T05:25:45.310374+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-08-02T05:57:28.980172Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0acde5940 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0acde5940 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-08-02T09:26:13.374839Z'
indexed_at: '2026-08-02T09:26:13.374845Z'
---
