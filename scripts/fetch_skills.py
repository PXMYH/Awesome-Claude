#!/usr/bin/env python3
"""Fetch skills from source repositories via GitHub API."""

import json
import re
import time
from datetime import datetime
from pathlib import Path

import requests
from slugify import slugify

from config import (
    DATA_DIR,
    GITHUB_API_BASE,
    GITHUB_TOKEN,
    SOURCE_REPOS,
    CATEGORY_MAP,
)


def get_headers():
    """Get headers for GitHub API requests."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers


def fetch_repo_contents(owner: str, repo: str, path: str, branch: str = "main") -> list:
    """Fetch contents of a directory from GitHub."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()


def fetch_file_content(owner: str, repo: str, path: str, branch: str = "main") -> str:
    """Fetch raw content of a file from GitHub."""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_skill_markdown(content: str, filename: str) -> dict:
    """Parse a skill markdown file and extract metadata."""
    # Extract name from filename (remove .md extension)
    name = filename.replace(".md", "").replace("-", " ").title()

    # Try to extract title from markdown
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        name = title_match.group(1).strip()

    # Extract description (first paragraph after title)
    desc_match = re.search(r"^#\s+.+\n\n(.+?)(?:\n\n|$)", content, re.MULTILINE | re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else f"Claude skill for {name}"
    description = description[:200] + "..." if len(description) > 200 else description

    # Extract tools mentioned (look for common patterns)
    tools = []
    tool_patterns = [
        r"\b(Python|JavaScript|TypeScript|Go|Rust|Java|Ruby|PHP)\b",
        r"\b(REST|GraphQL|gRPC|WebSocket)\b",
        r"\b(Docker|Kubernetes|AWS|GCP|Azure)\b",
        r"\b(React|Vue|Angular|Node\.js|Django|Flask|FastAPI)\b",
        r"\b(PostgreSQL|MySQL|MongoDB|Redis|SQLite)\b",
        r"\b(pytest|Jest|Mocha|JUnit)\b",
    ]
    for pattern in tool_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        tools.extend(matches)
    tools = list(set(tools))[:10]  # Dedupe and limit

    # Create prompt preview (first 500 chars of content)
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


def fetch_skills_from_repo(repo_config: dict) -> list:
    """Fetch all skills from a single repository."""
    owner = repo_config["owner"]
    repo = repo_config["repo"]
    branch = repo_config["branch"]
    categories_path = repo_config["categories_path"]

    print(f"Fetching skills from {owner}/{repo}...")
    skills = []

    try:
        # Get list of category folders
        categories = fetch_repo_contents(owner, repo, categories_path, branch)

        for category_item in categories:
            if category_item["type"] != "dir":
                continue

            category_folder = category_item["name"]
            category_info = CATEGORY_MAP.get(category_folder, {
                "slug": slugify(category_folder),
                "name": category_folder.replace("-", " ").title()
            })

            print(f"  Processing category: {category_folder}")

            # Get skill files in this category
            try:
                skill_files = fetch_repo_contents(
                    owner, repo, f"{categories_path}/{category_folder}", branch
                )
            except requests.HTTPError:
                print(f"    Could not fetch category {category_folder}")
                continue

            for skill_file in skill_files:
                if not skill_file["name"].endswith(".md"):
                    continue
                if skill_file["name"].lower() == "readme.md":
                    continue

                print(f"    Fetching: {skill_file['name']}")

                try:
                    content = fetch_file_content(
                        owner, repo,
                        f"{categories_path}/{category_folder}/{skill_file['name']}",
                        branch
                    )

                    skill_data = parse_skill_markdown(content, skill_file["name"])
                    skill_id = slugify(skill_file["name"].replace(".md", ""))

                    skill = {
                        "id": skill_id,
                        "slug": skill_id,
                        **skill_data,
                        "category": category_info["slug"],
                        "category_display": category_info["name"],
                        "source_repo": f"{owner}/{repo}",
                        "source_path": f"{categories_path}/{category_folder}/{skill_file['name']}",
                        "source_url": f"https://github.com/{owner}/{repo}/blob/{branch}/{categories_path}/{category_folder}/{skill_file['name']}",
                        "fetched_at": datetime.utcnow().isoformat() + "Z",
                    }

                    skills.append(skill)
                    time.sleep(0.1)  # Rate limiting

                except requests.HTTPError as e:
                    print(f"    Error fetching {skill_file['name']}: {e}")
                    continue

    except requests.HTTPError as e:
        print(f"Error fetching from {owner}/{repo}: {e}")

    return skills


def main():
    """Main entry point."""
    all_skills = []

    for repo_config in SOURCE_REPOS:
        if not repo_config.get("enabled", True):
            continue
        skills = fetch_skills_from_repo(repo_config)
        all_skills.extend(skills)

    print(f"\nFetched {len(all_skills)} skills total")

    # Save to JSON
    output_file = DATA_DIR / "raw_skills.json"
    with open(output_file, "w") as f:
        json.dump(all_skills, f, indent=2)

    print(f"Saved to {output_file}")


if __name__ == "__main__":
    main()
