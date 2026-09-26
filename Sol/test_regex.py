import re
import urllib.parse

def test():
    user = "jules"
    password = "password@123:"
    host = "1.2.3.4"
    port = "8080"

    user_enc = urllib.parse.quote(user, safe='')
    password_enc = urllib.parse.quote(password, safe='')
    proxy_auth = f"{user_enc}:{password_enc}@{host}:{port}"
    url = f"http://{proxy_auth}"

    # Simulate exception message containing the url
    e_str = f"HTTPSConnectionPool(host='api.devnet.solana.com', port=443): Max retries exceeded with url: / (Caused by ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 407 Proxy Authentication Required'))) -- proxy was {url}"

    sanitized_error = re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', e_str)
    print(f"Original: {e_str}")
    print(f"Sanitized: {sanitized_error}")

test()
