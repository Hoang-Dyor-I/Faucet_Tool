## 2024-05-18 - Mask Credentials in Console Logs and Errors
**Vulnerability:** Proxy credentials (username and password) were printed in plaintext in console logs and raw exception messages.
**Learning:** Raw string interpolations of proxy URLs and unhandled exception traces easily leak sensitive information if not actively masked before outputting to the console.
**Prevention:** Always parse sensitive strings to isolate and mask credentials before logging, and use regex replacements (`re.sub`) to sanitize exception messages to strip plain text credentials.
