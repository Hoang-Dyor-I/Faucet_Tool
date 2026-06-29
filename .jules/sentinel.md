## 2024-06-29 - Secure Logging & Proxy Masking
**Vulnerability:** Proxy passwords were being logged in plaintext during startup and when unhandled exceptions surfaced the underlying URL details from `requests`.
**Learning:** Hardcoded split logic didn't account for colons in passwords, and raw exceptions often embed sensitive connection URLs.
**Prevention:** Always mask credentials via custom regex on exception strings, use `maxsplit` on proxy parsing, and proactively redact sensitive properties before passing them to console print functions.
