## 2023-10-24 - Credentials Leakage in Logs and Exceptions
**Vulnerability:** Plaintext proxy credentials (passwords) were exposed in standard output, and could be leaked in full URL formats during unhandled `requests` exception stack traces.
**Learning:** Raw proxy strings and exception objects contain sensitive data. Printing them directly inadvertently exposes credentials.
**Prevention:** Always parse sensitive strings to isolate and mask credentials before logging, and use robust regex sanitization to mask passwords in error messages.
