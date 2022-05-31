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
        """Add asset in amount and currency specified in the arguments,
        to the portfolio"""

        if (
            code == ""
            or currency == ""
            or not code.isalpha()
            or not currency.isalpha()
            or unit_price < 0
            or amount <= 0
        ):
            raise ValueError("Invalid input!")

        if code in self._portfolio.assets:
            cur_amount = self._portfolio.assets[code]["amount"]
            amount += cur_amount

        self._portfolio.assets[code] = {
            "unit_price": unit_price,
            "amount": amount,
            "currency": f"{currency}",
        }
        self._portfolio.data["assets"] = self._portfolio.assets

    def remove_asset(self, code: str, amount: float) -> None:
        """remove specified amount of asset from portfolio"""

        if code == "" or not code.isalpha() or amount < 0:
            raise ValueError("Invalid input!")

        if code not in self._portfolio.assets:
            raise ValueError("Asset with that code doesn't exists.")

        # if amount to remove is higher than current amount of assets
        # remove all assets
        curr_amount = self._portfolio.assets[code]["amount"]
        amount_to_remove = min(curr_amount, amount)

        curr_amount -= amount_to_remove

        if curr_amount == 0:
            del self._portfolio.assets[code]
        else:
            self._portfolio.assets[code]["amount"] = curr_amount

    def update_balance(self, value: float, currency: str) -> None:
        """decrease balance of given currency in portfolio"""

        if currency is None or currency == "" or not currency.isalpha():
            raise ValueError("Invalid currency")

        if currency in self._portfolio.currencies:
            current_value = self._portfolio.currencies[currency]
            value += current_value

        self._portfolio.currencies[currency] = value

    def buy_asset(
        self, code: str, unit_price: float, amount: float, currency: str
    ) -> None:
        """add an asset to portfolio, create history record for
        the transaction and update currency balance of the portfolio"""

        self.add_asset(
            code=code, amount=amount, unit_price=unit_price, currency=currency
        )

        self.add_transaction_record(
            code=code,
            amount=amount,
            unit_price=unit_price,
            currency=currency,
            type="BUY",
        )

        transaction_value = unit_price * amount
        self.update_balance(-transaction_value, currency)

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
