## 2024-05-18 - Mask Credentials in Logs and Exceptions
**Vulnerability:** Plaintext proxy credentials (usernames and passwords) were logged to the console during normal operation and exposed in exception messages raised by the `requests` library when proxy connections failed.
**Learning:** Exception messages from libraries like `requests` can implicitly echo back configured proxy URLs, which often contain credentials. Standard console logging of proxy configuration strings also leads to sensitive data exposure if credentials are not explicitly redacted beforehand.
**Prevention:** Always parse or split sensitive strings to isolate and mask credentials before logging. For exception handling, sanitize error messages using regex to mask passwords while preserving debugging context.
