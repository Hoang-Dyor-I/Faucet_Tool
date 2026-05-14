import sys
import unittest
from unittest.mock import patch, mock_open, MagicMock

with patch('builtins.open', mock_open(read_data='dummy')), patch.dict('sys.modules', {'requests': MagicMock()}):
    import Sol_Devnet

class TestProxyFunctions(unittest.TestCase):
    def test_mask_proxy(self):
        self.assertEqual(Sol_Devnet.mask_proxy("127.0.0.1:8080:admin:secret"), "127.0.0.1:8080:admin:***")
        self.assertEqual(Sol_Devnet.mask_proxy("invalid"), "***")

    def test_get_proxy_dict(self):
        proxy = Sol_Devnet.get_proxy_dict("127.0.0.1:8080:admin@name:pass:word")
        self.assertIn("admin%40name", proxy["http"])
        self.assertIn("pass%3Aword", proxy["http"])
        self.assertIsNone(Sol_Devnet.get_proxy_dict("invalid"))

if __name__ == "__main__":
    unittest.main()
