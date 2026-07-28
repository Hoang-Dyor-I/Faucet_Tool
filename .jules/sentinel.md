## 2024-05-18 - Mask Proxy Credentials in Error Logs and Output
**Vulnerability:** Plaintext proxy passwords leaking in standard output and unhandled request exceptions. Also missing URL encoding for proxy authentication.
**Learning:** Using raw proxy strings without percent-encoding is dangerous. Unsanitized python exception objects like those from requests often contain sensitive proxy connection details in full.
**Prevention:** Always parse, format, and mask sensitive connection strings before logging. Sanitize unknown exception messages with regex `re.sub` for proxies before writing to output, and URL encode proxy credentials properly before passing to networking libraries.
