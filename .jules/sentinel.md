## 2024-03-21 - [Secure Logging] Hide Proxy Credentials
**Vulnerability:** Proxy configurations (`host:port:user:password`) were logged in plain text, exposing `user:password` credentials in console logs and exceptions.
**Learning:** Hardcoded full string printings like `print(f"Proxy: {proxy}")` often fail to account for secrets embedded within the string structure (e.g. auth parts).
**Prevention:** Always parse or split sensitive strings (e.g. proxy configurations) to isolate and mask credentials before logging. Fail securely by showing generic errors instead of raw exceptions or response texts.
