## 2024-05-24 - Fix Proxy Credential Leakage and Injection Risks
**Vulnerability:** Proxy credentials (user:pass) were logged in plaintext, not URL-encoded causing injection risks, and generic exceptions leaked stack traces.
**Learning:** Hardcoded formatting and broad exception handling in iterative network scripts expose sensitive proxy configurations and internal error states.
**Prevention:** Always mask credentials before logging, URL-encode sensitive components, and use safe, generic error messages.