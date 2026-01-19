---
id: aws-cdk-aws-cdk-development
slug: aws-cdk-aws-cdk-development
name: AWS CDK Development
description: When GitHub Actions workflow files exist in the repository, ensure all
  checks defined in `.github/workflows/` pass before committing. This prevents CI/CD
  failures and maintains code quality standards.
prompt_preview: "---\nname: aws-cdk-development\ndescription: AWS Cloud Development\
  \ Kit (CDK) expert for building cloud infrastructure with TypeScript/Python. Use\
  \ when creating CDK stacks, defining CDK constructs, implementing infrastructure\
  \ as code, or when the user mentions CDK, CloudFormation, IaC, cdk synth, cdk deploy,\
  \ or wants to define AWS infrastructure programmatically. Covers CDK app structure,\
  \ construct patterns, stack composition, and deployment workflows.\ncontext: fork\n\
  skills:\n  - aws-mcp-setup\nallowe..."
full_prompt_length: 10343
tools_mentioned:
- Python
- Go
- python
- aws
- JavaScript
- typescript
- AWS
- TypeScript
- Java
- REST
category: infrastructure
category_display: Infrastructure
source_repo: zxkane/aws-skills
source_path: plugins/aws-cdk/skills/aws-cdk-development/SKILL.md
source_url: https://github.com/zxkane/aws-skills/blob/main/plugins/aws-cdk/skills/aws-cdk-development/SKILL.md
fetched_at: '2026-01-19T00:20:28.644979+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:29:48.763691Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, specific
      tool configurations, and strong guidance on AWS documentation requirements.
      It follows excellent prompt engineering practices with explicit instructions
      for tool usage, dependency management, and best practices. The only minor limitation
      is the somewhat complex MCP tool naming conventions that might require user
      familiarity.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate practical value for AWS CDK development
      with comprehensive coverage of infrastructure as code workflows. It integrates
      real-time AWS documentation access, handles credential scenarios gracefully,
      and includes critical best practices like resource naming conventions that prevent
      deployment conflicts. The pre-deployment validation hook and dependency management
      make it production-ready for real development teams.
  overall_rating: 4.75
  summary: An excellent, production-ready skill that combines comprehensive CDK guidance
    with integrated AWS documentation access and smart tool orchestration, making
    it highly valuable for real-world infrastructure development.
  tags_suggested:
  - aws
  - cdk
  - infrastructure
  - iac
  - cloudformation
  - typescript
  - python
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:36.883499Z'
indexed_at: '2026-01-19T01:30:36.883504Z'
---
