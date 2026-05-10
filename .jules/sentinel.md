## 2024-05-10 - Credential and Internal State Leakage
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext, and full exception objects were printed to standard output upon connection errors.
**Learning:** In automated scripts, iterative network calls often use authenticated proxies. Printing the raw proxy configuration exposes credentials in the CI/CD pipeline or local console. Similarly, printing `Exception` objects can leak internal stack or environmental context.
**Prevention:** Always parse and sanitize (e.g., replace password with `***`) proxy strings before logging. Use generic, safe error messages in `except` blocks instead of formatting the exception object itself.
