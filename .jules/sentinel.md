## 2024-05-21 - Sensitive Data Exposure in Logs
**Vulnerability:** Proxy passwords (credentials) were printed in plain text to standard output via generic print statements and exception messages.
**Learning:** Hardcoded `print` statements during iterative processes can leak secrets if objects containing credentials are not sanitized. In Python, raw exception output can include HTTP proxy URLs with embedded plaintext passwords.
**Prevention:** Always mask credentials before logging. Use regex to sanitize exception output when interacting with libraries like `requests` using authenticated proxies. Encapsulate script initialization in main blocks.
