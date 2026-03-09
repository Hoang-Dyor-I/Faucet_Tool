## 2024-03-09 - [Fix exposed credentials in logs]
**Vulnerability:** The script logged proxy configurations in plaintext and exception messages, exposing username and password credentials.
**Learning:** Proxy strings containing `host:port:user:password` should be parsed and masked to isolate credentials before logging. Exception messages should log a safe generic error instead of raw exception details.
**Prevention:** Always parse sensitive strings to isolate credentials before logging and use safe, generic error messages.
