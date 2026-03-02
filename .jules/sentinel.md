## 2024-05-24 - [Exposed Proxy Credentials in Logs]
**Vulnerability:** The script was directly logging the proxy authentication credentials (username and password) string in plaintext.
**Learning:** Logs are a common place for sensitive information to leak, especially when iterating over configuration objects or connection strings without first sanitizing them.
**Prevention:** Always mask, redact, or hash sensitive fields (like passwords, keys, or tokens) within connection strings or objects before they are passed to logging or print functions.
