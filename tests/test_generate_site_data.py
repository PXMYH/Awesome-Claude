"""Tests for generate_site_data.py"""

import pytest
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from generate_site_data import (
    generate_skill_yaml,
    generate_search_index,
    generate_categories_data,
    generate_site_meta,
)


class TestGenerateSkillYaml:
    """Tests for generate_skill_yaml function."""

    def test_combines_skill_evaluation_and_metrics(self):
        skill = {
            "id": "test-skill",
            "name": "Test Skill",
            "description": "A test skill",
        }
        evaluation = {
            "prompt_quality": {"score": 4.0},
            "usefulness": {"score": 4.5},
            "overall_rating": 4.25,
        }
        metrics = {"stars": 100, "forks": 20}

        result = generate_skill_yaml(skill, evaluation, metrics)

        assert result["id"] == "test-skill"
        assert result["evaluation"] == evaluation
        assert result["github_metrics"] == metrics
        assert "indexed_at" in result

    def test_removes_raw_content(self):
        skill = {
            "id": "test",
            "raw_content": "This should be removed",
            "name": "Test",
        }

        result = generate_skill_yaml(skill, {}, {})

        assert "raw_content" not in result


class TestGenerateSearchIndex:
    """Tests for generate_search_index function."""

    def test_creates_search_entries(self):
        skills = [
            {
                "id": "skill-1",
                "slug": "skill-1",
                "name": "Skill One",
                "description": "First skill",
                "category": "cat-1",
                "category_display": "Category One",
                "evaluation": {"overall_rating": 4.5},
            }
        ]

        result = generate_search_index(skills)

        assert len(result) == 1
        assert result[0]["id"] == "skill-1"
        assert result[0]["name"] == "Skill One"
        assert result[0]["rating"] == 4.5
        assert "/skills/skill-1/" in result[0]["url"]

    def test_handles_missing_evaluation(self):
        skills = [{"id": "skill-1", "slug": "skill-1", "name": "Skill", "description": "", "category": "cat", "category_display": "Cat"}]

        result = generate_search_index(skills)

        assert result[0]["rating"] == 0


class TestGenerateCategoriesData:
    """Tests for generate_categories_data function."""

    def test_counts_skills_per_category(self):
        skills = [
            {"category": "cat-1", "category_display": "Category One", "evaluation": {"overall_rating": 4.0}},
            {"category": "cat-1", "category_display": "Category One", "evaluation": {"overall_rating": 5.0}},
            {"category": "cat-2", "category_display": "Category Two", "evaluation": {"overall_rating": 3.0}},
        ]

        result = generate_categories_data(skills)

        cat1 = next(c for c in result if c["slug"] == "cat-1")
        cat2 = next(c for c in result if c["slug"] == "cat-2")

        assert cat1["count"] == 2
        assert cat2["count"] == 1

    def test_calculates_average_rating(self):
        skills = [
            {"category": "cat-1", "category_display": "Cat", "evaluation": {"overall_rating": 4.0}},
            {"category": "cat-1", "category_display": "Cat", "evaluation": {"overall_rating": 5.0}},
        ]

        result = generate_categories_data(skills)

        assert result[0]["avg_rating"] == 4.5


class TestGenerateSiteMeta:
    """Tests for generate_site_meta function."""

    def test_counts_total_skills(self):
        skills = [{}, {}, {}]

        result = generate_site_meta(skills)

        assert result["total_skills"] == 3

    def test_calculates_average_rating(self):
        skills = [
            {"evaluation": {"overall_rating": 4.0}},
            {"evaluation": {"overall_rating": 5.0}},
        ]

        result = generate_site_meta(skills)

        assert result["avg_rating"] == 4.5

    def test_includes_last_updated(self):
        result = generate_site_meta([])

        assert "last_updated" in result

    def test_handles_empty_skills_list(self):
        result = generate_site_meta([])

        assert result["total_skills"] == 0
        assert result["avg_rating"] == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
