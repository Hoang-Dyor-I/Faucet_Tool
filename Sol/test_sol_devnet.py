import sys
from unittest.mock import MagicMock, patch
import pytest
import io
import time
import random

# Mock requests
sys.modules['requests'] = MagicMock()

import Sol.Sol_Devnet as sol

def test_get_proxy_dict():
    # 4 parts
    res = sol.get_proxy_dict("1.2.3.4:8080:user:pass")
    assert res == {"http": "http://user:pass@1.2.3.4:8080", "https": "http://user:pass@1.2.3.4:8080"}

    # 2 parts
    res = sol.get_proxy_dict("1.2.3.4:8080")
    assert res == {"http": "http://1.2.3.4:8080", "https": "http://1.2.3.4:8080"}

    # invalid
    assert sol.get_proxy_dict("1.2.3.4") is None

@patch('Sol.Sol_Devnet.time.sleep')
def test_request_faucet_abort_on_none_proxy(mock_sleep):
    sys.modules['requests'].post.reset_mock()
    sol.request_faucet("wallet1", "invalid_proxy")
    sys.modules['requests'].post.assert_not_called()
    mock_sleep.assert_called_once()

@patch('Sol.Sol_Devnet.time.sleep')
@patch('sys.stdout', new_callable=io.StringIO)
def test_request_faucet_no_exception_leak(mock_stdout, mock_sleep):
    sys.modules['requests'].post.side_effect = Exception("Secret API Error 12345")
    sol.request_faucet("wallet1", "1.2.3.4:8080")
    output = mock_stdout.getvalue()
    assert "Secret API Error 12345" not in output
    assert "⚠️ Lỗi proxy hoặc kết nối cho wallet1" in output
