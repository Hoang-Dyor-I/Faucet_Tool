## 2024-06-18 - Sensitive Data Exposure in Logs and Errors
**Vulnerability:** Proxy credentials (`user:password`) and internal stack traces were exposed in console output upon script execution and during exceptions.
**Learning:** Generic exception handlers (`Exception as e`) and raw logging of proxy strings often expose internal configurations or credentials without explicit sanitization or filtering.
**Prevention:** Implement a standard masking or filtering layer for logging configurations, particularly credentials, and explicitly control exception outputs (e.g., catching specific errors or returning safe generic error strings like `type(e).__name__`).
