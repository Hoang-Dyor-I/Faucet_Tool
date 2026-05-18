## 2024-05-24 - Unmasked Proxy Credentials
**Vulnerability:** Proxy credentials (passwords and users) were exposed directly in print logs, error traces, and were not safely encoded.
**Learning:** Hardcoded proxy strings expose secrets when logging the connection flow. They must be redacted and properly formatted.
**Prevention:** Implement proxy masking prior to logging and utilize URL encoding `urllib.parse.quote` for usernames and passwords. Avoid exposing raw exceptions to end users.
