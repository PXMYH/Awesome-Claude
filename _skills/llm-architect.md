---
id: llm-architect
slug: llm-architect
name: Llm Architect
description: Claude skill for Llm Architect
prompt_preview: '---

  name: llm-architect

  description: "Use when designing LLM systems for production, implementing fine-tuning
  or RAG architectures, optimizing inference serving infrastructure, or managing multi-model
  deployments. Specifically:\\n\\n<example>\\nContext: A startup needs to deploy a
  custom LLM application with sub-200ms latency, fine-tuned on domain-specific data\\nuser:
  \"Design a production LLM architecture that supports our use case with sub-200ms
  P95 latency, includes fine-tuning capability, a...'
full_prompt_length: 9108
tools_mentioned: []
category: 05-data-ai
category_display: 05 Data Ai
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/05-data-ai/llm-architect.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/llm-architect.md
fetched_at: '2026-02-10T04:30:25.578215Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:00:57.825344Z'
  prompt_quality:
    score: 4.5
    reasoning: 'The prompt demonstrates strong clarity and specificity with well-structured
      sections covering LLM architecture, fine-tuning, RAG, and serving patterns.
      It follows best practices by including checklists and systematic workflows.
      However, it has a significant gap: the workflow section is incomplete (ends
      abruptly at ''Implementation''), and the communication protocol references a
      context manager that isn''t defined or implemented in the prompt.'
  usefulness:
    score: 4.0
    reasoning: The prompt provides comprehensive coverage of LLM system design topics
      with practical checklists and architectural patterns that would benefit developers
      building production LLM applications. It offers real-world value through structured
      approaches to optimization, safety, and deployment. The main limitation is the
      incomplete workflow, which reduces immediate actionability for users expecting
      a complete implementation guide.
  overall_rating: 4.25
  summary: A well-structured but incomplete LLM architect prompt that excels in technical
    depth and organization but needs completion of the workflow section and clarification
    of the communication protocol to be fully actionable.
  tags_suggested:
  - llm-architecture
  - system-design
  - production-deployment
  - optimization
  - rag-systems
github_metrics:
  stars: 10075
  forks: 1084
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-10T04:30:47.641906Z'
indexed_at: '2026-02-10T04:30:57.302207Z'
---
