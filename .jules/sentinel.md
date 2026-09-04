## 2024-05-24 - Credentials leakage in exceptions and logs
**Vulnerability:** Plaintext proxy credentials were leaked in standard output through direct logging and unhandled requests exceptions exposing URL components.
**Learning:** The `requests` library automatically percent-encodes credentials in exception messages, making regex matching complex (e.g. passwords containing special characters like `@` are rendered as `%40`).
**Prevention:** Use `urllib.parse.quote` for explicit safe credential encoding and sanitize raw exception objects before logging using a robust regex `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))` to preserve context without exposing credentials.
