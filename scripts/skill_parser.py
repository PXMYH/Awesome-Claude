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


def find_skill_files_recursive(owner: str, repo: str, branch: str, path: str = "", depth: int = 0, max_depth: int = 3) -> list:
    """
    Recursively search for SKILL.md files up to max_depth levels.
    Returns list of paths where SKILL.md files were found.
    """
    if depth > max_depth:
        return []

    contents = fetch_repo_contents(owner, repo, path, branch)
    if not contents:
        return []

    found_paths = []
    skip_dirs = {".github", ".git", "docs", "examples", "tests", "test", "scripts", "assets", "images",
                 ".claude-plugin", "node_modules", "__pycache__", "venv", ".venv", "dist", "build"}

    # Check for SKILL.md in current directory
    for item in contents:
        if item["type"] == "file" and item["name"].upper() == "SKILL.MD":
            found_paths.append(path if path else ".")
            break

    # Recurse into subdirectories
    if depth < max_depth:
        for item in contents:
            if item["type"] != "dir":
                continue
            dir_name = item["name"]
            if dir_name.startswith(".") or dir_name.lower() in skip_dirs:
                continue
            subpath = f"{path}/{dir_name}" if path else dir_name
            found_paths.extend(find_skill_files_recursive(owner, repo, branch, subpath, depth + 1, max_depth))
            time.sleep(0.02)  # Rate limit protection

    return found_paths


def detect_skill_format(owner: str, repo: str, branch: str = None, topics: list = None, stars: int = 0) -> dict | None:
    """
    Detect what format of skills a repo contains.
    Returns a config dict if skills found, None otherwise.

    Uses recursive search for SKILL.md files up to 3 levels deep,
    then analyzes the paths to determine the format.
    """
    if branch is None:
        branch = get_default_branch(owner, repo)

    contents = fetch_repo_contents(owner, repo, "", branch)
    if not contents:
        return None

    dir_names = {item["name"]: item for item in contents if item["type"] == "dir"}
    file_names = {item["name"].upper(): item for item in contents if item["type"] == "file"}

    # Check for SKILL.md at root first (most common case)
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

    # Check for categories/ directory (special format)
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

    # Check for plugins/ directory (special format)
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

    # Recursive search for SKILL.md files up to 3 levels deep
    skill_paths = find_skill_files_recursive(owner, repo, branch, "", 0, 3)

    if not skill_paths:
        # Fallback: check for flat .md files in skills/ directory
        if "skills" in dir_names:
            skills_contents = fetch_repo_contents(owner, repo, "skills", branch)
            if skills_contents:
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
        return None

    # Analyze paths to determine format
    # Extract the common parent directory pattern
    if len(skill_paths) == 1 and skill_paths[0] == ".":
        # Single SKILL.md at root (already handled above, but just in case)
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "",
            "format": "root_skill",
            "default_category": guess_category(owner, repo, topics),
            "stars": stars,
        }

    # Check if all skills are under a common parent directory
    common_parents = set()
    for p in skill_paths:
        parts = p.split("/")
        if len(parts) >= 1 and parts[0] != ".":
            common_parents.add(parts[0])

    # Single skill in a subdirectory (e.g., linear/SKILL.md or ios-simulator-skill/SKILL.md)
    if len(skill_paths) == 1:
        skill_path = skill_paths[0]
        parts = skill_path.split("/")
        if len(parts) == 1:
            # Skill is one level deep (e.g., "linear" or "ios-simulator-skill")
            return {
                "owner": owner,
                "repo": repo,
                "branch": branch,
                "path": skill_path,
                "format": "single_subfolder",
                "default_category": guess_category(owner, repo, topics),
                "stars": stars,
            }
        else:
            # Skill is deeper (e.g., "skills/my-skill")
            parent = "/".join(parts[:-1])
            return {
                "owner": owner,
                "repo": repo,
                "branch": branch,
                "path": parent,
                "format": "skill_folders",
                "default_category": guess_category(owner, repo, topics),
                "stars": stars,
            }

    # Multiple skills found
    if len(common_parents) == 1:
        # All skills under one directory (e.g., skills/, scientific-skills/)
        parent = list(common_parents)[0]
        category = "scientific" if "scientific" in parent.lower() else guess_category(owner, repo, topics)
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": parent,
            "format": "skill_folders",
            "default_category": category,
            "stars": stars,
        }
    else:
        # Skills in multiple root-level directories (ComposioHQ format)
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "",
            "format": "root_skill_folders",
            "default_category": guess_category(owner, repo, topics),
            "stars": stars,
        }


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

    elif format_type == "single_subfolder":
        # Single skill in a subdirectory (e.g., linear/SKILL.md)
        for skill_filename in ["SKILL.md", "skill.md", "Skill.md"]:
            try_path = f"{path}/{skill_filename}"
            content = fetch_file_content(owner, repo, try_path, branch)
            if content:
                # Use folder name for skill ID, but could also use repo name
                folder_name = path.split("/")[-1] if "/" in path else path
                skill_data = parse_skill_markdown(content, f"{folder_name}.md")
                skills.append(make_skill(skill_data, slugify(folder_name), default_category, try_path))
                break

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
