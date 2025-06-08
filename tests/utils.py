import hashlib

from pathlib import Path


def md5sum(file_path: Path) -> str:
    """
    Generate the MD5 hash of a file.\n
    Only use this function for small files, as it reads the entire file into memory.

    :param file_path: the path to the file.
    :returns: the MD5 hash.
    :raises TypeError: if the file path is not a ``Path`` object.
    :raises FileNotFoundError: if the file does not exist.
    :raises RuntimeError: if an error occurs while reading the file.
    """

    if not isinstance(file_path, Path):
        raise TypeError(
            f"Parameter file_path must be a Path object, but is {type(file_path)}."
        )

    if not file_path.is_file():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    try:
        with file_path.open("rb") as file:
            return hashlib.md5(file.read()).hexdigest()
    except Exception as e:
        raise RuntimeError(
            f"An error occurred while reading the file {file_path}: {e}"
        ) from e
