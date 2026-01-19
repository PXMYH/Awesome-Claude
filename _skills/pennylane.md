---
id: pennylane
slug: pennylane
name: PennyLane
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: pennylane

  description: Hardware-agnostic quantum ML framework with automatic differentiation.
  Use when training quantum circuits via gradients, building hybrid quantum-classical
  models, or needing device portability across IBM/Google/Rigetti/IonQ. Best for variational
  algorithms (VQE, QAOA), quantum neural networks, and integration with PyTorch/JAX/TensorFlow.
  For hardware-specific optimizations use qiskit (IBM) or cirq (Google); for open
  quantum systems use qutip.

  license: Apache-2.0...'
full_prompt_length: 8216
tools_mentioned:
- python
- go
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/pennylane/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/pennylane/SKILL.md
fetched_at: '2026-01-19T00:19:18.896618+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:37:03.045687Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is well-structured with clear sections for overview, installation,
      quick start, and core capabilities. It provides specific code examples and references
      to detailed documentation. However, the 'Common Workflows' section is incomplete
      (cut off mid-example), which reduces clarity and completeness.
  usefulness:
    score: 5.0
    reasoning: This is highly practical for quantum computing developers, covering
      real-world use cases like VQE, QAOA, and hybrid quantum-classical models. It
      provides actionable installation commands, working code examples, and clear
      guidance on when to use PennyLane versus alternatives like Qiskit or Cirq. The
      comprehensive coverage of device management and optimization makes it immediately
      valuable.
  overall_rating: 4.75
  summary: A high-quality, comprehensive skill prompt that effectively guides users
    on quantum machine learning with PennyLane, though the incomplete workflow example
    slightly detracts from its polish.
  tags_suggested:
  - quantum-computing
  - machine-learning
  - scientific-computing
  - quantum-ml
  - hybrid-models
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.883602Z'
indexed_at: '2026-01-19T01:30:35.883607Z'
---
