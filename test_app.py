
import unittest
from unittest.mock import MagicMock
from app import WebApp


class TestWebApp(unittest.TestCase):

    def test_homepage(self):
        handler = WebApp.__new__(WebApp)
        handler.wfile = MagicMock()
        handler.send_response = MagicMock()
        handler.send_header = MagicMock()
        handler.end_headers = MagicMock()

        handler.do_GET()

        handler.send_response.assert_called_once_with(200)
        handler.wfile.write.assert_called_once_with(
            b"<h1>Welcome to my DevOps CI/CD Pipeline!</h1>"
        )


if __name__ == "__main__":
    unittest.main()
