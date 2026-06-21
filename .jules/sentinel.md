## 2024-05-24 - Credential Leakage in Raw Exception Logs
**Vulnerability:** Raw exception logs and proxy initialization strings leaked plaintext credentials to the console. Exception objects like `requests.exceptions.ConnectionError` embed the full URL (including HTTP Basic Auth credentials) when a connection fails.
**Learning:** Built-in exception string representations for networking libraries often include connection URLs natively, causing unintended credential exposure even if the main code doesn't explicitly log the password.
**Prevention:** Always sanitize exception strings using regex (e.g., `re.sub(r'(://[^:]+:).*(@)', r'\1***\2', str(e))`) when handling network requests with inline credentials, and create dedicated mask functions for custom credential strings before logging.
