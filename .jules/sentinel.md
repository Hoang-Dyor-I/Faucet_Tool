## 2024-05-20 - Prevent Sensitive Data Exposure in Logs
**Vulnerability:** Proxy credentials (passwords) and raw exception objects were being logged directly to standard output, exposing sensitive information.
**Learning:** It is crucial to redact sensitive information such as proxy passwords before logging and to catch exceptions safely without revealing internal implementation details or stack traces.
**Prevention:** Always implement a redaction mechanism (e.g., `mask_proxy`) for sensitive strings before logging, and use generic error messages or extract only safe parts of an exception (e.g., `type(e).__name__`) when handling errors.
