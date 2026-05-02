## 2024-05-02 - Information Exposure via Print Statements
**Vulnerability:** Proxy credentials (passwords) and server exception internals were directly logged to console.
**Learning:** In simple scripts, `print` statements often lack the security review that formal logging mechanisms get, leading to unintentional leakage of credentials and stack traces.
**Prevention:** Always implement masking for credentials before logging and catch exceptions broadly to output sanitized messages rather than exception objects.
