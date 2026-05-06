## 2024-05-06 - Prevent Credentials Leakage in Devnet Proxy Config
**Vulnerability:** Proxy strings containing `user:password` were being printed in plaintext to the console, and uncaught network exceptions might leak internal details.
**Learning:** Proxy strings should be scrubbed of authentication components before logging. Catch-all exceptions around network requests should use safe generic errors rather than passing down full stack-trace objects.
**Prevention:** Implement string parsing or proxy-masking utilities explicitly designed for console outputs. Adopt fail-safe exceptions in iterative network batch processes.
