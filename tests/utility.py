import json

from pathlib import Path


def rm_tree(path: Path) -> None:
    """remove directory with all files inside"""

    for child in path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    path.rmdir()


def create_empty_portfolio(path: Path) -> None:
    empty_portfolio = {
        "assets": {},
        "transactions": [],
        "currencies": {},
        "categories": {},
    }
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(empty_portfolio))
