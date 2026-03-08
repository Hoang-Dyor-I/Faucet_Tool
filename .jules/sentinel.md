## 2024-05-24 - [Fix sensitive credential exposure in logs]
**Vulnerability:** Proxy credentials (including username and password) were being logged in plain text to the console, and unhandled exception objects which might contain sensitive internal details were being printed directly to error logs.
**Learning:** Raw string inputs that contain sensitive configuration data (like `host:port:user:pass`) and raw error objects from standard libraries must be sanitized before logging to prevent credential leakage or internal information exposure.
**Prevention:** Always parse or split sensitive strings (e.g. proxy configurations) to isolate and mask the credential portion (`user:pass`) before logging. Use safe, generic error messages instead of printing full exception objects directly.
