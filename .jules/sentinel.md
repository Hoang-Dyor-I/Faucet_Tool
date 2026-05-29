## 2024-05-24 - Credentials leakage in Exception logs
**Vulnerability:** Proxy credentials (username/password) were inadvertently logged in plaintext to the console when `requests.post()` raised connection or timeout exceptions.
**Learning:** Error logs from networking libraries that accept proxy strings/URLs can leak credentials if the entire exception object is directly stringified (`str(e)`) and printed.
**Prevention:** Exception messages must be explicitly sanitized, e.g. using regex to strip out credentials such as `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))` before logging, while preserving the surrounding context to aid debugging.
