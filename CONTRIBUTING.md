# Contributing

Thank you for your interest in contributing to the Claude Skills Directory!

## Ways to Contribute

### 1. Add a Skill Source

Submit a PR adding a new repo to `SOURCE_REPOS` in `scripts/config.py`:

```python
{
    "owner": "username",
    "repo": "repo-name",
    "branch": "main",
    "path": "skills",
    "format": "skill_folders",  # or "categories"
    "default_category": "community",
    "enabled": True
}
```

### 2. Improve Evaluation

Enhance the LLM evaluation prompt in `scripts/evaluate_skills.py` to better assess skill quality.

### 3. UI Improvements

- Modify layouts in `_layouts/`
- Update styles in `assets/css/`
- Improve components in `_includes/`

## Development Setup

```bash
# Clone and install
git clone https://github.com/PXMYH/Awesome-Claude.git
cd Awesome-Claude
uv sync

# Set up environment
cp .env.example .env
# Edit .env with your API keys

# Run tests
uv run pytest tests/ -v

# Run the data pipeline
uv run python scripts/discover_skills.py
uv run python scripts/fetch_skills.py
uv run python scripts/evaluate_skills.py
uv run python scripts/generate_site_data.py

# Build Jekyll site
bundle install
bundle exec jekyll serve
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure they pass
5. Submit a PR with a clear description
