## 2024-05-24 - Proxies leaking credentials in error logs
**Vulnerability:** Proxy credentials (username/password) were passed unencoded to the `requests` library and exposed in plaintext in exception logs on network failure.
**Learning:** `requests` masks standard URLs but fails to mask embedded proxy credentials containing special characters correctly unless appropriately sanitized in exception handling.
**Prevention:** Sanitize raw exception strings using regex to mask passwords in proxy URLs before logging, and URL-encode proxy username/passwords before constructing proxy URLs.
