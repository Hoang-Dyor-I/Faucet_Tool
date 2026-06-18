## 2023-10-24 - Credentials Masking in Logs and Exceptions
**Vulnerability:** Proxy passwords were leaked in plain text when logging proxy URLs and when the requests library raised connection exceptions containing the authenticated proxy URL.
**Learning:** External libraries like `requests` may embed full URLs (including basic auth credentials) in error messages. Direct logging of configuration items or unchecked exceptions can silently expose secrets in standard output or logs.
**Prevention:** Implement dedicated masking functions for configuration logging (e.g., parsing strings before printing) and sanitize exception messages via regex (e.g., `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))`) before logging.
