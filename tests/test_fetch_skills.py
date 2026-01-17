"""Tests for fetch_skills.py"""

import pytest
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from fetch_skills import parse_skill_markdown, fetch_repo_contents


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


class TestFetchRepoContents:
    """Tests for fetch_repo_contents function."""

    @patch("fetch_skills.requests.get")
    def test_makes_correct_api_call(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        fetch_repo_contents("owner", "repo", "path")

        mock_get.assert_called_once()
        call_url = mock_get.call_args[0][0]
        assert "owner" in call_url
        assert "repo" in call_url
        assert "path" in call_url

    @patch("fetch_skills.requests.get")
    def test_returns_json_response(self, mock_get):
        expected = [{"name": "file.md", "type": "file"}]
        mock_response = MagicMock()
        mock_response.json.return_value = expected
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = fetch_repo_contents("owner", "repo", "path")
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
