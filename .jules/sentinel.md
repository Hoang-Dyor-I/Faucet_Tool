## 2024-05-01 - Prevent password leakage in proxy logs and error handlers

**Vulnerability:** The script logs the raw proxy string (which includes the proxy password) directly to the console (`print(f"\n🌐 Đang dùng proxy: {proxy}")`). Furthermore, the generic exception block in `request_faucet` directly prints the caught exception object `e` to the console which could contain sensitive runtime information.

**Learning:** Logging unmasked proxy strings exposes plaintext passwords to the console/log files, and printing exception strings directly might leak connection details or inner representations that an attacker can use.

**Prevention:** Always implement a masking function (`mask_proxy`) before logging authentication strings. Also, handle exceptions by logging user-friendly, generic error messages rather than raw exception details.
