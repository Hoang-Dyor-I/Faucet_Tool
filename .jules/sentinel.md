## 2024-05-18 - Fix exposed proxy credentials in console logs and exceptions
**Vulnerability:** Proxy credentials (passwords) were logged in plaintext to the console via `print` statements and exception traces.
**Learning:** Python's `requests` exceptions can inadvertently leak URL-encoded credentials when exceptions are stringified.
**Prevention:** Sanitize exception messages using regex to mask passwords and pre-process logging statements to mask credentials before printing. Always URL-encode credentials when constructing proxy URLs.
