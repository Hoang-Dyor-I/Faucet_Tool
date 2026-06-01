## 2024-06-01 - Prevent Credential Exposure in Logs and Exceptions
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext directly to the console during normal operation and via leaked exception strings. In addition, credentials were not percent-encoded, which could lead to URL injection or parsing errors.
**Learning:** Python `requests` exceptions can leak full URLs including Basic Auth credentials if not explicitly sanitized, and `print` statements of configuration strings often leak passwords.
**Prevention:** Use regex `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))` to sanitize exception objects, and create explicit masking functions for configuration strings before logging. Use `urllib.parse.quote` for encoding credentials when building URLs.
