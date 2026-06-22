## 2024-05-24 - Credentials Logged in Cleartext
**Vulnerability:** Proxy credentials (passwords) were logged in cleartext both when announcing the proxy and within raw exception strings when requests failed.
**Learning:** Standard exception handling `except Exception as e: print(e)` can leak embedded sensitive URLs from underlying libraries like `requests`.
**Prevention:** Always parse or split strings to isolate and mask credentials before logging. Sanitize exception messages using regex `re.sub(r'(://[^:]+:).*(@)', r'\1***\2', str(e))` to preserve debugging context without leaking secrets.
