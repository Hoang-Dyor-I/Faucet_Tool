## 2024-05-24 - Masking Proxy Credentials in Logs and Network Errors
**Vulnerability:** Proxy credentials (username/password) were logged in plain text to the console, and unhandled exception logging could leak credentials embedded in proxy URLs.
**Learning:** Using raw proxy strings for console outputs and raw exception objects (`str(e)`) for network requests often inadvertently exposes sensitive basic auth credentials to standard output or logging systems.
**Prevention:** Always implement a dedicated masking function for proxy connection strings before printing, pre-parse proxies, and sanitize exception strings using regex to obscure sensitive components like passwords.
