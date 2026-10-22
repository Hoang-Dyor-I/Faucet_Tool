## 2024-10-22 - Credential Exposure in Proxy Logging and Exceptions
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext to the console during iteration and could leak in raw exceptions from the `requests` library.
**Learning:** Unsanitized logging of raw data and raw exception objects often inadvertently exposes sensitive credentials, especially when dealing with external proxies or network resources.
**Prevention:** Implement URL encoding for credentials to ensure correct transmission and mask/redact sensitive data before outputting to any logs or console.
