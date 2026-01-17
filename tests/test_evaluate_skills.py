"""Tests for evaluate_skills.py"""

import pytest
from unittest.mock import patch, MagicMock
import json
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from evaluate_skills import parse_evaluation_response, EVALUATION_PROMPT


class TestParseEvaluationResponse:
    """Tests for parse_evaluation_response function."""

    def test_parses_valid_json_response(self):
        response = {
            "choices": [{
                "message": {
                    "content": json.dumps({
                        "prompt_quality": {"score": 4.5, "reasoning": "Good quality"},
                        "usefulness": {"score": 4.0, "reasoning": "Very useful"},
                        "summary": "A great skill",
                        "tags_suggested": ["api", "rest"]
                    })
                }
            }]
        }

        result = parse_evaluation_response(response)

        assert result["prompt_quality"]["score"] == 4.5
        assert result["usefulness"]["score"] == 4.0
        assert result["summary"] == "A great skill"
        assert "api" in result["tags_suggested"]

    def test_handles_markdown_code_block(self):
        response = {
            "choices": [{
                "message": {
                    "content": "```json\n{\"prompt_quality\": {\"score\": 4.0, \"reasoning\": \"test\"}, \"usefulness\": {\"score\": 3.5, \"reasoning\": \"test\"}, \"summary\": \"test\", \"tags_suggested\": []}\n```"
                }
            }]
        }

        result = parse_evaluation_response(response)
        assert result["prompt_quality"]["score"] == 4.0

    def test_returns_default_on_invalid_json(self):
        response = {
            "choices": [{
                "message": {
                    "content": "This is not JSON"
                }
            }]
        }

        result = parse_evaluation_response(response)

        assert result["prompt_quality"]["score"] == 3.0
        assert result["usefulness"]["score"] == 3.0
        assert "Unable to evaluate" in result["prompt_quality"]["reasoning"]

    def test_returns_default_on_missing_keys(self):
        response = {}

        result = parse_evaluation_response(response)

        assert result["prompt_quality"]["score"] == 3.0
        assert result["summary"] == "Evaluation failed"


class TestEvaluationPrompt:
    """Tests for the evaluation prompt template."""

    def test_prompt_contains_placeholders(self):
        assert "{skill_name}" in EVALUATION_PROMPT
        assert "{category}" in EVALUATION_PROMPT
        assert "{skill_content}" in EVALUATION_PROMPT

    def test_prompt_requests_json_format(self):
        assert "JSON" in EVALUATION_PROMPT or "json" in EVALUATION_PROMPT

    def test_prompt_includes_scoring_criteria(self):
        assert "Prompt Quality" in EVALUATION_PROMPT
        assert "Usefulness" in EVALUATION_PROMPT
        assert "1-5" in EVALUATION_PROMPT


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
