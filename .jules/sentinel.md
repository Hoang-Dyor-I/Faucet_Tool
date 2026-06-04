## 2024-05-24 - Fix Plaintext Credential Leakage in Proxy Logs
**Vulnerability:** Proxy credentials (passwords) were being leaked in plaintext via console logs when initializing proxies and within raw exception messages when requests failed.
**Learning:** Hardcoded print() statements processing proxy strings and unhandled exception objects can inadvertently expose sensitive configuration data to monitoring tools and local logs.
**Prevention:** Implement pre-logging redaction for proxy strings and use regex sanitization on exception messages to explicitly mask sensitive URI components (like passwords) before emitting logs.
