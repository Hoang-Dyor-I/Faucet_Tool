## 2024-05-24 - Mask Sensitive Proxy Credentials in Logs
**Vulnerability:** Proxy credentials (username and password) were exposed in plaintext in standard output when logging proxy usage and during connection exception traces.
**Learning:** Python `requests` library might leak the constructed proxy auth string if connection exceptions are printed raw without sanitization. Additionally, custom formatted strings often contain sensitive data that developers forget to mask during routine prints.
**Prevention:** Always sanitize proxy strings before printing them and use non-greedy regex replacing (`re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`) for exception messages to mask credentials while preserving context.
