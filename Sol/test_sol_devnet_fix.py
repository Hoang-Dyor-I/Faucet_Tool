import unittest
from unittest.mock import patch, MagicMock
import sys
import re

sys.modules['requests'] = MagicMock()

from Sol_Devnet import get_proxy_dict, mask_proxy, request_faucet, main, read_lines

class TestSolDevnet(unittest.TestCase):
    def test_mask_proxy(self):
        self.assertEqual(mask_proxy("1.2.3.4:8080:user:pass:word"), "1.2.3.4:8080:user:***")
        self.assertEqual(mask_proxy("invalid"), "invalid")

    def test_get_proxy_dict(self):
        proxy = get_proxy_dict("1.2.3.4:8080:user:pass:word")
        self.assertIsNotNone(proxy)
        self.assertIn("user:pass%3Aword", proxy["http"])
        self.assertIsNone(get_proxy_dict("invalid"))

    @patch('Sol_Devnet.requests.post')
    @patch('builtins.print')
    def test_request_faucet_exception(self, mock_print, mock_post):
        mock_post.side_effect = Exception("ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 407 Proxy Authentication Required'))) for proxy url: http://user:p%40ssw%3Ard@1.2.3.4:8080")

        proxy_dict = {"http": "http://user:p%40ssw%3Ard@1.2.3.4:8080", "https": "http://user:p%40ssw%3Ard@1.2.3.4:8080"}
        request_faucet("wallet_abc", proxy_dict)

        printed_msg = mock_print.call_args[0][0]
        self.assertIn("user:***@1.2.3.4:8080", printed_msg)
        self.assertNotIn("p%40ssw%3Ard", printed_msg)

if __name__ == '__main__':
    unittest.main()
