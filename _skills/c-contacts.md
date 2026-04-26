---
id: c-contacts
slug: c-contacts
name: Contacts — Address Book
description: '- Always search by partial name (uses `contains`) to be flexible'
prompt_preview: "---\nname: c-contacts\ndescription: macOS Contacts — search, list,\
  \ and look up contact details via AppleScript.\ntags: [contacts, address-book, people,\
  \ phone]\n---\n\n# Contacts — Address Book\n\nAccess macOS Contacts app via AppleScript.\
  \ No CLI tool needed.\n\n## Commands\n\n```bash\n# Search for a contact by name\n\
  osascript -e 'tell application \"Contacts\"\n  set results to (every person whose\
  \ name contains \"John\")\n  set output to \"\"\n  repeat with p in results\n  \
  \  set output to output & name of p & linefeed..."
full_prompt_length: 1864
tools_mentioned: []
category: community
category_display: Community
source_repo: daxaur/openpaw
source_path: skills/c-contacts/SKILL.md
source_url: https://github.com/daxaur/openpaw/blob/main/skills/c-contacts/SKILL.md
fetched_at: '2026-04-26T04:59:01.575881+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-26T06:03:50.892212Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe111f29f0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe111f29f0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-26T07:41:25.710426Z'
indexed_at: '2026-04-26T07:41:25.710431Z'
---
