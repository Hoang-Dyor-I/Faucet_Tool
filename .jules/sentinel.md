## 2024-05-18 - Mask URL-encoded proxy credentials in exception logs
**Vulnerability:** Plain-text proxy credentials (including passwords with special characters) were leaked in application logs and unhandled requests exception messages.
**Learning:** requests exception stringification automatically includes the proxy URL, inadvertently logging sensitive passwords. These credentials can be percent-encoded, making simple string replacement insufficient for scrubbing.
**Prevention:** Always isolate and mask credentials before printing. For exceptions, sanitize using regex (e.g., re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))) to securely redact credentials.
