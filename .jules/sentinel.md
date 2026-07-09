## 2024-07-09 - Credentials Leak in Console Logs and Exception Strings
**Vulnerability:** Proxy credentials (username/password) were printed in plain text to the console during normal operation and could be leaked in `requests` exception stack traces.
**Learning:** Raw proxy string logs and unhandled third-party exception messages (like `requests.exceptions.ProxyError`) inherently expose sensitive authentication materials embedded in the URL.
**Prevention:** Mask passwords in strings before logging, explicitly parse and URL-encode credentials to avoid parsing vulnerabilities, and sanitize exception messages via regex (e.g., `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`) before output.
