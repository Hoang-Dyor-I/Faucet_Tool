## 2024-06-20 - [Fix Credentials Exposure in Logs]
**Vulnerability:** Proxy credentials (passwords) were exposed in plaintext during console logging and unhandled exception stack traces.
**Learning:** Raw string interpolations of connection strings and full exception objects easily leak sensitive parameters like credentials when printed.
**Prevention:** Always mask sensitive parts of connection strings (e.g., splitting by colon) and sanitize exception messages via regex (e.g., `re.sub(r'(://[^:]+:).*(@)', r'\1***\2', str(e))`) before logging them.
