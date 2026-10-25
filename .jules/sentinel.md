## 2024-05-24 - Mask Proxy Credentials in Error Logs
**Vulnerability:** The script logs full `requests` exceptions which inherently leak plain-text proxy credentials (username/password) embedded in the proxy URL on connection errors.
**Learning:** The `requests` library incorporates connection parameters (like proxy URLs) into exception stack traces to aid debugging, which inadvertently exposes secrets unless sanitized or masked before logging.
**Prevention:** Sanitize exception error messages using regex to mask passwords in proxy connection URLs or avoid logging raw, unhandled exceptions entirely.
