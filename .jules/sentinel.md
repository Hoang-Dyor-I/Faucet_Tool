## 2024-10-24 - Sensitive Data Exposure in Requests Exceptions and Logs
**Vulnerability:** Plaintext proxy credentials (username and password) are exposed via console logs and `requests` exception tracebacks.
**Learning:** `requests` automatically percent-encodes credentials in its error output. When printing exceptions directly, these encoded credentials can leak. Console logs also explicitly print the unmasked proxy string.
**Prevention:** Always mask sensitive strings before logging. Sanitize exception messages using regex `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))` to hide credentials, considering percent-encoding.
