## 2024-07-13 - [Credential Leakage in Logs and URLs]
**Vulnerability:** Proxy credentials (username and password) were logged in plaintext to the console and could be exposed in raw `requests` exception messages. Additionally, unescaped credentials in proxy URLs could cause parsing errors or credential injection.
**Learning:** `requests` exceptions often include the full URL (including inline credentials) that caused the failure, making generic exception printing dangerous. Global scope initialization of files also triggered side effects during imports.
**Prevention:** Always percent-encode credentials before constructing URLs, implement dedicated masking functions for logging, use regex to sanitize exception strings, and encapsulate script initialization within a `main()` block.
