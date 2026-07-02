## 2024-06-01 - Proxy Credentials Leakage
**Vulnerability:** Proxy credentials (username and password) were leaked in console logs and exception error messages.
**Learning:** The `requests` library automatically percent-encodes credentials in its error output, which affects regex matchers. Also, printing raw proxy strings and raw exception messages can easily leak sensitive credentials.
**Prevention:** Always parse or split sensitive strings to isolate and mask credentials before logging. Sanitize error messages using regex to mask passwords while preserving debugging context. Use non-greedy matching `.*?` to avoid swallowing the rest of the string.
