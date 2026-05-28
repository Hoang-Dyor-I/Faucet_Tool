## 2024-05-28 - Secure Credential Logging and URL Encoding
**Vulnerability:** Proxy credentials (username and password) were logged in plain text and could be exposed in raw exception messages. Proxy user/passwords were also not correctly percent-encoded, which could lead to URL injection issues.
**Learning:** In network operations handling authenticated proxy configurations, raw exception outputs from libraries like `requests` can leak credentials within URLs. Hardcoded string concatenation without URL encoding can easily break when special characters are used in passwords.
**Prevention:** Always mask proxy passwords before printing. Use regex `re.sub` to sanitize exception messages containing URLs. Use `urllib.parse.quote` to properly percent-encode proxy user credentials.
