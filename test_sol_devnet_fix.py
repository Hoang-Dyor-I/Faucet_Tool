import unittest
from unittest.mock import patch, MagicMock
import sys
import re

# Mock requests
sys.modules['requests'] = MagicMock()

# Mock builtins.open
mock_open = unittest.mock.mock_open(read_data="dummy\n")
with patch('builtins.open', mock_open):
    import Sol.Sol_Devnet as sol

class TestSecurityFix(unittest.TestCase):
    def test_regex_masking(self):
        # The password includes %21%40 for !@
        e_str = "ProxyError: Tunnel connection failed: 407 Proxy Authentication Required for http://usr:pwd%21%40@127.0.0.1:8080"
        safe_e = re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', e_str)
        self.assertNotIn('pwd%21%40', safe_e)
        self.assertIn('http://usr:***@127.0.0.1:8080', safe_e)

if __name__ == '__main__':
    unittest.main()
