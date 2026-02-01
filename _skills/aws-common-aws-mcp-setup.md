---
id: aws-common-aws-mcp-setup
slug: aws-common-aws-mcp-setup
name: AWS MCP Server Configuration Guide
description: '| Issue | Cause | Solution |'
prompt_preview: '---

  name: aws-mcp-setup

  description: Configure AWS Documentation MCP server to query up-to-date AWS knowledge,
  APIs, and best practices

  ---


  # AWS MCP Server Configuration Guide


  ## Overview


  This guide helps you configure AWS MCP tools for AI agents. Two options are available:


  | Option | Requirements | Capabilities |

  |--------|--------------|--------------|

  | **Full AWS MCP Server** | Python 3.10+, uvx, AWS credentials | Execute AWS API
  calls + documentation search |

  | **AWS Documentation MCP*...'
full_prompt_length: 4776
tools_mentioned:
- aws
- Python
- AWS
category: infrastructure
category_display: Infrastructure
source_repo: zxkane/aws-skills
source_path: plugins/aws-common/skills/aws-mcp-setup/SKILL.md
source_url: https://github.com/zxkane/aws-skills/blob/main/plugins/aws-common/skills/aws-mcp-setup/SKILL.md
fetched_at: '2026-02-01T04:30:07.257856+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:30:09.269633Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, tables,
      and code examples. It provides comprehensive step-by-step guidance with multiple
      configuration options and credential strategies. The only minor issue is an
      incomplete JSON snippet for the AWS Documentation MCP configuration that lacks
      closing braces.
  usefulness:
    score: 5.0
    reasoning: This is highly practical for developers working with AWS in AI agents,
      covering both full and documentation-only options with real-world scenarios.
      It includes specific commands, IAM permission examples, and credential configuration
      patterns that users can immediately implement. The guide addresses common edge
      cases like checking existing configurations and choosing the appropriate option
      based on environment.
  overall_rating: 4.75
  summary: An excellent, production-ready configuration guide that balances technical
    depth with accessibility, though it contains a minor formatting issue in the final
    JSON example.
  tags_suggested:
  - AWS
  - MCP
  - Infrastructure
  - Configuration
  - Documentation
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:51.082929Z'
indexed_at: '2026-02-01T04:32:51.082934Z'
---
