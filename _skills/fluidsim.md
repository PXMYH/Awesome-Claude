---
id: fluidsim
slug: fluidsim
name: FluidSim
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: fluidsim\ndescription: Framework for computational fluid\
  \ dynamics simulations using Python. Use when running fluid dynamics simulations\
  \ including Navier-Stokes equations (2D/3D), shallow water equations, stratified\
  \ flows, or when analyzing turbulence, vortex dynamics, or geophysical flows. Provides\
  \ pseudospectral methods with FFT, HPC support, and comprehensive output analysis.\n\
  license: CeCILL FREE SOFTWARE LICENSE AGREEMENT\nmetadata:\n    skill-author: K-Dense\
  \ Inc.\n---\n\n# FluidSim\n\n## O..."
full_prompt_length: 10212
tools_mentioned:
- go
- Python
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/fluidsim/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/fluidsim/SKILL.md
fetched_at: '2026-01-25T03:51:34.309946+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:28:38.113474Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections for
      installation, workflow, and solver selection. It provides specific code examples
      and parameter configurations, though it lacks explicit error handling guidance
      for common CFD issues like numerical instability or convergence failures.
  usefulness:
    score: 5.0
    reasoning: This is highly practical for computational fluid dynamics practitioners,
      offering a complete workflow from installation to analysis. The inclusion of
      multiple solver types (2D/3D Navier-Stokes, stratified flows, shallow water)
      and performance optimization features makes it immediately valuable for scientific
      computing tasks.
  overall_rating: 4.75
  summary: An excellent, production-ready prompt that provides comprehensive CFD simulation
    capabilities with clear documentation and practical examples, though it could
    benefit from more troubleshooting guidance for numerical issues.
  tags_suggested:
  - scientific-computing
  - computational-fluid-dynamics
  - numerical-simulation
  - high-performance-computing
  - python-framework
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:51.852659Z'
indexed_at: '2026-01-25T04:05:51.852668Z'
---
