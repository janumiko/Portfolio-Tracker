import unittest

from pathlib import Path

from src.controllers.file_handler import FileHandler
from tests.utility import create_empty_portfolio, rm_tree


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

    def tearDown(self) -> None:
        if self.testing_path.exists():
            rm_tree(self.testing_path)

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
        create_empty_portfolio(self.test_file_path)

        # add name:path to file handler dictionary
        self.file_handler._portfolios[
            self.test_file_name
        ] = self.test_file_path

        return super().setUp()

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
            rm_tree(self.testing_path)

        return super().tearDown()


class TestUploadFile(unittest.TestCase):
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
        create_empty_portfolio(self.test_file_path)

        return super().setUp()

    def test_upload_file(self):
        """upload file with provided unique valid name

        should create file with provided name
        """
        test_name = self.test_file_name + "uploaded"

        with open(self.test_file_path, "rb") as file:
            self.file_handler.upload_portfolio(test_name, file)

        self.assertTrue(
            Path(self.TEST_DATA_PATH + f"/{test_name}.json").exists()
        )

    def test_upload_file_exists(self):
        """upload file with provided name which exists already

        should raise FileExistsError
        """

        with open(self.test_file_path, "rb") as file:
            self.assertRaises(
                FileExistsError,
                self.file_handler.upload_portfolio,
                self.test_file_name,
                file,
            )

        self.assertTrue(
            Path(self.TEST_DATA_PATH + f"/{self.test_file_name}.json").exists()
        )

    def tearDown(self) -> None:
        if self.testing_path.exists():
            rm_tree(self.testing_path)

        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
