## 2024-09-27 - Masking Proxy Credentials in Exception Outputs
**Vulnerability:** Proxy passwords can be leaked in plaintext in logs/console output when unhandled network exceptions from libraries like `requests` contain the full URL connection string (e.g., inside ProxyError).
**Learning:** Exception messages automatically embed context strings which might include the raw `http://user:pass@host:port` configuration. Simply not printing the config directly isn't enough; exceptions themselves must be sanitized.
**Prevention:** Use regex replacement (e.g., `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))`) to intercept and redact credentials from exception string representations before logging or printing them.
