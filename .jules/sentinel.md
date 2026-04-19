## 2024-04-19 - Stop Proxy Credentials Leakage in Logs and Error Handling
**Vulnerability:** Proxy credentials (user:pass) were being printed in plaintext to the console output, exceptions were exposing full stack traces to the logs, and proxy schemes defaulted to unencrypted `http://` for HTTPS.
**Learning:** Hardcoded or user-supplied strings containing sensitive information must be split or parsed and securely masked prior to printing. Generic error messages prevent internal information disclosure when connection issues occur.
**Prevention:** Always sanitize strings that contain authorization credentials before logging, use `https://` for secure connections, and catch exceptions securely using generic messages rather than printing the exception object directly.
