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

# Fetch and evaluate skills (requires API keys)
export GITHUB_TOKEN=your_token
export OPENROUTER_API_KEY=your_key
uv run python scripts/fetch_skills.py
uv run python scripts/evaluate_skills.py
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
│   ├── fetch_skills.py
│   ├── evaluate_skills.py
│   └── generate_site_data.py
├── tests/               # Unit tests
└── .github/workflows/   # CI/CD
```

## Data Sources

Currently indexing from:
- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) - 100+ specialized subagents
- [anthropics/skills](https://github.com/anthropics/skills) - Official Anthropic skills (pdf, docx, xlsx, etc.)
- [obra/superpowers](https://github.com/obra/superpowers) - Community skills library (TDD, debugging, planning)

## Evaluation Criteria

Skills are evaluated on two dimensions (1-5 scale):

1. **Prompt Quality**: Clarity, specificity, edge case handling, best practices
2. **Usefulness**: Real-world value, completeness, actionability

GitHub metrics (stars, forks, issues) are displayed separately.

## Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| `GITHUB_TOKEN` | GitHub API access (auto-provided in Actions) |
| `OPENROUTER_API_KEY` | LLM evaluation via OpenRouter |

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

1. **Add a skill source**: Submit a PR adding a new repo to `SOURCE_REPOS`
2. **Improve evaluation**: Enhance the LLM prompt in `evaluate_skills.py`
3. **UI improvements**: Modify layouts in `_layouts/` and CSS in `assets/css/`

## License

MIT

## Acknowledgments

- [awesome-claude](https://github.com/tonysurfly/awesome-claude) - Original awesome list aggregation
- [VoltAgent](https://github.com/VoltAgent) - Subagents collection
- [anthropics/skills](https://github.com/anthropics/skills) - Official Anthropic skills
- [obra/superpowers](https://github.com/obra/superpowers) - Community skills library
- [OpenRouter](https://openrouter.ai) - LLM API access
