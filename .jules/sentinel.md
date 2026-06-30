## 2024-05-23 - Hardcoded Plaintext Credentials in Logs and Exception Tracebacks
**Vulnerability:** Proxy credentials (username and passwords) were logged in plaintext to the console and could be exposed in exception tracebacks. Special characters in passwords could also cause injection issues.
**Learning:** Raw string concatenations for URL schemas and direct printing of exception objects bypass intended credential protections. Network library logs often include the raw request URL containing embedded credentials.
**Prevention:** Always mask credentials in logging components, sanitize exception strings via regex to remove passwords, and properly percent-encode all URL components using standard libraries.
