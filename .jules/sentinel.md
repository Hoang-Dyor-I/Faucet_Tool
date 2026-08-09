## 2024-08-09 - Stop Leaking Proxy Credentials in Exceptions and Console Logs
**Vulnerability:** Proxy passwords were being exposed in plaintext in console output when switching proxies, and leaked via `requests` module exception messages on connection failures.
**Learning:** `requests` automatically percent-encodes credentials in exception strings, so standard regex sanitizers might fail to mask URL-encoded passwords. Also, global variables for proxies were leading to unmasked access in multiple functions.
**Prevention:** Always use safe parsing (`maxsplit`, `urllib.parse.quote`) when building proxy strings, mask credentials before logging, and apply regex sanitization `re.sub(r'(://[^:@/]+:)[^:@/]+(@)', r'\1***\2', str(e))` to exceptions to prevent inadvertent leaks.
