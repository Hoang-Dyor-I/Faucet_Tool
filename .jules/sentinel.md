## 2024-05-16 - Prevent proxy credential exposure and command injection
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext. Proxy credentials with special characters were not URL-encoded, potentially leading to errors or URL injection vulnerabilities.
**Learning:** Failing to sanitize proxy connection strings and not masking them before logging can expose secrets and allow malformed credentials to break parsing or requests.
**Prevention:** Always mask proxy passwords before logging. Use maxsplit when parsing proxy strings to avoid breaking on passwords with colons. Always URL-encode usernames and passwords inside proxy connection URLs using urllib.parse.quote.
