import urllib.parse
import re

def mask_proxy(proxy_str):
    try:
        parts = proxy_str.split(":", 3)
        if len(parts) == 4:
            host, port, user, password = parts
            return f"{host}:{port}:{user}:***"
    except Exception:
        pass
    return proxy_str

def get_proxy_dict(proxy_str):
    parts = proxy_str.split(":", 3)
    if len(parts) != 4:
        return None
    host, port, user, password = parts
    user_enc = urllib.parse.quote(user, safe='')
    password_enc = urllib.parse.quote(password, safe='')
    proxy_auth = f"{user_enc}:{password_enc}@{host}:{port}"
    return {
        "http": f"http://{proxy_auth}",
        "https": f"http://{proxy_auth}"
    }

proxy = "1.2.3.4:8080:myuser:mypasswordwith:colon"
print(mask_proxy(proxy))
print(get_proxy_dict(proxy))

e = "ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 407 Proxy Authentication Required', urllib3.exceptions.ProxyError('Cannot connect to proxy http://myuser:mypasswordwith:colon@1.2.3.4:8080')))"
sanitized = re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))
print(sanitized)
