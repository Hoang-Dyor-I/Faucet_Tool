## 2024-05-18 - Prevent Sensitive Data Exposure in Logs and Exceptions
**Vulnerability:** The proxy credentials, including passwords, were being printed in plaintext to the console and could leak through raw exception stack traces from the `requests` library.
**Learning:** Raw exception strings from network libraries (like `requests`) often preserve the full requested URL, which might contain inline basic auth credentials. Logging them naked is an exposure vector.
**Prevention:** Always scrub sensitive patterns from exception strings before logging, pre-parse proxies, and explicitly mask parts containing passwords before printing to the terminal.
