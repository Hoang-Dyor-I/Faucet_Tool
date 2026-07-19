## 2024-10-24 - Secure Exception Logging for Proxy Credentials
**Vulnerability:** Raw exception objects from the requests library can leak full proxy URLs, including plaintext passwords, in error messages and stack traces.
**Learning:** Even when standard console logs are sanitized, network libraries may automatically embed the active connection URL into their exception strings. When using authenticated proxies, the credentials are included in this URL, leading to inadvertent log exposure.
**Prevention:** Always sanitize exception strings using regex (e.g., `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`) before logging them. Ensure non-greedy matching (`.*?`) is used to avoid swallowing subsequent parts of the message.
