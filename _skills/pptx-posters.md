---
id: pptx-posters
slug: pptx-posters
name: PPTX Research Posters (HTML-Based)
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: pptx-posters\ndescription: Create research posters using\
  \ HTML/CSS that can be exported to PDF or PPTX. Use this skill ONLY when the user\
  \ explicitly requests PowerPoint/PPTX poster format. For standard research posters,\
  \ use latex-posters instead. This skill provides modern web-based poster design\
  \ with responsive layouts and easy visual integration.\nallowed-tools: [Read, Write,\
  \ Edit, Bash]\nlicense: MIT license\nmetadata:\n    skill-author: K-Dense Inc.\n\
  ---\n\n# PPTX Research Posters (HTML-Bas..."
full_prompt_length: 14451
tools_mentioned:
- go
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/pptx-posters/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/pptx-posters/SKILL.md
fetched_at: '2026-02-01T04:28:30.473228+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:37:45.519667Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly specific and well-structured with clear conditional
      logic for when to use this skill versus the default latex-posters skill. It
      provides excellent constraints for AI-generated visual elements with specific,
      measurable requirements (e.g., 3-4 elements max, 10 words max, 80pt+ font sizes).
      The inclusion of concrete examples and strict enforcement rules demonstrates
      strong prompt engineering practices.
  usefulness:
    score: 4.0
    reasoning: This skill addresses a specific, practical need for users who require
      PowerPoint-compatible posters for editing or institutional requirements. The
      workflow guidance for generating AI visuals is actionable and follows modern
      poster design principles. However, the utility is somewhat limited by the strict
      requirement for explicit PPTX requests, which may cause users to miss this skill
      when they actually need it.
  overall_rating: 4.25
  summary: A well-crafted, highly specific skill prompt that excels in constraint
    definition and workflow guidance, though its narrow use case and strict conditional
    logic may limit its discoverability for users who need PowerPoint-compatible posters.
  tags_suggested:
  - poster-design
  - html-css
  - pptx-export
  - ai-visuals
  - scientific-communication
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:49.920392Z'
indexed_at: '2026-02-01T04:32:49.920398Z'
---
