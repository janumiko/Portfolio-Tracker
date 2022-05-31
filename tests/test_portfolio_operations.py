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

        assets = self.portfolio_controller._portfolio.assets

        # test if test asset name in assets
        self.assertIn(test_asset["name"], assets.keys())

        asset = assets[test_asset["name"]]

        # test if the values are the same
        self.assertEqual(asset["unit_price"], test_asset["unit_price"])
        self.assertEqual(asset["amount"], test_asset["amount"])
        self.assertEqual(asset["currency"], test_asset["currency"])

    def _check_add_asset_exception(
        self, test_asset: Dict, exception: Exception
    ) -> None:
        """Check if portoflio add_asset raises provided exception,
        also check if asset is not added into portfolio assets.
        """

        self.assertRaises(
            exception,
            self.portfolio_controller.add_asset,
            test_asset["name"],
            test_asset["unit_price"],
            test_asset["amount"],
            test_asset["currency"],
        )

        assets = self.portfolio_controller._portfolio.assets

        # check if asset was not added to assets
        self.assertNotIn(test_asset["name"], assets.keys())

    def test_add_example(self) -> None:
        """Add asset with valid input

        Should add an asset to portfolio with values provided in arguments.
        """

        test_asset = self.asset_template
        self._check_add_valid_asset(test_asset)

    def test_add_empty_name(self) -> None:
        """Add asset provided with empty string as name

        Should raise ValueError
        """

        test_asset = self.asset_template
        test_asset["name"] = ""

        self._check_add_asset_exception(test_asset, ValueError)

    def test_add_negative_unitprice(self) -> None:
        """Add asset with negative unit price

        Should raise ValueError
        """

        test_asset = self.asset_template
        test_asset["unit_price"] = -1

        self._check_add_asset_exception(test_asset, ValueError)

    def test_add_negative_amount(self) -> None:
        """Add asset with negative amount

        Should raise ValueError
        """

        test_asset = self.asset_template
        test_asset["amount"] = -10
        self._check_add_asset_exception(test_asset, ValueError)

    def test_add_empty_currency(self) -> None:
        """Add asset with empty string as currency

        Should raise ValueError
        """

        test_asset = self.asset_template
        test_asset["currency"] = ""
        self._check_add_asset_exception(test_asset, ValueError)


class TestRemoveAsset(unittest.TestCase):
    def setUp(self) -> None:
        self.portfolio_controller = PortfolioController(Path("/"), "test")

        # constants for test asset
        self._TEST_ASSET_NAME = "testname"
        self._TEST_ASSET_UNIT_PRICE = 100
        self._TEST_ASSET_AMOUNT = 1000
        self._TEST_ASSET_CURRENCY = "USD"

        # create test asset inside portfolio
        self._initialize_example_portfolio()

        return super().setUp()

    def _initialize_example_portfolio(self) -> None:
        """Create portfolio with example asset"""

        self.portfolio_controller._portfolio.assets[self._TEST_ASSET_NAME] = {
            "unit_price": self._TEST_ASSET_UNIT_PRICE,
            "amount": self._TEST_ASSET_AMOUNT,
            "currency": self._TEST_ASSET_CURRENCY,
        }

    def _check_remove_asset_exception(self, name, amount, exception) -> None:
        """Call remove_asset with provided arguments
        and check if provided exception was raised
        """

        self.assertRaises(
            exception, self.portfolio_controller.remove_asset, name, amount
        )

    def _check_remove_asset_valid(self, name, amount) -> None:
        """Remove asset with provided arguments

        If removed amount is less than current amount of asset
        check if amount after removal is correct

        else check if asset was removed from the portfolio
        """

        self.portfolio_controller.remove_asset(name, amount)
        if amount < self._TEST_ASSET_AMOUNT:
            self.assertEqual(
                self.portfolio_controller._portfolio.assets[name]["amount"],
                self._TEST_ASSET_AMOUNT - amount,
            )
        else:
            self.assertNotIn(name, self.portfolio_controller._portfolio.assets)

    def test_remove_nonexisting_asset(self) -> None:
        """Remove asset which is not in portfolio.

        Should raise ValueError
        """

        self._check_remove_asset_exception("", 10, ValueError)

    def test_remove_negative_amount(self) -> None:
        """Remove negative amount of asset from portfolio.

        Should raise ValueError
        """

        self._check_remove_asset_exception("testname", -10, ValueError)

    def test_remove_not_all_assets(self) -> None:
        """Remove some (not all) amount of asset from portfolio

        Should decrease amount of asset"""

        self._check_remove_asset_valid("testname", self._TEST_ASSET_AMOUNT - 1)

    def test_remove_all_assets(self) -> None:
        """Remove whole (all) amount of asset from portfolio

        Should remove asset from portfolio"""

        self._check_remove_asset_valid("testname", self._TEST_ASSET_AMOUNT)


class TestBuyAsset(unittest.TestCase):
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

    def _check_buy_valid_asset(self, test_asset: Dict) -> None:
        """buy asset to portfolio and check if it is in portfolio assets
        and has the same values as provided in arguments.
        """

        self.portfolio_controller.buy_asset(
            test_asset["name"],
            test_asset["unit_price"],
            test_asset["amount"],
            test_asset["currency"],
        )

        assets = self.portfolio_controller._portfolio.assets

        # test if test asset name in assets
        self.assertIn(test_asset["name"], assets.keys())

        asset = assets[test_asset["name"]]

        # test if the values are the same
        self.assertEqual(asset["unit_price"], test_asset["unit_price"])
        self.assertEqual(asset["amount"], test_asset["amount"])
        self.assertEqual(asset["currency"], test_asset["currency"])

        self.assertEqual(
            1, len(self.portfolio_controller._portfolio.transactions)
        )

    def _check_buy_asset_exception(
        self, test_asset: Dict, exception: Exception
    ) -> None:
        """Check if portoflio buy_asset raises provided exception,
        also check if asset is not added into portfolio assets.
        """

        self.assertRaises(
            exception,
            self.portfolio_controller.buy_asset,
            test_asset["name"],
            test_asset["unit_price"],
            test_asset["amount"],
            test_asset["currency"],
        )

        assets = self.portfolio_controller._portfolio.assets

        # check if asset was not added to assets
        self.assertNotIn(test_asset["name"], assets.keys())

        # check if transaction record was not created
        self.assertEqual(
            0, len(self.portfolio_controller._portfolio.transactions)
        )

    def test_buy_example(self) -> None:
        """buy asset with provided valid arguments

        Should add an asset to portfolio with values provided in arguments.
        And create a transaction record in transaction history
        """

        test_asset = self.asset_template
        self._check_buy_valid_asset(test_asset)

    def test_buy_empty_name(self) -> None:
        """Buy asset with empty string as name

        Should raise ValueError
        """

        test_asset = self.asset_template
        test_asset["name"] = ""

        self._check_buy_asset_exception(test_asset, ValueError)

    def test_buy_negative_unitprice(self) -> None:
        """Buy asset with negative unit price

        Should raise ValueError
        """

        test_asset = self.asset_template
        test_asset["unit_price"] = -1

        self._check_buy_asset_exception(test_asset, ValueError)

    def test_buy_negative_amount(self) -> None:
        """Buy negative amount of asset

        Should raise ValueError
        """

        test_asset = self.asset_template
        test_asset["amount"] = -10
        self._check_buy_asset_exception(test_asset, ValueError)

    def test_buy_empty_currency(self) -> None:
        """Buy an asset with empty string as currency

        Should raise ValueError
        """

        test_asset = self.asset_template
        test_asset["currency"] = ""
        self._check_buy_asset_exception(test_asset, ValueError)


class TestSellAsset(unittest.TestCase):
    def setUp(self) -> None:
        self.portfolio_controller = PortfolioController(Path("/"), "test")

        # constants for test asset
        self._TEST_ASSET_NAME = "testname"
        self._TEST_ASSET_UNIT_PRICE = 100
        self._TEST_ASSET_AMOUNT = 1000
        self._TEST_ASSET_CURRENCY = "USD"

        self._asset_template = {
            "name": self._TEST_ASSET_NAME,
            "unit_price": self._TEST_ASSET_UNIT_PRICE,
            "amount": self._TEST_ASSET_AMOUNT,
            "currency": self._TEST_ASSET_CURRENCY,
        }

        # create test asset inside portfolio
        self._initialize_example_portfolio()

        return super().setUp()

    def _initialize_example_portfolio(self) -> None:
        """Create portfolio with example asset"""

        self.portfolio_controller._portfolio.assets[self._TEST_ASSET_NAME] = {
            "unit_price": self._TEST_ASSET_UNIT_PRICE,
            "amount": self._TEST_ASSET_AMOUNT,
            "currency": self._TEST_ASSET_CURRENCY,
        }

    @property
    def asset_template(self) -> Dict:
        return self._asset_template.copy()

    def _check_sell_valid_asset(self, test_asset) -> None:
        """Remove asset with provided arguments

        If removed amount is less than current amount of asset
        check if amount after removal is correct

        else check if asset was removed from the portfolio

        assert if transaction record was created
        """

        self.portfolio_controller.sell_asset(
            test_asset["name"],
            test_asset["unit_price"],
            test_asset["amount"],
            test_asset["currency"],
        )

        if test_asset["amount"] < self._TEST_ASSET_AMOUNT:
            self.assertEqual(
                self.portfolio_controller._portfolio.assets[
                    test_asset["name"]
                ]["amount"],
                self._TEST_ASSET_AMOUNT - test_asset["amount"],
            )
        else:
            self.assertNotIn(
                test_asset["name"], self.portfolio_controller._portfolio.assets
            )

        self.assertEqual(
            1, len(self.portfolio_controller._portfolio.transactions)
        )

    def _check_sell_asset_exception(
        self, test_asset: Dict, exception: Exception
    ) -> None:
        """Check if portoflio sell asster function raises provided exception,
        also check if asset is not added into portfolio assets
        and transaction record was not created
        """

        self.assertRaises(
            exception,
            self.portfolio_controller.sell_asset,
            test_asset["name"],
            test_asset["unit_price"],
            test_asset["amount"],
            test_asset["currency"],
        )

        # check if transaction record was not created
        self.assertEqual(
            0, len(self.portfolio_controller._portfolio.transactions)
        )

    def test_sell_not_all(self) -> None:
        """sell less than current amount of asset

        should create an transaction record, and
        remove amount of asset equal to provided amount in argument
        """

        test_asset = self.asset_template
        test_asset["amount"] -= 1
        self._check_sell_valid_asset(test_asset)

    def test_sell_all(self) -> None:
        """sell asset with amount equal to current asset amount

        should create a transaction record and remove asset from portfolio
        """

        test_asset = self.asset_template
        self._check_sell_valid_asset(test_asset)

    def test_sell_over_all(self) -> None:
        """sell more asset than current amount

        should raise ValueError

        should not create a transaction record
        """

        test_asset = self.asset_template
        self._check_sell_valid_asset(test_asset)

    def test_sell_empty_name(self) -> None:
        """sell asset with empty string as name argument

        should raise ValueError

        should not create a transaction record
        """

        test_asset = self.asset_template
        test_asset["name"] = ""

        self._check_sell_asset_exception(test_asset, ValueError)

    def test_sell_negative_unitprice(self) -> None:
        """sell asset with negative unit price argument

        should raise ValueError

        should not create a transaction record
        """

        test_asset = self.asset_template
        test_asset["unit_price"] = -1

        self._check_sell_asset_exception(test_asset, ValueError)

    def test_sell_negative_amount(self) -> None:
        """sell negative amount of asset

        should raise ValueError

        should not create a transaction record
        """

        test_asset = self.asset_template
        test_asset["amount"] = -10

        self._check_sell_asset_exception(test_asset, ValueError)

    def test_sell_empty_currency(self) -> None:
        """sell asset with empty string as currency argument

        should raise ValueError

        should not create a transaction record
        """

        test_asset = self.asset_template
        test_asset["currency"] = ""

        self._check_sell_asset_exception(test_asset, ValueError)


class TestTransactionsRecords(unittest.TestCase):
    def setUp(self) -> None:
        self.portfolio_controller = PortfolioController(Path("/"), "test")
        return super().setUp()

    def test_add_transaction_record(self) -> None:
        """create simple transaction record

        check for correct values with provided asset arguments"""

        transaction_type = "BUY"
        asset = {
            "code": "test",
            "unit_price": 10,
            "amount": 200,
            "currency": "USD",
        }

        self.portfolio_controller.add_transaction_record(
            type=transaction_type,
            code=asset["code"],
            unit_price=asset["unit_price"],
            amount=asset["amount"],
            currency=asset["currency"],
        )

        # get the transaction record
        transaction = self.portfolio_controller._portfolio.transactions[-1]

        # check if transaction record is correct
        self.assertEqual(transaction["type"], transaction_type)
        self.assertEqual(transaction["code"], asset["code"])
        self.assertEqual(transaction["unit_price"], asset["unit_price"])
        self.assertEqual(transaction["amount"], asset["amount"])
        self.assertEqual(transaction["currency"], asset["currency"])

    def test_add_mult_transactions(self) -> None:
        """create multiple transactions records

        check for correct values with provided asset arguments"""

        transaction_types = ("BUY", "SELL")

        asset = {
            "code": "test",
            "unit_price": 10,
            "amount": 200,
            "currency": "USD",
        }
        self.portfolio_controller.add_transaction_record(
            type=transaction_types[0],
            code=asset["code"],
            unit_price=asset["unit_price"],
            amount=asset["amount"],
            currency=asset["currency"],
        )

        self.portfolio_controller.add_transaction_record(
            type=transaction_types[1],
            code=asset["code"],
            unit_price=asset["unit_price"],
            amount=asset["amount"],
            currency=asset["currency"],
        )

        # check the transaction records
        t1 = self.portfolio_controller._portfolio.transactions[-1]
        t2 = self.portfolio_controller._portfolio.transactions[-2]

        self.assertEqual(t1["type"], transaction_types[1])
        self.assertEqual(t1["code"], asset["code"])
        self.assertEqual(t1["unit_price"], asset["unit_price"])
        self.assertEqual(t1["amount"], asset["amount"])
        self.assertEqual(t1["currency"], asset["currency"])

        self.assertEqual(t2["type"], transaction_types[0])
        self.assertEqual(t2["code"], asset["code"])
        self.assertEqual(t2["unit_price"], asset["unit_price"])
        self.assertEqual(t2["amount"], asset["amount"])
        self.assertEqual(t2["currency"], asset["currency"])

    def test_add_transaction_dates(self) -> None:
        """create multiple transactions records and check for date order

        subsequent transactions should have increasing dates"""

        asset = {
            "code": "test",
            "unit_price": 10,
            "amount": 200,
            "currency": "USD",
        }

        for _ in range(50):
            self.portfolio_controller.add_transaction_record(
                type="test",
                code=asset["code"],
                unit_price=asset["unit_price"],
                amount=asset["amount"],
                currency=asset["currency"],
            )

        # check if older transactions have older dates
        transactions = self.portfolio_controller._portfolio.transactions

        for i in range(len(transactions) - 1):
            self.assertLessEqual(
                transactions[i]["date"], transactions[i + 1]["date"]
            )


class TestPortfolioBalance(unittest.TestCase):
    def setUp(self) -> None:
        self.portfolio_controller = PortfolioController(Path("/"), "test")
        return super().setUp()

    def _check_update_balance(
        self, amount: int, currency: str, target_amount: int
    ) -> None:
        self.portfolio_controller.update_balance(amount, currency)
        self.assertEqual(
            self.portfolio_controller._portfolio.currencies[currency],
            target_amount,
        )

    def test_balance_empty_name(self) -> None:
        """update balance of empty name portfolio

        should raise ValueError
        """

        test_value, test_currency = 100, ""
        self.assertRaises(
            ValueError,
            self.portfolio_controller.update_balance,
            test_value,
            test_currency,
        )

    def test_balance_negative(self) -> None:
        """update balance by negative amount

        should decrease value
        """

        test_value, test_currency = -100, "USD"
        self._check_update_balance(test_value, test_currency, test_value)

    def test_balance_positive(self) -> None:
        """update balance by positive amount

        should increase value
        """

        test_value, test_currency = 100, "USD"
        self._check_update_balance(test_value, test_currency, test_value)

    def test_balance_zero(self) -> None:
        """update balance by zero

        should not change current value
        """

        test_value, test_currency = 0, "USD"
        self._check_update_balance(test_value, test_currency, test_value)

    def test_balance_multiple(self) -> None:
        """update balance multiple times

        should have valid amount
        """

        test_value, test_currency = 100, "USD"

        for i in range(1, 100):
            self._check_update_balance(
                test_value, test_currency, i * test_value
            )

        for i in range(98, -100, -1):
            self._check_update_balance(
                -test_value, test_currency, i * test_value
            )


if __name__ == "__main__":
    unittest.main()
