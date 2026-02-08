---
id: toon-formatter
slug: toon-formatter
name: TOON v2.0 Format Expert
description: '- **Specification**: https://github.com/toon-format/spec'
prompt_preview: "---\nname: toon-formatter\ndescription: Token-Oriented Object Notation\
  \ (TOON) format expert for 30-60% token savings on structured data. Auto-applies\
  \ to arrays with 5+ items, tables, logs, API responses, database results. Supports\
  \ tabular, inline, and expanded formats with comma/tab/pipe delimiters. Triggers\
  \ on large JSON, data optimization, token reduction, structured data, arrays, tables,\
  \ logs, metrics, TOON.\nallowed-tools: Read, Write, Edit, Bash\nmodel: sonnet\n\
  license: MIT\nmetadata:\n  author: r..."
full_prompt_length: 6146
tools_mentioned:
- javascript
- rest
- react
category: community
category_display: Community
source_repo: raintree-technology/claude-starter
source_path: skills/toon-formatter/SKILL.md
source_url: https://github.com/raintree-technology/claude-starter/blob/main/skills/toon-formatter/SKILL.md
fetched_at: '2026-02-08T04:32:33.899453+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:03:03.003647Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured with comprehensive
      specifications, multiple format examples, and clear trigger conditions. It follows
      best practices by providing explicit 'when to use' and 'when not to use' guidance,
      though it lacks explicit handling for edge cases like malformed data or conversion
      errors.
  usefulness:
    score: 5.0
    reasoning: This skill provides substantial real-world value for token optimization
      in AI workflows, particularly for API responses, logs, and database results
      where 30-60% savings are significant. It's immediately actionable with concrete
      examples and covers the most common structured data scenarios comprehensively.
  overall_rating: 4.75
  summary: An excellent, production-ready skill that delivers clear token savings
    for structured data with comprehensive specifications and practical examples,
    though it could benefit from more explicit error handling guidance.
  tags_suggested:
  - data optimization
  - token reduction
  - structured data
  - format conversion
  - API efficiency
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.674402Z'
indexed_at: '2026-02-08T04:36:45.674408Z'
---
