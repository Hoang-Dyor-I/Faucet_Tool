## 2024-05-24 - Masking Credentials in Logs and Error Messages
**Vulnerability:** Proxy credentials (username and password) were exposed in plaintext via console logs and exception stack traces, and were vulnerable to injection due to missing URL encoding.
**Learning:** Raw exception strings from `requests` will dump the request URL including inline proxy credentials if a connection fails. Unencoded special characters in proxy passwords can also break URL parsing.
**Prevention:** Always URL-encode credentials using `urllib.parse.quote` before constructing URLs, and apply regex sanitization (e.g., `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`) to mask passwords before logging exception messages.
