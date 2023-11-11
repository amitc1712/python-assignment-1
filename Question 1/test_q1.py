import unittest
from unittest.mock import patch, MagicMock
from mysql import connector
from main import DBHelper


class TestDBHelper(unittest.TestCase):
    """
    Test the datbase connection using a Mock test
    """

    @patch.object(connector, "connect")
    def test_db_connection(self, mock_connect):
        mock_connect.return_value = MagicMock()
        config_file = "test_config.ini"
        db_helper = DBHelper(config_file)

        connection = db_helper.con

        mock_connect.assert_called_once_with(**db_helper.config["database"])
        self.assertIsNotNone(connection)


if __name__ == "__main__":
    unittest.main()
