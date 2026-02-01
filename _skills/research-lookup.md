---
id: research-lookup
slug: research-lookup
name: Research Information Lookup
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: research-lookup\ndescription: Look up current research\
  \ information using Perplexity Sonar Pro Search or Sonar Reasoning Pro models through\
  \ OpenRouter. Automatically selects the best model based on query complexity. Search\
  \ academic papers, recent studies, technical documentation, and general research\
  \ information with citations.\nallowed-tools: [Read, Write, Edit, Bash]\nlicense:\
  \ MIT license\nmetadata:\n    skill-author: K-Dense Inc.\n---\n\n# Research Information\
  \ Lookup\n\n## Overview\n\nThis skill..."
full_prompt_length: 20735
tools_mentioned:
- go
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/research-lookup/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/research-lookup/SKILL.md
fetched_at: '2026-02-01T04:28:34.137873+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:41:38.983240Z'
  prompt_quality:
    score: 4.0
    reasoning: 'The prompt is well-structured with clear sections and specific examples,
      but contains a critical flaw: it references a ''scientific-schematics'' skill
      and a ''Nano Banana Pro'' tool that are not defined in the allowed tools list.
      This creates ambiguity about actual capabilities and could lead to execution
      errors. The core research lookup instructions are clear and specific.'
  usefulness:
    score: 4.5
    reasoning: The skill addresses a genuine need for current research information
      with proper citations, which is valuable for scientific work. The model selection
      based on query complexity is practical. However, the usefulness is diminished
      by the undefined external dependencies (schematics generation) that may not
      be available in the actual environment.
  overall_rating: 4.25
  summary: A well-conceived research lookup skill with practical applications in scientific
    work, but significantly hampered by references to undefined external tools and
    skills that create implementation ambiguity.
  tags_suggested:
  - research
  - academic
  - perplexity
  - citations
  - scientific
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.005847Z'
indexed_at: '2026-02-01T04:32:50.005854Z'
---
