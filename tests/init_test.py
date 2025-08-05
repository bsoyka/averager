"""Test the package __init__ module."""

from pathlib import Path

from averager import __version__

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore[no-redef]


def test_version() -> None:
    """Test that the package version matches the pyproject.toml."""
    pyproject_path = Path(__file__).parent.parent / 'pyproject.toml'
    with pyproject_path.open('rb') as file:
        pyproject = tomllib.load(file)

    assert __version__ == pyproject['project']['version']
