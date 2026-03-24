## 2024-05-01 - Exposed Credentials and Internal Data Leakage in Logs
**Vulnerability:** The Solana Devnet script was logging the full raw proxy string (including user:password) and printing full exception stack traces (`response.text` and `e`) directly to the console.
**Learning:** Raw input strings should always be validated and parsed before logging. Internal error messages and full exceptions must be masked to prevent exposure of system state and infrastructure details.
**Prevention:** Always parse sensitive strings to extract and mask credentials before passing them to log statements. Use generic, safe error messages in `except` blocks instead of dumping raw exception objects.
