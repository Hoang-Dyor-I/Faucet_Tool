## 2024-05-13 - [Proxy Credential Exposure in Requests]
**Vulnerability:** Proxy passwords can be leaked when printing the raw proxy string and when handling request exceptions. Furthermore, special characters in passwords will cause URL parsing issues.
**Learning:** Raw exception strings in Python's `requests` can expose URL configurations with embedded proxy credentials. These passwords should also be properly url-encoded.
**Prevention:** Mask passwords with regex sanitization on exception logs and ensure passwords in proxy URLs are properly percent-encoded before passing to `requests`.
