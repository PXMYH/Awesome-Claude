---
id: verify-web-app-runtime
slug: verify-web-app-runtime
name: Verify Web App Runtime
description: <!-- Keep under 500 lines. Extract large examples to references/EXAMPLES.md
  if needed. -->
prompt_preview: "---\nname: verify-web-app-runtime\ndescription: >\n  Verify that\
  \ a frontend or visual change actually works by running the app in\n  headless Chromium\
  \ and observing pixels plus console output — runtime\n  verification for WebGL,\
  \ GPGPU, Canvas, and WebAudio surfaces that static\n  review and unit tests cannot\
  \ cover. Launches with the SwiftShader/ANGLE\n  flags WebGL2 needs, probes EXT_color_buffer_half_float\
  \ before trusting a\n  GPGPU path, asserts visibilityState === 'visible' and non-black\
  \ canvas\n  lum..."
full_prompt_length: 15295
tools_mentioned:
- Python
- python
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/verify-web-app-runtime/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/verify-web-app-runtime/SKILL.md
fetched_at: '2026-07-26T05:34:26.215939+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-26T08:50:33.770318Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1607e7a2d0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f1607e7a2d0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-26T09:24:31.541529Z'
indexed_at: '2026-07-26T09:24:31.541534Z'
---
