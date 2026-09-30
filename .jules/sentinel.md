## 2024-09-30 - Sensitive Data Exposure in Proxy Credentials
**Vulnerability:** The Solana devnet bot logs raw proxy strings and unhandled requests exceptions which leak plaintext proxy passwords (including those in the URL) to standard output.
**Learning:** Incomplete log sanitization and exception handling without URL-encoding user credentials can result in secrets exposure in logs/tracebacks.
**Prevention:** Implement `mask_proxy` for standard logs, explicitly url-encode proxy credentials when constructing the proxy dict, and use regex replacements to sanitize full `Exception` tracebacks and messages containing credentials before logging.
