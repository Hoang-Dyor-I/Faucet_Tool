## 2025-01-20 - Prevent Credential Leak in Proxy Config Logging
**Vulnerability:** Proxy credentials (username and password) were printed directly to console and inadvertently leaked via `requests` exception strings, and special characters were not URL-encoded causing injection-like bugs.
**Learning:** Using raw proxy strings with passwords in logging or exception handling is highly prone to credential leaks.
**Prevention:** Always percent-encode proxy credentials, sanitize exception error messages with regex, and explicitly mask sensitive sections of proxy configurations before logging.
