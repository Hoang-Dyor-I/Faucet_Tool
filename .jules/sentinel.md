## 2024-04-24 - Prevent Credential Leakage in Logs
**Vulnerability:** Raw proxies containing user credentials and passwords were hardcoded to print to stdout.
**Learning:** Printing unparsed or unsanitized connection strings leads to credential leakage in internal logs.
**Prevention:** Always parse and mask sensitive credential structures before printing to output streams.
