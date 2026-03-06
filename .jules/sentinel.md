## $(date +%Y-%m-%d) - [CRITICAL] Fix Exposed Proxy Credentials in Logs
**Vulnerability:** Proxy credentials (passwords) were exposed in plaintext in the application console logs in `Sol/Sol_Devnet.py`.
**Learning:** Hardcoded formatting (like `split(":")` expecting exactly 4 items) is risky for strings with varying formats like proxies (e.g. `host:port` vs `host:port:user:pass`). This can cause application crashes or over-redaction (logging `***redacted***` for everything) if not handled properly.
**Prevention:** Implement safe string splitting and explicit handling for different lengths (e.g., checking `len(parts)`) before extracting sensitive data for redaction. Always ensure logging functions don't leak credentials by explicitly parsing them out.
