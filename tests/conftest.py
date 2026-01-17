"""Pytest configuration for Claude Skills Directory tests."""

import sys
from pathlib import Path

# Add scripts directory to Python path
scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))
