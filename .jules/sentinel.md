## 2024-05-20 - Exposing Proxy Credentials in Logs and Exception Objects
**Vulnerability:** Proxy credentials (username/password) were being printed in plain text to the console, and internal exceptions were being exposed directly to standard output.
**Learning:** Generic print statements or string formatting applied to structured credential strings (like proxy addresses) or raw exception objects bypass standard Python security controls leading to potential data exposure.
**Prevention:** Always mask credentials via helper functions like `mask_proxy` before logging, and always sanitize error handling to show safe, generic errors instead of raw exceptions.
