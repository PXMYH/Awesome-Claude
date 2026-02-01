---
id: scientific-writing
slug: scientific-writing
name: Scientific Writing
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: scientific-writing

  description: Core skill for the deep research and writing tool. Write scientific
  manuscripts in full paragraphs (never bullet points). Use two-stage process with
  (1) section outlines with key points using research-lookup then (2) convert to flowing
  prose. IMRAD structure, citations (APA/AMA/Vancouver), figures/tables, reporting
  guidelines (CONSORT/STROBE/PRISMA), for research papers and journal submissions.

  allowed-tools: [Read, Write, Edit, Bash]

  license: MIT licens...'
full_prompt_length: 34547
tools_mentioned:
- go
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/scientific-writing/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/scientific-writing/SKILL.md
fetched_at: '2026-02-01T04:28:35.736830+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T03:53:17.260097Z'
  prompt_quality:
    score: 4.5
    reasoning: 'The prompt is highly structured and specific, clearly defining the
      IMRAD process, citation styles, and mandatory visual elements. It effectively
      uses a two-stage workflow (outline then prose) and includes concrete tool commands.
      However, it has a critical flaw: it mandates the use of a specific external
      tool (''scientific-schematics'' and ''generate-image'') that is not listed in
      the ''allowed-tools'' section, creating a potential execution failure.'
  usefulness:
    score: 4.0
    reasoning: This skill is highly practical for academic and research contexts,
      offering a comprehensive framework for manuscript generation that includes literature-backed
      writing and strict adherence to reporting guidelines. The inclusion of visual
      generation requirements adds significant value for modern scientific publishing.
      However, its utility is slightly diminished by the dependency on external tools
      not defined in the prompt, which could confuse users attempting to implement
      it.
  overall_rating: 4.25
  summary: A robust and detailed prompt for scientific writing that enforces high
    standards of structure and visual communication, though it suffers from a critical
    inconsistency regarding tool dependencies.
  tags_suggested:
  - scientific-writing
  - academic-research
  - manuscript-generation
  - reporting-guidelines
  - visual-communication
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.036271Z'
indexed_at: '2026-02-01T04:32:50.036277Z'
---
