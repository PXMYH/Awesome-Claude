#!/usr/bin/env python3
"""
Discover and fetch Claude skills from awesome-claude and related repos.

This script:
1. Fetches the awesome-claude README from GitHub
2. Extracts all GitHub repo links that might contain skills
3. Probes each repo to detect skill format
4. Fetches skills from all discovered repos
5. Outputs combined skills data
"""

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from slugify import slugify

from config import (
    DATA_DIR,
    GITHUB_API_BASE,
    GITHUB_TOKEN,
)

# Curated lists to parse for skill repo links
AWESOME_LISTS = [
    "tonysurfly/awesome-claude",
    "travisvn/awesome-claude-skills",
    "BehiSecc/awesome-claude-skills",
]

# Repos to skip (not skills, or duplicates)
SKIP_REPOS = {
    "anthropics/anthropic-sdk-python",
    "anthropics/anthropic-sdk-typescript",
    "anthropics/anthropic-sdk-java",
    "anthropics/anthropic-sdk-go",
    "anthropics/anthropic-sdk-php",
    "anthropics/anthropic-sdk-csharp",
    "anthropics/anthropic-sdk-ruby",
    "anthropics/claude-agent-sdk-python",
    "anthropics/claude-agent-sdk-typescript",
    "anthropics/claude-cookbooks",
    "anthropics/claude-quickstarts",
    "anthropics/courses",
    "punkpeye/awesome-mcp-servers",  # MCP servers, not skills
    "langgptai/awesome-claude-prompts",  # Prompts, not skills
    "hesreallyhim/awesome-claude-code",  # CLI tools, not skills
    "vijaythecoder/awesome-claude-agents",  # Agents list, not skill repo
    "tonysurfly/awesome-claude",  # Meta list
    "travisvn/awesome-claude-skills",  # Meta list
    "BehiSecc/awesome-claude-skills",  # Meta list
}

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
        return core["remaining"], core["limit"]
    return 0, 0


def wait_for_rate_limit():
    """Wait if rate limited."""
    remaining, limit = check_rate_limit()
    if remaining < 5:
        print(f"\n⚠️  Rate limit low: {remaining}/{limit} remaining")
        if not GITHUB_TOKEN:
            print("   Set GITHUB_TOKEN for higher limits (5000/hr vs 60/hr)")
        print("   Waiting 60 seconds...")
        time.sleep(60)
        return True
    return False


def fetch_readme(owner: str, repo: str) -> str | None:
    """Fetch README content from a GitHub repo."""
    # Try common README filenames
    for filename in ["README.md", "readme.md", "Readme.md"]:
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{filename}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        # Try master branch
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{filename}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    return None


def extract_github_repos(text: str) -> set[str]:
    """Extract GitHub repo references from text."""
    repos = set()

    # Match github.com URLs
    url_pattern = r'github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_.-]+)'
    for match in re.finditer(url_pattern, text):
        owner, repo = match.groups()
        # Clean repo name (remove .git, trailing slashes, anchors)
        repo = re.sub(r'(\.git|/.*|#.*)$', '', repo)
        if repo and not repo.startswith('.'):
            repos.add(f"{owner}/{repo}")

    return repos


def fetch_repo_contents(owner: str, repo: str, path: str = "", branch: str = "main") -> list | None:
    """Fetch contents of a directory from GitHub."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None


def get_default_branch(owner: str, repo: str) -> str:
    """Get the default branch for a repo."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json().get("default_branch", "main")
    return "main"


def detect_skill_format(owner: str, repo: str) -> dict | None:
    """
    Detect what format of skills a repo contains.

    Returns a config dict if skills found, None otherwise.
    """
    print(f"  Probing {owner}/{repo}...")

    # Get default branch
    branch = get_default_branch(owner, repo)

    # Get root contents
    contents = fetch_repo_contents(owner, repo, "", branch)
    if not contents:
        return None

    dir_names = {item["name"]: item for item in contents if item["type"] == "dir"}
    file_names = {item["name"].upper(): item for item in contents if item["type"] == "file"}

    # Check for SKILL.md at root (single skill repo)
    if "SKILL.MD" in file_names:
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "",
            "format": "root_skill",
            "default_category": guess_category(owner, repo),
        }

    # Check for skills/ directory
    if "skills" in dir_names:
        skills_contents = fetch_repo_contents(owner, repo, "skills", branch)
        if skills_contents:
            # Check if it's skill_folders format (folders with SKILL.md inside)
            for item in skills_contents[:3]:  # Check first few
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
                                    "default_category": guess_category(owner, repo),
                                }
            # Check if it has .md files directly
            for item in skills_contents:
                if item["name"].endswith(".md") and item["name"].lower() != "readme.md":
                    return {
                        "owner": owner,
                        "repo": repo,
                        "branch": branch,
                        "path": "skills",
                        "format": "flat_md",
                        "default_category": guess_category(owner, repo),
                    }

    # Check for scientific-skills/ directory (K-Dense-AI style)
    if "scientific-skills" in dir_names:
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "scientific-skills",
            "format": "skill_folders",
            "default_category": "scientific",
        }

    # Check for categories/ directory (VoltAgent style)
    if "categories" in dir_names:
        return {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "path": "categories",
            "format": "categories",
            "default_category": guess_category(owner, repo),
        }

    # Check for plugins/ directory (trailofbits style)
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
                            "default_category": guess_category(owner, repo),
                        }

    return None


def sanitize_category(name: str) -> tuple[str, str]:
    """
    Sanitize category name by removing leading numbers and formatting.

    Returns (slug, display_name) tuple.
    """
    # Remove leading numbers like "01-", "05-", "10-"
    clean_name = re.sub(r"^\d+[-_\s]*", "", name)

    # Create slug (lowercase, hyphenated)
    slug = slugify(clean_name)

    # Create display name (title case, spaces)
    display = clean_name.replace("-", " ").replace("_", " ").title()

    return slug, display


def guess_category(owner: str, repo: str) -> str:
    """Guess category based on repo name/owner."""
    combined = f"{owner}/{repo}".lower()

    for keyword, category in CATEGORY_KEYWORDS.items():
        if keyword in combined:
            return category

    return "community"


def fetch_file_content(owner: str, repo: str, path: str, branch: str = "main") -> str | None:
    """Fetch raw content of a file from GitHub."""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_skill_markdown(content: str, filename: str) -> dict:
    """Parse a skill markdown file and extract metadata."""
    name = filename.replace(".md", "").replace("-", " ").title()

    # Try to extract title from markdown
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        name = title_match.group(1).strip()

    # Extract description
    desc_match = re.search(r"^#\s+.+\n\n(.+?)(?:\n\n|$)", content, re.MULTILINE | re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else f"Claude skill for {name}"
    description = description[:200] + "..." if len(description) > 200 else description

    # Extract tools mentioned
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

    # Create prompt preview
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

    skills = []

    if format_type == "root_skill":
        # Single SKILL.md at root
        content = fetch_file_content(owner, repo, "SKILL.md", branch)
        if content:
            skill_data = parse_skill_markdown(content, f"{repo}.md")
            skill_id = slugify(repo)
            category_slug, category_display = sanitize_category(default_category)
            skills.append({
                "id": skill_id,
                "slug": skill_id,
                **skill_data,
                "category": category_slug,
                "category_display": category_display,
                "source_repo": f"{owner}/{repo}",
                "source_path": "SKILL.md",
                "source_url": f"https://github.com/{owner}/{repo}/blob/{branch}/SKILL.md",
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            })

    elif format_type == "skill_folders":
        # skills/<folder>/SKILL.md format
        contents = fetch_repo_contents(owner, repo, path, branch)
        if contents:
            for item in contents:
                if item["type"] != "dir":
                    continue

                folder_name = item["name"]

                # Try different SKILL.md casing
                skill_path = None
                content = None
                for skill_filename in ["SKILL.md", "skill.md", "Skill.md"]:
                    try_path = f"{path}/{folder_name}/{skill_filename}"
                    content = fetch_file_content(owner, repo, try_path, branch)
                    if content:
                        skill_path = try_path
                        break

                if content and skill_path:
                    skill_data = parse_skill_markdown(content, f"{folder_name}.md")
                    skill_id = slugify(folder_name)
                    category_slug, category_display = sanitize_category(default_category)
                    skills.append({
                        "id": skill_id,
                        "slug": skill_id,
                        **skill_data,
                        "category": category_slug,
                        "category_display": category_display,
                        "source_repo": f"{owner}/{repo}",
                        "source_path": skill_path,
                        "source_url": f"https://github.com/{owner}/{repo}/blob/{branch}/{skill_path}",
                        "fetched_at": datetime.now(timezone.utc).isoformat(),
                    })
                    time.sleep(0.05)

    elif format_type == "flat_md":
        # skills/*.md format (md files directly in skills folder)
        contents = fetch_repo_contents(owner, repo, path, branch)
        if contents:
            for item in contents:
                if not item["name"].endswith(".md"):
                    continue
                if item["name"].lower() == "readme.md":
                    continue

                file_path = f"{path}/{item['name']}"
                content = fetch_file_content(owner, repo, file_path, branch)

                if content:
                    skill_data = parse_skill_markdown(content, item["name"])
                    skill_id = slugify(item["name"].replace(".md", ""))
                    category_slug, category_display = sanitize_category(default_category)
                    skills.append({
                        "id": skill_id,
                        "slug": skill_id,
                        **skill_data,
                        "category": category_slug,
                        "category_display": category_display,
                        "source_repo": f"{owner}/{repo}",
                        "source_path": file_path,
                        "source_url": f"https://github.com/{owner}/{repo}/blob/{branch}/{file_path}",
                        "fetched_at": datetime.now(timezone.utc).isoformat(),
                    })
                    time.sleep(0.05)

    elif format_type == "categories":
        # categories/<category>/<skill>.md format
        contents = fetch_repo_contents(owner, repo, path, branch)
        if contents:
            for category_item in contents:
                if category_item["type"] != "dir":
                    continue

                category_name = category_item["name"]
                category_slug, category_display = sanitize_category(category_name)

                category_contents = fetch_repo_contents(owner, repo, f"{path}/{category_name}", branch)
                if not category_contents:
                    continue

                for skill_file in category_contents:
                    if not skill_file["name"].endswith(".md"):
                        continue
                    if skill_file["name"].lower() == "readme.md":
                        continue

                    file_path = f"{path}/{category_name}/{skill_file['name']}"
                    content = fetch_file_content(owner, repo, file_path, branch)

                    if content:
                        skill_data = parse_skill_markdown(content, skill_file["name"])
                        skill_id = slugify(skill_file["name"].replace(".md", ""))
                        skills.append({
                            "id": skill_id,
                            "slug": skill_id,
                            **skill_data,
                            "category": category_slug,
                            "category_display": category_display,
                            "source_repo": f"{owner}/{repo}",
                            "source_path": file_path,
                            "source_url": f"https://github.com/{owner}/{repo}/blob/{branch}/{file_path}",
                            "fetched_at": datetime.now(timezone.utc).isoformat(),
                        })
                        time.sleep(0.05)

    elif format_type == "plugins_with_skills":
        # plugins/<plugin>/skills/<skill>/SKILL.md format
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
                        skill_id = slugify(f"{plugin['name']}-{folder['name']}")
                        category_slug, category_display = sanitize_category(default_category)
                        skills.append({
                            "id": skill_id,
                            "slug": skill_id,
                            **skill_data,
                            "category": category_slug,
                            "category_display": category_display,
                            "source_repo": f"{owner}/{repo}",
                            "source_path": skill_path,
                            "source_url": f"https://github.com/{owner}/{repo}/blob/{branch}/{skill_path}",
                            "fetched_at": datetime.now(timezone.utc).isoformat(),
                        })
                        time.sleep(0.05)

    return skills


def main():
    """Main entry point."""
    print("=" * 60)
    print("Claude Skills Discovery")
    print("=" * 60)

    # Check rate limit status
    remaining, limit = check_rate_limit()
    print(f"\nGitHub API: {remaining}/{limit} requests remaining")
    if not GITHUB_TOKEN:
        print("⚠️  No GITHUB_TOKEN set - using unauthenticated rate limit (60/hr)")
        print("   Export GITHUB_TOKEN for higher limits (5000/hr)")
    if remaining < 20:
        print(f"⚠️  Low rate limit! Script may not complete.")
        if remaining < 5:
            print("   Exiting to avoid rate limit errors.")
            return

    # Step 1: Collect all repo references from awesome lists
    print("\n[1/4] Fetching awesome lists...")
    all_repos = set()

    for awesome_repo in AWESOME_LISTS:
        owner, repo = awesome_repo.split("/")
        print(f"  Fetching {awesome_repo}...")
        readme = fetch_readme(owner, repo)
        if readme:
            repos = extract_github_repos(readme)
            print(f"    Found {len(repos)} repo references")
            all_repos.update(repos)
        time.sleep(0.5)

    print(f"\n  Total unique repos found: {len(all_repos)}")

    # Step 2: Filter out non-skill repos
    print("\n[2/4] Filtering repos...")
    candidate_repos = all_repos - SKIP_REPOS
    print(f"  Candidates after filtering: {len(candidate_repos)}")

    # Step 3: Probe each repo to detect skill format
    print("\n[3/4] Probing repos for skills...")
    skill_configs = []

    for repo_full in sorted(candidate_repos):
        parts = repo_full.split("/")
        if len(parts) != 2:
            continue
        owner, repo = parts

        config = detect_skill_format(owner, repo)
        if config:
            print(f"    ✓ {repo_full}: {config['format']}")
            skill_configs.append(config)
        else:
            print(f"    ✗ {repo_full}: no skills detected")

        time.sleep(0.3)

    print(f"\n  Repos with skills: {len(skill_configs)}")

    # Step 4: Fetch skills from all detected repos
    print("\n[4/4] Fetching skills...")
    all_skills = []

    for config in skill_configs:
        repo_name = f"{config['owner']}/{config['repo']}"
        print(f"\n  Fetching from {repo_name}...")

        skills = fetch_skills_from_config(config)
        print(f"    Found {len(skills)} skills")
        all_skills.extend(skills)

        time.sleep(0.5)

    # Deduplicate by skill ID
    seen_ids = set()
    unique_skills = []
    for skill in all_skills:
        if skill["id"] not in seen_ids:
            seen_ids.add(skill["id"])
            unique_skills.append(skill)

    print(f"\n{'=' * 60}")
    print(f"Total skills fetched: {len(all_skills)}")
    print(f"Unique skills: {len(unique_skills)}")
    print(f"{'=' * 60}")

    # Save results
    output_file = DATA_DIR / "discovered_skills.json"
    with open(output_file, "w") as f:
        json.dump(unique_skills, f, indent=2)
    print(f"\nSaved to {output_file}")

    # Save discovered configs for reference
    configs_file = DATA_DIR / "discovered_repos.json"
    with open(configs_file, "w") as f:
        json.dump(skill_configs, f, indent=2)
    print(f"Repo configs saved to {configs_file}")

    # Summary by category
    print("\nSkills by category:")
    categories = {}
    for skill in unique_skills:
        cat = skill.get("category", "unknown")
        categories[cat] = categories.get(cat, 0) + 1

    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
