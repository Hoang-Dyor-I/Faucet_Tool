import sys
import threading
from unittest.mock import MagicMock, patch

# Mock requests before importing
sys.modules['requests'] = MagicMock()

from Sol.Sol_Devnet import get_proxy_dict, mask_proxy, request_faucet

def test_mask_proxy():
    # Valid 4-part proxy
    assert mask_proxy("192.168.1.1:8080:admin:secret") == "192.168.1.1:8080:***:***"

    # Invalid proxy (no credentials)
    assert mask_proxy("192.168.1.1:8080") == "***"

def test_get_proxy_dict():
    # Valid 4-part proxy
    proxy_str = "127.0.0.1:9000:user1:pass1"
    expected = {
        "http": "http://user1:pass1@127.0.0.1:9000",
        "https": "http://user1:pass1@127.0.0.1:9000"
    }
    assert get_proxy_dict(proxy_str) == expected

    # Invalid proxy (no credentials)
    assert get_proxy_dict("127.0.0.1:9000") is None

@patch('Sol.Sol_Devnet.time.sleep')
@patch('Sol.Sol_Devnet.requests.post')
def test_request_faucet_safely(mock_post, mock_sleep):
    # Test early return on invalid proxy
    request_faucet("wallet_abc", None)
    mock_post.assert_not_called()
    assert mock_sleep.called

    # Test valid proxy dict works and doesn't print raw traceback
    proxy_dict = {"http": "http://user:pass@host:port"}
    # Make request fail
    mock_post.side_effect = Exception("Internal Secret Error")

    # Capture print
    import io
    from contextlib import redirect_stdout
    f = io.StringIO()
    with redirect_stdout(f):
        request_faucet("wallet_abc", proxy_dict)

    output = f.getvalue()
    # Ensure raw error isn't leaked
    assert "Internal Secret Error" not in output
    # Ensure generic warning is printed
    assert "⚠️ Lỗi proxy hoặc kết nối" in output
