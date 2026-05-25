## 2024-05-25 - Prevent Plaintext Credential Leaks in Logs
**Vulnerability:** Proxy credentials (passwords) were exposed in plain text in terminal output and exception logs.
**Learning:** Raw exception strings and formatted log strings often leak sensitive data when network connections fail or configurations are logged.
**Prevention:** Always mask credentials (e.g. using regex) before printing exception strings and use specialized formatting functions for logging sensitive connection details.
