from typing import List, Dict


class Portfolio:
    def __init__(self, name: str, data: Dict) -> None:
        raise NotImplementedError

    @property
    def name(self) -> str:
        raise NotImplementedError

    @name.setter
    def name(self, name: str) -> None:
        raise NotImplementedError

    @property
    def data(self) -> Dict:
        raise NotImplementedError

    @data.setter
    def data(self, data: Dict) -> None:
        raise NotImplementedError

    @property
    def assets(self) -> Dict:
        raise NotImplementedError

    @assets.setter
    def assets(self, assets: Dict) -> None:
        raise NotImplementedError

    @property
    def transactions(self) -> List[Dict]:
        raise NotImplementedError

    @transactions.setter
    def transactions(self, transactions: List[Dict]) -> None:
        raise NotImplementedError

    @property
    def currencies(self) -> Dict:
        raise NotImplementedError

    @currencies.setter
    def currencies(self, currencies: Dict) -> None:
        raise NotImplementedError
