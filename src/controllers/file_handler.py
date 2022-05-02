from pathlib import Path
from typing import Optional, Dict


class FileHandler:
    def __init__(self, data_path: Path, portfolios: Dict = {}) -> None:
        raise NotImplementedError

    @property
    def data_path(self) -> None:
        raise NotImplementedError

    @data_path.setter
    def data_path(self, data_path: str) -> None:
        raise NotImplementedError

    @property
    def portfolios(self) -> Dict:
        raise NotImplementedError

    @portfolios.setter
    def portfolios(self, portfolios: Dict) -> None:
        raise NotImplementedError

    def check_file_name(self, name: str) -> None:
        raise NotImplementedError

    def add_portfolio(self, name: str, path: Path) -> None:
        raise NotImplementedError

    def create_data_dir(self) -> None:
        raise NotImplementedError

    def get_portfolio_path(self, name: str) -> Optional[Path]:
        raise NotImplementedError

    def load_portfolios(self) -> None:
        raise NotImplementedError

    def create_empty_portfolio(self, name: str) -> None:
        raise NotImplementedError

    def upload_portfolio(self, name: str, portfolio_file) -> None:
        raise NotImplementedError

    def remove_portfolio(self, name: str) -> None:
        raise NotImplementedError
