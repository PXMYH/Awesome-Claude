---
id: windows-vm
slug: windows-vm
name: Headless Windows 11 VM
description: '- **Node.js is not pre-installed** — the Claude Code install script
  (`irm https://claude.ai/install.ps1 | iex`) will report success but `claude` won''t
  work without Node. Install Node.js via MSI first.'
prompt_preview: '---

  name: windows-vm

  description: Create, manage, or connect to a headless Windows 11 VM running in Docker
  with SSH access. Use when the user wants to spin up, stop, restart, or SSH into
  a Windows VM.

  argument-hint: "[create|start|stop|restart|ssh|status]"

  allowed-tools: Bash, Read, Write

  ---


  # Headless Windows 11 VM


  Manage a headless Windows 11 VM running via [dockur/windows](https://github.com/dockur/windows)
  in Docker with KVM acceleration. The VM is accessible via SSH only — no RDP or GUI...'
full_prompt_length: 9988
tools_mentioned:
- Docker
- docker
- Node.js
category: community
category_display: Community
source_repo: obra/superpowers-lab
source_path: skills/windows-vm/SKILL.md
source_url: https://github.com/obra/superpowers-lab/blob/main/skills/windows-vm/SKILL.md
fetched_at: '2026-03-29T04:39:00.537730+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-29T05:57:46.466785Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f9d974ac1a0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f9d974ac1a0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-29T07:03:20.849850Z'
indexed_at: '2026-03-29T07:03:20.849859Z'
---
