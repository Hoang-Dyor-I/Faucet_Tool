## 2024-07-10 - Sensitive Data Exposure in Requests Exceptions
**Vulnerability:** The `requests` library in Python includes the full proxy URL (with URL-encoded credentials) in certain exception messages (like ProxyError). Printing the raw exception object in a try-catch block leaks these credentials to standard output/logs.
**Learning:** Even if we mask credentials when intentionally logging proxy strings, underlying network libraries often re-attach the credentials to exception strings. We must sanitize the string representation of network exceptions using regex before logging.
**Prevention:** Always cast network exceptions to string and apply a sanitization regex (e.g., `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`) to strip credentials before logging or returning error messages.
