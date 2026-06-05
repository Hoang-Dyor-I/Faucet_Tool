## 2024-06-05 - Leaking proxy credentials in standard output
**Vulnerability:** Proxy passwords and credentials were being logged to standard output when proxy connection errors occurred or during the proxy iteration process.
**Learning:** Python's Exception string representation captures the full internal state, including sensitive components of proxy URLs. The lack of standard credential masking caused this data to leak into server logs. Additionally, credentials with special characters weren't URL encoded.
**Prevention:** Mask all sensitive strings containing authentication data before logging them. Always URL encode strings used for proxy auth.
