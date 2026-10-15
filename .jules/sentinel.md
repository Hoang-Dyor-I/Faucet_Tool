## 2024-05-24 - Unmasked Proxy Credentials Logging
**Vulnerability:** Proxy credentials (username and password) were being logged in plaintext to the console during iteration and within raw exception objects when `requests` failed.
**Learning:** Python's `requests` library includes proxy credentials in exception strings when a proxy connection fails, and simple print statements of proxy configuration strings leak secrets.
**Prevention:** Always mask proxy/URL passwords before logging (e.g., using a masking function for config strings and regex replacement for exception messages), and ensure credentials are URL-encoded when constructing proxy URIs.
