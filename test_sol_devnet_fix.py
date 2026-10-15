import urllib.parse
import re

def get_proxy_dict(proxy_str):
    parts = proxy_str.split(":", 3)
    if len(parts) != 4:
        return None
    host, port, user, password = parts
    user_encoded = urllib.parse.quote(user, safe='')
    password_encoded = urllib.parse.quote(password, safe='')
    proxy_auth = f"{user_encoded}:{password_encoded}@{host}:{port}"
    return {
        "http": f"http://{proxy_auth}",
        "https": f"http://{proxy_auth}"
    }

def mask_proxy(proxy_str):
    parts = proxy_str.split(":", 3)
    if len(parts) == 4:
        return f"{parts[0]}:{parts[1]}:{parts[2]}:***"
    return proxy_str

def test_mask_proxy():
    proxy = "1.2.3.4:8080:user:pass123"
    assert mask_proxy(proxy) == "1.2.3.4:8080:user:***"

def test_regex():
    e = "Connection to http://user:pass123@1.2.3.4:8080 failed"
    masked = re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', e)
    assert masked == "Connection to http://user:***@1.2.3.4:8080 failed"

def test_url_encode():
    proxy = "1.2.3.4:8080:user@name:pass:word"
    d = get_proxy_dict(proxy)
    assert d["http"] == "http://user%40name:pass%3Aword@1.2.3.4:8080"

test_mask_proxy()
test_regex()
test_url_encode()
print("All tests passed.")
