from pathlib import Path


def rm_tree(path: Path) -> None:
    """remove directory with all files inside"""

    for child in path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    path.rmdir()
