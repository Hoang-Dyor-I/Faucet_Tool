## 2025-04-22 - Prevent Data Leakage in Script Output
**Vulnerability:** Proxy passwords (credentials) and internal stack/network error details were being printed to the console output.
**Learning:** Hardcoded logs during proxy assignment and exception blocks leaked credentials and internal configuration.
**Prevention:** Always parse or split strings (e.g. proxy parts) to isolate and mask credentials before logging, and use generic error messages in exception handling blocks instead of printing the Exception object directly.
