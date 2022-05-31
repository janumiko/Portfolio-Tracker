import json

from pathlib import PosixPath, Path
from typing import Dict

from src.models.portfolio import Portfolio


class PortfolioController:
    def __init__(self, portfolio_path: Path, portfolio_name: str):
        self.path = portfolio_path
        self._portfolio = Portfolio(
            portfolio_name,
            {
                "assets": {},
                "transactions": [],
                "currencies": {},
                "categories": {},
            },
        )

        if self.path.is_file():
            self._load_file_data()

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, path: Path) -> None:
        if isinstance(path, str):
            path = Path(path)

        if isinstance(path, Path) or isinstance(path, PosixPath):
            self._path = path
        else:
            raise ValueError("Invalid path type!")

    def _load_file_data(self) -> None:
        """load data from file specified in controller path"""

        with open(self.path, "r") as file:
            self._portfolio.data = json.load(file)

    def _save_file_data(self) -> None:
        """save current portfolio class data
        to json file specified in controller path"""

        with open(self.path, "w") as file:
            file.write(json.dumps(self._portfolio.data))

    @property
    def portfolio_name(self) -> str:
        """return name from portfolio class"""

        return self._portfolio.name

    @property
    def portfolio_data(self) -> dict:
        """return data dictionary from portfolio class"""

        return self._portfolio.data

    @property
    def portfolio_assets(self) -> dict:
        """return assets dictionary from portfolio class"""

        return self._portfolio.assets

    @property
    def portfolio_transactions(self) -> dict:
        """return transactions dictionary from portfolio class"""

        return self._portfolio.transactions

    @property
    def portfolio_currencies(self) -> dict:
        """return currencies dictionary from portfolio class"""
        return self._portfolio.currencies

    def add_asset(
        self, code: str, unit_price: float, amount: float, currency: str
    ) -> None:
        raise NotImplementedError

    def remove_asset(self, code: str, amount: float) -> None:
        raise NotImplementedError

    def update_balance(self, value: float, currency: str) -> None:
        raise NotImplementedError

    def buy_asset(
        self, code: str, unit_price: float, amount: float, currency: str
    ) -> None:
        raise NotImplementedError

    def sell_asset(
        self, code: str, unit_price: float, amount: float, currency: str
    ) -> None:
        raise NotImplementedError

    def add_transaction_record(
        self,
        type: str,
        code: str,
        unit_price: float,
        amount: float,
        currency: str,
    ) -> None:
        raise NotImplementedError
