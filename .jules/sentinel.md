## 2024-05-27 - [Fix proxy credential leakage in logs]
**Vulnerability:** Proxy credentials (passwords) were being logged in plaintext to the console during normal operation and within unhandled exception strings.
**Learning:** Raw string concatenations and directly printing raw exception objects can silently leak credentials. `requests` error objects may contain the full proxy URL including credentials.
**Prevention:** Always parse and redact sensitive fields before logging. Use regex to sanitize exception messages (e.g., `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))`) and apply URL-encoding to credentials before constructing connection URLs to avoid injection.
