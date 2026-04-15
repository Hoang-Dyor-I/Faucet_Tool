
## 2024-04-15 - [Exposed Proxy Credentials in Logs]
**Vulnerability:** Proxy credentials (user:password) in the format `host:port:user:password` were printed directly to console output and exposed in exception traceback string representations when network errors occurred.
**Learning:** Raw proxy connection strings containing authentication were used directly in formatted strings and passed directly to exceptions, making it easy to accidentally log secrets.
**Prevention:** Implement a credential masking function (e.g., `mask_proxy`) before printing any formatted strings containing credentials. Never print the raw exception object `e` directly in network error catching blocks; use `type(e).__name__` or safe generic strings instead to prevent leaking the full connection URL.
