## 2024-05-24 - Credential Exposure in Logs and Exception Handling
**Vulnerability:** Proxy credentials (passwords) were exposed in plaintext in standard output logs and exception stack traces when `requests` failed.
**Learning:** Raw exception strings and directly printed strings often contain unmasked sensitive data, especially when connection errors echo back URLs with credentials.
**Prevention:** Always implement a dedicated masking function (e.g., regex redaction) before logging variables or exception objects that may contain secrets.
