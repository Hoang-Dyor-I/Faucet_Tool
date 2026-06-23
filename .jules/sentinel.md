## 2024-06-23 - Prevent Proxy Credentials Leak in Logs
**Vulnerability:** Raw proxy strings containing plaintext passwords were logged directly to the console, and unhandled exception traces exposed formatted URLs with embedded credentials.
**Learning:** Using generic logging/printing for structured connection strings or printing raw exceptions easily leaks secrets. Any credential string mapping should securely mask the fields before reaching the stdout.
**Prevention:** Implement `mask_proxy` for formatted log statements, pre-parse connections safely with URL-encoding for special characters, and sanitize exception messages via `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))` before logging.
