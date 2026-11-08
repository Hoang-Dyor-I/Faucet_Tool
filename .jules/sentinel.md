## 2024-11-08 - Secure Proxy Credential Handling
**Vulnerability:** Proxy credentials (passwords with special characters) were unencoded in URLs, risking injection. Raw exceptions from requests were printed, leaking plaintext passwords via URLs in stdout.
**Learning:** `requests` exceptions often include the full URL. If proxy URLs include credentials, they must be masked before logging to avoid credential leaks. Also, credentials must be URL encoded (e.g. `urllib.parse.quote`) when manually building URL strings.
**Prevention:** Always URL-encode credentials manually embedded in URLs. Always sanitize `requests` exceptions (e.g. via regex to replace the password portion) before logging/printing them when handling sensitive proxies.
