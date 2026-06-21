---
id: bulk-rnaseq
slug: bulk-rnaseq
name: Bulk RNA-seq
description: '- nf-core/rnaseq: https://nf-co.re/rnaseq · STAR: https://github.com/alexdobin/STAR
  · Salmon: https://salmon.readthedocs.io'
prompt_preview: '---

  name: bulk-rnaseq

  description: End-to-end bulk RNA-seq orchestrator — takes raw FASTQ reads through
  QC and trimming (FastQC, fastp/Trim Galore), alignment and quantification (STAR,
  Salmon, featureCounts), assembles a gene-level counts matrix, then hands off to
  differential expression (pydeseq2), pathway/GSEA enrichment (pathway-enrichment),
  and publication figures (scientific-visualization). Use whenever the user has bulk
  RNA-seq reads or quant output and wants a complete, reproducible diffe...'
full_prompt_length: 14560
tools_mentioned:
- docker
- Go
- python
- Python
- go
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: skills/bulk-rnaseq/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/bulk-rnaseq/SKILL.md
fetched_at: '2026-06-21T06:49:12.391907+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-21T07:00:34.415413Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaaa667050 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaaa667050 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-21T10:33:59.389685Z'
indexed_at: '2026-06-21T10:33:59.389691Z'
---
