## 2024-06-10 - URL Credentials Exposure in Requests and Logs
**Vulnerability:** Proxy credentials (username and password) were exposed in raw exception traces, logged to standard output, and not correctly URL encoded when containing special characters.
**Learning:** When using requests with proxies containing authentication details, exception objects might leak the URL including credentials in plaintext.
**Prevention:** Always sanitize exception messages with regex to mask credentials before logging, URL encode usernames and passwords in proxy URLs, and pre-mask sensitive log messages displaying configuration strings.
