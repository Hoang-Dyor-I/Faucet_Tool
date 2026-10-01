## 2024-10-01 - Exposed sensitive data in logs
**Vulnerability:** Application printed unmasked proxy URLs containing plaintext passwords in error logs, and printed plaintext proxy passwords when starting batches.
**Learning:** Raw exception strings from HTTP libraries (like requests) often contain fully constructed URLs with credentials embedded, which get leaked when exceptions are printed directly.
**Prevention:** Sanitize exception messages using regex before logging to mask credentials, and ensure sensitive connection strings are masked in standard informational logs.
