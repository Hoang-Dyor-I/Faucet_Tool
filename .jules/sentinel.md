## 2024-11-20 - Plaintext Proxy Credentials Leak and Injection Prevention
**Vulnerability:** Proxy credentials (username and password) were being logged in plaintext to the console and in exception stack traces. Additionally, special characters in credentials were not URL-encoded, leading to potential URL construction failures or injection-like issues.
**Learning:** Hardcoded, unmasked credentials in logs or console output are a security risk. Unencoded special characters in URLs can break `requests` proxy parsing.
**Prevention:** Always mask passwords before logging them. Always URL-encode username and password components using `urllib.parse.quote` before constructing connection strings. Use regex to sanitize exception strings.
