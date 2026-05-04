## 2024-05-24 - Prevent Credential Exposure in Logs and Exceptions
**Vulnerability:** Raw proxy credentials (username/password) were printed in logs and full exception objects were printed in the output when proxy failures occurred, leading to credential leaks.
**Learning:** Raw string concatenations and unhandled `Exception as e` printouts can leak sensitive data via logging in asynchronous/batch processes. Pre-parsing data and masking it solves this.
**Prevention:** Implement a standard credential masking function for logging and avoid printing raw exceptions (`e`) or full responses (`response.text`) that could leak environment or external payload data.
