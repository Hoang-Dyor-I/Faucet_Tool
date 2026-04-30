## 2024-04-30 - Fix Exposed sensitive data in logs
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext, and full exception stack traces were printed to stdout. Malformed proxies could also crash the loop.
**Learning:** Network configuration loops often log full strings by default, exposing embedded credentials. Broad exception catching that prints the exception object can leak internal application state.
**Prevention:** Implement a dedicated function to mask sensitive strings before logging. Pre-parse configurations safely to reject malformed input. Use generic error messages instead of printing raw exception objects.
