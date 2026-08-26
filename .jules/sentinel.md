## 2024-08-26 - Prevent credential leakage in logs and exceptions
**Vulnerability:** Proxy credentials (username and password) were logged in plaintext in standard output and exception messages. Passwords with special characters were improperly handled and lacked URL encoding.
**Learning:** Raw string formatting and printing exception objects without sanitization can expose embedded secrets in URLs or proxy strings.
**Prevention:** Always mask credentials before logging using maxsplit=3, use URL encoding for credentials with special characters, and apply regex sanitization for exceptions containing URLs.
