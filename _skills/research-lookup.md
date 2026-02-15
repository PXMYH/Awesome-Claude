---
id: research-lookup
slug: research-lookup
name: Research Information Lookup
description: Whether you need quick fact-finding or deep analytical synthesis, this
  skill automatically adapts to deliver the right level of research support for your
  scientific writing needs.
prompt_preview: '---

  name: research-lookup

  description: "Look up current research information using Perplexity''s Sonar Pro
  Search or Sonar Reasoning Pro models through OpenRouter. Automatically selects the
  best model based on query complexity. Search academic papers, recent studies, technical
  documentation, and general research information with citations."

  allowed-tools: [Read, Write, Edit, Bash]

  ---


  # Research Information Lookup


  ## Overview


  This skill enables real-time research information lookup using Perpl...'
full_prompt_length: 24535
tools_mentioned:
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/research-lookup/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/research-lookup/SKILL.md
fetched_at: '2026-02-15T04:21:17.068441+00:00'
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
  fetched_at: '2026-02-15T04:33:50.237393Z'
indexed_at: '2026-02-15T04:33:50.237398Z'
---
