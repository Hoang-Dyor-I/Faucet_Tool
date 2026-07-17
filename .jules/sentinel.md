## 2024-05-24 - [Exposed Proxy Credentials in Console Logs and Exceptions]
**Vulnerability:** Proxy credentials (passwords) were exposed in plaintext in stdout via standard console prints and uncensored requests module exception messages.
**Learning:** Raw proxy connection strings contain sensitive credentials and must be parsed and masked before logging. External library exceptions (like requests) can leak connection URLs in their error representations, requiring proactive regex filtering.
**Prevention:** Always implement a dedicated masking function (e.g., replacing passwords with `***`) before passing connection strings to loggers or standard output. Sanitize exception messages using safe URL parsers or regex when dealing with network requests involving authenticated endpoints.
