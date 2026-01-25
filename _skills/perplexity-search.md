---
id: perplexity-search
slug: perplexity-search
name: Perplexity Search
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: perplexity-search

  description: Perform AI-powered web searches with real-time information using Perplexity
  models via LiteLLM and OpenRouter. This skill should be used when conducting web
  searches for current information, finding recent scientific literature, getting
  grounded answers with source citations, or accessing information beyond the model
  knowledge cutoff. Provides access to multiple Perplexity models including Sonar
  Pro, Sonar Pro Search (advanced agentic search), and Sonar R...'
full_prompt_length: 14894
tools_mentioned:
- go
- Python
- PostgreSQL
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/perplexity-search/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/perplexity-search/SKILL.md
fetched_at: '2026-01-25T03:51:39.777714+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:37:14.211550Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, specific
      instructions, and practical examples. It follows prompt engineering best practices
      by defining scope, constraints, and providing actionable guidance. The only
      minor limitation is that it's truncated mid-sentence in the 'Crafting Effective
      Queries' section, which slightly impacts completeness.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate real-world value for accessing current
      information beyond model knowledge cutoffs, which is critical for scientific
      research and development tasks. It comprehensively covers setup, usage, model
      selection, and query crafting with practical examples. The integration with
      OpenRouter and LiteLLM makes it highly actionable for users needing real-time
      web-grounded information with citations.
  overall_rating: 4.75
  summary: A highly practical and well-documented skill that effectively bridges the
    gap between AI models and real-time web information, making it invaluable for
    scientific research and current information retrieval.
  tags_suggested:
  - web-search
  - real-time-information
  - scientific-research
  - literature-review
  - source-citations
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:52.020899Z'
indexed_at: '2026-01-25T04:05:52.020905Z'
---
