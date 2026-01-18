# Design Decisions

This document tracks design decisions made during implementation.

---

## Decision 1: Two-Channel Discovery Architecture
**Date**: 2025-01-18
**Context**: Need to discover skills from multiple sources (GitHub search + manual curation)
**Decision**: Implemented two separate discovery scripts with shared parsing module:
- `github_discover.py` - Searches GitHub for repos with 100+ stars
- `manual_discover.py` - Reads from curated `sources.yaml`
- `skill_parser.py` - Shared module for repo probing and skill parsing

**Rationale**:
- Separation of concerns allows independent updates
- Manual curation provides quality control
- GitHub search enables automatic discovery of new repos
- Shared parser reduces code duplication

---

## Decision 2: Skill Format Detection
**Date**: 2025-01-18
**Context**: Different repos organize skills in different formats
**Decision**: Support multiple skill formats:
- `skill_folders` - `skills/<name>/SKILL.md`
- `root_skill_folders` - `<name>/SKILL.md` at root level
- `flat_md` - `skills/*.md` files directly
- `categories` - `categories/<cat>/*.md`
- `plugins_with_skills` - `plugins/<name>/skills/<skill>/SKILL.md`
- `root_skill` - Single `SKILL.md` at root

**Rationale**: Real-world repos use various conventions; supporting multiple formats maximizes skill discovery.

---

## Decision 3: Star-Based Filtering
**Date**: 2025-01-18
**Context**: GitHub search returns many repos, need quality filter
**Decision**: Default minimum 100 stars for GitHub discovery
**Rationale**:
- Stars indicate community validation
- Reduces noise from abandoned/low-quality repos
- Configurable via `--min-stars` flag for flexibility

---

## Decision 4: Deduplication Strategy
**Date**: 2025-01-18
**Context**: Same skill may appear in multiple repos
**Decision**: Keep skill from higher-star repo when duplicates found
**Rationale**: Higher-star repos likely have better maintained/validated content

---

## Decision 5: Integration with Existing Pipeline
**Date**: 2025-01-18
**Context**: New discovery scripts need to work with existing fetch/evaluate/generate pipeline
**Decision**: New discovery outputs to `scripts/data/` in same format as existing `fetch_skills.py`
**Rationale**: Minimal changes to existing pipeline; new scripts augment rather than replace

---

## Pending Decisions

### P1: Merge Strategy for Multiple Discovery Sources
**Question**: How to merge skills from GitHub discovery vs manual discovery vs existing fetch_skills.py?
**Options**:
1. Run all three and merge outputs
2. Replace fetch_skills.py with new discovery scripts
3. Keep fetch_skills.py for specific repos, use discovery for broader search

**Current Choice**: Option 3 - Keep existing scripts working, new discovery augments the catalog

### P2: Weekly Automation Schedule
**Question**: When should weekly GitHub discovery run?
**Options**:
1. Same schedule as daily update
2. Separate weekly job
3. Manual trigger only initially

**Current Choice**: Option 3 initially, then move to Option 2 once validated
