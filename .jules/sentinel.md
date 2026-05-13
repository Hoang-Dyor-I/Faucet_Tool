## 2024-05-24 - Credentials Exposed in Logs and URLs
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext, and special characters in credentials were not URL-encoded, leading to potential malformed URLs or injection. Raw exception objects were also printed, exposing internal state.
**Learning:** Sensitive data in configuration strings must be actively parsed and masked before logging, and credentials must always be safely encoded before inclusion in URIs.
**Prevention:** Implement a secure logging convention to mask credentials and always use `urllib.parse.quote` for credentials in URLs.
