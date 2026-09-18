## 2026-09-18 - Mask Proxy Credentials in Output and Error Messages
**Vulnerability:** The script directly printed raw proxy configurations and unhandled exceptions that could expose proxy usernames and passwords (potentially containing special characters) in plain text logs.
**Learning:** Hardcoded `split(":")` parsing is brittle to passwords containing colons, and exceptions originating from HTTP libraries like `requests` often expose full request context including proxy connection URLs with embedded credentials.
**Prevention:** Always percent-encode credentials and explicitly mask sensitive portions of proxy configurations before printing. Sanitize exceptions using regex replacement to ensure logs don't inadvertently expose connection strings.
