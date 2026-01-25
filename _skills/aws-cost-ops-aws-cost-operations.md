---
id: aws-cost-ops-aws-cost-operations
slug: aws-cost-ops-aws-cost-operations
name: AWS Cost & Operations
description: 'Common alarm configurations for:'
prompt_preview: "---\nname: aws-cost-operations\ndescription: This skill provides\
  \ AWS cost optimization, monitoring, and operational best practices with integrated\
  \ MCP servers for billing analysis, cost estimation, observability, and security\
  \ assessment.\nskills:\n  - aws-mcp-setup\nallowed-tools:\n  - mcp__pricing__*\n\
  \  - mcp__costexp__*\n  - mcp__cw__*\n  - mcp__aws-mcp__*\n  - mcp__awsdocs__*\n\
  \  - Bash(aws ce *)\n  - Bash(aws cloudwatch *)\n  - Bash(aws logs *)\n  - Bash(aws\
  \ budgets *)\n  - Bash(aws cloudtrail *)\n  - Bash(a..."
full_prompt_length: 11159
tools_mentioned:
- AWS
- Kubernetes
- rest
- Python
- aws
category: infrastructure
category_display: Infrastructure
source_repo: zxkane/aws-skills
source_path: plugins/aws-cost-ops/skills/aws-cost-operations/SKILL.md
source_url: https://github.com/zxkane/aws-skills/blob/main/plugins/aws-cost-ops/skills/aws-cost-operations/SKILL.md
fetched_at: '2026-01-25T03:52:49.652563+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:30:18.901460Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is well-structured with clear sections and specific tool
      configurations. It follows best practices by defining hooks for pre-tool verification
      and providing fallback guidance when MCP tools are unavailable. However, the
      prompt is cut off mid-sentence in the CloudTrail section, which is a significant
      quality issue.
  usefulness:
    score: 4.0
    reasoning: This skill provides high practical value for AWS cost optimization
      and operations, covering comprehensive monitoring, cost analysis, and security
      assessment capabilities. The integrated MCP servers address real-world DevOps
      and FinOps tasks, though the incomplete CloudTrail section reduces completeness.
  overall_rating: 4.25
  summary: A robust AWS operations skill with strong prompt engineering and practical
    value, but needs completion of the CloudTrail section to be fully effective.
  tags_suggested:
  - aws
  - cost-optimization
  - monitoring
  - devops
  - finops
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:53.230806Z'
indexed_at: '2026-01-25T04:05:53.230812Z'
---
