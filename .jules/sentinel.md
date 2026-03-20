## 2024-03-20 - [Proxy Credential Exposure in Logs]
**Vulnerability:** Proxy credentials (username/password) were being logged in plain text, and full exception objects were being printed, potentially exposing internal system details.
**Learning:** Hardcoded formatting of proxy strings in logs can inadvertently expose sensitive authentication details. Exception handling should avoid exposing raw error objects to the user.
**Prevention:** Always mask sensitive parts of connection strings (e.g., `host:port:***:***`) before logging. Use generic error messages instead of printing raw exception objects (`Exception as e`).
