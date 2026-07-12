## 2024-07-12 - Proxy Credentials Leakage
**Vulnerability:** Plaintext proxy credentials leaked in console logs and unhandled exception traces.
**Learning:** Unsanitized third-party configurations containing credentials can accidentally leak via standard exception stringification or diagnostic logs if not masked.
**Prevention:** Implement credential masking before logging URIs, and sanitize exception messages via regex (`re.sub`) to remove credentials from any embedded URLs.
