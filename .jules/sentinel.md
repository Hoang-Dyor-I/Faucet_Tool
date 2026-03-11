## 2024-05-24 - Masking Proxy Credentials and Exceptions
**Vulnerability:** Proxy credentials (user:password) and raw exception details were being printed to standard output in the devnet airdrop script.
**Learning:** Hardcoded print statements often expose sensitive data like proxy authentication and network tracebacks.
**Prevention:** Always split and mask proxy strings before logging. Catch exceptions and log generic, safe error messages instead of printing the full exception object.
