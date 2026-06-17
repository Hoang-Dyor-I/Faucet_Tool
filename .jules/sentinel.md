## 2024-06-17 - Prevent Plaintext Credential Logging in Proxy Exceptions
**Vulnerability:** Proxy passwords were leaked in plaintext both directly when logging the proxy list string and within exception messages thrown by the requests library when proxy connections failed.
**Learning:** Even when printing high-level objects like standard exception strings, underlying libraries (like `requests`) might leak sensitive details embedded in URLs unless specifically sanitized.
**Prevention:** Always sanitize exception strings using regex (e.g., masking the password part of the URL) and parse sensitive strings to explicitly mask credentials before console logging.
