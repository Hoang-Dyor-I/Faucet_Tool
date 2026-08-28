## 2024-05-24 - Credential Leak in Proxy Logs and Exceptions
**Vulnerability:** Proxy passwords were being exposed in plaintext via console logs (`print(f"🌐 Đang dùng proxy: {proxy}")`) and potentially embedded in `requests` exception messages if the HTTP request failed.
**Learning:** Raw proxy strings naturally expose credentials. Furthermore, exception messages from HTTP libraries can embed full connection URIs containing secrets unless explicitly sanitized.
**Prevention:** Implement a dedicated proxy masking function before logging, percent-encode credentials for URIs, and use regex sanitization on exception messages to redact secrets.
