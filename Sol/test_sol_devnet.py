import unittest
from unittest.mock import patch, MagicMock
import sys

sys.modules['requests'] = MagicMock()
import Sol_Devnet

# Avoid FileNotFoundError when importing module
Sol_Devnet.wallets = []
Sol_Devnet.proxies = []

class TestSolDevnet(unittest.TestCase):
    def test_mask_proxy(self):
        self.assertEqual(Sol_Devnet.mask_proxy("1.2.3.4:8080:user:pass"), "1.2.3.4:8080:***:***")
        self.assertEqual(Sol_Devnet.mask_proxy("invalid_proxy"), "invalid_proxy")

    def test_get_proxy_dict(self):
        valid = Sol_Devnet.get_proxy_dict("1.2.3.4:8080:user:pass")
        self.assertEqual(valid["http"], "http://user:pass@1.2.3.4:8080")

        invalid = Sol_Devnet.get_proxy_dict("1.2.3.4:8080")
        self.assertIsNone(invalid)

    @patch('Sol_Devnet.requests.post')
    def test_request_faucet_invalid_proxy(self, mock_post):
        # Should return early without calling requests.post
        Sol_Devnet.request_faucet("wallet_addr", "invalid_proxy")
        mock_post.assert_not_called()

if __name__ == '__main__':
    unittest.main()
