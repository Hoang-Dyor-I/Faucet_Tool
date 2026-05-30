## 2024-05-24 - Fix Proxy Credential Leakage in Logs
**Vulnerability:** Application leaked proxy passwords in plaintext in both normal console logging and unhandled exception traces.
**Learning:** Raw exception strings often expose complete URLs including inline HTTP Basic Auth credentials. String splitting without `maxsplit` truncates passwords containing the delimiter.
**Prevention:** Mask proxy strings before printing, use `maxsplit` when unpacking user credentials, pre-parse proxies into dictionaries securely before passing them to threads, and sanitize exceptions using regex `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))`.
