## 2024-07-25 - Credential Leakage in Exception Messages
**Vulnerability:** Proxy passwords leaked in plaintext via `requests` library exception strings.
**Learning:** `requests` automatically percent-encodes credentials (e.g., `@` becomes `%40`) within its error outputs, meaning regex sanitization must be careful not to consume unintended parts of the URL if trying to match the literal separator `@` vs encoded characters.
**Prevention:** Always use non-greedy matching `.*?(@)` after the `user:` part to accurately mask passwords without breaking the exception context.
