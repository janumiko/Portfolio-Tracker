from pathlib import Path
from typing import Optional, Dict


class FileHandler:
    def __init__(self, data_path: Path, portfolios: Dict = {}) -> None:
        self.data_path = data_path
        self.portfolios = portfolios

    @property
    def data_path(self) -> None:
        return self._data_path

    @data_path.setter
    def data_path(self, data_path: str) -> None:
        if isinstance(data_path, str):
            data_path = Path(data_path)

        if not data_path or data_path.stem == "":
            raise Exception("Path cannot be empty")
        self._data_path = data_path

    @property
    def portfolios(self) -> Dict:
        return self._portfolios

    @portfolios.setter
    def portfolios(self, portfolios: Dict) -> None:
        if isinstance(portfolios, dict):
            self._portfolios = portfolios
        else:
            raise ValueError("Portfolios should be a dictionary")

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
