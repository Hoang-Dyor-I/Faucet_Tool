## 2024-07-14 - Prevent Plaintext Credential Logging in Proxy Scripts
**Vulnerability:** Proxy passwords and credentials were being logged to the console in plaintext and could be exposed in exception error messages.
**Learning:** Hardcoded string splitting and naive printing/logging of configurations containing secrets can inadvertently leak credentials into application logs. Furthermore, the `requests` library incorporates credentials into its error messages when a proxy connection fails.
**Prevention:** Always parse or split sensitive strings to isolate and mask credentials before logging. Use non-greedy regex replacement to sanitize raw exception strings from third-party libraries, and URL-encode credentials to prevent special characters from breaking URL parsing.
