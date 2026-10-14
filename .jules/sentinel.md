## 2024-05-18 - Credentials exposure in proxy logic
**Vulnerability:** Proxy credentials (username/password) were printed in raw exception logs and console outputs, and special characters were improperly parsed, leading to injection-like errors.
**Learning:** Hardcoding or exposing proxy connection URLs without sanitization allows sensitive information leakage, especially when exceptions propagate full URLs, and poor string parsing leads to URL truncation.
**Prevention:** Always parse or split sensitive strings using maxsplit and mask them before logging. Sanitize exception strings with regex to hide credentials.
