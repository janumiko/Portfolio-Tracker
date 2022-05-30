import unittest

from pathlib import Path

from src.controllers.file_handler import FileHandler


class TestCreatePortfolio(unittest.TestCase):
    def setUp(self) -> None:
        self.TEST_DATA_PATH = "tests/test_data"
        self.testing_path = Path(self.TEST_DATA_PATH)

        # create directory if does not exist
        self.testing_path.mkdir(exist_ok=True)

        self.file_handler = FileHandler(self.testing_path)

        return super().setUp()

    def test_create_valid(self) -> None:
        """create portfolio with valid name

        should create file in provided data_path
        """

        test_portf_name = "test"
        self.file_handler.create_empty_portfolio(test_portf_name)

        self.assertTrue(
            Path(
                self.TEST_DATA_PATH + "/" + test_portf_name + ".json"
            ).is_file()
        )

    def test_create_empty_name(self) -> None:
        """create portfolio with empty name

        should raise ValueError
        """

        test_portf_name = ""

        self.assertRaises(
            ValueError,
            self.file_handler.create_empty_portfolio,
            test_portf_name,
        )

        self.assertFalse(
            Path(
                self.TEST_DATA_PATH + "/" + test_portf_name + ".json"
            ).is_file()
        )

    def _rm_tree(self, path: Path) -> None:
        """remove directory with all files inside"""

        for child in path.iterdir():
            if child.is_file():
                child.unlink()
            else:
                self._rm_tree(child)
        path.rmdir()

    def tearDown(self) -> None:
        if self.testing_path.exists():
            self._rm_tree(self.testing_path)

        return super().tearDown()


class TestRemovePortfolio(unittest.TestCase):
    def setUp(self) -> None:
        self.TEST_DATA_PATH = "tests/test_data"
        self.testing_path = Path(self.TEST_DATA_PATH)

        # create directory if does not exist
        self.testing_path.mkdir(exist_ok=True)

        self.test_file_name = "test"
        self.test_file_path = Path(
            self.TEST_DATA_PATH + f"/{self.test_file_name}.json"
        )

        self.file_handler = FileHandler(self.testing_path)

        # create test portfolio file
        self._create_empty_file()

        # add name:path to file handler dictionary
        self.file_handler._portfolios[
            self.test_file_name
        ] = self.test_file_path

        return super().setUp()

    def _create_empty_file(self) -> None:
        with open(self.test_file_path, "w", encoding="utf-8") as file:
            file.write("")

    def _rm_tree(self, path: Path) -> None:
        """remove directory with all files inside"""

        for child in path.iterdir():
            if child.is_file():
                child.unlink()
            else:
                self._rm_tree(child)
        path.rmdir()

    def test_remove_file(self) -> None:
        """remove existing portfolio

        should remove file in provided name
        """
        self.file_handler.remove_portfolio(self.test_file_name)
        self.assertFalse(self.test_file_path.exists())

    def test_remove_empty_name(self) -> None:
        """remove portfolio with empty name

        should raise ValueError
        """

        test_portf_name = ""

        self.assertRaises(
            ValueError,
            self.file_handler.remove_portfolio,
            test_portf_name,
        )

        self.assertTrue(self.test_file_path.exists())

    def test_remove_nonexisting(self) -> None:
        """remove non existing portfolio file

        should raise FileNotFoundError
        """

        self.assertRaises(
            FileNotFoundError,
            self.file_handler.remove_portfolio,
            self.test_file_name + "a",
        )

        self.assertTrue(self.test_file_path.exists())

    def tearDown(self) -> None:
        if self.testing_path.exists():
            self._rm_tree(self.testing_path)

        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
