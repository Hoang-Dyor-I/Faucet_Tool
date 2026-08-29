## 2024-05-18 - Mask Proxy Credentials in Python Output
**Vulnerability:** The Solana Devnet script prints the full proxy string (which includes the proxy's plain-text password) to the terminal output during runtime, and exception messages from `requests` leaked URL-encoded passwords.
**Learning:** Variables handled for debug prints, error logs, and stack traces must explicitly sanitize and mask credentials before outputting, as standard libraries like `requests` might include full URLs (including proxy credentials) in their exceptions.
**Prevention:** Always implement parsing or regex string replacement (e.g., matching URL authority sections and subbing with `***`) prior to printing connection errors or logging current proxy usages.
