## 2023-10-24 - Prevent Credential Leakage in Logs and Exceptions
**Vulnerability:** Proxy credentials (username and password) were exposed in plaintext in console logs when printing proxy configuration, and potentially in full exception traces when connection errors occurred.
**Learning:** Raw proxy strings and full exception objects can contain sensitive basic auth credentials. Printing them directly without sanitization exposes secrets to logs.
**Prevention:** Always implement a `mask_proxy` function to redact passwords before logging proxy strings. Sanitize exception messages using regex (e.g., `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))`) before logging to mask passwords.
