## 2024-05-24 - Prevent Credential Leakage in Raw Exceptions
**Vulnerability:** Plaintext proxy credentials embedded in connection URLs were exposed when the raw Exception object was printed upon connection failure. Additionally, the plaintext credentials were comprehensively logged when initializing the proxy.
**Learning:** Exception objects from networking libraries (like `requests`) often include the full URL. In authenticated proxies, this means printing `str(e)` directly exposes user credentials in logs.
**Prevention:** Always use regex to sanitize `str(e)` to redact passwords (e.g., `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))`) and ensure proxy details logged to the console are separately masked.
