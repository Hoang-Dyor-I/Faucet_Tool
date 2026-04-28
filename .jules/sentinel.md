## 2024-04-28 - Secure Application Logging and State Init
**Vulnerability:** Proxy credentials (passwords) and generic exceptions (which could leak internal routing or token state) were being dumped to standard output.
**Learning:** Hardcoded split logic assuming perfectly formatted proxy strings crashes scripts with unhandled Type/Value errors; logging raw string templates without masking is a classic path for log leakage.
**Prevention:** Mask known secret-containing structures before sending to stdout/logs and catch broader application errors with generic external messages to prevent internal leakage.
