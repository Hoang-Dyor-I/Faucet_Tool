## 2024-07-16 - Hardcoded Proxy Credentials Logging & URL Injection
**Vulnerability:** Proxy credentials (username/password) were printed directly to console and also leaked via exception messages when `requests` failed. Additionally, passwords with special characters were not URL-encoded, causing invalid proxy configurations.
**Learning:** `requests` automatically includes proxy URLs with credentials in some exceptions, requiring masking. And URL encoding is vital for user inputs within URLs.
**Prevention:** Implement `mask_proxy` for standard logs, use regex string redaction for exception messages (e.g., `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`), and always `urllib.parse.quote` credentials before inserting them into a URL string.
