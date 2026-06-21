---
id: pipeline-gpu-kernel
slug: pipeline-gpu-kernel
name: Pipeline GPU Kernel
description: '- `analyze-kernel-bottleneck` — identify whether the kernel is memory-bound
  and calculate the compute/load ratio that drives variant selection'
prompt_preview: "---\nname: pipeline-gpu-kernel\ndescription: >\n  Apply software\
  \ pipelining (double-buffering) to a tiled GPU kernel to overlap\n  global memory\
  \ loads with Tensor Core computation. Covers prologue/loop/epilogue\n  restructuring,\
  \ LDG-register vs cp.async (LDGSTS) variant selection based on\n  compute/load ratio,\
  \ shared memory budget verification against architecture-specific\n  occupancy cliffs,\
  \ and SASS-level verification of load/compute overlap.\nlicense: MIT\nallowed-tools:\
  \ Read Write Edit Bash Grep Gl..."
full_prompt_length: 18916
tools_mentioned: []
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/pipeline-gpu-kernel/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/pipeline-gpu-kernel/SKILL.md
fetched_at: '2026-06-21T06:52:19.719364+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-21T09:45:47.231684Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9fa55e0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9fa55e0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-21T10:34:02.870516Z'
indexed_at: '2026-06-21T10:34:02.870521Z'
---
