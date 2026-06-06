## 2024-06-06 - Credential Exposure in Error Logging and Console Output
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext to the console and could be fully leaked via unhandled exception objects when network errors occurred with the `requests` library.
**Learning:** Exception stringification may dump raw URLs containing plaintext credentials if proxy usage fails. Furthermore, custom proxy formats (e.g. `host:port:user:pass`) logged globally leak sensitive details.
**Prevention:** Always mask passwords via regex from exception outputs (e.g., `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))`) and redact proxy credentials in custom string logging explicitly. Never log unmasked connection strings.
