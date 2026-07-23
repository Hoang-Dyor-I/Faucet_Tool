import re
import urllib.parse
import threading
import time
import random
from unittest.mock import MagicMock, patch

import Sol.Sol_Devnet as Sol_Devnet

# We will mock requests to test
with patch('requests.post') as mock_post:
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": "ok"}
    mock_post.return_value = mock_response

    proxy_dict = {
        "http": "http://user%40name:p%40ssword@127.0.0.1:8080",
        "https": "http://user%40name:p%40ssword@127.0.0.1:8080"
    }

    # Should not raise
    Sol_Devnet.request_faucet("wallet1", proxy_dict)

    # Test Exception logging
    mock_post.side_effect = Exception("ProxyError: Cannot connect to proxy. URL: http://user:p@ssword123!@127.0.0.1:8080")
    Sol_Devnet.request_faucet("wallet2", proxy_dict)

print("Test complete.")
