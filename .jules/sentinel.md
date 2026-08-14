## 2024-10-31 - Proxy Credentials Exposure in Logs and Exceptions
**Vulnerability:** Proxy credentials (username and password) were directly logged to stdout and exposed in unhandled requests exception stack traces, leading to credential leakage. Additionally, passwords containing special characters weren't URL-encoded, causing injection risks.
**Learning:** Raw proxy strings were logged without redaction, and `requests` exceptions embed full proxy URLs. Credentials weren't safely percent-encoded before interpolation.
**Prevention:** Always percent-encode proxy credentials, sanitize exception messages via regex to mask passwords, and explicitly implement redacting log handlers or formatter functions before printing sensitive variables.
