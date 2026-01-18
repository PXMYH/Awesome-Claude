# Claude Skills Directory

[![Deploy to GitHub Pages](https://github.com/PXMYH/Awesome-Claude/actions/workflows/deploy.yml/badge.svg)](https://github.com/PXMYH/Awesome-Claude/actions/workflows/deploy.yml)
[![Update Skills Data](https://github.com/PXMYH/Awesome-Claude/actions/workflows/update-data.yml/badge.svg)](https://github.com/PXMYH/Awesome-Claude/actions/workflows/update-data.yml)

A curated directory that aggregates, evaluates, and ranks Claude skills, agents, and subagents using LLM-as-judge evaluation.

## Features

- **Skill Aggregation**: Automatically fetches skills from community awesome lists
- **LLM Evaluation**: Each skill is evaluated by Claude for prompt quality and usefulness
- **GitHub Metrics**: Shows stars, forks, and last commit date
- **Search & Filter**: Find skills by category, rating, or keyword
- **Daily Updates**: GitHub Actions keeps data fresh

## Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/PXMYH/Awesome-Claude.git
cd Awesome-Claude

# Install Python dependencies with uv
uv sync

# Run tests
uv run pytest tests/ -v

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys (see Configuration section below)

# Discovery (two channels)
uv run python scripts/github_discover.py   # GitHub search (100+ stars, weekly)
uv run python scripts/manual_discover.py   # Curated sources.yaml

# Or use legacy single-script discovery
uv run python scripts/discover_skills.py   # Find skill repos

# Fetch and process
uv run python scripts/fetch_skills.py      # Fetch skills from repos
uv run python scripts/fetch_github_metrics.py
uv run python scripts/evaluate_skills.py   # LLM evaluation (requires OPENROUTER_API_KEY)
uv run python scripts/generate_site_data.py

# Build Jekyll site (requires Ruby)
bundle install
bundle exec jekyll serve
```

## Project Structure

```
├── _config.yml          # Jekyll configuration
├── _data/               # Skill data (YAML)
├── _skills/             # Jekyll collection
├── _layouts/            # Page templates
├── _includes/           # Reusable components
├── assets/              # CSS, JS
├── scripts/             # Python data pipeline
│   ├── github_discover.py    # GitHub search discovery (100+ stars)
│   ├── manual_discover.py    # Curated sources discovery
│   ├── skill_parser.py       # Shared parsing module
│   ├── sources.yaml          # Curated skill repo list
│   ├── fetch_skills.py       # Fetch skills from repos
│   ├── fetch_github_metrics.py
│   ├── evaluate_skills.py    # LLM evaluation
│   └── generate_site_data.py
├── tests/               # Unit tests
├── .env.example         # Environment variable template
└── .github/workflows/   # CI/CD
```

## Skill Discovery

### Two Discovery Channels

1. **GitHub Search** (`github_discover.py`)
   - Searches GitHub for "awesome claude skills" repos
   - Filters by 100+ stars for quality
   - Run weekly to discover new repos
   - Found 428 unique skills from 47 repos

2. **Manual Curation** (`manual_discover.py`)
   - Reads from `scripts/sources.yaml`
   - Easy to contribute via PR
   - Found 135 unique skills from 7 repos

### Supported Skill Formats

| Format | Structure | Example |
|--------|-----------|---------|
| `skill_folders` | `skills/<name>/SKILL.md` | anthropics/skills |
| `root_skill_folders` | `<name>/SKILL.md` at root | ComposioHQ/awesome-claude-skills |
| `flat_md` | `skills/*.md` files | obra/superpowers-skills |
| `categories` | `categories/<cat>/*.md` | VoltAgent/awesome-claude-skills |
| `plugins_with_skills` | `plugins/<p>/skills/<s>/SKILL.md` | trailofbits/skills |

## Data Sources

Currently indexing from:
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) - 21k+ stars
- [anthropics/skills](https://github.com/anthropics/skills) - Official Anthropic skills
- [trailofbits/skills](https://github.com/trailofbits/skills) - Security-focused skills
- [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) - 98 skills
- And 40+ more repos discovered via GitHub search

## Evaluation Criteria

Skills are evaluated on two dimensions (1-5 scale):

1. **Prompt Quality**: Clarity, specificity, edge case handling, best practices
2. **Usefulness**: Real-world value, completeness, actionability

GitHub metrics (stars, forks, issues) are displayed separately.

## Configuration

### Environment Variables

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
```

| Variable | Description | Required |
|----------|-------------|----------|
| `GITHUB_TOKEN` | GitHub API access for higher rate limits (5000/hr vs 60/hr). [Create token](https://github.com/settings/tokens) | Recommended |
| `OPENROUTER_API_KEY` | LLM evaluation via [OpenRouter](https://openrouter.ai/keys) | For evaluation |

In GitHub Actions, these are configured as repository secrets.

### Adding New Skill Sources

Edit `scripts/config.py` to add new repositories. Two repo formats are supported:

#### Format 1: Category-based (`categories`)

For repos with structure: `categories/<category-folder>/<skill>.md`

```python
{
    "owner": "VoltAgent",
    "repo": "awesome-claude-code-subagents",
    "branch": "main",
    "path": "categories",
    "format": "categories",
    "enabled": True
}
```

#### Format 2: Skill folders (`skill_folders`)

For repos with structure: `skills/<skill-folder>/SKILL.md`

```python
{
    "owner": "anthropics",
    "repo": "skills",
    "branch": "main",
    "path": "skills",
    "format": "skill_folders",
    "default_category": "official",  # Category slug for all skills in this repo
    "enabled": True
}
```

#### Configuration Options

| Field | Required | Description |
|-------|----------|-------------|
| `owner` | Yes | GitHub username or organization |
| `repo` | Yes | Repository name |
| `branch` | Yes | Branch to fetch from (usually `main`) |
| `path` | Yes | Path to skills directory in repo |
| `format` | Yes | `categories` or `skill_folders` |
| `default_category` | No | Category slug for skill_folders format |
| `enabled` | No | Set `False` to skip this repo |

#### Adding New Categories

If using a new `default_category`, add it to `CATEGORY_MAP` in `config.py`:

```python
CATEGORY_MAP = {
    # ... existing categories ...
    "my-category": {"slug": "my-category", "name": "My Category"},
}
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
