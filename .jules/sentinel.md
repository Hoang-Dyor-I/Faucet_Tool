## 2024-04-12 - Prevent Credential Leak in Logs and Secure Error Handling
**Vulnerability:** Proxy credentials (username/password) were logged in plain text, and raw exceptions were printed which could expose internal stack traces or sensitive data.
**Learning:** Always validate and sanitize sensitive data strings before logging (e.g., masking credentials). Catch blocks must genericize errors to avoid information disclosure.
**Prevention:** Implement masking helpers for credentials before logging, validate object properties format, and log only generic exceptions like `type(e).__name__`.
