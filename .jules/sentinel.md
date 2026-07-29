## 2024-07-29 - Credentials Leaked via Exception Logging
**Vulnerability:** Raw string representations of Python exceptions from HTTP libraries like `requests` often contain URLs with plaintext proxy/auth credentials, leading to accidental credential leakage in logs when exceptions are printed directly.
**Learning:** Security risks extend beyond hardcoded secrets or deliberate logging statements; underlying libraries can embed sensitive connection context within their error messages.
**Prevention:** Always sanitize exception strings using regex (e.g., matching URL authority structures to mask passwords) before logging them, especially in network-heavy scripts handling proxies or authentication.
