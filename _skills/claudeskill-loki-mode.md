---
id: claudeskill-loki-mode
slug: claudeskill-loki-mode
name: Loki Mode v5.28.0
description: '**v5.28.0 | Demo, quick mode, init, cost dashboard, 12 templates, GitHub
  Action | ~270 lines core**'
prompt_preview: '---

  name: loki-mode

  description: Multi-agent autonomous startup system. Triggers on "Loki Mode". Takes
  PRD to deployed product with zero human intervention. Requires --dangerously-skip-permissions
  flag.

  ---


  # Loki Mode v5.28.0


  **You are an autonomous agent. You make decisions. You do not ask questions. You
  do not stop.**


  **New in v5.0.0:** Multi-provider support (Claude/Codex/Gemini), abstract model
  tiers, degraded mode for non-Claude providers. See `skills/providers.md`.


  ---


  ## PRIORITY 1:...'
full_prompt_length: 10048
tools_mentioned: []
category: community
category_display: Community
source_repo: asklokesh/claudeskill-loki-mode
source_path: SKILL.md
source_url: https://github.com/asklokesh/claudeskill-loki-mode/blob/main/SKILL.md
fetched_at: '2026-02-08T04:32:08.587545+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:15:55.363647Z'
  prompt_quality:
    score: 2.5
    reasoning: The prompt is ambitious but poorly structured. It lacks clear, actionable
      instructions for the agent and contains incomplete patterns (e.g., 'Guardrails:'
      is cut off). While it defines a complex system architecture, the actual operational
      logic is vague, relying on external files that may not exist. The 'Quick Reference'
      is dense but not a substitute for explicit step-by-step guidance.
  usefulness:
    score: 2.0
    reasoning: The concept is theoretically useful for automating a full startup pipeline,
      but it's impractical for a single AI agent. It overpromises 'zero human intervention'
      and '100+ specialized agents' without a realistic mechanism for execution. The
      reliance on specific file paths and external systems makes it brittle and difficult
      to deploy in a real-world scenario.
  overall_rating: 2.25
  summary: An overly ambitious and poorly defined prompt that attempts to orchestrate
    a massive autonomous system but lacks the concrete, executable instructions needed
    for a single AI agent to function effectively.
  tags_suggested:
  - over-engineered
  - unrealistic
  - incomplete
  - autonomous-system
  - multi-agent
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:45.400765Z'
indexed_at: '2026-02-08T04:36:45.400771Z'
---
