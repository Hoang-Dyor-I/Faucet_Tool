## 2024-05-19 - Proxy Credential Leakage in Console Logs
**Vulnerability:** Proxy passwords (and usernames) were printed directly to standard output as plaintext in the main loop during script execution (`print(f"\\n🌐 Đang dùng proxy: {proxy}")`).
**Learning:** Console logging of configuration strings often inadvertently exposes secrets if sensitive parts of the string aren't masked before output.
**Prevention:** Always implement a redaction mechanism (e.g., `mask_proxy`) to obfuscate credentials (like replacing passwords with `***`) before logging connection strings or URIs.
