## 2024-05-24 - Exception Logging Leaks Credentials
**Vulnerability:** The unhandled exception logger in `request_faucet` exposed the plaintext proxy password by converting the `requests.exceptions.ProxyError` to a string which includes the proxy URL.
**Learning:** Python exception objects derived from network libraries often encapsulate full URLs with embedded credentials, making generic `print(e)` statements an unintentional leak path.
**Prevention:** Always sanitize exception messages involving network requests using regex (e.g., `re.sub(r'(://[^:]+:).*(@)', r'\1***\2', str(e))`) before logging to mask embedded credentials.
