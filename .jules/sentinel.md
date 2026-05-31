## 2024-05-31 - [Credential Exposure in Console Logs]
**Vulnerability:** [Proxy credentials (user/password) and full exception details containing credentials are exposed in plaintext console logs]
**Learning:** [Raw unparsed strings and exception objects log their entire payload which can inadvertently leak auth data]
**Prevention:** [Implement a dedicated masking function for proxy strings and sanitize exception messages via regex before logging them]
