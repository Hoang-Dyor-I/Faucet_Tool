## 2024-11-03 - Proxies Credential Exposure and Formatting Fixes
**Vulnerability:** Proxy passwords exposed in logs and unencoded proxy credentials causing connection errors.
**Learning:** Proxy credentials in exception messages and strings were exposed and special characters caused URL issues.
**Prevention:** Sanitize exceptions using regex, URL encode credentials, and mask passwords on console output.
