## 2024-05-18 - Prevent Proxy Credential Leakage in Logs
**Vulnerability:** Proxy passwords were leaked in plaintext in both regular console output and network exception trace logs.
**Learning:** `requests` network exceptions can dump the unredacted URL when throwing connection errors. Logging raw proxy connection strings also exposes passwords.
**Prevention:** Redact proxy passwords before logging to console, and catch/mask exceptions using regex `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))` to ensure passwords are not leaked during failures. Also use `urllib.parse.quote(value, safe='')` for credentials.
