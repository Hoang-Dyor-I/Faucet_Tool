## 2024-08-15 - Mask proxy credentials in logs
**Vulnerability:** Exposed sensitive data in logs (proxy credentials leaked via print and exception handling)
**Learning:** Raw exception objects and direct printing of proxy strings leak credentials in console logs and exception traces.
**Prevention:** Mask sensitive data using regex for exception strings and split/mask functions for formatted credentials before logging.
