import unittest

from pathlib import Path
from typing import Dict

from src.controllers.portfolio_controller import PortfolioController


class TestAddAsset(unittest.TestCase):
    def setUp(self) -> None:
        self.portfolio_controller = PortfolioController(Path("/"), "test")

        self._asset_template = {
            "name": "Test",
            "unit_price": 1,
            "amount": 10,
            "currency": "USD",
        }

        return super().setUp()

    @property
    def asset_template(self) -> Dict:
        return self._asset_template.copy()

    def _check_add_valid_asset(self, test_asset: Dict) -> None:
        """Add asset to portfolio and check if it is in portfolio assets
        and has the same values as provided in arguments.
        """

        self.portfolio_controller.add_asset(
            test_asset["name"],
            test_asset["unit_price"],
            test_asset["amount"],
            test_asset["currency"],
        )

        assets = self.portfolio_controller._portfolio._assets

        # test if test asset name in assets
        self.assertIn(test_asset["name"], assets.keys())

        asset = assets[test_asset["name"]]

        # test if the values are the same
        self.assertEqual(asset["unit_price"], test_asset["unit_price"])
        self.assertEqual(asset["amount"], test_asset["amount"])
        self.assertEqual(asset["currency"], test_asset["currency"])

    def test_add_example(self) -> None:
        """Test portfolio controller add_asset function
        provided valid example arguments

        Should add an asset to portfolio with values provided in arguments.
        """

        test_asset = self.asset_template
        self._check_add_valid_asset(test_asset)


if __name__ == "__main__":
    unittest.main()
