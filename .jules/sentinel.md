## 2024-04-01 - Credential Exposure in Logging
**Vulnerability:** The application was logging proxy strings in plaintext (`user:password@host:port`) and printing raw exception objects on connection errors.
**Learning:** Raw exception strings and raw configuration values can inadvertently leak credentials, sensitive internal API details, or local system state.
**Prevention:** Always parse and sanitize sensitive configuration strings (e.g., masking credentials) before logging, and use generic, secure error messages rather than printing the full exception stack or message.