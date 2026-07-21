## 2024-07-21 - Prevent Credentials Leakage in Request Exception Messages
**Vulnerability:** Hardcoded credentials and plain-text proxy authentication strings were exposed via logging request exceptions and printing unmasked proxy strings in the main loop.
**Learning:** Network request libraries often include full URLs (including embedded credentials) in their exception messages when connections fail. Simply catching and printing `Exception` without sanitization can inadvertently leak sensitive proxy or API credentials into application logs.
**Prevention:** Implement proactive credential masking by applying regex to exception messages before logging, percent-encode URL credentials to prevent injection, and explicitly mask secrets in pre-flight log messages.
