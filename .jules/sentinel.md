## 2024-07-05 - Redact Proxy Passwords and URL Encoding
**Vulnerability:** Proxy credentials (username and password) were printed in plaintext during exceptions from the requests module and proxy string was split incorrectly leading to password truncation. Password was not URL encoded leading to potential injections.
**Learning:** The `requests` library logs full URLs in exception messages including plaintext credentials. Split proxy with maxsplit=3 to prevent password truncation if it has colons. URL encoding is necessary to make credentials safe in URL format.
**Prevention:** Use regex to redact credentials from exceptions (`re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`). URL encode proxy username and password before constructing the proxy connection string.
