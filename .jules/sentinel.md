## 2024-03-10 - Secure Proxy Configuration and Exception Logging
**Vulnerability:** The script previously printed raw proxy configurations, including plaintext usernames and passwords, directly to the console during execution. Exception blocks also printed the raw error object, potentially leaking proxy URLs and credentials.
**Learning:** Logging configuration details and full exception objects can inadvertently leak sensitive authentication details embedded within connection strings (like proxies).
**Prevention:** Always parse or split sensitive strings to isolate and mask credentials before logging. Use safe, generic error messages instead of printing full exception objects to prevent internal information exposure.
