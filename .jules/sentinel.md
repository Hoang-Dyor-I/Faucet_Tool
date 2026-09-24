## 2024-06-11 - Exposed sensitive data in logs or error messages
**Vulnerability:** Proxy credentials formatted in strings were directly logged to the console without sanitization, and raw `requests` exceptions leaked URLs with plaintext credentials.
**Learning:** Hardcoded or concatenated proxy formats often contain plain credentials which end up being inadvertently logged during routine program flow or error handling.
**Prevention:** Always parse or split sensitive strings to isolate and mask credentials before logging. Sanitize exception messages using regex to mask passwords in URLs.
