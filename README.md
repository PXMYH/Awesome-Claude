# Claude Skills Directory

[![Deploy to GitHub Pages](https://github.com/atlantis/Awesome-Claude/actions/workflows/deploy.yml/badge.svg)](https://github.com/atlantis/Awesome-Claude/actions/workflows/deploy.yml)
[![Tests](https://github.com/atlantis/Awesome-Claude/actions/workflows/update-data.yml/badge.svg)](https://github.com/atlantis/Awesome-Claude/actions/workflows/update-data.yml)

A curated directory that aggregates, evaluates, and ranks Claude skills, agents, and subagents using LLM-as-judge evaluation.

## Features

- **Skill Aggregation**: Automatically fetches skills from community awesome lists
- **LLM Evaluation**: Each skill is evaluated by Claude for prompt quality and usefulness
- **GitHub Metrics**: Shows stars, forks, and last commit date
- **Search & Filter**: Find skills by category, rating, or keyword
- **Daily Updates**: GitHub Actions keeps data fresh

## Quick Start

### View the Directory

Visit [https://atlantis.github.io/Awesome-Claude](https://atlantis.github.io/Awesome-Claude)

### Local Development

```bash
# Clone the repository
git clone https://github.com/atlantis/Awesome-Claude.git
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

### Adding New Sources

Edit `scripts/config.py` to add new repositories:

```python
SOURCE_REPOS = [
    {
        "owner": "VoltAgent",
        "repo": "awesome-claude-code-subagents",
        "branch": "main",
        "categories_path": "categories",
        "enabled": True
    },
    # Add more repos here
]
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
- [OpenRouter](https://openrouter.ai) - LLM API access
