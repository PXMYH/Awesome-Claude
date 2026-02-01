---
id: clinical-reports
slug: clinical-reports
name: Clinical Report Writing
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: clinical-reports\ndescription: Write comprehensive clinical\
  \ reports including case reports (CARE guidelines), diagnostic reports (radiology/pathology/lab),\
  \ clinical trial reports (ICH-E3, SAE, CSR), and patient documentation (SOAP, H&P,\
  \ discharge summaries). Full support with templates, regulatory compliance (HIPAA,\
  \ FDA, ICH-GCP), and validation tools.\nallowed-tools: [Read, Write, Edit, Bash]\n\
  license: MIT License\nmetadata:\n    skill-author: K-Dense Inc.\n---\n\n# Clinical\
  \ Report Writing\n\n#..."
full_prompt_length: 40510
tools_mentioned:
- go
- python
- GCP
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/clinical-reports/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/clinical-reports/SKILL.md
fetched_at: '2026-02-01T04:28:17.983772+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:24:13.885681Z'
  prompt_quality:
    score: 1.5
    reasoning: The prompt is severely incomplete and contains critical structural
      failures. It abruptly cuts off mid-sentence in the CARE guidelines section,
      leaving the core instructions unfinished. The mandatory requirement to generate
      schematics references a non-existent 'scientific-schematics' skill and a bash
      script that likely doesn't exist in the environment, creating a hard dependency
      that will cause execution failure.
  usefulness:
    score: 1.0
    reasoning: The skill is fundamentally unusable due to its incomplete state and
      impossible requirements. The prompt cannot generate any clinical reports because
      it lacks the actual writing instructions, templates, or guidelines beyond the
      initial header. The mandatory schematic generation requirement is a showstopper
      as it references unavailable tools and scripts.
  overall_rating: 1.25
  summary: This is a non-functional prompt that appears to be a partial draft or template
    that was never completed. It contains a header and some conceptual framing but
    lacks the actual implementation details needed to write clinical reports, making
    it completely unusable for its intended purpose.
  tags_suggested:
  - incomplete
  - broken-dependency
  - unusable
  - needs-completion
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:49.687364Z'
indexed_at: '2026-02-01T04:32:49.687370Z'
---
