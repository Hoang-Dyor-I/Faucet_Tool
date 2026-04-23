## 2024-05-20 - Exposing proxy credentials and IP leaks
**Vulnerability:** Proxy credentials (username/password) logged in plaintext and malformed proxies crash proxy generation, falling back to direct connection which leaks IP.
**Learning:** Always mask sensitive parts of connection strings before logging and gracefully handle malformed configurations by returning safe defaults (like None) and aborting early.
**Prevention:** Use a dedicated parsing function that masks credentials for logging and ensures strict format validation before passing the proxy dictionary to requests.
