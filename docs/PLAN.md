# Claude Skills Directory - Implementation Plan

## Overview
A GitHub Pages website that aggregates, evaluates, and ranks Claude skills/agents using LLM-as-judge evaluation via OpenRouter.

**MVP Scope**: VoltAgent/awesome-claude-code-subagents (100+ subagents)
**Tech Stack**: Jekyll + GitHub Actions + Python scripts
**Evaluation**: LLM judge (Prompt Quality, Usefulness) + GitHub metrics (separate)

---

## Directory Structure

```
Awesome-Claude/
├── _config.yml                 # Jekyll configuration
├── _data/
│   ├── skills/                 # Individual skill YAML files
│   │   ├── api-designer.yml
│   │   └── ...
│   ├── categories.yml          # Category definitions
│   └── site_meta.yml           # Last updated, totals
├── _includes/
│   ├── skill-card.html         # Reusable skill card component
│   ├── rating-badge.html       # Star rating display
│   └── github-metrics.html     # Stars/forks/commit display
├── _layouts/
│   ├── default.html
│   ├── home.html
│   ├── category.html
│   └── skill.html              # Individual skill detail page
├── _sass/
│   └── main.scss
├── _skills/                    # Jekyll collection (auto-generated)
│   ├── api-designer.md
│   └── ...
├── assets/
│   ├── css/main.scss
│   └── js/
│       ├── search.js
│       └── search-index.json   # Generated search index
├── categories/                 # Category landing pages
│   ├── core-development.md
│   ├── language-specialists.md
│   └── ...
├── scripts/
│   ├── fetch_skills.py         # Fetch from VoltAgent repo
│   ├── fetch_github_metrics.py # Get stars/forks/commits
│   ├── evaluate_skills.py      # LLM evaluation via OpenRouter
│   ├── generate_site_data.py   # Create Jekyll data files
│   ├── config.py               # Centralized config
│   └── requirements.txt
├── .github/
│   └── workflows/
│       └── update-data.yml     # Daily automation
├── index.md                    # Homepage
├── Gemfile
└── README.md
```

---

## Data Schema

### Skill YAML (`_data/skills/api-designer.yml`)

```yaml
# Identity
id: "api-designer"
name: "API Designer"
slug: "api-designer"
description: "REST and GraphQL API architect"
category: "core-development"
category_display: "Core Development"

# Source
source_repo: "VoltAgent/awesome-claude-code-subagents"
source_path: "categories/01-core-development/api-designer.md"
source_url: "https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/api-designer.md"

# Content
prompt_preview: "First 500 chars of the skill prompt..."
full_prompt_length: 2340
tools_mentioned: ["REST", "GraphQL", "OpenAPI"]

# LLM Evaluation (separate from GitHub metrics)
evaluation:
  model: "anthropic/claude-3.5-sonnet"
  evaluated_at: "2025-01-17T10:30:00Z"
  prompt_quality:
    score: 4.2           # 1-5 scale
    reasoning: "Clear instructions with good examples..."
  usefulness:
    score: 4.5
    reasoning: "Highly practical for API design tasks..."
  overall_rating: 4.35   # Average of dimensions
  summary: "Well-crafted agent for API design with clear scope..."

# GitHub Metrics (objective, shown separately)
github_metrics:
  stars: 1250
  forks: 180
  last_commit: "2025-01-15"
  open_issues: 12
  fetched_at: "2025-01-17T02:00:00Z"

# Metadata
indexed_at: "2025-01-17T10:30:00Z"
```

---

## LLM Evaluation Prompt

```markdown
You are an expert evaluator of AI agent/skill prompts. Evaluate the following Claude skill/agent prompt.

**Skill Name:** {skill_name}
**Category:** {category}

**Prompt Content:**
```
{skill_content}
```

Evaluate on these dimensions (1-5 scale, with 0.5 increments):

## 1. Prompt Quality
- Clarity: Are instructions clear and unambiguous?
- Specificity: Does it define scope, constraints, and expected behavior?
- Edge Cases: Does it handle edge cases or provide fallback guidance?
- Best Practices: Does it follow prompt engineering best practices?

## 2. Usefulness/Practicality
- Real-world Value: Would this help with actual development tasks?
- Completeness: Does it cover the task comprehensively?
- Actionability: Can a user immediately benefit from this skill?

Respond in this exact JSON format:
{
  "prompt_quality": {
    "score": <number 1.0-5.0>,
    "reasoning": "<2-3 sentences explaining the score>"
  },
  "usefulness": {
    "score": <number 1.0-5.0>,
    "reasoning": "<2-3 sentences explaining the score>"
  },
  "summary": "<1-2 sentence overall assessment>",
  "tags_suggested": ["<tag1>", "<tag2>", "<tag3>"]
}
```

---

## Scripts

### 1. `fetch_skills.py`
- Clone/fetch VoltAgent repo via GitHub API
- Parse category folders, extract skill markdown files
- Extract frontmatter and content
- Save raw skills to `scripts/data/raw_skills.json`

### 2. `fetch_github_metrics.py`
- Call GitHub API for repo stats (VoltAgent repo)
- Get stars, forks, last commit, open issues
- Save to `scripts/data/github_metrics.json`

### 3. `evaluate_skills.py`
- Load raw skills
- For each skill, call OpenRouter API with evaluation prompt
- Parse JSON response, validate scores
- Cache results (skip if evaluated within 7 days)
- Save to `scripts/data/evaluations.json`

### 4. `generate_site_data.py`
- Merge raw skills + evaluations + GitHub metrics
- Generate `_data/skills/*.yml` files
- Generate `_skills/*.md` collection pages
- Generate `_data/categories.yml`
- Generate `assets/js/search-index.json`

---

## GitHub Actions Workflow

```yaml
name: Update Skills Data

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC
  workflow_dispatch:
    inputs:
      force_reevaluate:
        description: 'Force re-evaluation of all skills'
        type: boolean
        default: false

jobs:
  update-data:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r scripts/requirements.txt

      - name: Fetch skills
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python scripts/fetch_skills.py

      - name: Fetch GitHub metrics
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python scripts/fetch_github_metrics.py

      - name: Evaluate with LLM
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
        run: python scripts/evaluate_skills.py

      - name: Generate site data
        run: python scripts/generate_site_data.py

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add _data/ _skills/ assets/js/search-index.json
          git diff --staged --quiet || git commit -m "chore: update skills data"
          git push
```

---

## MVP Features

| Feature | Description |
|---------|-------------|
| Homepage | Grid of skill cards with ratings |
| Category Pages | Filter by Core Dev, Language, Infra, etc. |
| Skill Detail Page | Full evaluation + prompt preview + source link |
| LLM Ratings | Prompt Quality + Usefulness scores (1-5) |
| GitHub Metrics | Stars, forks, last commit (separate section) |
| Search | Client-side search by name/description |
| Filtering | Filter by category, minimum rating |
| Daily Updates | GitHub Actions automation |

---

## Implementation Order

1. **Jekyll scaffold** - Basic site structure, layouts, config
2. **Sample data** - Create 3-5 manual skill YAML files to test layouts
3. **Layouts & templates** - Homepage, category, skill detail pages
4. **Styling** - Clean, minimal CSS
5. **fetch_skills.py** - Data ingestion from VoltAgent
6. **evaluate_skills.py** - OpenRouter LLM evaluation
7. **generate_site_data.py** - Generate Jekyll data files
8. **GitHub Actions** - Automate the pipeline
9. **Search** - Client-side search functionality
10. **Polish** - Responsive design, edge cases

---

## Secrets Required

| Secret | Purpose |
|--------|---------|
| `OPENROUTER_API_KEY` | LLM evaluation API access |
| `GITHUB_TOKEN` | Auto-provided, for GitHub API and pushing |

---

## Estimated Costs

- **OpenRouter**: ~$1-2 per full evaluation run (100 skills × ~3K tokens × $0.003/1K)
- **GitHub Actions**: Free tier
- **GitHub Pages**: Free

---

## Files to Create (Implementation)

| Priority | File | Purpose |
|----------|------|---------|
| 1 | `_config.yml` | Jekyll config with collections |
| 2 | `Gemfile` | Ruby dependencies |
| 3 | `_layouts/default.html` | Base layout |
| 4 | `_layouts/home.html` | Homepage layout |
| 5 | `_layouts/skill.html` | Skill detail layout |
| 6 | `_includes/skill-card.html` | Card component |
| 7 | `index.md` | Homepage |
| 8 | `scripts/config.py` | Script configuration |
| 9 | `scripts/fetch_skills.py` | Data fetching |
| 10 | `scripts/evaluate_skills.py` | LLM evaluation |
| 11 | `scripts/generate_site_data.py` | Data generation |
| 12 | `.github/workflows/update-data.yml` | Automation |
