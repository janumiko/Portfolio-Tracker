from typing import List, Dict


class Portfolio:
    def __init__(self, name: str, data: Dict) -> None:
        self._name = name
        self._data = data

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def data(self) -> Dict:
        return self._data

    @data.setter
    def data(self, data: Dict) -> None:
        self._data = data

    @property
    def assets(self) -> Dict:
        return self.data["assets"]

    @assets.setter
    def assets(self, assets: Dict) -> None:
        self.data["assets"] = assets

    @property
    def transactions(self) -> List[Dict]:
        return self.data["transactions"]

    @transactions.setter
    def transactions(self, transactions: List[Dict]) -> None:
        self.data["transactions"] = transactions

    @property
    def currencies(self) -> Dict:
        return self.data["currencies"]

    @currencies.setter
    def currencies(self, currencies: Dict) -> None:
        self.data["currencies"] = currencies
