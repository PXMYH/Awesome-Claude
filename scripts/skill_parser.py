#!/usr/bin/env python3
"""
Shared skill parsing and repo probing utilities.

Used by both github_discover.py and manual_discover.py
"""

import re
import time
from datetime import datetime, timezone

import requests
from slugify import slugify

from config import GITHUB_API_BASE, GITHUB_TOKEN

# Category mapping based on repo characteristics
CATEGORY_KEYWORDS = {
    "scientific": "scientific",
    "security": "security",
    "trailofbits": "security",
    "data": "data-analytics",
    "analytics": "data-analytics",
    "test": "quality-security",
    "debug": "quality-security",
    "infrastructure": "infrastructure",
    "aws": "infrastructure",
    "devops": "infrastructure",
    "document": "documentation",
    "writing": "documentation",
    "official": "official",
    "anthropics": "official",
    "seo": "marketing",
    "marketing": "marketing",
    "influencer": "marketing",
    "legal": "legal",
    "law": "legal",
}


def get_headers():
    """Get headers for GitHub API requests."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers


def check_rate_limit():
    """Check GitHub API rate limit status."""
    url = f"{GITHUB_API_BASE}/rate_limit"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        data = response.json()
        core = data["resources"]["core"]
        search = data["resources"]["search"]
        return {
            "core_remaining": core["remaining"],
            "core_limit": core["limit"],
            "search_remaining": search["remaining"],
            "search_limit": search["limit"],
        }
    return {"core_remaining": 0, "core_limit": 0, "search_remaining": 0, "search_limit": 0}


def wait_for_rate_limit():
    """Wait if rate limited. Returns True if waited."""
    limits = check_rate_limit()
    if limits["core_remaining"] < 10:
        print(f"\n⚠️  Rate limit low: {limits['core_remaining']}/{limits['core_limit']}")
        print("   Waiting 60 seconds...")
        time.sleep(60)
        return True
    return False


def fetch_repo_contents(owner: str, repo: str, path: str = "", branch: str = "main") -> list | None:
    """Fetch contents of a directory from GitHub."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None


def fetch_file_content(owner: str, repo: str, path: str, branch: str = "main") -> str | None:
    """Fetch raw content of a file from GitHub."""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_default_branch(owner: str, repo: str) -> str:
    """Get the default branch for a repo."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json().get("default_branch", "main")
    return "main"


def get_repo_info(owner: str, repo: str) -> dict | None:
    """Get repo info including stars."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        data = response.json()
        return {
            "full_name": data["full_name"],
            "owner": data["owner"]["login"],
            "repo": data["name"],
            "stars": data["stargazers_count"],
            "description": data.get("description", ""),
            "default_branch": data.get("default_branch", "main"),
            "topics": data.get("topics", []),
        }
    return None


def sanitize_category(name: str) -> tuple[str, str]:
    """
    Sanitize category name.
    Returns (slug, display_name) tuple.
    """
    clean_name = re.sub(r"^\d+[-_\s]*", "", name)
    slug = slugify(clean_name)
    display = clean_name.replace("-", " ").replace("_", " ").title()
    return slug, display


def guess_category(owner: str, repo: str, topics: list = None) -> str:
    """Guess category based on repo name/owner/topics."""
    combined = f"{owner}/{repo}".lower()

    if topics:
        for topic in topics:
            topic_lower = topic.lower()
            for keyword, category in CATEGORY_KEYWORDS.items():
                if keyword in topic_lower:
                    return category

    for keyword, category in CATEGORY_KEYWORDS.items():
        if keyword in combined:
            return category

    return "community"


def detect_skill_format(owner: str, repo: str, branch: str = None, topics: list = None, stars: int = 0) -> dict | None:
    """
    Detect what format of skills a repo contains.
    Returns a config dict if skills found, None otherwise.
    """
    if branch is None:
        branch = get_default_branch(owner, repo)

    contents = fetch_repo_contents(owner, repo, "", branch)
    if not contents:
        return None

    dir_names = {item["name"]: item for item in contents if item["type"] == "dir"}
    file_names = {item["name"].upper(): item for item in contents if item["type"] == "file"}

    # Check for SKILL.md at root
    if "SKILL.MD" in file_names:
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "",
            "format": "root_skill",
            "default_category": guess_category(owner, repo, topics),
            "stars": stars,
        }

    # Check for skills/ directory
    if "skills" in dir_names:
        skills_contents = fetch_repo_contents(owner, repo, "skills", branch)
        if skills_contents:
            for item in skills_contents[:5]:
                if item["type"] == "dir":
                    subfolder = fetch_repo_contents(owner, repo, f"skills/{item['name']}", branch)
                    if subfolder:
                        for f in subfolder:
                            if f["name"].upper() == "SKILL.MD":
                                return {
                                    "owner": owner,
                                    "repo": repo,
                                    "branch": branch,
                                    "path": "skills",
                                    "format": "skill_folders",
                                    "default_category": guess_category(owner, repo, topics),
                                    "stars": stars,
                                }
            for item in skills_contents:
                if item["name"].endswith(".md") and item["name"].lower() != "readme.md":
                    return {
                        "owner": owner,
                        "repo": repo,
                        "branch": branch,
                        "path": "skills",
                        "format": "flat_md",
                        "default_category": guess_category(owner, repo, topics),
                        "stars": stars,
                    }

    # Check for scientific-skills/ directory
    if "scientific-skills" in dir_names:
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "scientific-skills",
            "format": "skill_folders",
            "default_category": "scientific",
            "stars": stars,
        }

    # Check for categories/ directory
    if "categories" in dir_names:
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "categories",
            "format": "categories",
            "default_category": guess_category(owner, repo, topics),
            "stars": stars,
        }

    # Check for plugins/ directory
    if "plugins" in dir_names:
        plugins_contents = fetch_repo_contents(owner, repo, "plugins", branch)
        if plugins_contents:
            for item in plugins_contents[:3]:
                if item["type"] == "dir":
                    subfolder = fetch_repo_contents(owner, repo, f"plugins/{item['name']}/skills", branch)
                    if subfolder:
                        return {
                            "owner": owner,
                            "repo": repo,
                            "branch": branch,
                            "path": "plugins",
                            "format": "plugins_with_skills",
                            "default_category": guess_category(owner, repo, topics),
                            "stars": stars,
                        }

    # Check for skill folders at root level (e.g., ComposioHQ format)
    # Look for directories with SKILL.md inside them at root
    skill_folders_at_root = []
    for name, item in list(dir_names.items())[:10]:  # Check first 10 dirs
        if name.startswith(".") or name.lower() in ("docs", "examples", "tests", "scripts", "assets", "images"):
            continue
        subfolder = fetch_repo_contents(owner, repo, name, branch)
        if subfolder:
            for f in subfolder:
                if f["name"].upper() == "SKILL.MD":
                    skill_folders_at_root.append(name)
                    break
        if len(skill_folders_at_root) >= 2:  # Found at least 2 skill folders
            break

    if len(skill_folders_at_root) >= 2:
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "",
            "format": "root_skill_folders",
            "default_category": guess_category(owner, repo, topics),
            "stars": stars,
        }

    return None


def parse_skill_markdown(content: str, filename: str) -> dict:
    """Parse a skill markdown file and extract metadata."""
    name = filename.replace(".md", "").replace("-", " ").title()

    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        name = title_match.group(1).strip()

    desc_match = re.search(r"^#\s+.+\n\n(.+?)(?:\n\n|$)", content, re.MULTILINE | re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else f"Claude skill for {name}"
    description = description[:200] + "..." if len(description) > 200 else description

    tools = []
    tool_patterns = [
        r"\b(Python|JavaScript|TypeScript|Go|Rust|Java|Ruby|PHP)\b",
        r"\b(REST|GraphQL|gRPC|WebSocket)\b",
        r"\b(Docker|Kubernetes|AWS|GCP|Azure)\b",
        r"\b(React|Vue|Angular|Node\.js|Django|Flask|FastAPI)\b",
        r"\b(PostgreSQL|MySQL|MongoDB|Redis|SQLite)\b",
    ]
    for pattern in tool_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        tools.extend(matches)
    tools = list(set(tools))[:10]

    prompt_preview = content[:500].strip()
    if len(content) > 500:
        prompt_preview += "..."

    return {
        "name": name,
        "description": description,
        "prompt_preview": prompt_preview,
        "full_prompt_length": len(content),
        "tools_mentioned": tools,
        "raw_content": content,
    }


def fetch_skills_from_config(config: dict) -> list:
    """Fetch skills based on detected config."""
    owner = config["owner"]
    repo = config["repo"]
    branch = config.get("branch", "main")
    path = config["path"]
    format_type = config["format"]
    default_category = config.get("default_category", "community")
    repo_stars = config.get("stars", 0)

    skills = []

    def make_skill(skill_data: dict, skill_id: str, category: str, source_path: str) -> dict:
        category_slug, category_display = sanitize_category(category)
        return {
            "id": skill_id,
            "slug": skill_id,
            **skill_data,
            "category": category_slug,
            "category_display": category_display,
            "source_repo": f"{owner}/{repo}",
            "source_path": source_path,
            "source_url": f"https://github.com/{owner}/{repo}/blob/{branch}/{source_path}",
            "repo_stars": repo_stars,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }

    if format_type == "root_skill":
        content = fetch_file_content(owner, repo, "SKILL.md", branch)
        if content:
            skill_data = parse_skill_markdown(content, f"{repo}.md")
            skills.append(make_skill(skill_data, slugify(repo), default_category, "SKILL.md"))

    elif format_type == "skill_folders":
        contents = fetch_repo_contents(owner, repo, path, branch)
        if contents:
            for item in contents:
                if item["type"] != "dir":
                    continue
                folder_name = item["name"]
                for skill_filename in ["SKILL.md", "skill.md", "Skill.md"]:
                    try_path = f"{path}/{folder_name}/{skill_filename}"
                    content = fetch_file_content(owner, repo, try_path, branch)
                    if content:
                        skill_data = parse_skill_markdown(content, f"{folder_name}.md")
                        skills.append(make_skill(skill_data, slugify(folder_name), default_category, try_path))
                        break
                time.sleep(0.05)

    elif format_type == "flat_md":
        contents = fetch_repo_contents(owner, repo, path, branch)
        if contents:
            for item in contents:
                if not item["name"].endswith(".md") or item["name"].lower() == "readme.md":
                    continue
                file_path = f"{path}/{item['name']}"
                content = fetch_file_content(owner, repo, file_path, branch)
                if content:
                    skill_data = parse_skill_markdown(content, item["name"])
                    skills.append(make_skill(skill_data, slugify(item["name"].replace(".md", "")), default_category, file_path))
                time.sleep(0.05)

    elif format_type == "categories":
        contents = fetch_repo_contents(owner, repo, path, branch)
        if contents:
            for category_item in contents:
                if category_item["type"] != "dir":
                    continue
                category_name = category_item["name"]
                category_contents = fetch_repo_contents(owner, repo, f"{path}/{category_name}", branch)
                if not category_contents:
                    continue
                for skill_file in category_contents:
                    if not skill_file["name"].endswith(".md") or skill_file["name"].lower() == "readme.md":
                        continue
                    file_path = f"{path}/{category_name}/{skill_file['name']}"
                    content = fetch_file_content(owner, repo, file_path, branch)
                    if content:
                        skill_data = parse_skill_markdown(content, skill_file["name"])
                        skills.append(make_skill(skill_data, slugify(skill_file["name"].replace(".md", "")), category_name, file_path))
                    time.sleep(0.05)

    elif format_type == "plugins_with_skills":
        plugins = fetch_repo_contents(owner, repo, path, branch)
        if plugins:
            for plugin in plugins:
                if plugin["type"] != "dir":
                    continue
                skills_path = f"{path}/{plugin['name']}/skills"
                skill_folders = fetch_repo_contents(owner, repo, skills_path, branch)
                if not skill_folders:
                    continue
                for folder in skill_folders:
                    if folder["type"] != "dir":
                        continue
                    skill_path = f"{skills_path}/{folder['name']}/SKILL.md"
                    content = fetch_file_content(owner, repo, skill_path, branch)
                    if content:
                        skill_data = parse_skill_markdown(content, f"{folder['name']}.md")
                        skills.append(make_skill(skill_data, slugify(f"{plugin['name']}-{folder['name']}"), default_category, skill_path))
                    time.sleep(0.05)

    elif format_type == "root_skill_folders":
        # Skill folders at root level (e.g., ComposioHQ format)
        contents = fetch_repo_contents(owner, repo, "", branch)
        if contents:
            skip_dirs = {".github", ".git", "docs", "examples", "tests", "scripts", "assets", "images", ".claude-plugin"}
            for item in contents:
                if item["type"] != "dir":
                    continue
                folder_name = item["name"]
                if folder_name.startswith(".") or folder_name.lower() in skip_dirs:
                    continue
                for skill_filename in ["SKILL.md", "skill.md", "Skill.md"]:
                    try_path = f"{folder_name}/{skill_filename}"
                    content = fetch_file_content(owner, repo, try_path, branch)
                    if content:
                        skill_data = parse_skill_markdown(content, f"{folder_name}.md")
                        skills.append(make_skill(skill_data, slugify(folder_name), default_category, try_path))
                        break
                time.sleep(0.05)

    return skills


def deduplicate_skills(skills: list, prefer_higher_stars: bool = True) -> list:
    """Deduplicate skills by ID, optionally preferring higher-star repos."""
    skills_by_id = {}
    for skill in skills:
        skill_id = skill["id"]
        if skill_id not in skills_by_id:
            skills_by_id[skill_id] = skill
        elif prefer_higher_stars and skill.get("repo_stars", 0) > skills_by_id[skill_id].get("repo_stars", 0):
            skills_by_id[skill_id] = skill
    return list(skills_by_id.values())
