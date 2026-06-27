## 2024-05-24 - Mask Proxy Credentials in Console Logs
**Vulnerability:** Proxy passwords were leaked in plain text to the console during normal operation and exception handling.
**Learning:** Always sanitize configuration strings and exception tracebacks before logging, as exceptions (like from `requests`) may embed URLs containing raw credentials.
**Prevention:** Use a dedicated string masking function and regex substitution (`re.sub`) for error messages to sanitize outputs before printing them.
