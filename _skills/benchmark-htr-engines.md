---
id: benchmark-htr-engines
slug: benchmark-htr-engines
name: Benchmark HTR Engines
description: <!-- Keep under 500 lines. Extract large examples to references/EXAMPLES.md
  if needed. -->
prompt_preview: "---\nname: benchmark-htr-engines\ndescription: >\n  Select an OCR/HTR\
  \ engine by benchmarking candidates on the same labelled\n  samples — source ground\
  \ truth from open datasets (e.g. Hugging Face PAGE-XML\n  corpora) or hand-transcription,\
  \ wrap every engine behind a\n  transcribe(image_path) -> str adapter (vision-LLMs\
  \ via any OpenAI-compatible\n  endpoint, dedicated HTR REST APIs, cloud OCR), and\
  \ score with zero-dependency\n  raw CER, lenient CER, WER, and a critical name/date\
  \ token diff. Use when\n  ch..."
full_prompt_length: 19126
tools_mentioned:
- python
- rest
- REST
- Python
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/benchmark-htr-engines/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/benchmark-htr-engines/SKILL.md
fetched_at: '2026-07-12T05:34:26.362746+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-12T08:06:14.946480Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0064dbfa10 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f0064dbfa10 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-12T09:23:56.132784Z'
indexed_at: '2026-07-12T09:23:56.132789Z'
---
