---
id: c-network
slug: c-network
name: Networking
description: '- Use `doggo` for DNS debugging instead of `dig` or `nslookup`'
prompt_preview: '---

  name: c-network

  description: DNS lookups with doggo and readable HTTP requests with httpie — modern
  networking tools for the terminal.

  tags: [dns, http, networking, api]

  ---


  # Networking


  ## doggo (DNS client)


  ```bash

  # Basic DNS lookup

  doggo example.com


  # Specific record type

  doggo example.com MX

  doggo example.com AAAA

  doggo example.com TXT

  doggo example.com NS

  doggo example.com CNAME


  # Use specific nameserver

  doggo example.com --nameserver 1.1.1.1

  doggo example.com --nameserver 8.8.8.8...'
full_prompt_length: 1592
tools_mentioned: []
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-network/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-network/SKILL.md
fetched_at: '2026-03-22T04:19:51.494009+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-22T05:14:15.862253Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc3f5674980 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc3f5674980 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-22T06:44:15.716485Z'
indexed_at: '2026-03-22T06:44:15.716491Z'
---
