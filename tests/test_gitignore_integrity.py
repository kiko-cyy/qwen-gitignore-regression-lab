from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_gitignore_matches_byte_for_byte_baseline() -> None:
    actual = (ROOT / ".gitignore").read_bytes()
    expected = (ROOT / "tests" / "fixtures" / "gitignore.baseline").read_bytes()
    assert actual == expected, ".gitignore differs from the committed baseline"
