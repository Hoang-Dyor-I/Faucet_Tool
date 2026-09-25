## 2024-05-20 - Exposed Proxy Credentials in Logs
**Vulnerability:** Proxy passwords are intentionally printed in plaintext to the console logs via print statements and potentially leaked via unhandled `requests` exception strings.
**Learning:** Hardcoding log statements that print raw user-provided connection strings without scrubbing exposes sensitive credentials, and third-party library error messages often embed credentials from constructed URLs.
**Prevention:** Always parse or split sensitive strings to isolate and mask credentials before logging, and sanitize exception objects using regex before output.
