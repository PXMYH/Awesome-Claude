---
id: geopandas
slug: geopandas
name: GeoPandas
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: geopandas

  description: Python library for working with geospatial vector data including shapefiles,
  GeoJSON, and GeoPackage files. Use when working with geographic data for spatial
  analysis, geometric operations, coordinate transformations, spatial joins, overlay
  operations, choropleth mapping, or any task involving reading/writing/analyzing
  vector geographic data. Supports PostGIS databases, interactive maps, and integration
  with matplotlib/folium/cartopy. Use for tasks like buffer an...'
full_prompt_length: 7936
tools_mentioned:
- python
- go
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/geopandas/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/geopandas/SKILL.md
fetched_at: '2026-02-15T04:21:09.068226+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:29:42.448370Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, with comprehensive
      coverage of installation, core concepts, and common operations. It follows best
      practices by providing concrete code examples and linking to reference documentation.
      However, it lacks explicit edge case handling (e.g., CRS mismatches, missing
      geometry columns) and has a minor formatting issue with an incomplete code block
      in the visualization section.
  usefulness:
    score: 5.0
    reasoning: This is highly practical for real-world geospatial tasks, covering
      essential operations like reading/writing data, coordinate transformations,
      spatial joins, and visualization. The inclusion of optional dependencies and
      performance optimizations (like PyArrow) makes it immediately actionable for
      production workflows. It comprehensively addresses common use cases from data
      ingestion to analysis and mapping.
  overall_rating: 4.75
  summary: An excellent, production-ready skill prompt that provides comprehensive
    geospatial capabilities with clear examples and best practices, though it could
    benefit from more explicit edge case guidance and minor formatting fixes.
  tags_suggested:
  - geospatial
  - data-analysis
  - mapping
  - spatial-operations
  - vector-data
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:49.990249Z'
indexed_at: '2026-02-15T04:33:49.990255Z'
---
