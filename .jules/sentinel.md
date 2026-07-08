## 2024-05-24 - Exception Information Leakage via requests Library
**Vulnerability:** Unsanitized exceptions in the requests library leak proxy credentials (passwords) in plaintext when logging connection errors.
**Learning:** The requests library automatically includes the full URL in its exception messages when connection errors occur. Even if the password is URL-encoded, it remains visible in the logs, exposing sensitive credentials in debugging output.
**Prevention:** Always sanitize exception strings related to network requests using non-greedy regex (e.g., `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`) before logging to ensure passwords are masked while preserving the rest of the error context.
