## 2024-05-24 - Masking Proxy Credentials in Logs
**Vulnerability:** Proxy credentials (username and password) were exposed in plaintext in console logs when printing proxy strings and when connection errors occurred.
**Learning:** Hardcoded print statements and direct stringification of Exception objects can leak sensitive data in their messages.
**Prevention:** Use string splitting and regex substitutions to mask passwords before logging proxy info or exceptions.
