#!/usr/bin/env python3
"""
Discover Claude skills via GitHub search.

Searches GitHub for "awesome claude skills" repos with 100+ stars,
probes them for skill content, and outputs discovered skills.

Run weekly: python scripts/github_discover.py
"""

import argparse
import json
import time
from datetime import datetime, timezone

import requests

from config import DATA_DIR, GITHUB_API_BASE, GITHUB_TOKEN
from skill_parser import (
    check_rate_limit,
    detect_skill_format,
    deduplicate_skills,
    fetch_skills_from_config,
    get_headers,
    wait_for_rate_limit,
)

# Default minimum stars
MIN_STARS = 100

# Search queries
SEARCH_QUERIES = [
    "awesome claude skills",
    "claude code skills",
    "awesome agent skills",
]

# Repos to skip (not skill repos)
SKIP_REPOS = {
    "anthropics/anthropic-sdk-python",
    "anthropics/anthropic-sdk-typescript",
    "anthropics/claude-cookbooks",
    "anthropics/courses",
    "punkpeye/awesome-mcp-servers",
    "langgptai/awesome-claude-prompts",
    "vijaythecoder/awesome-claude-agents",
    "kimtth/awesome-azure-openai-llm",
}


def search_repos(query: str, min_stars: int) -> list[dict]:
    """Search GitHub for repos matching query with min_stars."""
    repos = []
    page = 1

    while True:
        url = f"{GITHUB_API_BASE}/search/repositories"
        params = {
            "q": f"{query} stars:>={min_stars}",
            "sort": "stars",
            "order": "desc",
            "per_page": 100,
            "page": page,
        }

        response = requests.get(url, headers=get_headers(), params=params)

        if response.status_code == 403:
            print("   Rate limited, waiting...")
            time.sleep(60)
            continue

        if response.status_code != 200:
            break

        data = response.json()
        items = data.get("items", [])

        for item in items:
            repos.append({
                "full_name": item["full_name"],
                "owner": item["owner"]["login"],
                "repo": item["name"],
                "stars": item["stargazers_count"],
                "default_branch": item.get("default_branch", "main"),
                "topics": item.get("topics", []),
            })

        if len(items) < 100:
            break
        page += 1
        time.sleep(2)

    return repos


def main():
    parser = argparse.ArgumentParser(description="Discover skills via GitHub search")
    parser.add_argument("--min-stars", type=int, default=MIN_STARS)
    parser.add_argument("--dry-run", action="store_true", help="Only list repos, don't fetch skills")
    parser.add_argument("--output", type=str, default=str(DATA_DIR / "github_skills.json"))
    args = parser.parse_args()

    print("=" * 60)
    print(f"GitHub Skills Discovery (min {args.min_stars} stars)")
    print("=" * 60)

    # Check rate limits
    limits = check_rate_limit()
    print(f"\nRate limits - Core: {limits['core_remaining']}/{limits['core_limit']}, "
          f"Search: {limits['search_remaining']}/{limits['search_limit']}")

    if not GITHUB_TOKEN:
        print("⚠️  No GITHUB_TOKEN - using low rate limits")

    # Search for repos
    print("\n[1/3] Searching GitHub...")
    all_repos = {}
    for query in SEARCH_QUERIES:
        print(f"  '{query}'...")
        repos = search_repos(query, args.min_stars)
        for r in repos:
            if r["full_name"] not in all_repos:
                all_repos[r["full_name"]] = r
        time.sleep(2)

    # Filter and sort
    candidates = [r for r in all_repos.values() if r["full_name"] not in SKIP_REPOS]
    candidates.sort(key=lambda x: x["stars"], reverse=True)

    print(f"\n  Found {len(candidates)} repos with {args.min_stars}+ stars")
    print("\n  Top repos:")
    for r in candidates[:10]:
        print(f"    {r['stars']:>6} ⭐  {r['full_name']}")

    if args.dry_run:
        print("\n[Dry run] Stopping before skill fetch")
        return

    # Probe repos
    print("\n[2/3] Probing repos for skills...")
    configs = []
    for r in candidates:
        wait_for_rate_limit()
        print(f"  {r['full_name']}...", end=" ")
        config = detect_skill_format(
            r["owner"], r["repo"], r["default_branch"], r.get("topics", []), r["stars"]
        )
        if config:
            print(f"✓ {config['format']}")
            configs.append(config)
        else:
            print("✗")
        time.sleep(0.3)

    print(f"\n  {len(configs)} repos have skills")

    # Fetch skills
    print("\n[3/3] Fetching skills...")
    all_skills = []
    for config in configs:
        name = f"{config['owner']}/{config['repo']}"
        print(f"  {name}...", end=" ")
        wait_for_rate_limit()
        skills = fetch_skills_from_config(config)
        print(f"{len(skills)} skills")
        all_skills.extend(skills)
        time.sleep(0.5)

    # Deduplicate
    unique = deduplicate_skills(all_skills)

    print(f"\n{'=' * 60}")
    print(f"Total: {len(all_skills)} skills, {len(unique)} unique")
    print("=" * 60)

    # Save
    with open(args.output, "w") as f:
        json.dump(unique, f, indent=2)
    print(f"\nSaved to {args.output}")

    # Save metadata
    metadata = {
        "source": "github_search",
        "discovered_at": datetime.now(timezone.utc).isoformat(),
        "min_stars": args.min_stars,
        "queries": SEARCH_QUERIES,
        "repos_found": len(candidates),
        "repos_with_skills": len(configs),
        "skills_total": len(all_skills),
        "skills_unique": len(unique),
    }
    with open(DATA_DIR / "github_metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)


if __name__ == "__main__":
    main()
