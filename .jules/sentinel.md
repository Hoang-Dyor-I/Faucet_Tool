## 2024-06-03 - Prevent Credential Leakage in Proxy Logs
**Vulnerability:** Proxy passwords, including those with special characters, could be leaked in plaintext through unhandled exception logs or direct console printing when using the `requests` library.
**Learning:** `requests` automatically includes proxy URLs (including credentials) in exception strings. We must sanitize these logs and percent-encode credentials during URL construction.
**Prevention:** Implement regex sanitization for error logs and use URL-encoding for credentials. Mask passwords before logging proxy strings.
