"""Tests for skill_parser.py - shared skill parsing module."""

import pytest
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from skill_parser import (
    sanitize_category,
    guess_category,
    parse_skill_markdown,
    deduplicate_skills,
    CATEGORY_KEYWORDS,
)


class TestSanitizeCategory:
    """Tests for sanitize_category function."""

    def test_removes_leading_numbers(self):
        slug, display = sanitize_category("01-core-development")
        assert slug == "core-development"
        assert display == "Core Development"

    def test_handles_underscores(self):
        slug, display = sanitize_category("data_analytics")
        assert slug == "data-analytics"
        assert display == "Data Analytics"

    def test_handles_plain_names(self):
        slug, display = sanitize_category("community")
        assert slug == "community"
        assert display == "Community"

    def test_handles_multiple_leading_numbers(self):
        slug, display = sanitize_category("10-infrastructure")
        assert slug == "infrastructure"
        assert display == "Infrastructure"


class TestGuessCategory:
    """Tests for guess_category function."""

    def test_detects_official_from_anthropics(self):
        result = guess_category("anthropics", "skills")
        assert result == "official"

    def test_detects_security_from_trailofbits(self):
        result = guess_category("trailofbits", "skills")
        assert result == "security"

    def test_detects_category_from_topics(self):
        result = guess_category("user", "repo", topics=["security", "audit"])
        assert result == "security"

    def test_defaults_to_community(self):
        result = guess_category("random", "repo")
        assert result == "community"

    def test_detects_scientific(self):
        result = guess_category("user", "scientific-skills")
        assert result == "scientific"

    def test_detects_marketing(self):
        result = guess_category("user", "seo-tools")
        assert result == "marketing"


class TestParseSkillMarkdown:
    """Tests for parse_skill_markdown function."""

    def test_extracts_title_from_markdown(self):
        content = "# API Designer\n\nThis is a description."
        result = parse_skill_markdown(content, "api-designer.md")
        assert result["name"] == "API Designer"

    def test_extracts_description(self):
        content = "# Test Skill\n\nThis is the description of the skill."
        result = parse_skill_markdown(content, "test.md")
        assert "This is the description" in result["description"]

    def test_truncates_long_description(self):
        content = "# Test\n\n" + "A" * 300
        result = parse_skill_markdown(content, "test.md")
        assert len(result["description"]) <= 203  # 200 + "..."

    def test_extracts_tools_mentioned(self):
        content = "# Test\n\nUses Python and JavaScript with REST APIs."
        result = parse_skill_markdown(content, "test.md")
        assert "Python" in result["tools_mentioned"]
        assert "JavaScript" in result["tools_mentioned"]
        assert "REST" in result["tools_mentioned"]

    def test_creates_prompt_preview(self):
        content = "# Test\n\n" + "Content " * 100
        result = parse_skill_markdown(content, "test.md")
        assert len(result["prompt_preview"]) <= 503  # 500 + "..."
        assert result["prompt_preview"].endswith("...")

    def test_calculates_full_prompt_length(self):
        content = "# Test\n\nSome content here."
        result = parse_skill_markdown(content, "test.md")
        assert result["full_prompt_length"] == len(content)

    def test_handles_filename_fallback(self):
        content = "No markdown title here, just text."
        result = parse_skill_markdown(content, "my-cool-skill.md")
        assert result["name"] == "My Cool Skill"

    def test_includes_raw_content(self):
        content = "# Test\n\nContent here."
        result = parse_skill_markdown(content, "test.md")
        assert result["raw_content"] == content


class TestDeduplicateSkills:
    """Tests for deduplicate_skills function."""

    def test_removes_duplicates_by_id(self):
        skills = [
            {"id": "skill-1", "name": "Skill 1", "repo_stars": 100},
            {"id": "skill-1", "name": "Skill 1 Duplicate", "repo_stars": 50},
            {"id": "skill-2", "name": "Skill 2", "repo_stars": 200},
        ]
        result = deduplicate_skills(skills)
        assert len(result) == 2
        ids = [s["id"] for s in result]
        assert "skill-1" in ids
        assert "skill-2" in ids

    def test_keeps_higher_star_version(self):
        skills = [
            {"id": "skill-1", "name": "Low Stars", "repo_stars": 50},
            {"id": "skill-1", "name": "High Stars", "repo_stars": 100},
        ]
        result = deduplicate_skills(skills, prefer_higher_stars=True)
        assert len(result) == 1
        assert result[0]["name"] == "High Stars"

    def test_keeps_first_when_stars_disabled(self):
        skills = [
            {"id": "skill-1", "name": "First", "repo_stars": 50},
            {"id": "skill-1", "name": "Second", "repo_stars": 100},
        ]
        result = deduplicate_skills(skills, prefer_higher_stars=False)
        assert len(result) == 1
        assert result[0]["name"] == "First"

    def test_handles_missing_repo_stars(self):
        skills = [
            {"id": "skill-1", "name": "No Stars"},
            {"id": "skill-1", "name": "Has Stars", "repo_stars": 100},
        ]
        result = deduplicate_skills(skills)
        assert len(result) == 1
        assert result[0]["name"] == "Has Stars"

    def test_handles_empty_list(self):
        result = deduplicate_skills([])
        assert result == []


class TestCategoryKeywords:
    """Tests for CATEGORY_KEYWORDS mapping."""

    def test_has_required_categories(self):
        required = ["scientific", "security", "official", "infrastructure"]
        for cat in required:
            assert cat in CATEGORY_KEYWORDS.values()

    def test_anthropics_maps_to_official(self):
        assert CATEGORY_KEYWORDS.get("anthropics") == "official"

    def test_trailofbits_maps_to_security(self):
        assert CATEGORY_KEYWORDS.get("trailofbits") == "security"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
