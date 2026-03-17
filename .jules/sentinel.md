## 2024-05-24 - Masking Proxy Credentials
**Vulnerability:** Proxy credentials (user:pass) were logged in plaintext.
**Learning:** Logging should always sanitize proxy strings to prevent the leakage of credentials in logs. Additionally, exception printing leaked stack trace and potentially sensitive request context.
**Prevention:** Sanitize any proxy strings before logging and mask generic exception outputs to avoid leaking sensitive stack traces and request data.