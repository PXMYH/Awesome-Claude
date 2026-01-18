"""Configuration for Claude Skills Directory scripts."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env file from project root
load_dotenv(Path(__file__).parent.parent / ".env")

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
DATA_DIR = SCRIPTS_DIR / "data"
CACHE_DIR = DATA_DIR / "cache"
OUTPUT_DATA_DIR = PROJECT_ROOT / "_data"
OUTPUT_SKILLS_DIR = PROJECT_ROOT / "_skills"
ASSETS_JS_DIR = PROJECT_ROOT / "assets" / "js"

# Create directories
DATA_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)

# Source repositories
# format: "categories" = category folders with .md files inside (VoltAgent style)
#         "skill_folders" = flat skill folders with SKILL.md inside (Anthropic style)
SOURCE_REPOS = [
    {
        "owner": "VoltAgent",
        "repo": "awesome-claude-code-subagents",
        "branch": "main",
        "path": "categories",
        "format": "categories",
        "enabled": True
    },
    {
        "owner": "anthropics",
        "repo": "skills",
        "branch": "main",
        "path": "skills",
        "format": "skill_folders",
        "default_category": "official",
        "enabled": True
    },
    {
        "owner": "obra",
        "repo": "superpowers",
        "branch": "main",
        "path": "skills",
        "format": "skill_folders",
        "default_category": "community",
        "enabled": True
    }
]

# API Configuration
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "xiaomi/mimo-v2-flash:free"
GITHUB_API_BASE = "https://api.github.com"

# API Keys (from environment)
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Rate Limits
OPENROUTER_RPM = 10  # requests per minute
GITHUB_RPM = 30

# Evaluation Settings
SKIP_CACHED_EVALUATIONS = True
EVALUATION_CACHE_DAYS = 7  # Re-evaluate after 7 days

# Category mappings from folder names to display names
CATEGORY_MAP = {
    # VoltAgent categories
    "01-core-development": {"slug": "core-development", "name": "Core Development"},
    "02-language-specialists": {"slug": "language-specialists", "name": "Language Specialists"},
    "03-infrastructure": {"slug": "infrastructure", "name": "Infrastructure"},
    "04-quality-security": {"slug": "quality-security", "name": "Quality & Security"},
    "05-data-analytics": {"slug": "data-analytics", "name": "Data & Analytics"},
    "06-documentation": {"slug": "documentation", "name": "Documentation"},
    # Default categories for flat skill repos
    "official": {"slug": "official", "name": "Official Anthropic Skills"},
    "community": {"slug": "community", "name": "Community Skills"},
}
