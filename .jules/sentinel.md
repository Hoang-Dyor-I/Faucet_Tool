## 2024-10-06 - Credential Exposure in Proxy Logging
**Vulnerability:** Proxy passwords and credentials were exposed in plaintext when logging raw proxy strings and exception objects (via `requests` errors).
**Learning:** Raw exception strings from network libraries can leak sensitive URLs containing credentials. Proxy strings should be parsed carefully to support special characters.
**Prevention:** Always mask credentials in logging and sanitize exception strings using regex. Pre-parse and percent-encode credentials using `urllib.parse.quote`.
