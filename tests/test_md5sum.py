import pytest

from pathlib import Path
from tests.utils import md5sum


def test_md5sum_file_valid(tmp_path):
    """The MD5 checksum for a valid file must match the expected value."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Hello, World!")

    # MD5 of "Hello, World!"
    expected_md5 = "65a8e27d8879283831b664bd8b7f0ad4"

    assert md5sum(file_path) == expected_md5


def test_md5sum_invalid_path_type():
    """The ``md5sum`` function must raise a ``TypeError`` if the file path is not a ``Path`` object."""
    with pytest.raises(TypeError):
        md5sum("test_file.txt")  # type: ignore


def test_md5sum_file_not_found():
    """The ``md5sum`` function must raise a ``FileNotFoundError`` for a non-existent file."""
    file_path = Path("test_file.txt")

    with pytest.raises(FileNotFoundError):
        md5sum(file_path)


def test_md5sum_runtime_error(tmp_path):
    """The ``md5sum`` function must raise a ``RuntimeError`` if an error occurs while reading the file."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Hello, World!")

    # Remove read permissions to simulate an error
    file_path.chmod(0o000)

    try:
        with pytest.raises(RuntimeError):
            md5sum(file_path)
    finally:
        # Restore permissions so the file can be deleted
        file_path.chmod(0o644)
        file_path.unlink()
