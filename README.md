# BranchOps Public

## Objective

Provide a public-safe BranchOps repository for product narrative, screenshots, architecture summaries, and roadmap material without exposing internal implementation details.

## System Design

- `docs/PRODUCT_OVERVIEW.md`: public explanation of the BranchOps platform
- `docs/PUBLIC_ROADMAP.md`: sanitized roadmap and milestone framing
- `assets/`: screenshots, diagrams, and public-safe visuals only
- `scripts/validate_public_repo.py`: validation that this repo stays public-safe
- `.github/workflows/validate-public-repo.yml`: CI boundary enforcement

## Execution Steps

1. Publish only product summary, visuals, and public documentation here.
2. Keep live code, infrastructure, secrets, and internal docs in `OffDaBranch/branchops-platform`.
3. Run `python scripts/validate_public_repo.py` before committing.
4. Add screenshots or diagrams only after reviewing them for internal data leakage.

## Risks

- Do not copy code, environment files, or infrastructure folders into this repository.
- Treat every file here as potentially public and redistributable.

## Optimization

- This repo becomes the clean public proof surface for demos, fundraising, or partner conversations.
- The validator prevents accidental leakage from the private platform repo.
