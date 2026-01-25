---
id: spec-miner
slug: spec-miner
name: Spec Miner
description: '- **Feature Forge** - Creates specs for new features'
prompt_preview: "---\nname: spec-miner\ndescription: Use when understanding legacy\
  \ or undocumented systems, creating documentation for existing code, or extracting\
  \ specifications from implementations. Invoke for legacy analysis, code archaeology,\
  \ undocumented features.\ntriggers:\n  - reverse engineer\n  - legacy code\n  -\
  \ code analysis\n  - undocumented\n  - understand codebase\n  - existing system\n\
  role: specialist\nscope: review\nallowed-tools: Read, Grep, Glob, Bash\noutput-format:\
  \ document\n---\n\n# Spec Miner\n\nReverse-eng..."
full_prompt_length: 2965
tools_mentioned: []
category: community
category_display: Community
source_repo: jeffallan/claude-skills
source_path: skills/spec-miner/SKILL.md
source_url: https://github.com/jeffallan/claude-skills/blob/main/skills/spec-miner/SKILL.md
fetched_at: '2026-01-25T03:52:24.857096+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-25T04:01:52.396037Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear role definition,
      workflow steps, and constraints. It follows best practices by defining triggers,
      scope, and output format upfront. The reference system is innovative but introduces
      potential dependency issues if referenced files don't exist.
  usefulness:
    score: 4.5
    reasoning: This skill addresses a common and valuable real-world problem of understanding
      legacy/undocumented systems. The EARS format and structured output provide immediate
      value for documentation and onboarding. The dual-hat approach (Arch/QA) ensures
      comprehensive analysis, though the tool limitation to Read/Grep/Glob/Bash may
      restrict some modern codebase analysis capabilities.
  overall_rating: 4.5
  summary: A well-crafted, professional-grade prompt that excels at structured legacy
    code analysis with clear workflows and documentation standards, though its external
    reference dependencies could be a practical limitation.
  tags_suggested:
  - legacy-analysis
  - code-documentation
  - reverse-engineering
  - software-archaeology
  - specification-extraction
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:52.924953Z'
indexed_at: '2026-01-25T04:05:52.924958Z'
---
