## 2024-06-14 - Prevent Credential Leakage in Proxy Configuration
**Vulnerability:** Proxy passwords, sometimes containing colons, were logged to console in plaintext and exposed through requests exception messages.
**Learning:** Raw exception strings from HTTP clients like `requests` can encapsulate the request URL, leaking proxy credentials in plaintext (e.g. `http://user:pass@host:port`).
**Prevention:** Always mask credentials via Regex before logging exceptions, and encode proxy credentials explicitly using URL-safe formats.
