#!/usr/bin/env python3
"""Generate Jekyll data files from fetched and evaluated skills."""

import json
from datetime import datetime
from pathlib import Path

import yaml

from config import (
    DATA_DIR,
    OUTPUT_DATA_DIR,
    OUTPUT_SKILLS_DIR,
    ASSETS_JS_DIR,
    CATEGORY_MAP,
)


def load_json(filepath: Path) -> dict:
    """Load JSON file."""
    if not filepath.exists():
        return {}
    with open(filepath) as f:
        return json.load(f)


def save_yaml(data: dict, filepath: Path):
    """Save data as YAML."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def generate_skill_yaml(skill: dict, evaluation: dict, github_metrics: dict) -> dict:
    """Generate YAML data for a single skill."""
    # Remove raw_content to keep files smaller
    skill_copy = {k: v for k, v in skill.items() if k != "raw_content"}

    return {
        **skill_copy,
        "evaluation": evaluation,
        "github_metrics": github_metrics,
        "indexed_at": datetime.utcnow().isoformat() + "Z",
    }


def generate_skill_markdown(skill_data: dict) -> str:
    """Generate markdown file content for Jekyll collection."""
    frontmatter = yaml.dump(skill_data, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{frontmatter}---\n"


def generate_search_index(skills: list) -> list:
    """Generate search index for client-side search."""
    return [
        {
            "id": s["id"],
            "name": s["name"],
            "description": s["description"],
            "category": s["category"],
            "category_display": s["category_display"],
            "rating": s.get("evaluation", {}).get("overall_rating", 0),
            "url": f"/skills/{s['slug']}/",
        }
        for s in skills
    ]


def generate_categories_data(skills: list) -> list:
    """Generate categories data with skill counts."""
    categories = {}

    for skill in skills:
        cat_slug = skill["category"]
        if cat_slug not in categories:
            categories[cat_slug] = {
                "slug": cat_slug,
                "name": skill["category_display"],
                "count": 0,
                "avg_rating": 0,
                "ratings_sum": 0,
            }
        categories[cat_slug]["count"] += 1
        rating = skill.get("evaluation", {}).get("overall_rating", 0)
        categories[cat_slug]["ratings_sum"] += rating

    # Calculate averages
    result = []
    for cat in categories.values():
        if cat["count"] > 0:
            cat["avg_rating"] = round(cat["ratings_sum"] / cat["count"], 2)
        del cat["ratings_sum"]
        result.append(cat)

    return sorted(result, key=lambda x: x["name"])


def generate_site_meta(skills: list) -> dict:
    """Generate site metadata."""
    total_rating = sum(s.get("evaluation", {}).get("overall_rating", 0) for s in skills)
    avg_rating = round(total_rating / len(skills), 2) if skills else 0

    return {
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "total_skills": len(skills),
        "avg_rating": avg_rating,
    }


def main():
    """Main entry point."""
    # Load data
    raw_skills = load_json(DATA_DIR / "raw_skills.json")
    evaluations = load_json(DATA_DIR / "evaluations.json")
    github_metrics = load_json(DATA_DIR / "github_metrics.json")

    if not raw_skills:
        print("No skills data found. Run fetch_skills.py first.")
        return

    if isinstance(raw_skills, dict):
        raw_skills = list(raw_skills.values())

    print(f"Processing {len(raw_skills)} skills...")

    # Create output directories
    OUTPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_JS_DIR.mkdir(parents=True, exist_ok=True)
    skills_data_dir = OUTPUT_DATA_DIR / "skills"
    skills_data_dir.mkdir(parents=True, exist_ok=True)

    processed_skills = []

    for skill in raw_skills:
        skill_id = skill["id"]

        # Get evaluation (or default)
        evaluation = evaluations.get(skill_id, {
            "model": "default",
            "evaluated_at": datetime.utcnow().isoformat() + "Z",
            "prompt_quality": {"score": 3.0, "reasoning": "Not yet evaluated"},
            "usefulness": {"score": 3.0, "reasoning": "Not yet evaluated"},
            "overall_rating": 3.0,
            "summary": "Pending evaluation",
        })

        # Get GitHub metrics (from source repo)
        source_repo = skill.get("source_repo", "")
        metrics = github_metrics.get(source_repo, {
            "stars": 0,
            "forks": 0,
            "open_issues": 0,
            "last_commit": None,
            "fetched_at": datetime.utcnow().isoformat() + "Z",
        })

        # Generate skill data
        skill_data = generate_skill_yaml(skill, evaluation, metrics)
        processed_skills.append(skill_data)

        # Save individual skill YAML in _data/skills/
        save_yaml(skill_data, skills_data_dir / f"{skill_id}.yml")

        # Generate skill markdown for Jekyll collection
        skill_md = generate_skill_markdown(skill_data)
        skill_md_path = OUTPUT_SKILLS_DIR / f"{skill_id}.md"
        with open(skill_md_path, "w") as f:
            f.write(skill_md)

        print(f"  Generated: {skill_id}")

    # Generate categories data
    categories_data = generate_categories_data(processed_skills)
    save_yaml(categories_data, OUTPUT_DATA_DIR / "categories.yml")

    # Generate site meta
    site_meta = generate_site_meta(processed_skills)
    save_yaml(site_meta, OUTPUT_DATA_DIR / "site_meta.yml")

    # Generate search index
    search_index = generate_search_index(processed_skills)
    with open(ASSETS_JS_DIR / "search-index.json", "w") as f:
        json.dump(search_index, f)

    print(f"\nGenerated:")
    print(f"  - {len(processed_skills)} skill files")
    print(f"  - categories.yml")
    print(f"  - site_meta.yml")
    print(f"  - search-index.json")


if __name__ == "__main__":
    main()
