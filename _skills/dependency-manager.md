---
id: dependency-manager
slug: dependency-manager
name: Dependency Manager
description: Claude skill for Dependency Manager
prompt_preview: '---

  name: dependency-manager

  description: "Use this agent when you need to audit dependencies for vulnerabilities,
  resolve version conflicts, optimize bundle sizes, or implement automated dependency
  updates. Specifically:\\n\\n<example>\\nContext: A project has accumulated security
  vulnerabilities in its dependency tree that need immediate remediation.\\nuser:
  \"We have 12 high-severity CVEs in our dependencies. Can you help fix them?\"\\nassistant:
  \"I''ll use the dependency-manager agent to sca...'
full_prompt_length: 8787
tools_mentioned:
- Go
- PHP
- JavaScript
- Python
- React
category: 06-developer-experience
category_display: 06 Developer Experience
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/06-developer-experience/dependency-manager.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/06-developer-experience/dependency-manager.md
fetched_at: '2026-02-07T04:07:48.475037Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:03:00.611639Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is highly structured with clear categories and checklists,
      demonstrating strong specificity in scope definition. However, it's incomplete—the
      development workflow section cuts off mid-sentence, and the communication protocol
      lacks implementation details for the context query. While the content is comprehensive,
      the abrupt ending and missing sections reduce clarity and completeness.
  usefulness:
    score: 4.0
    reasoning: The prompt provides exceptional real-world value with detailed checklists
      covering security, compliance, optimization, and multi-ecosystem support. It
      addresses critical developer pain points like vulnerability management and version
      conflicts. The actionable frameworks and systematic approach would immediately
      benefit teams managing complex dependency trees, though the incomplete workflow
      limits immediate implementation.
  overall_rating: 3.75
  summary: A well-structured but incomplete prompt that excels in comprehensive scope
    definition and practical frameworks, though execution guidance is truncated and
    requires completion for full utility.
  tags_suggested:
  - dependency-management
  - security-auditing
  - package-manager
  - developer-tools
  - multi-ecosystem
github_metrics:
  stars: 9780
  forks: 1066
  open_issues: 2
  last_commit: '2026-02-06'
  fetched_at: '2026-02-07T04:08:16.529193Z'
indexed_at: '2026-02-07T04:08:26.800373Z'
---
