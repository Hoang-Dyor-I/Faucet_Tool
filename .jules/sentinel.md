## 2024-05-18 - [Prevent Password Leaks in Proxy Strings]
**Vulnerability:** Proxy credentials (passwords) were being logged in plain text.
**Learning:** Raw string concatenations and simple loops can unintentionally expose sensitive strings embedded within proxy config strings (`host:port:user:pass`).
**Prevention:** Always parse or split sensitive configuration strings to isolate and mask credentials (using functions like `mask_proxy`) before allowing them to be written to console output or persistent logs.
