## 2023-10-24 - Proxy Credential Leakage in Request Exceptions
**Vulnerability:** The `requests` library logs unredacted proxy URLs containing plaintext username and password in exception messages during connection failures.
**Learning:** Handling proxy URLs requires explicit credential masking before outputting them to logs or consoles, and passwords with special chars must be URL-encoded for proper transmission.
**Prevention:** Implement custom redaction logic using regex `re.sub` for exception messages, manually redact URLs for console logging, and encode special characters using `urllib.parse.quote` for proxy credentials.
