---
id: rag-architect
slug: rag-architect
name: RAG Architect
description: Vector databases (Pinecone, Weaviate, Chroma, Qdrant, Milvus, pgvector),
  embedding models (OpenAI, Cohere, Sentence Transformers, BGE, E5), chunking algorithms,
  semantic search, hybrid search, BM25, r...
prompt_preview: "---\nname: rag-architect\ndescription: Use when building RAG systems,\
  \ vector databases, or knowledge-grounded AI applications requiring semantic search,\
  \ document retrieval, or context augmentation.\nlicense: MIT\nmetadata:\n  author:\
  \ https://github.com/Jeffallan\n  version: \"1.0.0\"\n  domain: data-ml\n  triggers:\
  \ RAG, retrieval-augmented generation, vector search, embeddings, semantic search,\
  \ vector database, document retrieval, knowledge base, context retrieval, similarity\
  \ search\n  role: architect\n  sc..."
full_prompt_length: 4450
tools_mentioned:
- python
category: community
category_display: Community
source_repo: jeffallan/claude-skills
source_path: skills/rag-architect/SKILL.md
source_url: https://github.com/jeffallan/claude-skills/blob/main/skills/rag-architect/SKILL.md
fetched_at: '2026-02-15T04:22:06.703885+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:00:04.725742Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear role definition,
      specific triggers, and a comprehensive workflow. It follows prompt engineering
      best practices by including constraints (MUST DO/MUST NOT DO) and output templates.
      The only minor weakness is the incomplete Knowledge Reference section at the
      end, which appears truncated.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate, actionable value for developers building
      RAG systems. It covers the entire lifecycle from requirements analysis to evaluation,
      with specific technical guidance on vector databases, chunking, and retrieval
      optimization. The constraints and reference guides make it practical for real-world
      production systems.
  overall_rating: 4.75
  summary: An excellent, production-ready prompt that provides comprehensive guidance
    for RAG system design with clear constraints and actionable workflows.
  tags_suggested:
  - RAG
  - vector-databases
  - semantic-search
  - system-design
  - ai-architecture
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:51.183146Z'
indexed_at: '2026-02-15T04:33:51.183152Z'
---
