from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    ROOT / "README.md",
    ROOT / "docs" / "PRODUCT_OVERVIEW.md",
    ROOT / "docs" / "PUBLIC_ROADMAP.md",
    ROOT / "assets" / ".gitkeep",
]

FORBIDDEN_PATHS = [
    ROOT / "apps",
    ROOT / "packages",
    ROOT / "infra",
    ROOT / ".env",
    ROOT / ".env.local",
    ROOT / ".env.example",
]


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_PATHS:
        if not path.exists():
            errors.append(f"Missing required public repo path: {path.relative_to(ROOT)}")

    for path in FORBIDDEN_PATHS:
        if path.exists():
            errors.append(f"Forbidden internal path present in public repo: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Public repo validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
