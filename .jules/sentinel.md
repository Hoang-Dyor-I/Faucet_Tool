## 2024-04-18 - [Exposed Sensitive Data in Logs]
**Vulnerability:** Raw proxy strings containing `user:password` and raw exceptions/HTTP responses were printed to standard output.
**Learning:** Hardcoded print statements without credential masking or sanitization will inevitably leak secrets and internal application state to external logs.
**Prevention:** Implement secure logging wrappers that sanitize inputs (e.g., masking credentials based on expected format) and use generic error messages for the user-facing output while keeping detailed traces strictly in secure logs.
