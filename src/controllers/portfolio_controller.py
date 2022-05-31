from pathlib import Path
from typing import Dict


class PortfolioController:
    def __init__(self, portfolio_path: Path, portfolio_name: str):
        raise NotImplementedError

    @property
    def path(self) -> Path:
        raise NotImplementedError

    @path.setter
    def path(self, path: Path) -> None:
        raise NotImplementedError

    def get_file_data(self) -> None:
        raise NotImplementedError

    def save_file_data(self) -> None:
        raise NotImplementedError

    def get_portf_name(self) -> str:
        raise NotImplementedError

    def get_portf_data(self) -> Dict:
        raise NotImplementedError

    def get_portf_assets(self) -> Dict:
        raise NotImplementedError

    def get_portf_transactions(self) -> Dict:
        raise NotImplementedError

    def get_portf_currencies(self) -> Dict:
        raise NotImplementedError

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
