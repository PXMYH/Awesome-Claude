---
id: etetoolkit
slug: etetoolkit
name: ETE Toolkit Skill
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: etetoolkit\ndescription: Phylogenetic tree toolkit (ETE).\
  \ Tree manipulation (Newick/NHX), evolutionary event detection, orthology/paralogy,\
  \ NCBI taxonomy, visualization (PDF/SVG), for phylogenomics.\nlicense: GPL-3.0 license\n\
  metadata:\n    skill-author: K-Dense Inc.\n---\n\n# ETE Toolkit Skill\n\n## Overview\n\
  \nETE (Environment for Tree Exploration) is a toolkit for phylogenetic and hierarchical\
  \ tree analysis. Manipulate trees, analyze evolutionary events, visualize results,\
  \ and integrate with b..."
full_prompt_length: 18703
tools_mentioned:
- go
- sqlite
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/etetoolkit/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/etetoolkit/SKILL.md
fetched_at: '2026-01-25T03:51:33.820098+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:27:57.457169Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides clear examples and specific code snippets for tree
      manipulation and analysis, demonstrating good clarity for users familiar with
      phylogenetics. However, it lacks comprehensive edge case handling (e.g., malformed
      trees, missing alignments) and has incomplete coverage of NCBI taxonomy integration,
      which is mentioned but not elaborated. The structure follows best practices
      with categorized capabilities but could benefit from more explicit constraints
      and error handling guidance.
  usefulness:
    score: 4.0
    reasoning: This skill offers high real-world value for phylogenomics researchers
      and bioinformaticians working with gene trees, orthology detection, and evolutionary
      event analysis. The practical examples for tree manipulation, orthology detection,
      and format conversion are immediately actionable for common tasks in comparative
      genomics. The integration with NCBI taxonomy, though incomplete in the prompt,
      would significantly enhance its utility for taxonomic-aware analyses.
  overall_rating: 3.75
  summary: A solid phylogenetic analysis skill with strong practical examples for
    tree manipulation and evolutionary event detection, though it needs better edge
    case handling and completion of the taxonomy integration section to reach its
    full potential.
  tags_suggested:
  - phylogenetics
  - bioinformatics
  - tree-analysis
  - orthology-detection
  - evolutionary-biology
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:51.837959Z'
indexed_at: '2026-01-25T04:05:51.837965Z'
---
