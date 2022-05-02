import unittest

from pathlib import Path

from src.controllers.portfolio_controller import PortfolioController


class TestAddAsset(unittest.TestCase):
    def setUp(self) -> None:
        self.portfolio_controller = PortfolioController(Path("/"), "test")
        return super().setUp()

    def test_add_asset(self) -> None:
        test_asset = {
            "name": "Test",
            "unit_price": "1",
            "amount": "10",
            "currency": "USD",
        }

        self.portfolio_controller.add_asset(
            test_asset["name"],
            test_asset["unit_price"],
            test_asset["amount"],
            test_asset["currency"],
        )

        assets = self.portfolio_controller._portfolio._assets

        # test if test asset is in assets
        self.assertIn(test_asset["name"], assets.keys())

        asset = assets[test_asset["name"]]

        # test if the values are the same
        self.assertEqual(asset["unit_price"], test_asset["unit_price"])
        self.assertEqual(asset["amount"], test_asset["amount"])
        self.assertEqual(asset["currency"], test_asset["currency"])


if __name__ == "__main__":
    unittest.main()
