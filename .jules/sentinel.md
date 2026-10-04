## 2024-05-30 - Exposed proxy credentials in logs and errors
**Vulnerability:** Proxy credentials (passwords) were exposed in plaintext in console logs when rotating proxies, and full proxy URLs with plaintext credentials could be leaked in `requests` exception strings.
**Learning:** The `requests` library automatically percent-encodes credentials in its error output. Hardcoded prints of proxy credentials and unhandled exception objects can leak these secrets.
**Prevention:** Implement credential masking before logging (e.g. `mask_proxy`), URL-encode user credentials securely via `urllib.parse.quote`, and sanitize error messages using regex to scrub credentials from exception objects.
