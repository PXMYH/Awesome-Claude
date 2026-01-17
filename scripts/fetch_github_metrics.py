#!/usr/bin/env python3
"""Fetch GitHub metrics for source repositories."""

import json
from datetime import datetime

import requests

from config import (
    DATA_DIR,
    GITHUB_API_BASE,
    GITHUB_TOKEN,
    SOURCE_REPOS,
)


def get_headers():
    """Get headers for GitHub API requests."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers


def fetch_repo_metrics(owner: str, repo: str) -> dict:
    """Fetch metrics for a repository."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    data = response.json()

    # Get last commit date
    commits_url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits?per_page=1"
    commits_response = requests.get(commits_url, headers=get_headers())
    commits_response.raise_for_status()
    commits = commits_response.json()

    last_commit = None
    if commits:
        last_commit = commits[0]["commit"]["committer"]["date"][:10]

    return {
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "open_issues": data.get("open_issues_count", 0),
        "last_commit": last_commit,
        "fetched_at": datetime.utcnow().isoformat() + "Z",
    }


def main():
    """Main entry point."""
    metrics = {}

    for repo_config in SOURCE_REPOS:
        if not repo_config.get("enabled", True):
            continue

        owner = repo_config["owner"]
        repo = repo_config["repo"]
        repo_key = f"{owner}/{repo}"

        print(f"Fetching metrics for {repo_key}...")

        try:
            repo_metrics = fetch_repo_metrics(owner, repo)
            metrics[repo_key] = repo_metrics
            print(f"  Stars: {repo_metrics['stars']}, Forks: {repo_metrics['forks']}")
        except Exception as e:
            print(f"  Error: {e}")
            metrics[repo_key] = {
                "stars": 0,
                "forks": 0,
                "open_issues": 0,
                "last_commit": None,
                "fetched_at": datetime.utcnow().isoformat() + "Z",
                "error": str(e),
            }

    # Save metrics
    output_file = DATA_DIR / "github_metrics.json"
    with open(output_file, "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"\nSaved to {output_file}")


if __name__ == "__main__":
    main()
