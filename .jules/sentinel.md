## 2023-10-30 - Masking Passwords in Exception Strings
**Vulnerability:** Passwords in proxy URLs can be leaked in plaintext if a full raw exception object is logged or printed.
**Learning:** The `requests` library automatically percent-encodes credentials in its error output. So when masking passwords with regex, you need to account for encoded characters (like %40 instead of @).
**Prevention:** Use regex (e.g., `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))`) to mask passwords before logging exception messages to avoid credential leakage.
