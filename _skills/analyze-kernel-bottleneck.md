---
id: analyze-kernel-bottleneck
slug: analyze-kernel-bottleneck
name: Analyze Kernel Bottleneck
description: '- `pipeline-gpu-kernel` -- implement software pipelining with cp.async
  when analysis identifies a memory-bound kernel with low compute/load ratio'
prompt_preview: "---\nname: analyze-kernel-bottleneck\ndescription: >\n  Systematically\
  \ identify whether a GPU kernel is compute-bound, memory-bound,\n  or latency-bound\
  \ using roofline analysis, occupancy calculations, compute/load\n  ratio per tile,\
  \ and SASS instruction inspection. Produces a decision matrix\n  for optimization\
  \ strategy selection (cp.async, warp interleaving, tiling,\n  double-buffering,\
  \ or CuAssembler hand-tuning).\nlicense: MIT\nallowed-tools: Read Grep Glob Bash\n\
  metadata:\n  author: Philipp Thoss\n  ve..."
full_prompt_length: 17023
tools_mentioned: []
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/analyze-kernel-bottleneck/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/analyze-kernel-bottleneck/SKILL.md
fetched_at: '2026-04-12T04:48:48.135706+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-12T06:17:19.463231Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f3993612ea0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f3993612ea0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-12T07:23:21.037561Z'
indexed_at: '2026-04-12T07:23:21.037567Z'
---
