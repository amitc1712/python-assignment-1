import unittest
from unittest.mock import patch, Mock
from main import anti_html


class TestAntiHtml(unittest.TestCase):
    @patch("requests.get")
    def test_anti_html(self, mock_get):
        mock_response = Mock()
        mock_response.content = "<html><body><h1>Hello, World!</h1></body></html>"
        mock_get.return_value = mock_response

        result = anti_html("https://www.example.com")

        self.assertEqual(result, "Hello, World!")

    @patch("requests.get")
    def test_anti_html_no_content(self, mock_get):
        mock_response = Mock()
        mock_response.content = ""
        mock_get.return_value = mock_response

        result = anti_html("https://www.example.com")

        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
