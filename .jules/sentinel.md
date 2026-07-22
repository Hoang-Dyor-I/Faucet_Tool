## 2024-05-18 - Credentials Leak in Request Exceptions
**Vulnerability:** Proxy credentials (username and password) were printed in plain text during proxy connection error handling and in initialization logs.
**Learning:** The `requests` library incorporates credentials in its internal error messages (e.g. `Connection refused for URL: http://user:pass@host`), which can expose plain text credentials when the exception `e` is logged.
**Prevention:** Always mask the password component using regex (e.g., `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`) before logging generic exceptions. Additionally, encode passwords using `urllib.parse.quote` for URL construction.
