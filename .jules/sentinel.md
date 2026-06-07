
## 2024-06-07 - Insecure Proxy Credential Logging
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext and exposed through raw exception traces. Proxy passwords with special characters were also unencoded and incorrectly truncated.
**Learning:** Raw string manipulation (`split(":")`) truncates passwords containing colons, and raw exception printing (`str(e)`) leaks parsed URL components including credentials. Side-effect module initialization complicates testing.
**Prevention:** Use `maxsplit=3` when parsing credentials, `urllib.parse.quote` for encoding, regex `re.sub(r'(://[^:]+:)[^@]+(@)', r'\1***\2', str(e))` to sanitize exceptions, and wrap script execution logic in `main()`.
