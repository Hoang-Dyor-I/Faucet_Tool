## 2024-05-30 - Prevent Credential Leaks in Console Logs
**Vulnerability:** Proxy passwords are leaked in plain text when script prints what proxy is used, or in requests exception strings. In addition, passwords and usernames could cause errors when parsing or sending if not urlencoded.
**Learning:** Raw proxy strings and full exception messages can inadvertently expose sensitive credentials. Python requests library formats these in specific ways when raising errors.
**Prevention:** Apply regex sanitization to exception error messages, manually mask credentials before printing to console, and use urllib.parse.quote when assembling URLs with proxies.
