## 2024-06-12 - Sensitive Data Exposure in Logs and Exceptions
**Vulnerability:** Proxy passwords were being printed in plaintext to the console during normal operation and via unhandled exception traces.
**Learning:** Raw credentials should never be directly passed into formatted log strings. Exception traces can inherently leak connection URIs containing credentials.
**Prevention:** Pre-process strings used for network connections to safely parse credentials (e.g., using maxsplit=3) and ensure logs actively mask passwords through dedicated masking functions and regex sanitization in exception handlers.
