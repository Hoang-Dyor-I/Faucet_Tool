## 2024-08-08 - Prevent Plaintext Credential Exposure in Proxy Configuration
**Vulnerability:** Proxy credentials (username/password) were printed in plaintext to the console and could be leaked via unhandled `requests` exceptions. Credentials were also vulnerable to special character truncation/injection due to lack of URL encoding.
**Learning:** External configurations containing secrets are easily leaked if printed directly without sanitization, and parsing must account for delimiters within the secret itself (e.g. colons in passwords).
**Prevention:** Always mask credentials before logging, use non-greedy regex replacement for exception messages, and apply strict URL-encoding (`urllib.parse.quote`) when injecting credentials into URIs.
