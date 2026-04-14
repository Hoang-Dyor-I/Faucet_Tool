## 2024-04-14 - Early Return Rate Limiting Bypass
**Vulnerability:** Fast-loop causing CPU spike/rate-limit triggers.
**Learning:** Adding an early return in a tight loop function (like a threaded network request) without duplicating the sleep/delay mechanism causes the loop to spin out of control when encountering errors.
**Prevention:** Always ensure iterative delay/rate-limit mechanisms (`time.sleep`) are applied even in error or early-return paths to maintain loop cadence.
