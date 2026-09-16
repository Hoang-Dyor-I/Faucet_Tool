## 2024-05-24 - Masking Sensitive Proxy Credentials and URL Encoding
**Vulnerability:** Proxy credentials (passwords) are logged in plaintext to the console and exposed in raw exception messages. Additionally, passwords with special characters are not URL-encoded.
**Learning:** Sensitive proxy credentials used in requests can be inadvertently exposed through raw exception tracebacks and loop logs if not explicitly sanitized. Furthermore, failing to URL-encode proxy credentials risks malformed URLs.
**Prevention:** Implement proxy password masking before logging to console or printing exception objects using regex (e.g., `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))`), and always use `urllib.parse.quote(value, safe='')` for credentials during URL construction.
