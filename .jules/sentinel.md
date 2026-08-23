## 2024-08-23 - Prevent Sensitive Credential Exposure in Logs
**Vulnerability:** Proxy credentials (username and password) were being logged in plaintext to the console, and unhandled requests exceptions could leak the full proxy URL with credentials.
**Learning:** Unsanitized logging of connection strings and raw exception objects from HTTP clients can inadvertently expose authentication credentials, violating secure logging practices.
**Prevention:** Always mask credentials (e.g., passwords) using regex or string splitting before logging, and URL-encode credentials when constructing connection strings.
