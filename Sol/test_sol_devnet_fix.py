import unittest
from unittest.mock import patch, MagicMock
import sys
import urllib.parse

sys.modules['requests'] = MagicMock()

import Sol_Devnet

class TestSolDevnetSecurity(unittest.TestCase):
    def test_mask_proxy(self):
        proxy = "127.0.0.1:8080:user:secret123"
        masked = Sol_Devnet.mask_proxy(proxy)
        self.assertEqual(masked, "127.0.0.1:8080:user:***")

    def test_get_proxy_dict_encoding(self):
        proxy = "127.0.0.1:8080:user@name:pass:word"
        result = Sol_Devnet.get_proxy_dict(proxy)
        user_enc = urllib.parse.quote("user@name", safe='')
        pass_enc = urllib.parse.quote("pass:word", safe='')
        expected_url = f"http://{user_enc}:{pass_enc}@127.0.0.1:8080"
        self.assertEqual(result["http"], expected_url)

    def test_get_proxy_dict_malformed(self):
        proxy = "invalid_proxy"
        self.assertIsNone(Sol_Devnet.get_proxy_dict(proxy))

    @patch('builtins.print')
    def test_request_faucet_exception_logging(self, mock_print):
        proxy_dict = {"http": "http://user:secretpass@127.0.0.1:8080"}
        sys.modules['requests'].post.side_effect = Exception("ProxyError: Cannot connect to http://user:secretpass@127.0.0.1:8080")
        with patch('time.sleep'):
            Sol_Devnet.request_faucet("dummy_wallet", proxy_dict)

        # Verify print output does not contain the password
        print_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Lỗi proxy" in call for call in print_calls))
        self.assertFalse(any("secretpass" in call for call in print_calls))

if __name__ == '__main__':
    unittest.main()
