## 2024-05-24 - Credential Leakage in Logs and Exception Messages
**Vulnerability:** Raw proxy credentials (including plaintext passwords) were being logged to the console natively and leaked via unhandled exception traces from the `requests` library.
**Learning:** Exception stringification often includes raw URLs and sensitive parameters. Standard logging practices easily capture these implicitly.
**Prevention:** Implement explicit proxy credential masking using `.split(":", 3)` and redact exception trace messages using regular expressions (e.g., `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))`) before printing. Ensure credentials in URIs are percent-encoded to prevent library-level injection or crashes.
