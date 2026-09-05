## 2024-05-24 - Secure Exception Logging Pattern
**Vulnerability:** Unsanitized exception objects (e.g., from `requests` library) can leak plaintext proxy credentials in their error strings, exposing sensitive data to logs.
**Learning:** Python's `str(e)` on networking exceptions often contains the full URL with embedded credentials. Simply catching and printing exceptions without sanitization is a leak vector.
**Prevention:** Implement regex-based redaction (e.g. `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))`) before logging exception messages to isolate and mask passwords while preserving debugging context.
