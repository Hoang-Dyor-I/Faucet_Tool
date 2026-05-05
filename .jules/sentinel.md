## 2025-05-05 - Mask Sensitive Proxy Credentials in Logs and Errors
**Vulnerability:** The proxy password details were at risk of being logged directly or exposed as part of the requests Exception details in stdout logs.
**Learning:** Hardcoded full printing of proxy objects or stringified exceptions in python network requests will often result in sensitive credentials leaking via console logs, especially in batch proxy setups.
**Prevention:** Always extract and mask proxy credentials with asterisks before logging them. Instead of printing the raw exception strings (`e`) from network requests, print safe, static error messages. Use parsing functions like `mask_proxy` to ensure the masking logic is consistent.
