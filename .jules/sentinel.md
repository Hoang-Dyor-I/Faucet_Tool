
## 2024-08-03 - Credential Leak in Proxy Exceptions & Missing URL-Encoding
**Vulnerability:** The script logged raw `requests` library exceptions which exposed plaintext proxy credentials in error messages. Additionally, proxy credentials with special characters were injected directly into URLs without URL-encoding, leading to potential URL injection or connection failures.
**Learning:** `requests` exceptions often include the full connection URL in string output. Simply printing `str(e)` on a network error leaks embedded basic-auth credentials. Also, standard parsing does not handle URL special characters safely by default.
**Prevention:** Always use regex or string manipulation to sanitize exception strings by masking `(://[^:]+:).*?(@)` before logging to console/files. Ensure `urllib.parse.quote()` is applied to user/pass fragments when manually constructing auth URLs.
