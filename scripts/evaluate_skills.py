#!/usr/bin/env python3
"""Evaluate skills using LLM-as-judge via OpenRouter."""

import json
import os
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from config import (
    DATA_DIR,
    CACHE_DIR,
    OPENROUTER_BASE_URL,
    OPENROUTER_MODEL,
    OPENROUTER_API_KEY,
    EVALUATION_CACHE_DAYS,
    SKIP_CACHED_EVALUATIONS,
)


EVALUATION_PROMPT = """You are an expert evaluator of AI agent/skill prompts. Evaluate the following Claude skill/agent prompt.

**Skill Name:** {skill_name}
**Category:** {category}

**Prompt Content:**
```
{skill_content}
```

Evaluate on these dimensions (1-5 scale, with 0.5 increments):

## 1. Prompt Quality
- Clarity: Are instructions clear and unambiguous?
- Specificity: Does it define scope, constraints, and expected behavior?
- Edge Cases: Does it handle edge cases or provide fallback guidance?
- Best Practices: Does it follow prompt engineering best practices?

## 2. Usefulness/Practicality
- Real-world Value: Would this help with actual development tasks?
- Completeness: Does it cover the task comprehensively?
- Actionability: Can a user immediately benefit from this skill?

Respond in this exact JSON format (no markdown, just raw JSON):
{{"prompt_quality": {{"score": <number 1.0-5.0>, "reasoning": "<2-3 sentences>"}}, "usefulness": {{"score": <number 1.0-5.0>, "reasoning": "<2-3 sentences>"}}, "summary": "<1-2 sentence overall assessment>", "tags_suggested": ["<tag1>", "<tag2>", "<tag3>"]}}"""


def get_cache_path(skill_id: str) -> Path:
    """Get cache file path for a skill evaluation."""
    return CACHE_DIR / f"{skill_id}_eval.json"


def is_cache_valid(cache_path: Path) -> bool:
    """Check if cached evaluation is still valid."""
    if not cache_path.exists():
        return False
    if not SKIP_CACHED_EVALUATIONS:
        return False

    with open(cache_path) as f:
        cached = json.load(f)

    evaluated_at = datetime.fromisoformat(cached["evaluated_at"].replace("Z", "+00:00"))
    expiry = evaluated_at + timedelta(days=EVALUATION_CACHE_DAYS)

    return datetime.now(evaluated_at.tzinfo) < expiry


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=60))
def call_openrouter(prompt: str) -> dict:
    """Call OpenRouter API for evaluation."""
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY not set")

    response = requests.post(
        f"{OPENROUTER_BASE_URL}/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": OPENROUTER_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 1000,
        },
        timeout=60,
    )
    response.raise_for_status()
    return response.json()


def parse_evaluation_response(response: dict) -> dict:
    """Parse LLM response into structured evaluation."""
    try:
        content = response["choices"][0]["message"]["content"]
        # Try to parse as JSON
        # Remove any markdown code blocks if present
        content = content.strip()
        if content.startswith("```"):
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        content = content.strip()

        return json.loads(content)
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Error parsing response: {e}")
        # Return default evaluation
        return {
            "prompt_quality": {"score": 3.0, "reasoning": "Unable to evaluate"},
            "usefulness": {"score": 3.0, "reasoning": "Unable to evaluate"},
            "summary": "Evaluation failed",
            "tags_suggested": [],
        }


def evaluate_skill(skill: dict) -> dict:
    """Evaluate a single skill."""
    skill_id = skill["id"]
    cache_path = get_cache_path(skill_id)

    # Check cache
    if is_cache_valid(cache_path):
        print(f"  Using cached evaluation for {skill_id}")
        with open(cache_path) as f:
            return json.load(f)

    print(f"  Evaluating {skill_id}...")

    # Build prompt
    prompt = EVALUATION_PROMPT.format(
        skill_name=skill["name"],
        category=skill["category_display"],
        skill_content=skill.get("raw_content", skill.get("prompt_preview", ""))[:4000],
    )

    try:
        response = call_openrouter(prompt)
        parsed = parse_evaluation_response(response)

        evaluation = {
            "model": OPENROUTER_MODEL,
            "evaluated_at": datetime.utcnow().isoformat() + "Z",
            "prompt_quality": parsed["prompt_quality"],
            "usefulness": parsed["usefulness"],
            "overall_rating": round(
                (parsed["prompt_quality"]["score"] + parsed["usefulness"]["score"]) / 2, 2
            ),
            "summary": parsed["summary"],
            "tags_suggested": parsed.get("tags_suggested", []),
        }

        # Cache result
        with open(cache_path, "w") as f:
            json.dump(evaluation, f, indent=2)

        time.sleep(6)  # Rate limiting (10 RPM)
        return evaluation

    except Exception as e:
        print(f"  Error evaluating {skill_id}: {e}")
        return {
            "model": OPENROUTER_MODEL,
            "evaluated_at": datetime.utcnow().isoformat() + "Z",
            "prompt_quality": {"score": 3.0, "reasoning": f"Evaluation error: {str(e)[:100]}"},
            "usefulness": {"score": 3.0, "reasoning": f"Evaluation error: {str(e)[:100]}"},
            "overall_rating": 3.0,
            "summary": "Evaluation failed",
            "tags_suggested": [],
        }


def main():
    """Main entry point."""
    # Load raw skills
    raw_skills_file = DATA_DIR / "raw_skills.json"
    if not raw_skills_file.exists():
        print("No raw_skills.json found. Run fetch_skills.py first.")
        return

    with open(raw_skills_file) as f:
        skills = json.load(f)

    print(f"Evaluating {len(skills)} skills...")

    evaluations = {}
    for skill in skills:
        evaluation = evaluate_skill(skill)
        evaluations[skill["id"]] = evaluation

    # Save evaluations
    output_file = DATA_DIR / "evaluations.json"
    with open(output_file, "w") as f:
        json.dump(evaluations, f, indent=2)

    print(f"\nSaved evaluations to {output_file}")


if __name__ == "__main__":
    main()
