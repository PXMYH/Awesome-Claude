#!/usr/bin/env python3
"""
Discover Claude skills from manually curated sources.

Reads repos from sources.yaml and fetches skills from each.
Community members can contribute by adding repos to sources.yaml.

Run: python scripts/manual_discover.py
"""

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

from config import DATA_DIR, SCRIPTS_DIR
from skill_parser import (
    check_rate_limit,
    deduplicate_skills,
    detect_skill_format,
    fetch_skills_from_config,
    get_repo_info,
    wait_for_rate_limit,
)

SOURCES_FILE = SCRIPTS_DIR / "sources.yaml"


def load_sources() -> list[dict]:
    """Load curated sources from YAML file."""
    if not SOURCES_FILE.exists():
        print(f"⚠️  {SOURCES_FILE} not found, creating default...")
        create_default_sources()

    with open(SOURCES_FILE) as f:
        data = yaml.safe_load(f)

    return data.get("repos", [])


def create_default_sources():
    """Create default sources.yaml with known good repos."""
    default = {
        "repos": [
            {
                "repo": "anthropics/skills",
                "category": "official",
                "description": "Official Anthropic skills",
            },
            {
                "repo": "VoltAgent/awesome-claude-skills",
                "description": "VoltAgent curated skills",
            },
            {
                "repo": "travisvn/awesome-claude-skills",
                "description": "Community curated skills",
            },
            {
                "repo": "ComposioHQ/awesome-claude-skills",
                "description": "Composio skills collection",
            },
            {
                "repo": "hesreallyhim/awesome-claude-code",
                "description": "Awesome Claude Code collection",
            },
        ]
    }
    with open(SOURCES_FILE, "w") as f:
        yaml.dump(default, f, default_flow_style=False, sort_keys=False)
    print(f"Created {SOURCES_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Discover skills from curated sources")
    parser.add_argument("--output", type=str, default=str(DATA_DIR / "manual_skills.json"))
    parser.add_argument("--sources", type=str, default=str(SOURCES_FILE))
    args = parser.parse_args()

    print("=" * 60)
    print("Manual Skills Discovery (from sources.yaml)")
    print("=" * 60)

    # Load sources
    sources = load_sources()
    print(f"\nLoaded {len(sources)} curated sources")

    # Check rate limits
    limits = check_rate_limit()
    print(f"Rate limits - Core: {limits['core_remaining']}/{limits['core_limit']}")

    # Process each source
    print("\n[1/2] Probing sources...")
    configs = []

    for source in sources:
        repo_str = source["repo"]
        parts = repo_str.split("/")
        if len(parts) != 2:
            print(f"  ✗ Invalid repo format: {repo_str}")
            continue

        owner, repo = parts
        override_category = source.get("category")

        wait_for_rate_limit()
        print(f"  {repo_str}...", end=" ")

        # Get repo info for stars
        info = get_repo_info(owner, repo)
        if not info:
            print("✗ not found")
            continue

        # Detect format
        config = detect_skill_format(
            owner, repo, info["default_branch"], info.get("topics", []), info["stars"]
        )

        if config:
            if override_category:
                config["default_category"] = override_category
            print(f"✓ {config['format']} ({info['stars']} ⭐)")
            configs.append(config)
        else:
            print(f"✗ no skills ({info['stars']} ⭐)")

        time.sleep(0.3)

    print(f"\n  {len(configs)} sources have skills")

    # Fetch skills
    print("\n[2/2] Fetching skills...")
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
        "source": "manual_curated",
        "discovered_at": datetime.now(timezone.utc).isoformat(),
        "sources_file": str(SOURCES_FILE),
        "sources_count": len(sources),
        "repos_with_skills": len(configs),
        "skills_total": len(all_skills),
        "skills_unique": len(unique),
    }
    with open(DATA_DIR / "manual_metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)


if __name__ == "__main__":
    main()
